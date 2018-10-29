# coding: utf-8


def assemble_success_msg(data):
    return {
        "msg": "success",
        "data": data,
    }


def assemble_fail_msg(data):
    return {
        "msg": "fail",
        "data": " ",
    }
