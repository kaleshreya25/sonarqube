def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def buggy_function(x):
    if x == 1:
        return True
    elif x == 2:
        return False
    else:
        print("Unexpected input!")  # intentionally noisy for SonarQube to flag
        return None

if __name__ == "__main__":
    print(add(2, 3))
    print(subtract(5, 2))
    buggy_function(3)
