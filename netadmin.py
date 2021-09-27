import argparse

class Netadmin:
    def __init__(self):
        pass


#netadmin

def main(self):
    cli = argparse.ArgumentParser('NETADMIN MODULE')
    cli.add_argument(dest='--config',default='./config/input.json')
    cli.parse_args()

    pass

if "__name__" == "__main__":
    main()

