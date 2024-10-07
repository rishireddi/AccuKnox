from django.dispatch import Signal, receiver
from .models import Item

# Create a custom signal
my_transaction_signal = Signal()

# Receiver function
@receiver(my_transaction_signal)
def my_transaction_signal_receiver(sender, **kwargs):
    item_id = kwargs.get('item_id')
    item = Item.objects.get(id=item_id)
    item.description = "Updated in signal handler"
    item.save()
    print("Signal handler updated item description.")
