# To run with available gpus:
# ```
# python3 demo2.py --target nvidia
# ```
# To run with cpu (very slow):
# ```
# python3 demo2.py
# ```
# The CPU run is so slow that it feels
# like it's hanging.


import cudaq

def ghz_state(N):

    kernel = cudaq.make_kernel()
    q = kernel.qalloc(N)

    kernel.h(q[0])
    for i in range(N - 1):
      kernel.cx(q[i], q[i + 1])

    kernel.mz(q)
    return kernel

n = 30
print("Preparing GHZ state for", n, "qubits.")
kernel = ghz_state(n)
counts = cudaq.sample(kernel)
counts.dump()
