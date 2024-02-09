
DEDUCTION_BASE = 20_000
DEDUCTION_OTHER = 1000+14400
MARGINAL_RATES = {
    2023: [
        (10_000, 0.02, 20_000),
        (10_000, 0.035, 30_000),
        (40_000, 0.07, 40_000),
        (40_000, 0.115, 80_000),
        (40_000, 0.15, 120_000),
        (40_000, 0.18, 160_000),
        (40_000, 0.19, 200_000),
        (40_000, 0.195, 240_000),
        (40_000, 0.2, 280_000),
        (None, 0.22, 320_000),
    ],
    2024: [
        (10_000, 0.02, 20_000),
        (10_000, 0.035, 30_000),
        (40_000, 0.07, 40_000),
        (40_000, 0.115, 80_000),
        (40_000, 0.15, 120_000),
        (40_000, 0.18, 160_000),
        (40_000, 0.19, 200_000),
        (40_000, 0.195, 240_000),
        (40_000, 0.2, 280_000),
        (180_000, 0.22, 320_000),
        (500_000, 0.23, 500_000),
        (None, 0.24, 1000_000),
    ],
}

def iras(gross_income: float, year: int=2023) -> float:
    income_bracket = DEDUCTION_BASE + DEDUCTION_OTHER
    if gross_income <= income_bracket:
        return 0
    tax_fixed = 0
    for ri in MARGINAL_RATES[year]:
        if ri[0] and gross_income > income_bracket + ri[0]:
            income_bracket += ri[0]
            tax_fixed += ri[0] * ri[1]
        else:
            return tax_fixed + (gross_income - income_bracket) * ri[1]
