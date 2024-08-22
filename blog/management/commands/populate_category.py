from blog.models import Category
from typing import Any
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "This command inserts post data"

    def handle(self, *args: Any, **options:Any):
       Category.objects.all().delete()
       
       categories=["Sports","Tech","Arts","Science","Food"]

       for category_name in categories:
           Category.objects.create(name=category_name)

