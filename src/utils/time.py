import random
from datetime import datetime, timedelta

def random_past_datetime(start_years_ago=8, end_years_ago=0):
    start = datetime.now() - timedelta(days=365 * start_years_ago)
    end = datetime.now() - timedelta(days=365 * end_years_ago)
    delta = end - start
    return start + timedelta(seconds=random.randint(0, int(delta.total_seconds())))

def after(dt, min_days=0, max_days=30):
    return dt + timedelta(days=random.randint(min_days, max_days))
