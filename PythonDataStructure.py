library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]
item = ("The Art of War", "Sun Tzu")

temp_list = list(library)
if item not in temp_list:
    temp_list.append(item)
    library = tuple(temp_list)
    print(library)
else:
    print("Book already exists. Please try a different title.")