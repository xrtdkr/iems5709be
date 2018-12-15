# coding: utf-8

from django.utils import timezone
from ierg4210Be.settings import SALT
from hashlib import sha1


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


def password_hash(string):
    return sha1(string + SALT).hexdigest()


def password_verify(password, password_hashed):
    if sha1(password + SALT).hexdigest() == password_hashed:
        return True

    else:
        return False
