import time
import array

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

    # 3. Memory benchmark
    # Reference time: 100 seconds
    print("Starting Memory Benchmark...")
    
    # We use a smaller size (10^8) to fit in MacBook RAM 
    # and will scale the result in the report.
    mem_size = 10**8 
    # Create an array of 4-byte integers
    mem_array = array.array('I', [0] * mem_size)
    
    start_mem = time.time()
    
    for i in range(mem_size):
        # Read from array
        temp = mem_array[i]
        # Write to array
        mem_array[i] = 1
        
    end_mem = time.time()
    print(f"Memory Total time: {end_mem - start_mem} seconds")

    # 4. Hard Drive Benchmark 1 (100 byte blocks)
    print("Starting Hard Drive Benchmark 1...")
    block_size_1 = 100
    file_size = 10**9 # 1GB
    
    start_hd1 = time.time()
    # Write
    with open("test1.bin", "wb") as f:
        data = b"0" * block_size_1
        for _ in range(file_size // block_size_1):
            f.write(data)
    # Read
    with open("test1.bin", "rb") as f:
        for _ in range(file_size // block_size_1):
            f.read(block_size_1)
    end_hd1 = time.time()
    print(f"HD Benchmark 1 Total time: {end_hd1 - start_hd1} seconds")

if __name__ == "__main__":
    run_benchmarks()

