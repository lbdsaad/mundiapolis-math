#!/usr/bin/env python3

def np_slice(matrix, axes={}):
    return matrix[
        tuple([slice(*axes.get(ax, (None, None)))
               for ax in range(max(axes)+1)])]
