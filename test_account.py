from account import *
import pytest

class TestAccount():
    def test_init(self):
        for accountName in [ "TEST_ACCOUNT", "John" ]:
            t = Account(accountName)
            assert pytest.approx(0) == t.get_balance()
            assert accountName is t.get_name()

    def test_deposit(self):
        t = Account("TEST_ACCOUNT")
        
        # Bad amounts
        assert False == t.deposit(-1)
        assert pytest.approx(0) == t.get_balance()

        assert False == t.deposit(0)
        assert pytest.approx(0) == t.get_balance()

        # Int
        assert True == t.deposit(10)
        assert pytest.approx(10) == t.get_balance()

        # Float
        assert True == t.deposit(.5)
        assert pytest.approx(10.5) == t.get_balance()

        # Bad amounts w/ non-zero balance
        assert False == t.deposit(-1)
        assert pytest.approx(10.5) == t.get_balance()
        
        assert False == t.deposit(0)
        assert pytest.approx(10.5) == t.get_balance()
        
    def test_withdraw(self):
        t = Account("TEST_ACCOUNT")

        # large withdraw w/ 0 balance
        assert False == t.withdraw(1)
        assert pytest.approx(0) == t.get_balance()

        # Negative withdraw
        assert False == t.withdraw(-1)
        assert pytest.approx(0) == t.get_balance()

        # Zero withdraw
        assert False == t.withdraw(0)
        assert pytest.approx(0) == t.get_balance()

        t.deposit(10)
        # Negative withdraw w/ non-zero balance
        assert False == t.withdraw(-1)
        assert pytest.approx(10) == t.get_balance()

        # Zero withdraw w/ non-zero balance
        assert False == t.withdraw(0)
        assert pytest.approx(10) == t.get_balance()

        # Int withdraw
        assert True == t.withdraw(1)
        assert pytest.approx(9) == t.get_balance()

        # Float withdraw
        assert True == t.withdraw(1.5)
        assert pytest.approx(7.5) == t.get_balance()

        # Large float withdraw
        assert False == t.withdraw(10.5)
        assert pytest.approx(7.5) == t.get_balance()

        # Large int withdraw
        assert False == t.withdraw(10)
        assert pytest.approx(7.5) == t.get_balance()
        
        # Back to 0 withdraws
        assert True == t.withdraw(.5)
        assert True == t.withdraw(7.0)
        assert pytest.approx(0) == t.get_balance()
        

    def test_get_balance(self):
        t = Account("TEST_ACCOUNT")

        # Initial bal
        assert pytest.approx(0) == t.get_balance()

        # Float deposit
        assert True == t.deposit(5.5)
        assert pytest.approx(5.5) == t.get_balance()

        # Int deposit
        assert True == t.deposit(5)
        assert pytest.approx(10.5) == t.get_balance()

        # Int withdraw
        assert True == t.withdraw(1)
        assert pytest.approx(9.5) == t.get_balance()

        # Float withdraw
        assert True == t.withdraw(1.0)
        assert pytest.approx(8.5) == t.get_balance()

        # Float large withdraw
        assert False == t.withdraw(99.99)
        assert pytest.approx(8.5) == t.get_balance()

        # int large withdraw
        assert False == t.withdraw(11)
        assert pytest.approx(8.5) == t.get_balance()

        # Zeroing
        assert True == t.withdraw(8.5)
        assert pytest.approx(0) == t.get_balance()

        # Non-zeroing
        assert True == t.deposit(5)
        assert pytest.approx(5) == t.get_balance()

        # Negative amount w/ non-zero balance
        assert False == t.deposit(-5)
        assert pytest.approx(5) == t.get_balance()
        assert False == t.withdraw(-5)
        assert pytest.approx(5) == t.get_balance()

        # zero amount w/ non-zero balance
        assert False == t.deposit(0)
        assert pytest.approx(5) == t.get_balance()
        assert False == t.withdraw(0)
        assert pytest.approx(5) == t.get_balance() 

    def test_get_name(self, *args):
        for nameTest in args:
            t = Account(nameTest)
            assert nameTest == t.get_name()


if __name__ == "__main__":
    tester = TestAccount()

    tester.test_init()
    tester.test_get_name("t", "John Oliver", "Ted Teddybear")
    tester.test_get_balance()
    tester.test_withdraw()
    tester.test_deposit()