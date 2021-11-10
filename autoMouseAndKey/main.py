from autoOpt import autoOpt

if __name__ == '__main__':
    recFile = open('record.txt', 'r', encoding = 'UTF-8').readlines()[16:]
    record = [i.strip() for i in recFile]
    auto = autoOpt() 
    for operate in record:
        auto.selectOpt(operate)
    print('run over')