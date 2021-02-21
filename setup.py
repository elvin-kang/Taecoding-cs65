import os

root_dir = os.path.dirname(os.path.realpath(__file__))

python_script = """print("Hello World")

total = 0

for i in range(101):
    total += i  # try changing this line an submit pull request..

print(f"Sum of 1 throgh 100 is {total}")

# This is a comment
# You can try to modify
# comment

# Write your own code below
"""

for i in range(1, 11):
    path = os.path.join(root_dir, f"group_{i}")
    if not os.path.exists(path):
        os.mkdir(path)

    with open(os.path.join(path, "sample.py"), 'w') as f:
        f.write(python_script)
