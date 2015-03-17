# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        (b'auth', b'__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tahun_Akademik',
            fields=[
                ('kode_tahun_akademik', models.AutoField(serialize=False, primary_key=True)),
                ('nama_tahun_akademik', models.CharField(max_length=9)),
                ('semester', models.CharField(default=b'1', max_length=1, choices=[(b'1', b'Ganjil'), (b'0', b'Genap')])),
                ('status', models.CharField(default=b'N', max_length=1, choices=[(b'A', b'Aktif'), (b'N', b'Tidak Aktif')])),
                ('created_by', models.IntegerField(null=True)),
                ('updated_by', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name=b'Tgl Dibuat')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name=b'Tgl Diubah')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
