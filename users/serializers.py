from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = CustomUser
        fields = ['id', 'user_id','first_name', 'middle_name', 'last_name' ,'email', 'phone_number','gender', 'birth_date', 'date_joined', 'password']
        extra_kwargs = {
            'date_joined': {'read_only': True},
            'user_id': {'read_only': True}
        } 

    def create(self, validated_data):
        user = CustomUser.objects.create_user(email=validated_data['email'], 
                                              first_name=validated_data['first_name'], 
                                              last_name=validated_data['last_name'],
                                              middle_name=validated_data.get('middle_name', ''),
                                              phone_number=validated_data['phone_number'],
                                              gender=validated_data['gender'],
                                              birth_date=validated_data['birth_date'],
                                              password=validated_data['password']
                                            )
        return user
    
    def update(self, instance, validated_data):
        #removed password from validated data to prevent setting it directly
        password = validated_data.pop('password', None)
        
        #update other fields as usual
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            
        #set and hash the new password if provided
        if password:
            instance.set_password(password)
            
        instance.save()
        return instance
    
    