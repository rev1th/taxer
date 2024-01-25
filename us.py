
DEDUCTION_BASE = 12_950
SOCIAL_RATE = 0.062
SOCIAL_MAX = 147_000
MEDICARE_RATE_0 = 0.0145
MEDICARE_LIMIT = 200_000
MEDICARE_RATE_1 = 0.0235
PROGRESSIVE_RATES = [
    (10_275, 0.1),
    (41_775, 0.12),
    (89_075, 0.22),
    (170_050, 0.24),
    (215_950, 0.32),
    (539_900, 0.35),
    (None, 0.37),
]
STATE_PROGRESSIVE_RATES = {
    'California': [
        (8_931, 0.01),
        (21_174, 0.02),
        (33_420, 0.04),
        (46_393, 0.06),
        (58_633, 0.08),
        (299_507, 0.093),
        (359_407, 0.103),
        (599_011, 0.113),
        (999_999, 0.123),
        (None, 0.133),
    ],
    'Chicago': [
        (2375, 0),
        (None, 0.0495)
    ],
    'NewYork': [
        (8_500, 0.04),
        (11_700, 0.045),
        (13_900, 0.0525),
        (21_400, 0.059),
        (80_650, 0.0597),
        (215_400, 0.0633),
        (1077_550, 0.0685),
        (5000_000, 0.0965),
        (25_000_000, 0.103),
        (None, 0.109),
    ],
    'NewJersey': [
        (20_000, 0.014),
        (35_000, 0.0175),
        (40_000, 0.035),
        (75_000, 0.0525),
        (500_000, 0.0637),
        (1000_000, 0.0897),
        (None, 0.1075),
    ]
}
CITY_PROGRESSIVE_RATES = {
    'NYC': [
        (12_000, 0.03078),
        (25_000, 0.03762),
        (50_000, 0.03819),
        (None, 0.03876),
    ],
}
def irs(gross_income, state=None, city=None):
    tax_total = min(gross_income, SOCIAL_MAX)*SOCIAL_RATE + min(gross_income, MEDICARE_LIMIT)*MEDICARE_RATE_0
    tax_total += max(gross_income-MEDICARE_LIMIT, 0)*MEDICARE_RATE_1
    if gross_income <= DEDUCTION_BASE:
        return tax_total
    taxable_income = gross_income - DEDUCTION_BASE
    income_slab_limit = 0
    tax_slab_fixed = 0
    for i in PROGRESSIVE_RATES:
        if i[0] and taxable_income > i[0]:
            tax_slab_fixed += (i[0] - income_slab_limit) * i[1]
            income_slab_limit = i[0]
        else:
            tax_total += tax_slab_fixed + (taxable_income - income_slab_limit) * i[1]
            break
    if state and state in STATE_PROGRESSIVE_RATES:
        state_income_slab_limit = 0
        state_tax_slab_fixed = 0
        for i in STATE_PROGRESSIVE_RATES[state]:
            if i[0] and gross_income > i[0]:
                state_tax_slab_fixed += (i[0] - state_income_slab_limit) * i[1]
                state_income_slab_limit = i[0]
            else:
                tax_total += state_tax_slab_fixed + (gross_income - state_income_slab_limit) * i[1]
                break
    if city and city in CITY_PROGRESSIVE_RATES:
        city_income_slab_limit = 0
        city_tax_slab_fixed = 0
        for i in CITY_PROGRESSIVE_RATES[city]:
            if i[0] and gross_income > i[0]:
                city_tax_slab_fixed += (i[0] - city_income_slab_limit) * i[1]
                city_income_slab_limit = i[0]
            else:
                tax_total += city_tax_slab_fixed + (gross_income - city_income_slab_limit) * i[1]
                break
    return tax_total