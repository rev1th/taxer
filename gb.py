
DEDUCTION_BASE = 12_570
PROGRESSIVE_RATES = {
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
    income_slab_limit = DEDUCTION_BASE
    if gross_income <= income_slab_limit:
        return 0
    tax_fixed = 0
    for ri in PROGRESSIVE_RATES[year]:
        if ri[0] and gross_income > ri[0]:
            tax_fixed += (ri[0] - income_slab_limit) * ri[1]
            income_slab_limit = ri[0]
        else:
            if gross_income > RELIEF_LIMIT:
                if gross_income >= RELIEF_LIMIT + DEDUCTION_BASE*2:
                    income_slab_limit -= DEDUCTION_BASE
                else:
                    income_slab_limit -= (gross_income - RELIEF_LIMIT)/2
            return tax_fixed + (gross_income - income_slab_limit) * ri[1]
