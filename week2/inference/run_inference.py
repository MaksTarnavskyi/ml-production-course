import numpy as np
from sklearn.linear_model import PassiveAggressiveClassifier
import concurrent.futures
from typing import Tuple
import time
from tqdm import tqdm
from concurrent.futures import wait
import time
from multiprocessing import Pool, cpu_count

CPU_COUNT = max(cpu_count() - 1, 1)

def train_model(x_train: np.ndarray, y_train: np.ndarray) -> PassiveAggressiveClassifier:
    clf = PassiveAggressiveClassifier()
    clf.fit(x_train, y_train)
    return clf


def get_data() -> Tuple[np.ndarray, np.ndarray, np.ndarray]:
    x_train = np.random.rand(100, 10)
    y_train = np.random.randint(2, size=100)

    x_test = np.random.rand(1_000_000, 10)
    return x_train, y_train, x_test


def predict(model: PassiveAggressiveClassifier, x: np.ndarray) -> np.ndarray:
    return model.predict(x)


def run_inference(model: PassiveAggressiveClassifier, x_test: np.ndarray, batch_size: int = 2048) -> np.ndarray:
    y_pred = []
    for i in tqdm(range(0, x_test.shape[0], batch_size)):
        x_batch = x_test[i : i + batch_size]
        y_batch = predict(model, x_batch)
        y_pred.append(y_batch)
    return np.concatenate(y_pred)


def run_inference_process_pool(model: PassiveAggressiveClassifier, x_test: np.ndarray, max_workers: int = 16) -> np.ndarray:
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        chunk_size = len(x_test) // max_workers

        chunks = []
        # split in to chunks
        for i in range(0, len(x_test), chunk_size):
            chunks.append(x_test[i : i + chunk_size])

        futures = []
        # submit chunks for inference
        for chunk in chunks:
            future = executor.submit(run_inference, model=model, x_test=chunk)
            futures.append(future)

        # wait for all futures
        wait(futures)

        y_pred = []
        for future in futures:
            y_batch = future.result()
            y_pred.append(y_batch)
    return np.concatenate(y_pred)

def run_inference_multiprocess_pool(model: PassiveAggressiveClassifier, x_test: np.ndarray, n_jobs: int = CPU_COUNT) -> np.ndarray:
    
    chunk_size = len(x_test) // n_jobs

    chunks = []
    # split in to chunks
    for i in range(0, len(x_test), chunk_size):
        chunks.append(x_test[i : i + chunk_size])

    y_pred = []
    pool = Pool(n_jobs)
    result_map = pool.map(self._preprocess_chunk_for_train, chunk_split)
    pool.close()
    pool.join()

    return np.concatenate(y_pred)


def main():
    x_train, y_train, x_test = get_data()
    print('Data generated')
    model = train_model(x_train, y_train)
    print('Model trained')

    s = time.monotonic()
    _ = run_inference(model=model, x_test=x_test)
    print(f"Inference one worker {time.monotonic() - s}")

    s = time.monotonic()
    max_workers = 16
    _ = run_inference_process_pool(model=model, x_test=x_test)
    print(f"Inference {max_workers} workers {time.monotonic() - s}")

    s = time.monotonic()
    _ = run_inference_multiprocess_pool(model=model, x_test=x_test)
    print(f"Inference {CPU_COUNT} jobs {time.monotonic() - s}")


if __name__ == "__main__":
    main()
