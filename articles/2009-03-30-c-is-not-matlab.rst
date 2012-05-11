C is not MATLAB
===============

:date: 2009-03-30
:category: programming
:tags: c, matlab

Refactoring some code at work today, I came across a classic example of somebody attempting to use 
one language like another.  The project in question is a port from MATLAB to C, and the purpose of 
the function is to see if a square matrix is symmetrical within a certain tolerance.

The implementation I replaced worked somewhat like this:

.. code-block:: c

    int check_symmetry(double *mtx, int n, double tolerance)
    {
        /* Allocate memory to work in */
        double *mtx_trans = (double *) malloc(n * n * sizeof(double));
        double *mtx_diff = (double *) malloc(n * n * sizeof(double));

        /* Matrix transpose */
        matxtrans(mtx, n, n, mtx_trans);
        /* Matrix subtract */
        matxsub(mtx, n, n, mtx_trans, n, n, mtx_sub);

        /* Assume matrix is symmetric to start with */
        int symmetric = TRUE;

        /* Iterate through rows */
        for (int i = 0; i < n; ++i)
        {
            /* Iterate through columns */
            for (int j = 0; j < n; ++j)
            {
                /* Was the difference greater than the tolerance? */
                double val = mtx_sub[i * n + j];
                if (fabs(val) > tolerance)
                {
                    /* Exception found: matrix not symmetric
                     * (but notice that we keep looping...) */
                    symmetric = FALSE;
                }
            }
        }

        /* Clean up memory allocations */
        free(mtx_trans);
        free(mtx_diff);

        /* ... and return the result */
        return symmetric;
    }

Now, what this is really doing is the equivalent to the following line of MATLAB:

.. code-block:: matlab

    symmetric = max(abs(mtx - mtx')) > tol;

This in itself highlights the massive differences between MATLAB, where matrix operations are 
fundamental, and C, where they are not.  While the above C code gets the correct answer, it's far 
from efficient.  What should be obvious is that the programmer translated the code, not the meaning.

To analyse this simple case: a symmetric matrix is reflected in the diagonal---the lower triangle is 
the same as the upper.  What we really are trying to find out is if any elements violate this 
constraint.  More verbosely: "does any element in the upper triangle differ from it's corresponding 
element in the lower triangle (by more than a certain value)?"  Once we've figured this out, the 
operation in C is much, much shorter:

.. code-block:: c

    int check_symmetry(double *mtx, int n, double tolerance)
    {
        /* Iterate through upper triangle only */
        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                /* Compare to lower triangle */
                if (fabs(mtx[i * n + j] - m[j * n + i]) > tolerance)
                    /* Exception found: matrix not symmetric */
                    return FALSE;
        /* No exceptions found: matrix is symmetric */
        return TRUE;
    }

This achieves the minimum number of iterations and element accesses by ignoring the diagonal, only 
iterating through the upper triangle and reversing the indices to access the lower triangle.  The 
only potential downside is that it's not as obvious what's going on, but *that's what comments are 
for!*

The lesson is that you should always make sure you're using the correct method for the tool, and not 
trying to hammer a screw in with a spanner.
