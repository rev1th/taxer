
from enum import StrEnum

from constants import *

class State(StrEnum):
    California = 'california'
    Illinois = 'illinois'
    NewYork = 'new_york'
    NewJersey = 'new_jersey'

class City(StrEnum):
    NewYork = 'new_york'


def get_base_deduction(year: int=None, status: Status= Status.Single):
    if year == 2022:
        return 12_950
    elif year == 2023:
        if status == Status.Married:
            return 27_700
        else:
            return 13_850
    else: # year == 2024
        if status == Status.Married:
            return 29_200
        else:
            return 14_600

SOCIAL_SECURITY_RATE = 0.062
def get_social_security_max(year: int=None):
    if year == 2023:
        return 147_000
    else:
        return 168_600

MEDICARE_RATE = 0.0145
def get_medicare_threshold(status: Status= Status.Single):
    if status == Status.Married:
        return 250_000
    else:
        return 200_000
MEDICARE_RATE_ADDITION = 0.009

def get_marginal_rates(year: int=None, status: Status= Status.Single):
    if year == 2022:
        if status == Status.Married:
            return [
                (10_275, 0.1),
                (41_775, 0.12),
                (89_075, 0.22),
                (170_050, 0.24),
                (215_950, 0.32),
                (539_900, 0.35),
                (None, 0.37),
            ]
        else:
            return []
    elif year == 2023:
        if status == Status.Married:
            return [
                (22_000, 0.1),
                (89_450, 0.12),
                (190_750, 0.22),
                (364_200, 0.24),
                (462_500, 0.32),
                (693_750, 0.35),
                (None, 0.37),
            ]
        else:
            return [
                (11_000, 0.1),
                (44_725, 0.12),
                (95_735, 0.22),
                (182_100, 0.24),
                (231_250, 0.32),
                (578_125, 0.35),
                (None, 0.37),
            ]
    else:
        if status == Status.Married:
            return [
                (23_200, 0.1),
                (94_300, 0.12),
                (201_050, 0.22),
                (383_900, 0.24),
                (487_450, 0.32),
                (731_200, 0.35),
                (None, 0.37),
            ]
        else:
            return [
                (11_600, 0.1),
                (47_150, 0.12),
                (100_525, 0.22),
                (191_950, 0.24),
                (243_725, 0.32),
                (609_350, 0.35),
                (None, 0.37),
            ]

def get_amt_marginal_exemption(year: int=None, status: Status= Status.Single):
    if year == 2022 or year == 2023:
        if status == Status.Married:
            return 126_500
        else:
            return 81_300
    else:
        if status == Status.Married:
            return 133_300
        else:
            return 85_700

def get_amt_marginal_rates(year: int=None, status: Status= Status.Single):
    if year >= 2023:
        if status == Status.Married:
            return [
                (220_700, 0.26),
                (None, 0.28),
            ]
        else:
            return [
                (110_350, 0.26),
                (None, 0.28),
            ]

def get_state_marginal_rates(state: State, year: int=None, status: Status= Status.Single):
    if state == State.California:
        return [
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
        ]
    elif state == State.Illinois:
        return [
            (2375, 0),
            (None, 0.0495)
        ]
    elif state == State.NewYork:
        if year == 2022:
            if status == Status.Married:
                return [
                    (17_150, 0.04),
                    (23_600, 0.045),
                    (27_900, 0.0525),
                    (161_550, 0.0585),
                    (323_200, 0.0625),
                    (2_155_350, 0.0685),
                    (5_000_000, 0.0965),
                    (25_000_000, 0.103),
                    (None, 0.109),
                ]
            else:
                return [
                    (8_500, 0.04),
                    (11_700, 0.045),
                    (13_900, 0.0525),
                    (80_650, 0.0585),
                    (215_400, 0.0625),
                    (1_077_550, 0.0685),
                    (5_000_000, 0.0965),
                    (25_000_000, 0.103),
                    (None, 0.109),
                ]
        else:
            # if year == 2023 and 
            if status == Status.Married:
                return [
                    (17_150, 0.04),
                    (23_600, 0.045),
                    (27_900, 0.0525),
                    (161_550, 0.055),
                    (323_200, 0.06),
                    (2_155_350, 0.0685),
                    (5_000_000, 0.0965),
                    (25_000_000, 0.103),
                    (None, 0.109),
                ]
            else:
                return [
                    (8_500, 0.04),
                    (11_700, 0.045),
                    (13_900, 0.0525),
                    (80_650, 0.055),
                    (215_400, 0.06),
                    (1_077_550, 0.0685),
                    (5_000_000, 0.0965),
                    (25_000_000, 0.103),
                    (None, 0.109),
                ]
    elif state == State.NewJersey:
        if status == Status.Married:
            return [
                (20_000, 0.014),
                (50_000, 0.0175),
                (70_000, 0.0245),
                (80_000, 0.035),
                (150_000, 0.05525),
                (500_000, 0.0637),
                (1000_000, 0.0897),
                (None, 0.1075),
            ]
        else:
            return [
                (20_000, 0.014),
                (35_000, 0.0175),
                (40_000, 0.035),
                (75_000, 0.05525),
                (500_000, 0.0637),
                (1000_000, 0.0897),
                (None, 0.1075),
            ]
    else:
        return []

def get_city_marginal_rates(city: City, year: int=None, status: Status= Status.Single):
    if city == City.NewYork:
        if status == Status.Single:
            return [
                (21_600, 0.03078),
                (45_000, 0.03762),
                (90_000, 0.03819),
                (None, 0.03876),
            ]
        else:
            return [
                (12_000, 0.03078),
                (25_000, 0.03762),
                (50_000, 0.03819),
                (None, 0.03876),
            ]
    else:
        return []

def irs(gross_income: float, state: State=None, city: City=None, year: int=2023, status: Status = Status.Single):
    tax_total = min(gross_income, get_social_security_max(year)) * SOCIAL_SECURITY_RATE
    tax_total += gross_income * MEDICARE_RATE
    tax_total += max(gross_income - get_medicare_threshold(status), 0) * MEDICARE_RATE_ADDITION

    fed_taxable_income = gross_income - get_base_deduction(year, status)
    fed_tax_total = 0
    if fed_taxable_income > 0:
        income_bracket = 0
        for ri in get_marginal_rates(year, status):
            if ri[0] and fed_taxable_income > ri[0]:
                fed_tax_total += (ri[0] - income_bracket) * ri[1]
                income_bracket = ri[0]
            else:
                fed_tax_total += (fed_taxable_income - income_bracket) * ri[1]
                break
    
    state_income_bracket = 0
    state_tax_total = 0
    for sri in get_state_marginal_rates(state, year, status):
        if sri[0] and gross_income > sri[0]:
            state_tax_total += (sri[0] - state_income_bracket) * sri[1]
            state_income_bracket = sri[0]
        else:
            state_tax_total += (gross_income - state_income_bracket) * sri[1]
            break
    
    city_income_bracket = 0
    city_tax_total = 0
    for cri in get_city_marginal_rates(city, year, status):
        if cri[0] and gross_income > cri[0]:
            city_tax_total += (cri[0] - city_income_bracket) * cri[1]
            city_income_bracket = cri[0]
        else:
            city_tax_total += (gross_income - city_income_bracket) * cri[1]
            break
    return tax_total + fed_tax_total + state_tax_total + city_tax_total
