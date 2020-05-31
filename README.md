# Vhinny - Financial Data API
Public API to access Vhinny's Financial Data. For more information, please visit us at https://www.vhinny.com/about

### Installation
Make sure you have Python 3.6+ on your system, then run ``` pip install vhinny ```

### Documentation

Start by importing the package
```
# Importing Vhinny always is a good place to start
from vhinny import Vhinny
```
Initiate your instance
```
vhi = Vhinny()
```
Looking for a Balance Sheet? Try this:
```
data = vhi.balance_sheet(ticker='AAPL', year=2012)
```
This will return a dictionary similar to the one below. Note, if we don't have data for a combination
of (ticker, year) you've specified, this call will return ``` None ```
```
# Sample response:
{
    'accounts_payable_items': 2012000000.0, 
    'accounts_receivable': 7885000000.0, 
    'assets': 93798000000.0, 
    'cash_and_equivalents': 14778000000.0, 
    'current_assets': 60454000000.0, 
    'filing_date': '2013-01-29', 
    'goodwill': 10537000000.0, 
    'intangible_assets': 7473000000.0, 
    'inventory': 505000000.0, 
    'liabilities': 22083000000.0, 
    'liabilities_current': 14337000000.0, 
    'liabilities_non_current': 7746000000.0, 
    'long_term_debt_current': 0.0, 
    'long_term_debt_non_current': 2988000000.0, 
    'non_current_assets': 33344000000.0, 
    'property_plant_and_equipment': 11854000000.0, 
    'reported_as_of': '2012-12-31', 
    'retained_earnings': 48342000000.0, 
    'stockholders_equity': 71715000000.0, 
    'treasury_stock_value': None
}
```
You can also request Income Statement, and the Statement of Cash Flows like so:
```
vhi.income_statement(ticker='AAPL', year=2012)
vhi.cash_flows(ticker='AAPL', year=2012)
```

Happy coding!