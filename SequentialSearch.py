def SequentialSearch(list, item):
    query_result = []
    for i in list:
        if i == item:
            query_result.append(i)
            print(query_result)
    if query_result == []:
        print('No results found')





items = ['Oranges', 'apples', 'milk', 200, 'pepper', 'bag']

SequentialSearch(items, 'milk')