<<<<<<< HEAD
/*
* File: 100-print_python_list_info.c

*/

#include <Python.h>

/**
* print_python_list_info - Prints basic info about Python lists.
* @p: A PyObject list.
*/
void print_python_list_info(PyObject *p)
=======
#include <Python.h>

<<<<<<< HEAD
/**
* print_python_list_info - Prints basic info about Python lists.
* @p: A PyObject list.
*/

void print_python_list_info(PyObject *p)
=======
void print_python_list_info(PyObject *p);
>>>>>>> 28d65fe447305dfdae639c63a4f73abec69dad0b
>>>>>>> 45fb2f01a550cc27fd4bf0b55c8bcbe224fc6bbb
{
int size, alloc, i;
PyObject *obj;

size = Py_SIZE(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*] Size of the Python List = %d ", size);
printf("[*] Allocated = %d ", alloc);

for (i = 0; i < size; i++)
{
printf("Element %d: ", i);

obj = PyList_GetItem(p, i);
printf("%s ", Py_TYPE(obj)->tp_name);
}
}
