from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from hibacsi import settings
from django.contrib import auth
import jwt
from app.serializers import AccountSerializer, UserSerializer, AdminSerializer, DoctorSerializer, HospitalSerializer, LoginSerializer, RegisterSerializer
from app.models import Account, User, Admin, Doctor, Hospital
from app.permissions import IsAdminPermission, IsDoctorPermission, IsHospitalPermission, IsUserPermission
import app.utils as utils
from rest_framework.decorators import authentication_classes, permission_classes
from datetime import datetime, timedelta
from rest_framework import serializers

# Create your views here.
@authentication_classes([])  # Loại bỏ xác thực
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer  
    def post(self, request):
        data = request.data
        username = data.get('username', '')
        email = data.get('email', '')
        password = data.get('password', '')
        isSuccess = utils.login_success(username=username, password=password, email=email)
        if isSuccess:
            account = Account.objects.get(username=username) if username != '' else Account.objects.get(email=email)
            refresh_token, access_token = utils.generateTokens(account)
            utils.updateRefreshToken(account.username, refresh_token)
            account = AccountSerializer(account)
            serializer_base = {'account': account.data, 'refresh_token': refresh_token, 'access_token': access_token}
            if account.data['role'] == 'user':
                try:
                    user = User.objects.get(account=account.data['id'])
                except User.DoesNotExist:
                    return Response({'detail': 'User does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                user = UserSerializer(user)
                serializer = {'user': user.data, **serializer_base}
            elif account.data['role'] == 'admin':
                try:
                    admin = Admin.objects.get(account=account.data['id'])
                except Admin.DoesNotExist:
                    return Response({'detail': 'Admin does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                admin = AdminSerializer(admin)
                serializer = {'admin': admin.data, **serializer_base}   
            elif account.data['role'] == 'doctor':
                try:
                    doctor = Doctor.objects.get(account=account.data['id'])
                except Doctor.DoesNotExist:
                    return Response({'detail': 'Doctor does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                doctor = DoctorSerializer(doctor)
                serializer = {'doctor': doctor.data, **serializer_base}
            elif account.data['role'] == 'hospital':
                try:
                    hospital = Hospital.objects.get(account=account.data['id'])
                except Hospital.DoesNotExist:
                    return Response({'detail': 'Hospital does not exist'}, status=status.HTTP_400_BAD_REQUEST)
                hospital = HospitalSerializer(hospital)
                serializer = {'hospital': hospital.data, **serializer_base}
            # add http for avatar
            base_url = r'http://' + request.get_host()
            if 'account' in serializer:
                if serializer['account']['avatar'] != None:
                    serializer['account']['avatar'] = base_url + serializer['account']['avatar']
            if 'user' in serializer:
                if serializer['user']['account']['avatar'] != None:
                    serializer['user']['account']['avatar'] = base_url + serializer['user']['account']['avatar']
            if 'doctor' in serializer:
                if serializer['doctor']['account']['avatar'] != None:
                    serializer['doctor']['account']['avatar'] = base_url + serializer['doctor']['account']['avatar']
            if 'hospital' in serializer:
                if serializer['hospital']['account']['avatar'] != None:
                    serializer['hospital']['account']['avatar'] = base_url + serializer['hospital']['account']['avatar']
            if 'admin' in serializer:
                if serializer['admin']['account']['avatar'] != None:
                    serializer['admin']['account']['avatar'] = base_url + serializer['admin']['account']['avatar']
            return Response(serializer, status=status.HTTP_200_OK)
        return Response({'detail': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)

# all user can register 
@authentication_classes([])  # Loại bỏ xác thực
class RegisterView(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data.copy()
        data['role'] = 'user'
        if 'password' in data:
            data['password'] = utils.hash_password(data['password'])
        account = AccountSerializer(data=data)
        if account.is_valid():
            account_results = account.save()
            refresh_token, access_token = utils.generateTokens(account_results)
            user = User.objects.create(account=account_results)
            user.save()
            user = UserSerializer(user)
            serializer = {'user': user.data, 'account': account.data, 'refresh_token': refresh_token, 'access_token': access_token}
            return Response(serializer, status=status.HTTP_201_CREATED)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes([IsAdminPermission])
class RegisterViewAdmin(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data.copy()
        data['role'] = 'admin'
        if 'password' in data:
            data['password'] = utils.hash_password(data['password'])
        account = AccountSerializer(data=data)
        if account.is_valid():
            account_results = account.save()
            refresh_token, access_token = utils.generateTokens(account_results)
            admin = Admin.objects.create(account=account_results)
            admin.save()
            admin = AdminSerializer(admin)
            serializer = {'admin': admin.data, 'account': account.data, 'refresh_token': refresh_token, 'access_token': access_token}
            return Response(serializer, status=status.HTTP_201_CREATED)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([IsHospitalPermission])
class RegisterViewDoctor(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data.copy()
        data['role'] = 'doctor'
        if 'password' in data:
            data['password'] = utils.hash_password(data['password'])
        account = AccountSerializer(data=data)
        if account.is_valid():
            account_results = account.save()
            refresh_token, access_token = utils.generateTokens(account_results)
            # get hospital id
            hospital = Hospital.objects.get(account=request.account)
            # Đảm bảo rằng `data` chỉ chứa các thuộc tính mà `Doctor` chấp nhận
            filtered_data = {key: value for key, value in data.items() if hasattr(Doctor, key)}
            doctor = Doctor.objects.create(account=account_results, hospital=hospital, **filtered_data)
            doctor.save()
            doctor = DoctorSerializer(doctor)
            serializer = {'doctor': doctor.data, 'account': account.data, 'refresh_token': refresh_token, 'access_token': access_token}
            return Response(serializer, status=status.HTTP_201_CREATED)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)
    
@permission_classes([IsAdminPermission])
class RegisterViewHospital(GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        data = request.data.copy()
        data['role'] = 'hospital'
        if 'password' in data:
            data['password'] = utils.hash_password(data['password'])
        account = AccountSerializer(data=data)
        if account.is_valid():
            account_results = account.save()
            refresh_token, access_token = utils.generateTokens(account_results)
            hospital = Hospital.objects.create(account=account_results)
            hospital.save()
            hospital = HospitalSerializer(hospital)
            serializer = {'hospital': hospital.data, 'account': account.data, 'refresh_token': refresh_token, 'access_token': access_token}
            return Response(serializer, status=status.HTTP_201_CREATED)
        return Response(account.errors, status=status.HTTP_400_BAD_REQUEST)
