#include <stdio.h>
#include <Python.h>
#include <time.h>

/**
* print_python_bytes - print some basic info about Python bytes objects
* @p: python object
* Return: nothing
**/
void print_python_bytes(PyObject *p)
{
char *s;
Py_ssize_t len, i;

printf("[.] bytes object info\n");
if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

PyBytes_AsStringAndSize(p, &s, &len);
printf("  size: %ld\n", len);
printf("  trying string: %s\n", s);
printf("  first %ld bytes: ", len > 10 ? 10 : len);
for (i = 0; i < (len > 10 ? 10 : len); i++)
printf("%02x ", (unsigned char)s[i]);
printf("\n");
}

/**
* print_python_list - print some basic info about Python lists
* @p: python object
* Return: nothing
**/
void print_python_list(PyObject *p)
{
Py_ssize_t i;
PyObject *in_list;

if (!PyList_Check(p))
{
printf("[*] Python list info\n");
return;
}

printf("[*] Python list info\n");
printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);
for (i = 0; i < PyList_Size(p); i++)
{
in_list = PySequence_GetItem(p, i);
printf("Element %ld: %s\n", i,
in_list->ob_type->tp_name);
if (strcmp(in_list->ob_type->tp_name, "bytes") == 0)
print_python_bytes(in_list);
}
}
