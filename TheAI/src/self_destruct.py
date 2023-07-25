```python
import os
import shutil

def self_destruct():
    """
    This function will delete all the data from the system.
    """
    try:
        # Path to the directory which needs to be deleted
        path = "/path/to/directory"

        # Check if the directory exists
        if os.path.exists(path):
            # Remove the directory and all its contents
            shutil.rmtree(path)
            print("SelfDestructActivated: The directory and all its contents have been deleted.")
        else:
            print("The directory does not exist.")
    except Exception as e:
        print("An error occurred while trying to delete the directory. Error: ", str(e))

if __name__ == "__main__":
    self_destruct()
```