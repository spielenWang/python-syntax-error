informationDict = {
    'abc': ['xx@gmail.com', 123],
    'ddd': ['dd@hotmail.com', 222],
    'efs': ['cineadf@126.com', 161]
}


def searchPeople(personsName):  # ……对，模块什么时候用，取决你自己的需求
    try:
        personsInfo = informationDict[personsName]
        print 'Name:' + personsName.title()
        print 'Email:' + personsInfo[0]
        print 'Num:' + str(personsInfo[1])
    except:
        print 'No information found for that name'

userWantsMore = True  # 常用的循环方法，创造一个对象，初始为T，运算结束后为F，跳出循环。
while userWantsMore == True:
    personsName = raw_input('Please input the Name:').lower()
    searchPeople(personsName)

    userWantsMore = False  # 赋值为False是为了跳出while循环
