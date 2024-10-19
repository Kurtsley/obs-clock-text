# Brian Beard 2024

import obspython as obs
from datetime import datetime

source_name = "Time Text"
interval = 1
text_color = 0x00FF00


def update_time():
    time_text = datetime.now().strftime("%H:%M:%S %p")
    source = obs.obs_get_source_by_name(source_name)
    if source:
        settings = obs.obs_source_get_settings(source)
        obs.obs_data_set_string(
            settings, "text", f"The service starts at 11:00 AM, the current time is: {time_text}")
        obs.obs_data_set_int(settings, "color", text_color)
        obs.obs_source_update(source, settings)
        obs.obs_source_release(source)


def script_description():
    return "This script updates a text source with the current time."


def script_update(settings):
    obs.timer_add(update_time, interval * 1000)


def script_unload():
    obs.timer_remove(update_time)
