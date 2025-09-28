# Simple Future Value calculator

def future_value(pv, r, n):
    return pv * (1 + r)**n

if __name__ == "__main__":
    pv = float(input("Enter Present Value (PV): "))
    r = float(input("Enter annual rate (as decimal, e.g. 0.05 for 5%): "))
    n = int(input("Enter number of years: "))

    fv = future_value(pv, r, n)
    print(f"Future Value: {fv:.2f}")
