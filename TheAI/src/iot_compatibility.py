```python
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# IoT compatibility status
iot_compatibility_status = False

def iot_compatible():
    """
    Function to check if the system is compatible with IoT devices.
    """
    global iot_compatibility_status

    # Get IoT compatibility status from environment variables
    iot_compatibility_status = os.getenv('IOT_COMPATIBILITY', 'False')

    if iot_compatibility_status.lower() == 'true':
        iot_compatibility_status = True
    else:
        iot_compatibility_status = False

    return iot_compatibility_status

def connect_iot_device(device_id):
    """
    Function to connect an IoT device to the system.
    """
    if not iot_compatibility_status:
        raise Exception("The system is not compatible with IoT devices.")

    # Connect the IoT device
    # This is a placeholder for the actual code to connect an IoT device
    print(f"IoT device {device_id} connected.")

def disconnect_iot_device(device_id):
    """
    Function to disconnect an IoT device from the system.
    """
    if not iot_compatibility_status:
        raise Exception("The system is not compatible with IoT devices.")

    # Disconnect the IoT device
    # This is a placeholder for the actual code to disconnect an IoT device
    print(f"IoT device {device_id} disconnected.")
```