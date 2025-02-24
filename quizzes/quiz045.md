# Paper Code
![image](https://github.com/user-attachments/assets/29e9c8bb-3a77-4b91-9446-ec1677ae0d04)

# Code
```.py
class WordCounter:
    def __init__(self):
        pass
    def WordCount(self, text):
        out = {}
        text_arr = text.split( )
        for word in text_arr:
            word_ = ''
            for char in word:
                if char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
                    word_ += char
            word = word_.lower()
            if word in out:
                out[word] +=1
            else:
                out[word] = 1
        return out
a = WordCounter()
print(a.WordCount('This is a sample text. It contains some words that will be counted.'))
```

# Proof of Work
<img width="1470" alt="image" src="https://github.com/user-attachments/assets/8eb30eb8-b620-453e-97e6-5b330bdfb04c" />
