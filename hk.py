
DEDUCTION_BASE = 132_000
DEDUCTION_OTHER = 18_000
PROGRESSIVE_RATES = [
    (50_000, 0.02),
    (50_000, 0.06),
    (50_000, 0.10),
    (50_000, 0.14),
    (None, 0.17),
]
STANDARD_RATE = 0.15
def ird(gross_income: float) -> float:
    income_slab_limit = DEDUCTION_BASE + DEDUCTION_OTHER
    if gross_income <= income_slab_limit:
        return 0
    tax_fixed = 0
    for ri in PROGRESSIVE_RATES:
        if ri[0]:
            if gross_income <= income_slab_limit + ri[0]:
                return tax_fixed + (gross_income - income_slab_limit) * ri[1]
            else:
                income_slab_limit += ri[0]
                tax_fixed += ri[0] * ri[1]
        else:
            return min(tax_fixed + (gross_income - income_slab_limit) * ri[1], gross_income*STANDARD_RATE)
