
DEDUCTION_BASE = 132_000
DEDUCTION_OTHER = 18_000
MARGINAL_RATES = [
    (50_000, 0.02),
    (50_000, 0.06),
    (50_000, 0.10),
    (50_000, 0.14),
    (None, 0.17),
]
STANDARD_RATE = 0.15

def ird(gross_income: float) -> float:
    income_bracket = DEDUCTION_BASE + DEDUCTION_OTHER
    if gross_income <= income_bracket:
        return 0
    tax_fixed = 0
    for ri in MARGINAL_RATES:
        if ri[0]:
            if gross_income <= income_bracket + ri[0]:
                return tax_fixed + (gross_income - income_bracket) * ri[1]
            else:
                income_bracket += ri[0]
                tax_fixed += ri[0] * ri[1]
        else:
            return min(tax_fixed + (gross_income - income_bracket) * ri[1], gross_income*STANDARD_RATE)
