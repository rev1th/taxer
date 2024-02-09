
DEDUCTION_OTHER = 150000
MARGINAL_RATES = [
    (250_000, 0),
    (500_000, 0.05),
    (1000_000, 0.2),
    # (750_000, 0.1),
    # (1_000_000, 0.15),
    # (1_250_000, 0.2),
    # (1_500_000, 0.25),
    (None, 0.3),
]
SURCHARGE_BASE = 5000000
SURCHARGE_RATES = [
    (100_00_000, 0.1),
    (200_00_000, 0.15),
    (500_00_000, 0.25),
    (10_00_00_000, 0.37),
    (None, 0.37)
]
CESS_RATE = 0.04

def itr(gross_income: float) -> float:
    income_bracket = 0
    tax_core_fixed = 0
    tax_core_total = 0
    for ri in MARGINAL_RATES:
        if ri[0] and gross_income > ri[0]:
            tax_core_fixed += (ri[0] - income_bracket) * ri[1]
            income_bracket = ri[0]
        else:
            tax_core_total = tax_core_fixed + (gross_income - income_bracket) * ri[1]
            break
    tax_surcharge_base = 0
    tax_surcharge_extra = tax_core_total
    if gross_income > SURCHARGE_BASE:
        surcharge_slab = SURCHARGE_BASE
        for sri in SURCHARGE_RATES:
            if sri[0] and gross_income > sri[0]:
                surcharge_slab = sri[0]
            else:
                tax_surcharge_base = itr(surcharge_slab)
                tax_surcharge_extra = min(tax_core_total * (1+sri[1]) - tax_surcharge_base, gross_income - surcharge_slab)
                break
    return tax_surcharge_base + tax_surcharge_extra * (1+CESS_RATE)
