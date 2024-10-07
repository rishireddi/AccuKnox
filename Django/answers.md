Topic: Django Signals

Question 1: By default are django signals executed synchronously or asynchronously? Please support your answer with a code snippet that conclusively proves your stance.

Answer 1: By default, Django signals are executed synchronously. This means that when a signal is sent, the receivers are called in the same thread, and the calling code must wait for all signal handlers to finish executing before continuing. The code that supports the above answer is in the file /myproject/django_signals/signals.py and views.py



Question 2: Do django signals run in the same thread as the caller? Please support your answer with a code snippet that conclusively proves your stance.

Answer 2 : Yes, Django signals run in the same thread as the caller by default. This means that when a signal is sent, the signal handlers (receivers) are executed in the same thread that initiated the signal, and any blocking operation in a signal handler will block the caller. The code that supports the above answer is in the file /myproject/django_threading/threading.py and views.py


Question 3: By default do django signals run in the same database transaction as the caller? Please support your answer with a code snippet that conclusively proves your stance. The code does not need to be elegant and production ready, we just need to understand your logic.

Answer 3 : By default, Django signals run in the same database transaction as the caller. This means that if the signal handler (receiver) performs database operations, they are part of the same transaction as the code that triggered the signal. If the caller's transaction is rolled back, any database changes made by the signal handlers will also be rolled back. The code that supports the above answer is in the file /myproject/django_db_transaction/transaction.py and views.py


Topic: Custom Classes in Python

Question : creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} followed by the width {width: <VALUE_OF_WIDTH>}


Answer : I've created a custom_class_rectangle project in myproject directory to answer the above question.