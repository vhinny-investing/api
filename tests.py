from vhinny import Vhinny
import unittest


class VhinnyTests(unittest.TestCase):

    vhinny = Vhinny()

    def test_balance_sheet(self):
        data = self.vhinny.balance_sheet(ticker='GOOG', year=2012)
        print(f'Balance Sheet: {data}')
        assert 'current_assets' in data, f'Expected item is not returned: current_assets'

    def test_income_statement(self):
        data = self.vhinny.income_statement(ticker='GOOG', year=2012)
        print(f'Income Statement: {data}')
        assert 'net_income' in data, f'Expected item is not returned: net_income'

    def test_cash_flows(self):
        data = self.vhinny.cash_flows(ticker='GOOG', year=2012)
        print(f'Cash Flows Statement: {data}')
        assert 'cash_at_period_end' in data, f'Expected item is not returned: cash_at_period_end'

    def test_invalide_ticker(self):
        data = self.vhinny.balance_sheet('HSPSD', 2013)

    # def test_stress(self):
    #     for i in range(100):
    #         data = self.vhinny.balance_sheet('AAPL', 2013)
    #         print(i, data)


if __name__ == '__main__':
    unittest.main()