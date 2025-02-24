# Code
```.py
from secure_password import check_hash
from my_lib import DatabaseManager

x = DatabaseManager('bitcoin_exchange.db')
result = x.search("SELECT * from ledger")
x.close()

for row in result:
    id, send_id, rece_id, amount, signature = row
    string_hash = f"id {id},sender_id {send_id},receiver_id {rece_id},amount {amount}"
    if check_hash(user_password=string_hash, hashed_password=signature):
        print("TX IS CORRECT")
    else:
        print("TX IS NOT CORRECT")
```

# Proof of work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/f34ac8b3-bca9-4d79-be95-895eb904f25c" />
