# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-03-05 04:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_delete_models'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='image_decl',
            unique_together=set([('name', 'tag')]),
        ),
        migrations.AlterUniqueTogether(
            name='networkslice_decl',
            unique_together=set([('network', 'slice')]),
        ),
        migrations.AlterUniqueTogether(
            name='port_decl',
            unique_together=set([('network', 'service_instance')]),
        ),
        migrations.AlterUniqueTogether(
            name='serviceinstanceattribute_decl',
            unique_together=set([('name', 'service_instance')]),
        ),
    ]