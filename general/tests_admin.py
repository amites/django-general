#!/usr/bin/env python
# -*- coding: utf-8 -
#
# @contact: marcoberi@gmail.com
# @version: 1.0
# @license: MIT http://www.opensource.org/licenses/mit-license.php
#

from django.db.models.base import ModelBase
from django.core.urlresolvers import reverse, NoReverseMatch
from django.contrib import admin
from django.contrib.auth.models import User

def adminviews_test(self, user=None, password=None):
    '''
    Auto test Admin add and changelist views.
    Original: http://djangosnippets.org/snippets/2518/

    Usage - Add the following to your tests.py:
        from django.test import TestCase
        from general.tests_admin import adminviews_test

        class TestAdminViews(TestCase):
            def test_admin_views(self):
                adminviews_test(self)
    '''
    if user is None:
        if password is None:
            password = "test"
        user = User.objects.create_superuser('test', 'test@test.com', password)
    self.client.login(username = user.username, password = password)
    pkg = self.__module__.rpartition('.')[0]
    models_mod = __import__(pkg + ".models")
    if not getattr(models_mod, "models", None):
        return
    for id_ in dir(models_mod.models):
        model = getattr(models_mod.models, id_)
        # Get ModelAdmin for this Model
        if isinstance(model, ModelBase) and model._meta.app_label == pkg and model in admin.site._registry:
            try:
                # Prevent error 405 if model_admin.has_add_permission always return False
                if admin.site._registry[model].has_add_permission(type("request", (), {"user": user})):
                    url = reverse("admin:%s_%s_add" % (model._meta.app_label, model._meta.module_name))
                    response = self.client.get(url, follow = True)
                    self.failUnlessEqual(response.status_code, 200,
                        "%s != %s -> %s, url: %s" % (response.status_code, 200, repr(model), url))
                    self.assertFalse("this_is_the_login_form" in response.content,
                        "login requested for %s" % str(model))
                url = reverse("admin:%s_%s_changelist" %
                              (model._meta.app_label, model._meta.module_name))
                response = self.client.get(url, follow = True)
                self.failUnlessEqual(response.status_code, 200,
                    "%s != %s -> %s, url: %s" % (response.status_code, 200, repr(model), url))
                self.assertFalse("this_is_the_login_form" in response.content,
                    "login requested for %s" % str(model))
            except NoReverseMatch:
                continue