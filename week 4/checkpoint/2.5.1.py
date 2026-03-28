import os
import pickle
CHECK_DIR = "checkpoints/"  # Directory for checkpoint files
if not os.path.exists(CHECK_DIR):  # Create directory if it doesn't exist
    os.makedirs(CHECK_DIR)
checkpoint_file = os.path.join(CHECK_DIR, "checkpoint_1.pkl")  # Unique file
with open(checkpoint_file, "wb") as f:
    pickle.dump({"task_count": 3}, f)
    print("Checkpoint for Process 1 saved!")