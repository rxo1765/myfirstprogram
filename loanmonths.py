def computesPmt(PV, r, n):
    """

    Parameters
    ----------
    PV : TYPE float 
    DESCRIPTION. present value (amt borrow)
    r : TYPE
        DESCRIPTION. interest rate APR
    n : TYPE integer
        DESCRIPTION. number of months to pay back loan

    Returns
    -------
    Pmt : TYPE
        DESCRIPTION. amt apid per month 
    
    """
    r =r/100 #convert APR to a decimal
    r = r/12
    
    Pmt = r * PV/(1-(1+r)**-n)
    return Pmt    
    
   
def computesPV(Pmt, r, n):
    """
    compute how much $$ you can borrow
    Parameters
    ----------
    Pmt : TYPE float
        DESCRIPTION. how much I can afford to for monthly payment
    r : TYPEfloat
        DESCRIPTION. interest rate APR
    n : TYPE integegr
        DESCRIPTION. number of months

    Returns
    -------
    PV : float
    DESCRIPTION. amount of $$ I can afford to borrow
    
    formula:
        Pv = (1-(1+r)**(-n) *Pmt/r

    """
    
    r = r/100 #convert APR to decimal
    r= r/12
    
    PV = (1-(1+r)**(-n)) * Pmt / r
    return PV
def computesN(Pmt, PV, r):
    
    
    """
    Pmt = r * PV/(1-(1+r)**-n)
    Pmt is how much you pay back/mo 
    r is interest rate per month
    n is number of months

    Parameters
    ----------
    Pmt : TYPE flaot
        DESCRIPTION. monthly payment
    PV : TYPE float
        DESCRIPTION. amount borrowed
    r : TYPE float
        DESCRIPTION. interest rate, APR

    Returns
    -------
    N : TYPE integer
        DESCRIPTION. Number of months to pay back loan

    """
    import numpy as np
    # convert r (APR) to a decimal, per month
    r = r/12 # converts to % per month
    r = r/100 # converts % to a decimal
    
    # given Pmt, Pv, r, we compute n
    
    n = -np.log( 1-PV*r/pmt) / np.log(1+r)
    n = round(n,1)
    
    return n
    
if __name__ == "__main__":
        
        import numpy as np

while(True):
    choice = int(input('enter choice 2 for PV, 1 for Pmt, 3 for n -> '))
    if (choice == 1 or choice ==2 or choice == 3): 
        break
    else:
        print(f"enter a 1 or a 2, or a 3 you entered {choice}\n")
        
if choice == 1:
    #compute pmt; input PV, r, n
    n = 48
    PV = input('enter PV:')
    PV = float(PV) 
    # equivalently PV = float(input('enter PV: '))
    print(f"PV ={PV} \n")
    
    r = input("interest APR:")
    r = float(r)
    
    print(f"interest = {r: 0.3f}\n")
    
    n= int(input('how many months:'))
    print(f"\nn = {n} months \n")

    pmt = computesPmt(PV, r, n)
    pmt = np.round(pmt, 2)
    print(f"payment is {pmt: } per month\n")

if choice == 2:
    #compute PV, input pmt, r, n
    pmt= input('enter pmt: ')
    pmt = float(pmt)
    #equivalently PV = float (input('enter PV: '))
    print(f"pmt = {pmt: 0.2f} \n")
    
    r= input('interest APR: ')
    r = float(r)
    n = input("enter number of months ")
    n = int(n)
    
    print (f"\nn = {n} months \n")
    
    PV = computesPV(pmt, r, n)
    #PV = np.round(pmt,2)
    print(f"amount I can borrow is ${PV: 0.2f}")

if choice == 3:
    #compute PV, input pmt, r, n
    PV = input('enter PV: ')
    PV = float(PV)
    pmt = input('enter pmt: ')
    pmt = float(pmt)
    
    r= input('interest APR: ')
    r = float(r)
    n = computesN(pmt, PV, r)
    
    print(f"\nn = {n} months \n")