
import os
import time
import argparse


parser = argparse.ArgumentParser(description='delete files older than a days')
parser.add_argument('-a', '--age', type=int, action='store', dest='age', help='age of files')
parser.add_argument('-p', '--path', type=str, action='store', dest='path', help='path to folder')
parser.add_argument('-s', '--save_last', type=int, action='store', dest='save_last', help='save last s files')
args = parser.parse_args()
current_time = time.time()

def file_del(path):

    files = os.listdir(path)
    for file in sorted(os.listdir(path), key=lambda x: os.path.getctime(path + '/' + x))[:-args.save_last]:
        creation_time = os.path.getctime(path + '/' + file)
        if os.path.isfile(path + '/' + file) and (current_time - creation_time) // (24 * 3600) >= args.age:
            os.unlink(path + '/' + file)
            print('{} removed'.format(file))
    return 0


if __name__ == '__main__':
    file_del(args.path)

