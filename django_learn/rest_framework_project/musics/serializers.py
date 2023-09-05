from rest_framework import serializers
from musics.models import Music

from django.utils.timezone import now

class ToUpperCaseCharField(serializers.CharField):
    def to_representation(self, value):
        return value.upper()

class MusicSerializer(serializers.ModelSerializer):
    # 新增欄位
    days_since_created = serializers.SerializerMethodField()
    # 欄位資料特別處理 轉大寫
    singer = ToUpperCaseCharField()

    class Meta:
        model = Music
        # fields = '__all__'
        fields = ('id', 'song', 'singer', 'last_modify_date', 'created', 'days_since_created')

    def get_days_since_created(self, obj):
        return (now() - obj.created).days