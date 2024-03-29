
DEDUCTION_BASE = 18200
MARGINAL_RATES = [
    (45_000, 0.19),
    (120_000, 0.325),
    (180_000, 0.37),
    (None, 0.45),
]
MEDICARE_RATE = 0.02
MEDICARE_MARGINAL_RATES = {
    2022: [
        (90_000, 0),
        (105_000, 0.01),
        (140_000, 0.0125),
        (None, 0.015),
    ],
    2023: [
        (93_000, 0),
        (108_000, 0.01),
        (144_000, 0.0125),
        (None, 0.015),
    ],
}

def to(gross_income: float, year: int=2023) -> float:
    income_bracket = DEDUCTION_BASE
    tax_total = gross_income * MEDICARE_RATE
    if gross_income <= income_bracket:
        return tax_total
    tax_fixed = 0
    for ri in MARGINAL_RATES:
        if ri[0] and gross_income > ri[0]:
            tax_fixed += (ri[0] - income_bracket) * ri[1]
            income_bracket = ri[0]
        else:
            tax_total += tax_fixed + (gross_income - income_bracket) * ri[1]
            break
    for sri in MEDICARE_MARGINAL_RATES[year]:
        if sri[0] and gross_income > sri[0]:
            continue
        else:
            tax_total += gross_income * sri[1]
            break
    return tax_total