
def add(*args: int) -> int:
    
    return sum(args)

def sub(x: int, y: int) -> int:
    
    return x - y

def mul(x, y):
    
    return x * y

def div(x, y):
    
    try:
        return x / y
    except ZeroDivisionError:
        return ZeroDivisionError

if __name__ == '__main__':
        
        print(add(5, 5))
        print(sub(5, 5))
        print(mul(5, 5))
        print(div(5, 5))
        
        pass
    
    
    