
GREEN = "\033[0;32m"
LIGHT_GREEN = "\033[1;32m"
END = "\033[0m"

def log_ok(txt):
    print(f"{GREEN}{txt}{END}")

def log_finished(txt):
    print(f"{LIGHT_GREEN}{txt}{END}")