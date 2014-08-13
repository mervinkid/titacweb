#coding=utf-8
__author__ = 'Mervin'
from django.db import models

class GlobalSettingManager(models.Manager):
    def get_settings(self):
        setting_list =  self.get_queryset().all()
        settings = {}
        for setting_item in setting_list:
            settings[str(setting_item.key)] = str(setting_item.value)
        return settings

class SlideManager(models.Manager):
    def get_enabled_slide(self):
        return self.get_queryset().filter(enable=1).order_by('-update')

class SolutionManager(models.Manager):
    def get_enabled_solution(self):
        return self.get_queryset().filter(enable=1)

    def get_solution_by_id(self, solution_id):
        try:
            return self.get_queryset().get(id=solution_id)
        except Exception:
            return None

