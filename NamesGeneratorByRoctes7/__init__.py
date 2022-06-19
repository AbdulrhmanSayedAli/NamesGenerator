import NamesGeneratorByRoctes7.main as main
def DrawRegular(name,drawnLetter):
        main.init(10,2,drawnLetter," ",False,[],False)
        main.Output(name)


def DrawWithCustomSize(name,drawnLetter,size):
    try:
        size=int(size)
    except:
        print('the size should be integer')
        return

    if size>100 or size<0 or size%5!=0:
        print('the size should be gretaer than zero and smaller than 100 aand divisible by five')
        return

    main.init(size,2,drawnLetter," ",False,[],False)
    main.Output(name)
    



def DrawWithRandomMode(name,choices):
    if type(choices)!=list:
        print('choices should be list')
        return
    
    main.init(10,2,"#"," ",True,choices,False)
    main.Output(name)



def DrawWithYourNameLettersMode(name):
    main.init(10,2,"#"," ",True,list(name),True)
    main.Output(name)