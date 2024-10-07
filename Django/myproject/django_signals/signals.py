import time
from django.dispatch import Signal, receiver
from django.core.signals import request_finished

# Create a custom signal
my_signal = Signal()

# Receiver function
@receiver(my_signal)
def my_signal_receiver(sender, **kwargs):
    print("Signal received, starting delay...")
    time.sleep(10)  # Simulate a long-running task
    print("Signal processed.")

# Connect to Django's request_finished signal to trigger our custom signal
@receiver(request_finished)
def request_finished_receiver(sender, **kwargs):
    print("Request finished, sending my_signal...")
    my_signal.send(sender=sender)
