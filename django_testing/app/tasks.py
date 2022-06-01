
from random import random
from unicodedata import name
from celery import shared_task

# from celery.utils.log import get_task_logger
# from time import sleep

# logger = get_task_logger(__name__)


@shared_task(name="sum_two_number")
def add(x, y):
    return x+y


@shared_task(name="multiply_two_numbers")
def mul(x, y):
    total = x*(y*random.randint(3, 100))


@shared_task(name="sum_list_number")
def xsum(numbers):
    return sum(numbers)
