import numpy as np
import time
from scipy.linalg import blas as scipy_blas

def generate_matrix(n, seed=42):
    np.random.seed(seed)
    return np.random.rand(n, n).astype(np.float64)

print ('Халявка Иван Андреевич 090301ПОВа-о24')

def matmul_naive(A, B):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.float64)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i, j] += A[i, k] * B[k, j]
    return C

def matmul_optimized(A, B, block_size=64):
    n = A.shape[0]
    C = np.zeros((n, n), dtype=np.float64)
    for i in range(0, n, block_size):
        for j in range(0, n, block_size):
            for k in range(0, n, block_size):
                # Блочное перемножение
                A_block = A[i:i+block_size, k:k+block_size]
                B_block = B[k:k+block_size, j:j+block_size]
                C[i:i+block_size, j:j+block_size] += np.dot(A_block, B_block)
    return C

def benchmark_matmul(matmul_func, A, B, name):
    start_time = time.time()
    C = matmul_func(A, B)
    elapsed_time = time.time() - start_time
    n = A.shape[0]
    complexity = 2 * n ** 3
    mflops = (complexity / elapsed_time) * 1e-6
    print(f"{name}:")
    print(f"  Time: {elapsed_time:.3f} s")
    print(f"  Performance: {mflops:.2f} MFlops")
    return C

if __name__ == "__main__":
    n = 2048
    A = generate_matrix(n)
    B = generate_matrix(n)

    # 1. Наивное перемножение
    benchmark_matmul(matmul_naive, A, B, "Naive matrix multiplication")

    # 2. BLAS (Intel MKL через SciPy)
    benchmark_matmul(scipy_blas.dgemm, A, B, "BLAS (dgemm)")

    # 3. Оптимизированный алгоритм (блочное перемножение)
    benchmark_matmul(matmul_optimized, A, B, "Optimized block multiplication")

    # Проверка корректности (сравнение с BLAS)
    C_blas = scipy_blas.dgemm(1.0, A, B)
    C_opt = matmul_optimized(A, B)
    assert np.allclose(C_blas, C_opt, atol=1e-5), "Optimized algorithm gives incorrect results!"
