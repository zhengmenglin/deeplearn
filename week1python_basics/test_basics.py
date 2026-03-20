# 测试题1：基础 + 列表推导式
from typing import LiteralString


def even_squares(n:int) -> list[int]:
    """返回0到n-1中所有偶数的平方列表"""
    # 用列表推导式写，不要for循环
    return [i**2 for i in range(n) if i % 2 == 0]

# 测试题2：字符串处理（不用切片[::-1]）
def reverse_words(s:str) -> str:
    """把句子单词反转顺序，例如 'hello world' -> 'world hello'"""
    # 不使用切片，用入栈出栈实现（更简洁版）
    words = s.split()
    return " ".join(reversed(words))

# 测试题3：简单OOP,什么是opp，opp就是对象和类
class BankAccount:
    def __init__(self, balance:float=0.0):
        self.balance = balance#初始化余额
    
    def deposit(self, amount:float) -> bool:#存款
        """存款"""
        # 实现
        self.balance += amount
        return True
    
    def withdraw(self, amount:float) -> bool:#取款
        # 实现（余额不足返回False）
        if self.balance < amount:
            return False
        self.balance -= amount
        return True

# 测试题4：用内置函数一行解决
def count_vowels(text):
    """返回字符串中元音字母(aeiouAEIOU)的总数，用sum + generator表达式"""
    # 用sum + generator表达式实现
    vowels = set("aeiouAEIOU")
    return sum(1 for char in text if char in vowels)

print(even_squares(10))          # 预期 [0, 4, 16, 36, 64]
print(reverse_words("hello python world"))
acc = BankAccount(100)
acc.deposit(50)
print(acc.withdraw(200))         # 预期 False
print(count_vowels("Hello World!"))  # 预期 3