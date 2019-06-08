"""
Implement the below file operations.
close() the file after each operation.
"""
def read_file(path):
    f = open(path, 'r')
    x = f.read()
    f.close()
    return x


def write_to_file(path, s):
    f = open(path, 'w+')
    f.write(s)
    f.close()


def append_to_file(path, s):
    f = open(path, 'a+')
    f.write(s)
    f.close()


def numbers_and_squares(n, file_path):
    """
    Save the first `n` natural numbers and their squares into a file in the csv format.
    Example file content for `n=3`:

    1,1
    2,4
    3,9
    """
    f=open(file_path,'w+')
    for i in range(n):
        j=i+1
        f.write("{},{}\n".format(j,j**2))
    f.close()