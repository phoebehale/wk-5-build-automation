import logging 
import numpy as np

#matrix = np.matrix([1,2],[3,4])

def wahoovian(m):
    logging.info("entering wahoovian function")
    rows, columns = m.shape
    if rows != columns: #if not square
        logging.warning("function not square")
        return m
    matrix = m.T
    negative = np.negative(matrix)
    return negative