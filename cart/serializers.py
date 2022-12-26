from rest_framework import serializers
from post.models import Post
from .models import Cart


class CartSerialzier(serializers.Serializer):
    product = serializers.IntegerField()
    count = serializers.IntegerField()

    def validate(self, attrs):
        data = {}
        try:
            product = Post.objects.get(pk=attrs['product'])
        except Post.DoesNotExist:
            raise serializers.ValidationError('Product not found!')
        count = attrs['count']
        data['count'] = count
        data['product'] = product.pk
        return data

    def save(self, **kwargs):
        data = self.validated_data
        user = kwargs['user']
        product = Post.objects.get(pk=data['product'])
        Cart.objects.create(
            product=product,
            user=user,
            count=data['count'])


class CartListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'
