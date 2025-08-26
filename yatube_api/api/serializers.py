from rest_framework import serializers
from django.contrib.auth import get_user_model
from posts.models import Comment, Post, Follow, Group

User = get_user_model()


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username', read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('author', 'post')


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, data):
        user = self.context['request'].user
        following = data['following']

        if user == following:
            raise serializers.ValidationError("Нельзя подписаться " \
            "на самого себя.")
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError("Вы уже подписаны " \
            "на этого пользователя.")
        return data

    def create(self, validated_data):
        user = self.context['request'].user
        following = validated_data['following']
        follow = Follow.objects.create(user=user, following=following)
        return follow
