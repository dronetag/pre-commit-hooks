import logging
import os
import sys
import itertools

from pathlib import Path
from typing import Sequence

from .utils import CalledProcessError, cmd_output


def has_domain_in_email(domain: str) -> bool:
    try:
        email = cmd_output('git', 'config', '--get', 'user.email')
    except CalledProcessError:
        return False
    return email.strip().endswith(f"@{domain}")


def main(argv: Sequence[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]
    if len(argv) == 0:
        logging.error("Please provide an email domain to check")
        return 1
    if os.getenv("CI") is not None:
        logging.info("CI: Skipping email domain check")
        return 0
    domains = itertools.takewhile(lambda a: not Path(a).exists(), argv)
    return 0 if any(map(has_domain_in_email, domains)) else 1


if __name__ == '__main__':
    raise SystemExit(main())
