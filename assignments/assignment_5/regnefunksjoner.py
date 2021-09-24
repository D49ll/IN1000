def addisjon(a, b):
    return a+b

def subtraksjon(a, b):
    return a-b

def divisjon(a, b):
    return a/b


def main():
    #Addisjonsjekk
    assert addisjon(5,5) == 10
    assert addisjon(-5,-5) == -10
    assert addisjon(5,-5) == 0

    #Subtraksjonsjekk
    assert subtraksjon(4,2) == 2
    assert subtraksjon(-4,-2) == -2
    assert subtraksjon(-4,2) == -6
    
    #Divisjonsjekk
    assert divisjon(4,4) == 1
    assert divisjon(-4,-4) == 1
    assert divisjon(4,-4) == -1


main()