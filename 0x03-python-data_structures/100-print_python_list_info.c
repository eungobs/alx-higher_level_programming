#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info -prints basic info.
 * @p: a Pyobject list.
 *
 * Return: nothing.
 */

void print_python_list_info(PyObject *p)
{
long int size = PyList_Size(p);
int i;
PyListObject *obj = (PyListObject *)p;

printf("[*] Size of the Python List = %li ", size);
printf("[*] Allocated = %li ", obj->allocated);
for (i = 0; i < size; i++)
printf("Element %i: %s ", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
