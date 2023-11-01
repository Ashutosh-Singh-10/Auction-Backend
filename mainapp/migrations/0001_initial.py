# Generated by Django 4.1.1 on 2023-05-05 08:26

from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuctionRoom',
            fields=[
                ('productName', models.CharField(max_length=50)),
                ('productDetail', models.CharField(max_length=150)),
                ('productPhoto', models.ImageField(null=True, upload_to='auctionItemPic/')),
                ('roomId', models.CharField(default=mainapp.models.roomIdGeneration, max_length=8, primary_key=True, serialize=False)),
                ('startTime', models.DateTimeField(auto_now_add=True)),
                ('endTime', models.DateTimeField(null=True)),
                ('bidDiff', models.IntegerField(default=500)),
                ('upperLimit', models.IntegerField(default=1000000)),
                ('lowerLimit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('email', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('otp', models.CharField(max_length=6)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254)),
                ('userId', models.CharField(default=mainapp.models.randomUserIdGeneration, max_length=254, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=50)),
                ('firstName', models.CharField(max_length=30)),
                ('lastName', models.CharField(blank=True, max_length=30, null=True)),
                ('userPhoto', models.ImageField(null=True, upload_to='profilePic/')),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidPrice', models.IntegerField()),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.auctionroom')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='auctionroom',
            name='roomOwner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user'),
        ),
    ]
