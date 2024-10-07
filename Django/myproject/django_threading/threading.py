import time
import threading
from django.dispatch import Signal, receiver

# Create a custom signal
my_threading_signal = Signal()

# Receiver function
@receiver(my_threading_signal)
def my_threading_signal_receiver(sender, **kwargs):
    print(f"Signal received in thread: {threading.get_ident()}")
    time.sleep(3)  # Simulate a long-running task
    print("Signal processed.")