#hello_name
# Python
def greet_user(person_name: str) -> None:
    """
    Prints a greeting using the provided name.
    Args:
    - person_name (str): The name to be used in the greeting.
    """
    print(f"Hello, {person_name}!")

#check for change CTRL + F5 runs file in VS code keyboard shortcuts
person_name: str = input("Please enter a name: ")
greet_user: str = greet_user(person_name)
print(greet_user)