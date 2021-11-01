# Generated by Django 3.2.4 on 2021-09-05 21:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('item', '0001_initial'),
        ('carrinho', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('quantidade_vendida', models.FloatField()),
                ('carrinho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pedidos', to='carrinho.carrinho')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.item')),
            ],
        ),
    ]
