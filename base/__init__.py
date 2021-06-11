""" Base app provides authentication system and opportunity to perform CRUD operations upon model's objects.

Base directory is one of the apps of this project. Functionality of this app allows users to login, logout, register to
the site. Users can create, update, delete and view posts.

This package consist of following modules and directories:
    - admin
    - apps.py
    - forms.py
    - models.py
    - signals.py
    - tests.py
    - urls.py
    - views.py
    - /migrations - stores history of app's models
    - /templates - stores templates which will be rendered and display to user by browser

When creating this package following imports have been made:
    - from django.urls import path
    - from django.db import models
    - from PIL import Image
    - from django.apps import AppConfig
    - from django.contrib import admin
    - from django import forms
    - from django.contrib.auth.models import User
    - from django.contrib.auth.forms import UserCreationForm
    - from django.dispatch import receiver
    - from django.db.models.signals import m2m_changed
    - from django.core.mail import send_mail
    - from django.contrib.auth.views import LogoutView, LoginView
    - from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
    - from django.urls import reverse_lazy
    - from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
    - from base.forms import UserRegisterForm
    - from django.contrib.auth import login
    - from django.shortcuts import redirect
"""
