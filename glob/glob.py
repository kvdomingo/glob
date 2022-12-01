import os
import sys
from pathlib import Path
from loguru import logger


def main():
    if len(in_1 := sys.argv[1:2]) == 0:
        logger.error("Missing glob")
        sys.exit(1)
    print(*Path(os.getcwd()).resolve().glob(in_1[0]), sep="\n")


if __name__ == "__main__":
    main()
