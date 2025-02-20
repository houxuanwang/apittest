import random
print(random.randint(1,100))
if __name__ == '__main__':
    print(random.randint(1,100))
    print("hello!")
    #帮我生成个冒泡排序算法
    def bubble_sort(lists):
        count = len(lists)
        for i in range(0, count):
            for j in range(i + 1, count):
                if lists[i] > lists[j]:
                    lists[i], lists[j] = lists[j], lists[i]
        return lists
    print(bubble_sort([36, 5, -12, 9, -21]))
    print(bubble_sort([3, 44, 38, 5, 47, 15, 36, 26, 27, 2, 46, 4, 19, 50, 48]))
    写段代码，收集特定目录下所有文件名中包含control的文件
    import os
    def get_file_name(file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if 'control' in file:
                    L.append(os.path.join(root, file))
        return L
    print(get_file_name(r'D:\test'))
    #写段代码，收集特定目录下所有文件名中包含control的文件
    import os
    def get_file_name(file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if 'control' in file:
                    L.append(os.path.join(root, file))
        return L
    print(get_file_name(r'D:\test'))
    #写段代码，收集特定目录下所有文件名中包含control的文件
    import os
    def get_file_name(file_dir):
        L = []
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if 'control' in file:
                    L.append(os.path.join(root, file))
        return L
    print(get_file_name(r'D:\test'))
