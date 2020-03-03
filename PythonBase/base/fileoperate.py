# -*-coding:utf-8-*-


def text_file_replace(source_file, target_file, old_str, new_str):
    with open(source_file, "r", encoding="utf8") as soc, open(target_file, "w", encoding="utf8") as tgt:
        readline = soc.readline()
        while readline:
            newline = readline.replace(old_str, new_str)
            tgt.write(newline)
            readline = soc.readline()


if __name__ == '__main__':
    text_file_replace('D:\\test\\test.sql', 'D:\\test\\test.sql', 'INSERT INTO',
                      'INSERT INTO "mes"."user_info" ')
