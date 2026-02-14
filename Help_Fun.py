import random
import re
from time import sleep

from Pre import *

def safe_delay():
    delay = random.uniform(DELAY_MIN, DELAY_MAX)
    print(f" wait {delay:.1f} seconds ")
    sleep(delay)


def is_recent(date_text):
    if "دقيقة" in date_text or "دقائق" in date_text:
        return True
    if "ساعة" in date_text or "ساعات" in date_text:
        return True
    if "أمس" in date_text:
        return MAX_DAYS >= 1

    if "يوم" in date_text or "أيام" in date_text:
        num = re.findall(r'\d+', date_text)
        if num:
            return int(num[0]) <= MAX_DAYS

    return False



def is_owner(ad_text):
    if "مستخدم خاص" in ad_text:
        return True
    return False
