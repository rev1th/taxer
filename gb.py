
DEDUCTION_BASE = 12_570
MARGINAL_RATES = {
    2022: [
        (50_270, 0.2),
        (150_000, 0.4),
        (None, 0.45),
    ],
    2023: [
        (50_270, 0.2),
        (125_140, 0.4),
        (None, 0.45),
    ],
}
RELIEF_LIMIT = 100000

def itr(gross_income: float, year: int=2023) -> float:
    income_bracket = DEDUCTION_BASE
    if gross_income <= income_bracket:
        return 0
    tax_fixed = 0
    for ri in MARGINAL_RATES[year]:
        if ri[0] and gross_income > ri[0]:
            tax_fixed += (ri[0] - income_bracket) * ri[1]
            income_bracket = ri[0]
        else:
            if gross_income > RELIEF_LIMIT:
                if gross_income >= RELIEF_LIMIT + DEDUCTION_BASE*2:
                    income_bracket -= DEDUCTION_BASE
                else:
                    income_bracket -= (gross_income - RELIEF_LIMIT)/2
            return tax_fixed + (gross_income - income_bracket) * ri[1]
