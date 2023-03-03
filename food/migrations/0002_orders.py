# Generated by Django 4.1.7 on 2023-03-03 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(blank=True, choices=[('A', 'Accepted'), ('R', 'Rejected'), ('F', 'Finished'), ('D', 'Delivered')], max_length=40, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.cart')),
                ('dish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.dishes')),
                ('restaurant_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='food.restaurant')),
            ],
        ),
    ]