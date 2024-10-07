# myapp/views.py
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from .models import Item
from .transaction import my_transaction_signal

def transaction_home(request):
    # Create an item
    item = Item.objects.create(name="Test Item", description="Initial description")

    try:
        with transaction.atomic():  # Start a transaction
            print("Transaction started.")

            # Send signal and pass item ID
            my_transaction_signal.send(sender='transaction_home_view', item_id=item.id)

            # Simulate an error (forcing rollback)
            raise Exception("Simulating an error to force rollback")

    except Exception as e:
        print(f"Exception occurred: {e}")
    
    # Check if the item description was updated or rolled back
    item.refresh_from_db()
    print(f"Item description after transaction: {item.description}")

    return HttpResponse("Signal transaction test")
