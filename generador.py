#! /C:\Users\Admin\AppData\Local\Microsoft\WindowsApps\python.exe

def my_generator(n):
    Value = 0
    while Value < n:
        yield Value # Produce current
        Value += 1 #Increment counter

if __name__ == "__main__":
    
    for item in my_generator(10000):
        print(item)