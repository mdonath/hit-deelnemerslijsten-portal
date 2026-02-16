
GREEN = "\033[0;32m"
LIGHT_GREEN = "\033[1;32m"
END = "\033[0m"

def log_ok(txt):
    """Logt een bericht in het groen, om aan te geven dat iets goed is gegaan."""
    print(f"{GREEN}{txt}{END}")


def log_finished(txt):
    """Logt een bericht in het lichtgroen, om aan te geven dat iets klaar is."""
    print(f"{LIGHT_GREEN}{txt}{END}")
