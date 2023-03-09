'''Eksempel program for dokumentasjon av kode, her skal programets virkemåte beskrives'''


def func_name(var1: str, var2: int) -> str:
    '''
    Her skal funksjonenes I/O og virkemåte beskrives i korte trekk\n
    Input:  var1: string
            var2: integer\n 
    Output: var1: string
            var2: string
    '''
    
    # merking av relevant info for utvilke:
    # bugs / improvments / To-Do / notes
    var1 = str(var1)
    var2 = str(var2)

    return var1, var2

print(func_name.__annotations__)
print(func_name.__doc__)


def avg(num: list) -> float:
    '''
    Regner ut gjennomsnitt av en liste, 
    kan kun inneholde float og int elementer\n
    Input:  num: list
    Output: avg: float 
    '''
    return sum(num) / len(num)


print(avg([0, 100]))