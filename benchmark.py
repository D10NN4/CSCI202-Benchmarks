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

if __name__ == "__main__":
    run_benchmarks()

