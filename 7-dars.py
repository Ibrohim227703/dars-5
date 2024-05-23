class FibonacciIterator:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        fib = self.a
        self.a, self.b = self.b, self.a + self.b
        return fib

fib_iter = FibonacciIterator()
for i, fib in zip(range(10), fib_iter):
    print(fib)





def fibonacci_generator():
    a, b = 0, 1
    try:
        while True:
            next_val = yield a
            if next_val is not None:
                a, b = next_val
            else:
                a, b = b, a + b
    except GeneratorExit:
        print("Generator closed")

fib_gen = fibonacci_generator()
for a in range(10):
    print(next(fib_gen))

fib_gen.send((10, 10))

print(next(fib_gen))
print(next(fib_gen))

fib_gen.throw(ValueError, "Some error")
fib_gen.close()



