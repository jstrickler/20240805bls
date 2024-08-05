import os

VARIABLE_NAME = "USERNAME"

print(f"{os.environ.get(VARIABLE_NAME, "NOT FOUND") = }")

