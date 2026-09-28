# Week 6 Assignment

- **safe_tools.py**: Contains safe functions for division, number conversion, and dictionary lookup.
- **unbreakable.py**: Contains the test code for the functions.

## Question: Why can the if check not catch abc on its own?

A standard if check cannot catch abc because abc is a string, not a number. The if statement simply evaluates a condition as True or False. It does not attempt to convert or parse data types. To catch invalid input like abc, you need to try to convert it (e.g., using int()) and except the ValueError that occurs when Python fails to convert the string into an integer.