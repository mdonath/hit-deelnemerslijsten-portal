import math
import os

import pandas as pd

from config import current_property, current_year

def create_password_kamp(kamp, hit_config):
    jaar = current_year(hit_config)
    return f"HIT{jaar}-{math.prod([ord(x) for x in kamp.lower()]) % jaar}"


def create_password_plaats(plaats, hit_config):
    jaar = current_year(hit_config)
    pincode = current_property(hit_config, 'pincodes')[plaats]
    return f"HIT-{plaats}-{jaar}-{pincode}"


def write_password_file(output_path, passwords, hit_config):
    df = pd.DataFrame({
        'Kamp': list(passwords.keys()),
        'Password': list(passwords.values()),
    })
    df.to_markdown(os.path.join(output_path, current_property(hit_config, 'passwords_file')), index=False)
