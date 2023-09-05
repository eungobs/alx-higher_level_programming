#include <Python.h>

/**
 * print_python_string - Print information about a Python string.
 * @p: A pointer to the Python object to be printed.
 *
 * This function prints information about a Python string, including its type,
 * length, and value. If @p is not a valid Python string, it prints an error message.
 */
void print_python_string(PyObject *p) 
{
    if (PyUnicode_Check(p)) 
    {
        const char *type = "compact unicode object";
        
        Py_ssize_t length = PyUnicode_GET_SIZE(p);

        const wchar_t *str_data = PyUnicode_AsWideCharString(p, &length);

        printf("[.] string object info\n");
        printf("  type: %s\n", type);
        printf("  length: %zd\n", length);
        printf("  value: %ls\n", str_data);

        PyMem_Free(str_data);
    } 
    else 
    {
        printf("[.] string object info\n");
        printf("  [ERROR] Invalid String Object\n");
    }
}
