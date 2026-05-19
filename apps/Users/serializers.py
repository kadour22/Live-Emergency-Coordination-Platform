from rest_framework import serializers

class test_serializer(serializers.Serializer) :
    
    product_id = serializers.IntegerField()
    
    def validate(self, data):
        """
        Check that start is before finish.
        """
        if data['product_id'] == 1:
            raise serializers.ValidationError("invalid ID")
        return data