# TODO Найдите количество книг, которое можно разместить на дискете
volume_disk = 1.44 * 1024 * 1024 #в байтах
count_page = 100
count_str = 50
count_symbol = 25
volume_symbol = 4 #в байтах
volume_one_book = volume_symbol * count_symbol * count_str * count_page
count_books = int(volume_disk/volume_one_book)
print("Количество книг, помещающихся на дискету:", count_books)
