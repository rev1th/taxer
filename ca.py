
DEDUCTION_BASE_0 = {
    2023: 15_000,
}
DEDUCTION_BASE_1 = {
    2023: 13_520,
}
RELIEF_LIMIT_RATE_0 = 0.26
RELIEF_LIMIT_RATE = 0.29
DEDUCTION_OTHER = {
    2023: 1368,
}
MARGINAL_RATES = {
    2023: [
        (53_539, 0.15),
        (106_717, 0.205),
        (165_430, 0.26),
        (235_675, 0.29),
        (None, 0.33),
    ],
}
STATE_MARGINAL_RATES = {
    2023: {        
        'Ontario': [
            (49_231, 0.0505),
            (98_463, 0.0915),
            (150_000, 0.1116),
            (220_000, 0.1216),
            (None, 0.1316),
        ],
    }
}

def cra(gross_income: float, state: str=None, year: int=2023):
    income_bracket = DEDUCTION_BASE_0[year] + DEDUCTION_OTHER[year]
    if gross_income <= income_bracket:
        return 0
    tax_total = 0
    taxable_income = gross_income - income_bracket
    income_bracket = 0
    tax_slab_fixed = 0
    for ri in MARGINAL_RATES[year]:
        if ri[1] == RELIEF_LIMIT_RATE:
            taxable_income += (DEDUCTION_BASE_0[year] - DEDUCTION_BASE_1[year])
        # elif ri[0] < taxable_income:
        #     taxable_income += (DEDUCTION_BASE_0 - DEDUCTION_BASE_1) / (ri[0] - income_bracket) \
        #         * (taxable_income + DEDUCTION_BASE_0 - income_bracket)
        if ri[0] and taxable_income > ri[0]:
            tax_slab_fixed += (ri[0] - income_bracket) * ri[1]
            income_bracket = ri[0]
        else:
            tax_total += tax_slab_fixed + (taxable_income - income_bracket) * ri[1]
            break
    if state:
        state_income_bracket = 0
        state_tax_slab_fixed = 0
        for sri in STATE_MARGINAL_RATES[year][state]:
            if sri[0] and gross_income > sri[0]:
                state_tax_slab_fixed += (sri[0] - state_income_bracket) * sri[1]
                state_income_bracket = sri[0]
            else:
                tax_total += state_tax_slab_fixed + (gross_income - state_income_bracket) * sri[1]
                break
    return tax_total