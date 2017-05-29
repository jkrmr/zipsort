import sys

from zipsort.zipsort import ZipSort

if __name__ == '__main__':
    usage = """
    Usage: python zipsort.py INPUT_FILE_PATH

    Example:
        python zipsort.py data/sample.txt

    Alternatively, stream input from stdin:

    cat INPUT_FILE_PATH | python zipsort.py
    """
    try:
        path_to_input = sys.argv[1]
        input_list = open(path_to_input).read()
    except IndexError:
        input_list = sys.stdin.read()
    except FileNotFoundError:
        print('Invalid input path: %s' % path_to_input)
        print(usage)
        exit(1)

    sorted = ZipSort(input_list).zip_sorted()
    sys.stdout.write('%s\n' % sorted)
