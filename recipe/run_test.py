#!/usr/bin/env python3

def test_version():
    import sys
    import grits

    try:
        target_version=sys.argv[1]
    except IndexError:
        return
    assert grits.__version__ == target_version

if __name__ == "__main__":
    test_version()
