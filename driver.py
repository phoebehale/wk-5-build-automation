import numpy as np
import logging  # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

#import greeter_lib  # Our local library with greeter()
import wahoovian

# The following is the preferred and accepted ("Pythonesque") way to divide a  program
# into multiple files:
#   (1) In the "main" file to be run, put all code that executes in function main()
#   (2) Put your own utlility or helper functions in a separate file that's imported,
#       like greeter_lib.py here.
#   (3) In the "main" file to be run, use the if-statement at the bottom of this file.


def main():
    logging.info("program has started")
    # Using Python's built-in logging.
    # See https://docs.python.org/3/howto/logging.html#logging-basic-tutorial

    # Configure the logger: The options on the first line matter most.
    #   The second line clear the log-file everytime the program runs.
    #   The last two lines add a time-stamp in a format I like.
    logging.basicConfig(filename='demo-log.txt', level=logging.DEBUG,
                        filemode='w',
                        format='%(asctime)s %(levelname)-8s %(message)s',
                        datefmt='%m/%d/%Y %H:%M:%S')

    # logging.debug('This message should go to the log file')
    # logging.info('So should this')
    # logging.warning('And this, too')

    logging.info('Program begins!')

    #greeter_lib.greeter("Our program begins!")

    # Let's use nump arrays as matrices and do matrix-addition.
    m1 = np.array([[2, 4], [5, -6]])
    m2 = np.array([[9, -3], [3, 6]])
    m3 = m1 + m2  # element wise addition
    print(m3)

    logging.info('Beginning matrix operations!')
    
    new_m1 = wahoovian.wahoovian(m1)
    print("Before:\n", m1, "\nAfter wahoovian:\n", new_m1)
    new_m2 = wahoovian.wahoovian(m2)
    print("Before:\n", m2, "\nAfter wahoovian:\n", new_m2)
    
    logging.info("Program ends!")






if __name__ == '__main__':
    main()

# What's the magic of the code right before this?
#    If this file is named main.py and it's run with:  python main.py
#       then the if is True and main() is executed.
#    But, if this file is imported then the method main() is defined but not executed.

