from rest_framework import serializers
from .models import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = ('id', 'id_libro', 'id_usuario', 'fec_prestamo', 'fec_devolucion')


    def create(self, validated_data):
        """
        Create and return a new `Prestamo` instance, given the validated data.
        """
        return Prestamo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Prestamo` instance, given the validated data.
        """
        #instance.id = validated_data.get('id', instance.id)
        instance.id_libro = validated_data.get('id_libro', instance.id_libro)
        instance.id_usuario = validated_data.get('id_usuario', instance.id_usuario)
        instance.fec_prestamo = validated_data.get('fec_prestamo', instance.fec_prestamo)
        instance.fec_devolucion = validated_data.get('fec_devolucion', instance.fec_devolucion)
        instance.save()
        return instance