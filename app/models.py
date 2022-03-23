from django.db import models


class blocked_ip(models.Model):
    sus_ips = models.CharField(max_length=16)


class Announcement(models.Model):
    anouncement = models.TextField(blank=True)


class UserJob(models.Model):
    ip = models.CharField(max_length=15)
    username = models.CharField(max_length=999999)
    repo = models.CharField(max_length=999999, blank=True)
    job_title = models.CharField(max_length=999999, unique=True)
    salary = models.IntegerField()


class Customer(models.Model):
    name = models.CharField(max_length=999999)
    group_of = models.IntegerField()
    project = models.CharField(max_length=999999)
    project_description = models.TextField(max_length=9999999)
    mean_age = models.IntegerField()
    leader_name = models.CharField(max_length=999999)
    leader_age = models.IntegerField()
    expected_profit_per_week = models.IntegerField()
    needs = models.TextField(max_length=999999)


class UserTodo(models.Model):
    username = models.CharField(max_length=999999)
    todo_title = models.CharField(max_length=999999)
    due_at = models.DateField()
    remind_before_days = models.IntegerField()


class Earning(models.Model):
    day = models.DateField()
    revenue = models.IntegerField()
    expense = models.IntegerField()
