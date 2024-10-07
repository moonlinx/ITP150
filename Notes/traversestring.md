# Traversing a string

> [!Example]
>
> ```python
> str = "Edgar Allen Poe"
> offset = 0
>
> if ch == " ":
>   break
> offset += 1
>
> # print("first name: " + str[:offset])")
> print(f"first name: {str[:offset]}")
> ```

## String Function: find(" ")

```python
offset = str.find(" ")
firstName = str[:offset]
str = str[offset + 1:]

str
```
