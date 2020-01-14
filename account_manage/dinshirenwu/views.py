from django.shortcuts import render
import os
from apscheduler.schedulers.blocking import BlockingScheduler
import datetime
import requests
from account_list.models import Accounts,User_account
from django.contrib.auth.models import User
# Create your views here.

