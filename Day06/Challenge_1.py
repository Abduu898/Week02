import time

def power(i,j):
    result =1
    for _ in range(j):
        result *=i
    return result



start = time.time()
result = power(42, 84)
elapsed = time.time() - start

print(result)
print(f"{elapsed:.6f}")