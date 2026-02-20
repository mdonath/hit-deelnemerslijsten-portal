from config import read_config
from loader import load
from transformer import transform
from writer import write
from log import log_finished


def main():
    hit_config = read_config('hit-prod.yaml')

    df = load(hit_config)
    df = transform(df)
    write(df, hit_config)

    log_finished("Alles klaar")


if __name__ == "__main__":
    main()
