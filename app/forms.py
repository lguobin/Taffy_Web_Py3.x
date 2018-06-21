# -*- coding: utf-8 -*-
"""
@author: Destroyers
@file: forms.py
@time: 2018年6月21日 05:26:14
"""

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, IntegerField, SubmitField, BooleanField
from wtforms.widgets.core import PasswordInput
from wtforms.validators import DataRequired, Email, NumberRange



class PasswordField(PasswordField):
    # 修改PasswordInput参数值显示密码
    widget = PasswordInput(hide_value=False)


class configForm(FlaskForm):
    taffy_dir = StringField("项目路径", description="不建议使用中文", validators=[DataRequired()])
    report_name = StringField("测试报告前缀", validators=[DataRequired()])
    auto_send = BooleanField("是否自动发送报告邮件")
    mail_host = StringField("邮件服务器地址", validators=[DataRequired()])
    mail_port = IntegerField("邮件服务器端口", validators=[DataRequired(), NumberRange(0, 65535)])
    mail_user = StringField("发件人地址", validators=[DataRequired(), Email()])
    mail_pwd = PasswordField("发件人密码/授权码", validators=[DataRequired()])
    mail_subject = StringField("邮件标题前缀", validators=[DataRequired()])
    mail_to = StringField("收件人地址", description='多个地址请以;分割', validators=[DataRequired()])
    submit_button = SubmitField("保存修改")
