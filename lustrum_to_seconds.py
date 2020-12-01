# WAY 1
seconds_minute = 60
hour_seconds = seconds_minute * 60
day_seconds = hour_seconds * 24
year_seconds = day_seconds * 365
lustrum_seconds = year_seconds * 5

print("Un lustro tiene", lustrum_seconds, "segundos.")

# WAY 2
year_to_seconds = 31536000
lustrum_to_seconds = 5 * year_to_seconds

print("Un lustro tiene", lustrum_to_seconds, "segundos.")