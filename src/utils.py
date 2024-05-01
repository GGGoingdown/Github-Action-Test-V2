import datetime

# Create UTC datetime
def create_utc_datetime():
    return datetime.datetime.now(datetime.timezone.utc)