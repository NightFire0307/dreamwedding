# -*- coding:utf-8 -*-
# Create By: My.Thunder
# Power By: YuXiaoyu
# 2019/4/24 12:03

from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', widget=forms.TextInput(attrs={'class': 'layui-input',
                                                                            'lay-verify': 'required',
                                                                            'placeholder': '请输入用户名',
                                                                            'autocomplete': 'off'}))
    password = forms.CharField(label='密码', widget=forms.PasswordInput(attrs={'class': 'layui-input',
                                                                            'lay-verify': 'required',
                                                                            'placeholder': '请输入密码',
                                                                            'autocomplete': 'off'}))