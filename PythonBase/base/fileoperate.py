# -*-coding:utf-8-*-


def text_file_replace(source_file, target_file, old_str, new_str):
    with open(source_file, "r", encoding="utf8") as soc, open(target_file, "w", encoding="utf8") as tgt:
        while readline:
            newline = readline.replace(old_str, new_str)
            tgt.write(newline)
            readline = soc.readline()


if __name__ == '__main__':
    text_file_replace('D:\\test\\performance.sql', 'D:\\test\\performance1.sql', 'INSERT INTO',
                      'INSERT INTO "mes"."performance_colligate" ')
