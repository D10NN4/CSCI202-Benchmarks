import time

def run_benchmarks():
    # 32-bit Integer operation benchmark
    # Reference time: 100 seconds
    print("Starting 32-bit Integer Benchmark...")
    
    start_time = time.time()

    # Math loops›
    a, b = 10, 20
    # 10^10 additions
    for _ in range(10**10):
        c = a + b
    # 5 * 10^9 multiplications
    for _ in range(5 * 10**9):
        c = a * b
    # 2 * 10^9 divisions
    for _ in range(2 * 10**9):
        c = a / b
    
    end_time = time.time()
    print(f"Total time: {end_time - start_time} seconds")

    print("Starting 64-bit Floating Point Benchmark...")
    
    start_float = time.time()
    
    x, y = 10.5, 20.5
    # 10^10 additions
    for _ in range(10**10):
        z = x + y
    # 5 * 10^9 multiplications
    for _ in range(5 * 10**9):
        z = x * y
    # 2 * 10^9 divisions
    for _ in range(2 * 10**9):
        z = x / y
        
    end_float = time.time()
    print(f"Floating Point Total time: {end_float - start_float} seconds")

if __name__ == "__main__":
    run_benchmarks()

