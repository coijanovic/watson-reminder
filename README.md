# Watson-Reminder

Minimal script that sends you a notification if your [Watson](https://github.com/TailorDev/Watson) timetracker is not active within working hours.
Run this script at an interval of your choice (e.g., using a cronjob or systemd timer).

## Config

You can edit your working days and hours directly in the script (`watson-reminder.py`):

- `WORKING_DAYS`: List of weekdays as integers (Monday = 0)
- `START_HOUR`: Starting hour as integer (24h format)
- `END_HOUR`: Ending hour as integer (24h format)
