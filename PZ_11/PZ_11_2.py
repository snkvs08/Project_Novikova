#Из заданной строки отобразить только символы пунктуации. Использовать
#библиотеку string.
#Строка: --msg-template="$FileDir$\{path}:{line}:{column}:{C}:({symbol}){msg}"

from string import punctuation
s = '--msg-template="$FileDir${path}:{line}:{column}:{C}:({symbol}){msg}"'
p = [i for i in s if i in punctuation]

print("Символы пунктуации:",''.join(p))
