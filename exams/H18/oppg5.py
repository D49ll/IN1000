def godkjenn(aldre):
    for familie in aldre:
        flagg = False
        for medlem in familie:
            if medlem >= 18:
                flagg = True
        if not flagg:
            return False
    return True



A = [[10,2,30],[10,12]]

print(godkjenn(A))
