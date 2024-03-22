
if __name__ == "__main__":
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}

    ft_list.pop()
    ft_list.append("World")
    print(ft_list)

    ft_new_touple = list(ft_tuple)
    ft_new_touple.pop()
    ft_new_touple.append("Turkiye!")
    ft_tuple = tuple(ft_new_touple)
    print(ft_tuple)

    ft_set.pop()
    ft_set.add("Kocaeli")
    print(ft_set)

    ft_dict["Hello"] = '42Kocaeli'
    print(ft_dict)
