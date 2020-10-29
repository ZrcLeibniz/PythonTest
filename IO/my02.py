try:
    f = open('a.txt', 'a', encoding='UTF-8')
    str_ = '张锐驰'
    str2_ = ['aa', 'bb', 'cc']
    f.write(str_)
    f.writelines(str2_)
except BaseException as e:
    print(e)
finally:
    f.close()
