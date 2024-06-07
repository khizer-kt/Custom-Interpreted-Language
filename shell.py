import lang

print("Lang Version 0")
while True:
    text = input('lang-> ')
    result, error = lang.run('<stdin>', text)

    if error: 
        print(error.as_string())
    else: 
        print(result)