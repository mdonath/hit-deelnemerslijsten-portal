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

    hit_config = read_config('hit.yaml')
    jaar = current_year(hit_config)
    new_pin_codes = {plaats: str(random_with_N_digits(6)) for plaats in plaatsen}
    
    current_property(hit_config, 'pincodes').update(new_pin_codes)

    with open('hit-prod.yaml', 'w') as f:
        yaml.dump(hit_config, f, sort_keys=False)


def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)


if __name__ == "__main__":
    main()

