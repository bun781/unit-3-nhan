# 1. Create the UML Diagram
<img width="910" alt="image" src="https://github.com/user-attachments/assets/d2d0792d-cdf8-47ff-84c2-4a6f713f81bb" />


# 2. Create the SQL queries to find the responsible for the fraudulent transaction.
```.sqlite
SELECT c.customer_id, c.first_name, c.last_name, t.account_id
FROM customers c
join accounts a
on a.customer_id = c.customer_id
join transactions t
on t.account_id = a.account_id
group by t.account_id, a.balance
having
    SUM(CASE WHEN t.transaction_type = 'deposit' THEN amount ELSE 0 END) -
    SUM(CASE WHEN t.transaction_type = 'withdraw' THEN amount ELSE 0 END) !=
    a.balance;
```

# 3. What is the name of the customer and the problem that resulted in the bankruptcy of the bank?
Matthew, Martin

Ashley, Taylor

Nicholas, Lewis

David, Clark

Daniel, Green
