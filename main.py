
import pandas as pd
import requests
import json

import au
import ca
import gb
import hk
import ind
import jp
import sg
import us
import world

import sys
import os
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(__file__)), 'common', 'src'))
from common import plotter

FX_API_URL = 'https://v6.exchangerate-api.com/v6/86cf0563936a598b9a7b0112/latest/USD'

def main():

    response = requests.get(FX_API_URL)
    if response.status_code != 200:
        raise RuntimeError(f'{response.url} URL request failed {response.reason}')
    result = json.loads(response.text)
    fx_rates = result['conversion_rates']
    hkd = fx_rates['HKD']
    sgd = fx_rates['SGD']
    inr = fx_rates['INR']
    jpy = fx_rates['JPY']
    gbp = fx_rates['GBP']
    aud = fx_rates['AUD']
    cad = fx_rates['CAD']

    income_min = 50_000
    income_max = 500_000
    income_inc = 10_000
    tax_net_perc = {}
    income_net = {}
    calc_info = [
        ('HongKong', hk.ird, hkd, {}),
        ('Singapore', sg.iras, sgd, {}),
        ('India', ind.itr, inr, {}),
        ('UK', gb.itr, gbp, {}),
        ('US-NewYork-M', us.irs, 1, dict(state=us.State.NewYork, city=us.City.NewYork, status=world.Status.Married)),
        ('US-NewYork', us.irs, 1, dict(state=us.State.NewYork, city=us.City.NewYork)),
        ('US-NewJersey-M', us.irs, 1, dict(state=us.State.NewJersey, status=world.Status.Married)),
        # ('US-Chicago', us.irs, 1, dict(state=us.State.Illinois)),
        ('US-Florida-M', us.irs, 1, dict(status=world.Status.Married)),
        ('US-Florida', us.irs, 1, {}),
        ('Australia', au.to, aud, {}),
        ('Japan-Tokyo', jp.nta, jpy, {}),
        ('Canada-Toronto', ca.cra, cad, dict(state='Ontario')),
        ]
    cols = [ci[0] for ci in calc_info]
    for income_i in range(income_min, income_max+1, income_inc):
        taxes_i = [ci[1](income_i * ci[2], **ci[3]) / ci[2] for ci in calc_info]
        income_net[income_i] = [income_i - ti for ti in taxes_i]
        tax_net_perc[income_i] = [ti/income_i for ti in taxes_i]
    tax_net_perc_df = pd.DataFrame.from_dict(tax_net_perc, orient='index', columns=cols)
    income_net_df = pd.DataFrame.from_dict(income_net, orient='index', columns=cols)
    plotter.plot_series(tax_net_perc_df, income_net_df, title='Taxes',
                        x_name='Gross Income($)', x_format=None, y_name='Net(%)', y_format=',.2%',
                        hovermode='y',
                        y2_name='Net($)', y2_format=None)

if __name__ == "__main__":
    main()
