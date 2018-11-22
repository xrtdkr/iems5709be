# coding: utf-8

from django.utils import timezone


class TimeHandle(object):

    @staticmethod
    def time2string(timezone_obj):
        return timezone_obj.strftime("%Y-%m-%d %H:%M:%S")

    @staticmethod
    def string2time(timezone_string):
        return timezone.datetime.strptime(timezone_string, "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def get_time_now_string():
        return timezone.now().strftime("%Y-%m-%d %H:%M:%S")


