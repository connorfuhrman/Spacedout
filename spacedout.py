"""Script to deal with spaces on an environmental variable."""

import os
import logging


def main(env_var: str) -> None:
    """Deal with spaces in a path."""
    logging.debug("Getting variable %s", env_var)
    var = os.environ.get(env_var)
    if var is None:
        raise ValueError(f"{env_var} is not set as an environmental variable")
    logging.debug("Got variable!")
    logging.debug("Variable contents are %s", var)
    fixed = do_fix(var)
    var = ':'.join(fixed)
    logging.info("Setting %s as %s", env_var, var)
    print(f"export {env_var}={var}")


def do_fix(contents: str) -> None:
    """Replace spaces with escape sequence."""
    paths = contents.split(':')
    fixed = []
    for p in paths:
        logging.debug("Path before fix: %s", p)
        if ' ' in p:
            logging.debug("This path contains a space!")
            p = p.replace(' ', '\ ')  # noqa W605  Yes I know this is an invalid escape sequence
            logging.debug("Replaced with %s", p)
        fixed.append(f"'{p}'")
    return fixed


def _do_test():
    test_var = "/opt/rh/devtoolset-9/root/usr/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/usr/lib/wsl/lib:/mnt/c/WINDOWS/system32:/mnt/c/WINDOWS:/mnt/c/WINDOWS/System32/Wbem:/mnt/c/WINDOWS/System32/WindowsPowerShell/v1.0/:/mnt/c/WINDOWS/System32/OpenSSH/:/mnt/c/Program Files/Docker/Docker/resources/bin:/mnt/c/Program Files/PuTTY/:/mnt/c/Users/ConnorFuhrman/AppData/Local/Microsoft/WindowsApps:/mnt/c/Users/ConnorFuhrman/AppData/Local/Programs/Microsoft VS Code/bin:/home/connorfuhrman/.local/bin:/home/connorfuhrman/bin"  # noqa E501  Yes this is too long... deal with it!
    os.environ["SPACEDOUT_TEST"] = test_var
    main("SPACEDOUT_TEST")


def _test():
    logging.basicConfig(level=logging.DEBUG)
    _do_test()


if __name__ == '__main__':
    from sys import argv
    main(argv[1])
