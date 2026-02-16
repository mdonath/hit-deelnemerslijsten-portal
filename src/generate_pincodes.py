from random import randint
import yaml

from config import current_property, current_year, read_config


def main():
    plaatsen = [
        'Alphen',
        'Dwingeloo',
        'Harderwijk',
        'Heerenveen',
        'Nijmegen',
        'Ommen',
        'Zandvoort',
        'Zeeland'
    ]

    hit_config = read_config()
    jaar = current_year(hit_config)
    new_pin_codes = {plaats: str(random_with_N_digits(6)) for plaats in plaatsen}
    new_full_passwords = {f"{plaats}_full": f"HIT-{plaats}-{jaar}-{new_pin_codes[plaats]}" for plaats in plaatsen}
    
    current_property(hit_config, 'pincodes').update(new_pin_codes | new_full_passwords)

    with open('hit2.yaml', 'w') as f:
        yaml.dump(hit_config, f)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


if __name__ == "__main__":
    main()

