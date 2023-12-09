from django.db import models


def on_delete():
    pass


class List(models.Model):
    """Список пунктов"""
    pass


class Item(models.Model):
    """Элемент списка"""
    text = models.TextField(default="")

    list = models.ForeignKey(List, default=None, on_delete=on_delete)


