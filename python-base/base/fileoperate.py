# -*-coding:utf-8-*-
import os

# region 文本操作
""" 文本操作，读写模式
r : 读取文件，若文件不存在则会报错
w: 写入文件，若文件不存在则会先创建再写入，会覆盖原文件
a : 写入文件，若文件不存在则会先创建再写入，但不会覆盖原文件，而是追加在文件末尾
rb,wb： 分别于r,w类似，但是用于读写二进制文件
r+ : 可读、可写，文件不存在也会报错，写操作时会覆盖
w+ : 可读，可写，文件不存在先创建，会覆盖
a+ : 可读、可写，文件不存在先创建，不会覆盖，追加在末尾
"""


class readTxt:
    filepath = "D:\log.txt"

    def read(file, mode='r', encoding="utf-8"):
        """read()一次性读取文本中全部的内容，以字符串的形式返回结果 """
        res = []
        with open(file=file, mode=mode, encoding=encoding) as f:
            data = f.read()
            print(data)
            res.append(data)
        return res

    def readline(file, mode='r', encoding="utf-8"):
        """readline() 只读取文本第一行的内容，以字符串的形式返回结果 """
        with open(file=file, mode=mode, encoding=encoding) as f:
            data = f.readline()
            print(data)
            return data

    def readline(file, mode='r', encoding="utf-8"):
        """readlines() 读取文本所有内容，并且以列表的格式返回结果，一般配合for in使用 """
        res = []
        with open(file=file, mode=mode, encoding=encoding) as f:
            for line in f.readlines():
                line = line.strip('\n')  # 去掉列表中每一个元素的换行符
                print(line)
                res.append(line)
        return res

    def wr(file, mode='w', encoding="utf-8", content=[]):
        """ 若filename不存在会自动创建，写之前会清空文件 """
        with open(file=file, mode=mode, encoding=encoding) as f:
            for i in content:
                # f.write(i)  # 自带文件关闭功能，不需要再写f.close()
                # f.newlines  # 换行 /r/n
                f.writelines(i)

    def wr(file, mode='a', encoding="utf-8", content=[]):
        """ 若filename不存在会自动创建，写之前不会清空文件 """
        with open(file=file, mode=mode, encoding=encoding) as f:
            for i in content:
                # f.write(i)  # 自带文件关闭功能，不需要再写f.close()
                # f.newlines  # 换行 /r/n
                f.writelines(i)


# endregion

def os_example():
    """ 获取当前路径：os.getcwd()     更改目录：os.chdir()         打开一个文件：os.open()
    获取文件夹下的所有文件和文件夹：os.listdir()
    创建一个目录：os.mkdir()     删除一个目录：os.rmdir()    文件夹或文件重命名：os.rename()  os.renames()
    基本统计：os.stat()  os.stat_result()      执行命令跟终端里一样：os.system()
    获取环境变量：os.getenv('PATH')  os.environ['PATH']
    获取绝对路径：os.path.abspath()    路径合并：os.path.join()
    检测是否是一个文件：os.path.isfile(path)
    检测是否是一个文件夹：os.path.isdir(path)
    检测路径是否存在：os.path.exists(path)           """
    print(os.getcwd())


def text_file_replace(source_file, target_file, old_str, new_str):
    """ SQL 文件替换字符，例如：缺少表名sql语句添加表名 """
    with open(source_file, "r", encoding="utf8") as soc, open(target_file, "w", encoding="utf8") as tgt:
        readline = soc.readline()
        while readline:
            newline = readline.replace(old_str, new_str)
            tgt.write(newline)
            readline = soc.readline()


def get_folders(dir, filter=None):
    file_name = []
    folder_name = []
    link_name = []
    for file in os.listdir(dir):
        if os.path.isfile(file):
            if filter is not None and os.path.splitext(file)[1] == filter:
                file_name.append(os.path.splitext(file)[0])
            else:
                file_name.append(os.path.splitext(file)[0])
        elif os.path.isdir(file):
            folder_name.append(file)
        elif os.path.islink(file):
            link_name.append(file)
    return file_name


def convert_path(path: str) -> str:
    """  任意系统的路径转换成当前系统的格式  """
    return path.replace(r'\/'.replace(os.sep, ''), os.sep)


if __name__ == '__main__':
    # text_file_replace('D:\\test\\test.sql', 'D:\\test\\performance1.sql', 'INSERT INTO',
    #                   'INSERT INTO "mes"."performance_colligate" ')
    # get_folders("")
    os_example()
    print("Program finished!")
