from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import SexualIntercourseLog, MoodLog, BloodFlowLog, MedicationLog, SymptomLog
from .serializers import (
    SexualIntercourseLogSerializer, MoodLogSerializer, BloodFlowLogSerializer,
    MedicationLogSerializer, SymptomLogSerializer
)
from users.models import CustomUser
from django.utils.dateparse import parse_date

#Intercourse Logs
class SexualIntercourseLogCreateView(generics.CreateAPIView):
    queryset = SexualIntercourseLog.objects.all()
    serializer_class = SexualIntercourseLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Sexual Intercourse Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class SexualIntercourseLogListView(generics.ListAPIView):
    serializer_class = SexualIntercourseLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SexualIntercourseLog.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "message": "Sexual Intercourse Logs retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except SexualIntercourseLog.DoesNotExist:
            return Response({"Sexual Intercourse logs does not exist"}, status=status.HTTP_404_NOT_FOUND)    
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class SexualIntercourseLogByDateView(generics.ListAPIView):
    serializer_class = SexualIntercourseLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        date_str = self.request.query_params.get("date", None)
        
        if not date_str:
            return SexualIntercourseLog.objects.none()
        
        date = parse_date(date_str)
        
        if not date:
            return SexualIntercourseLog.objects.none()
        
        return SexualIntercourseLog.objects.filter(user=user, date=date)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
                "message": "Sexual Intercourse Log retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except SexualIntercourseLog.DoesNotExist:
            return Response({"Sexual Intercourse Log not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)


class SexualIntercourseLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SexualIntercourseLogSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)  # Allow partial updates
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "message": "Sexual Intercourse Log updated successfully",
                "log": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_400_BAD_REQUEST)    

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "message": "Sexual Intercourse Log deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)},status=status.HTTP_400_BAD_REQUEST)      

#Moods logs
class MoodLogCreateView(generics.CreateAPIView):
    queryset = MoodLog.objects.all()
    serializer_class = MoodLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Mood Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class MoodLogListView(generics.ListAPIView):
    serializer_class = MoodLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MoodLog.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "message": "Mood Logs retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except MoodLog.DoesNotExist:
            return Response({"Mood logs does not exist"}, status=status.HTTP_404_NOT_FOUND)    
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class MoodLogByDateView(generics.ListAPIView):
    serializer_class = MoodLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        date_str = self.request.query_params.get("date", None)
        
        if not date_str:
            return MoodLog.objects.none()
        
        date = parse_date(date_str)
        
        if not date:
            return MoodLog.objects.none()
        
        return MoodLog.objects.filter(user=user, date=date)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
                "message": "Mood Log retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except MoodLog.DoesNotExist:
            return Response({"Mood Log not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class MoodLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MoodLogSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)  # Allow partial updates
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "message": "Mood Log updated successfully",
                "log": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "message": "Mood Log deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)    

#Blood Flow Logs
class BloodFlowLogCreateView(generics.CreateAPIView):
    queryset = BloodFlowLog.objects.all()
    serializer_class = BloodFlowLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Blood Flow Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class BloodFlowLogListView(generics.ListAPIView):
    serializer_class = BloodFlowLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return BloodFlowLog.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "message": "Blood Flow Logs retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except BloodFlowLog.DoesNotExist:
            return Response({"Blood Flow Logs does not exist"}, status=status.HTTP_404_NOT_FOUND)    
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST) 
        
class BloodLogByDateView(generics.ListAPIView):
    serializer_class = BloodFlowLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        date_str = self.request.query_params.get("date", None)
        
        if not date_str:
            return BloodFlowLog.objects.none()
        
        date = parse_date(date_str)
        
        if not date:
            return BloodFlowLog.objects.none()
        
        return BloodFlowLog.objects.filter(user=user, date=date)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
                "message": "Blood Flow Log retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except BloodFlowLog.DoesNotExist:
            return Response({"Blood Flow Log not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)   

class BloodFlowLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BloodFlowLogSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)  # Allow partial updates
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "message": "Blood Flow Log updated successfully",
                "log": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "message": "Blood Flow Log deleted successfully"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)    

#Medication Logs
class MedicationLogCreateView(generics.CreateAPIView):
    queryset = MedicationLog.objects.all()
    serializer_class = MedicationLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Medication Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class MedicationLogListView(generics.ListAPIView):
    serializer_class = MedicationLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return MedicationLog.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "message": "Medication Logs retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except MedicationLog.DoesNotExist:
            return Response({"Medication Log not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)   
        
class MedicationLogByDateView(generics.ListAPIView):
    serializer_class = MedicationLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        date_str = self.request.query_params.get("date", None)
        
        if not date_str:
            return MedicationLog.objects.none()
        
        date = parse_date(date_str)
        
        if not date:
            return MedicationLog.objects.none()
        
        return MedicationLog.objects.filter(user=user, date=date)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
                "message": "Medication Log retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except MedicationLog.DoesNotExist:
            return Response({"Medication Log not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)     

class MedicationLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = MedicationLogSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)  # Allow partial updates
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({
            "message": "Medication Log updated successfully",
            "log": serializer.data
        }, status=status.HTTP_200_OK)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({
            "message": "Medication Log deleted successfully"
        }, status=status.HTTP_200_OK)     

#Symptoms logs
class SymptomLogCreateView(generics.CreateAPIView):
    queryset = SymptomLog.objects.all()
    serializer_class = SymptomLogSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = request.data.get("user_id")
        if not user_id:
            return Response({'error': 'user_id is required'}, status=status.HTTP_400_BAD_REQUEST)
        if str(request.user.user_id) != user_id:
            return Response({'error': 'Unauthorized to log data for this user'}, status=status.HTTP_403_FORBIDDEN)
        try:
            user = CustomUser.objects.get(user_id=user_id)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save(user=user)
            return Response({
                'message': 'Symptom Log created successfully',
                'log': serializer.data
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class SymptomLogListView(generics.ListAPIView):
    serializer_class = SymptomLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SymptomLog.objects.filter(user=self.request.user)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            return Response({
                "message": "Symptoms Logs retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)  
        
class SymptomLogByDateView(generics.ListAPIView):
    serializer_class = SymptomLogSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user = self.request.user
        date_str = self.request.query_params.get("date", None)
        
        if not date_str:
            return SymptomLog.objects.none()
        
        date = parse_date(date_str)
        
        if not date:
            return SymptomLog.objects.none()
        
        return SymptomLog.objects.filter(user=user, date=date)
    
    def list(self, request, *args, **kwargs):
        try:
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            
            return Response({
                "message": "Symptom Log retrieved successfully",
                "logs": serializer.data
            }, status=status.HTTP_200_OK)
        except SymptomLog.DoesNotExist:
            return Response({"Symptom Log not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)           

class SymptomLogDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = SymptomLogSerializer
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **kwargs):
        try:
            partial = kwargs.pop('partial', False)  # Allow partial updates
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response({
                "message": "Symptoms Log updated successfully",
                "log": serializer.data
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)     

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({
                "message": "Symptoms Log deleted successfully"
            }, status=status.HTTP_200_OK) 
        except Exception as e:
            return Response({"Error:": str(e)}, status=status.HTTP_400_BAD_REQUEST)     

