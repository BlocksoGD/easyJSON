easyJSON v1.0

This module provides simple helpers for reading and writing JSON files in Python.

Functions:

1️⃣ getJson(path)
   • Reads a JSON file from the given file path.
   • Returns: a Python dictionary.
   • Usage:
       data = getJson("file.json")

2️⃣writeJson(data, path, indent=0, returnMessage=False)
   • Writes a Python dictionary to a JSON file at the given path.
   • Parameters:
       - data: the Python dictionary to save.
       - path: the target file path.
       - indent: (optional, default 0) number of spaces to indent JSON output.
       - returnMessage: (optional, default False) if True, prints a success message.
   • Returns: None.

Made by Blockso.
