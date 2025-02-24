# Code
```.py
class palNum:
    def __init__(self):
        pass
    def get_pal_list(self, A, B):
        out = []
        for i in range(A, B+1):
            a = str(i)
            if a == a[::-1]:
                out.append(i)
        return out

a = palNum()
print(a.get_pal_list(1, 9))
print(a.get_pal_list(10, 199))
```

# Proof of Work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/0198b458-e74b-4c1a-998c-f64a16abe9ed" />
