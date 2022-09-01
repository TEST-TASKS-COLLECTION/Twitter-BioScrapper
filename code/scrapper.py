#!/bin/python3

import argparse




if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A twitter bio scrapper")
    parser.add_argument("--handle", help="Twitter handle without the `@`")
    args = parser.parse_args()
    print(args.handle)