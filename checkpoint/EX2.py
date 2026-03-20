import os
import pickle
import random
import time
from multiprocessing import Process, Lock

CHECK_DIR = "checkpoints/"
if not os.path.exists(CHECK_DIR):
    os.makedirs(CHECK_DIR)


def save_checkpoint(process_id, state, checkpoint_number):
    """ Save the process state to a unique checkpoint file. """
    checkpoint_file = os.path.join(CHECK_DIR, f"checkpoint_{process_id}_{checkpoint_number}.pkl")
    with open(checkpoint_file, "wb") as f:
        pickle.dump(state, f)
    print(f"Checkpoint {checkpoint_number} saved for Process {process_id}: {state}")


def load_last_checkpoint(process_id):
    """ Load the last checkpoint for a given process. """
    checkpoints = [f for f in os.listdir(CHECK_DIR) if f.startswith(f"checkpoint_{process_id}")]
    if not checkpoints:
        return {"task_count": 0}  # If no checkpoint exists, start fresh

    # Sort and load the latest checkpoint
    checkpoints.sort()
    latest_checkpoint = checkpoints[-1]
    with open(os.path.join(CHECK_DIR, latest_checkpoint), "rb") as f:
        state = pickle.load(f)
    print(f"Loaded last checkpoint for Process {process_id}: {state}")
    return state


def worker_process(process_id, lock):
    """ Simulate a worker process with multiple checkpoints. """
    try:
        # Load the last checkpoint for this process
        state = load_last_checkpoint(process_id)
        task_count = state["task_count"]
        checkpoint_number = 1  # Start checkpoint numbering

        while task_count < 10:  # Limit task to 10 iterations
            # Simulate work by incrementing task_count
            task_count += 1
            print(f"Process {process_id} working: Task count = {task_count}")

            # Periodically save progress as an incremental checkpoint
            if task_count % 3 == 0:  # Save checkpoint every 3 iterations
                with lock:
                    state["task_count"] = task_count
                    checkpoint_number = task_count // 3
                    save_checkpoint(process_id, state, checkpoint_number)
                    # checkpoint_number += 1  # Increment checkpoint number

            # Simulate random failure (20% chance)
            if random.random() < 0.2:
                print(f"Process {process_id} crashed!")
                raise Exception("Process crash simulation.")

            time.sleep(1)  # Simulate work delay
    except Exception as e:
        print(f"Process {process_id} failure: {e}")
        # Simulate restart after crash by reloading last checkpoint
        worker_process(process_id, lock)


def main():
    processes = []
    lock = Lock()  # To synchronise access to the checkpoint files

    # Create worker processes
    for process_id in range(1, 4):
        p = Process(target=worker_process, args=(process_id, lock))
        processes.append(p)
        p.start()

    # Wait for all processes to finish
    for p in processes:
        p.join()

    print("All processes completed.")


if __name__ == "__main__":
    main()