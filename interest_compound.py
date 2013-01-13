## Compound Interest

def compintcalc():
    pval = float(raw_input("Enter Principal Amount: "))
    intrate = float(raw_input("Enter Annual Rate (Rate Per Year): "))
    yrs = float(raw_input("Enter Number of Years: "))
    times = float(raw_input("Enter Number of Times Interest is Compounded Each Year: "))
    aval = pval * ((1 + (intrate / times))**(times * yrs))
    print aval

compintcalc()