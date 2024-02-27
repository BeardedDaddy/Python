def greet_pythons(items: list) -> None:
    greeting = 'Hello'
    print(f'The ID of "greeting" in "greet_python" is {id(greeting)}')
    print(f'local namespace in "greet_python"(1): {locals()}')
    
    def make_greeting(item: str) -> str: # This a nested funtion which also makes it a local namespace  # noqa
        nonlocal greeting
        print(f'local namespace in "make_greeting"(1): {locals()}')
        greeting = 'Hi'
        print(f'The ID of "greeting" in "make_greeting" is {id(greeting)}')
        print(f'local namespace in "greet_python"(2): {locals()}')
        return f'{greeting} {item}'

    for item in items:
        print(make_greeting(item))
    print(f'Inside greet_pythons, "greeting" is {greeting}')
    print(f'The ID of "greeting" in "greet_python" is {id(greeting)}')
    print(f'local namespace in "greet_python"(1): {locals()}')
    

names = ['John']  # , 'Eric', 'Graham', 'Terry', 'Terry', 'Michael']

greet_pythons(names)
print(f'local namespace in "greet_python"(1): {locals()}')
