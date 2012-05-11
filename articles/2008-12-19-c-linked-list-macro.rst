C linked list macro
===================

:date: 2008-12-19
:category: programming
:tags: c

Here's a simple macro I came up with a few weeks ago for easily defining linked list types in C:

.. code-block:: c

    #define LINKED_LIST(type, name)     \
        struct name ## _ {              \
            struct name ## _ * next;    \
            type data;                  \
        };                              \
        typedef struct name ## _ name;

Usage is simple:

.. code-block:: c

    LINKED_LIST(int, int_ll);

gives the same type as:

.. code-block:: c

    struct int_ll_ {
        struct int_ll_ * next;
        int data;
    };
    typedef int_ll_ int_ll;
