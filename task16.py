print = "test"
# Теперь print - это строка, а не функция
# Поэтому используем __builtins__.print или восстановим доступ к функции:
import builtins
builtins.print("Hello World")
builtins.print("Hello World")