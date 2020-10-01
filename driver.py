import numpy as np
import logging  # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial


import wahoovian


def main():
    logging.info("program has started")
    # Using Python's built-in logging.

    # Configure the logger: The options on the first line matter most.
    #   The second line clear the log-file everytime the program runs.
    #   The last two lines add a time-stamp in a format I like.
    logging.basicConfig(filename='demo-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')


    # nump arrays as matrices and do matrix-addition.
    m1 = np.array([[2, 4], [5, -6]])
    m2 = np.array([[9, -3], [3, 6]])


    logging.info('Beginning matrix operations!')
    
    new_m1 = wahoovian.wahoovian(m1)
    print("Before:\n", m1, "\nAfter wahoovian:\n", new_m1)
    new_m2 = wahoovian.wahoovian(m2)
    print("Before:\n", m2, "\nAfter wahoovian:\n", new_m2)
    
    logging.info("Program ends!")



if __name__ == '__main__':
    main()

