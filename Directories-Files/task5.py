def writeList(lst, filename):
    with open(filename, 'w') as f:
        for item in lst:
            f.write(str(item) + '\n')
my_list = ["qwe", 2, 3, "asd  d", 5]
file_name = "sample.txt"
writeList(my_list, file_name)

