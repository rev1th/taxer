
PROGRESSIVE_RATES = [
    (1_950_000, 0.05),
    (3_300_000, 0.1),
    (6_950_000, 0.2),
    (9_000_000, 0.23),
    (18_000_000, 0.33),
    (40_000_000, 0.4),
    (None, 0.45)
]
DEDUCTION_SLABS = [
    (1_625_000, 0, 550_000),
    (1_800_000, 0.4, -100_000),
    (3_600_000, 0.3, 80_000),
    (6_600_000, 0.2, 440_000),
    (8_500_000, 0.1, 1_100_000),
    (None, 0, 1_950_000)
]
EXEMPTION_SLABS = [
    (24_000_000, 480_000, 430_000),
    (24_500_000, 320_000, 290_000),
    (25_000_000, 160_000, 150_000),
    (None, 0, 0),
]
HEALTH_INSURANCE_RATE = {
    2022: 0.04905,
    2023: 0.05,
}
HEALTH_INSURANCE_CAP = 1_390_000*12 + 5_730_000
PENSION_RATE = 0.0915
PENSION_CAP = (650_000+1_500_000)*12
UNEMPLOYMENT_INSURANCE_RATE = {
    2022: 0.003,
    2023: 0.006,
}
SURTAX_RATE = 0.021

PREFECTURAL_RATE = 0.04
PREFECTURAL_FIXED = 1500
MUNICIPAL_RATE = 0.06
MUNICIPAL_FIXED = 3500
def nta(gross_income: float, year: int=2023):
    social_security = gross_income * UNEMPLOYMENT_INSURANCE_RATE[year]
    social_security += min(gross_income, HEALTH_INSURANCE_CAP) * HEALTH_INSURANCE_RATE[year]
    social_security += min(gross_income, PENSION_CAP) * PENSION_RATE
    for ds_i in DEDUCTION_SLABS:
        if ds_i[0] is None or gross_income <= ds_i[0]:
            taxable_income = gross_income*(1-ds_i[1]) - ds_i[2]
            break
    national_taxable_income = taxable_income
    for es_i in EXEMPTION_SLABS:
        if es_i[0] and gross_income <= es_i[0]:
            national_taxable_income -= es_i[1]
            break
    income_slab_limit = 0
    national_tax_fixed = 0
    for r_i in PROGRESSIVE_RATES:
        if r_i[0] and national_taxable_income > r_i[0]:
            national_tax_fixed += (r_i[0] - income_slab_limit) * r_i[1]
            income_slab_limit = r_i[0]
        else:
            national_tax_total = national_tax_fixed + (national_taxable_income - income_slab_limit) * r_i[1]
            break
    local_taxable_income = taxable_income
    for es_i in EXEMPTION_SLABS:
        if es_i[0] and gross_income <= es_i[0]:
            local_taxable_income -= es_i[2]
            break
    inhabitant_tax = local_taxable_income * (PREFECTURAL_RATE+MUNICIPAL_RATE) + PREFECTURAL_FIXED+MUNICIPAL_FIXED
    return social_security + national_tax_total*(1 + SURTAX_RATE) + inhabitant_tax
