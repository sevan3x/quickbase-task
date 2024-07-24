#!/usr/bin/python3

import getopt
import sys

from processor import process


def main():
    args = _parse_arguments(sys.argv[1:])
    process(args['github_username'], args['subdomain'])


def _parse_arguments(argv):
    arguments_to_return = {
        "github_username": None,
        "subdomain": None,
    }

    try:
        opts, args = getopt.getopt(argv, "hu:s:", ["github_username=", "subdomain="])
    except getopt.GetoptError:
        print('quickbase_task.py -u <github_username> -s <subdomain>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('quickbase_task.py -u <github_username> -s <subdomain>')
            sys.exit()
        elif opt in ("-u", "--github_username"):
            arguments_to_return["github_username"] = arg
        elif opt in ("-s", "--subdomain"):
            arguments_to_return["subdomain"] = arg

    if arguments_to_return["github_username"] and arguments_to_return["subdomain"]:
        return arguments_to_return
    elif not arguments_to_return["github_username"] and arguments_to_return["subdomain"]:
        print("Please provide a Github username")
    elif arguments_to_return["github_username"] and not arguments_to_return["subdomain"]:
        print("Please provide a subdomain")
    else:
        print("Error while executing. Please use as follows:")
        print('quickbase_task.py -u <github_username> -s <subdomain>')

    sys.exit()


if __name__ == '__main__':
    main()
