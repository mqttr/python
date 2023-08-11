from account import *
import pytest

class TestAccount():
    def __init__(self):
        print("Running __init__")

        self.a1 = Account("John")

        self.test_init()
        self.test_get_name("t", "John Oliver", "Ted Teddybear")
        self.test_get_balance()
        self.test_withdraw()
        self.test_deposit()
        
        self.teardown_method()

    def teardown_method(self):
        print("Running teardown_method")

        del self.a1

    def test_init(self):
        print("Running test_init")

        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.get_name() == "John"

    def test_deposit(self):
        print("Running test_deposit")

        # Bad amounts
        assert False == self.a1.deposit(-1)
        assert pytest.approx(0) == self.a1.get_balance()

        assert False == self.a1.deposit(0)
        assert pytest.approx(0) == self.a1.get_balance()

        # Int
        assert True == self.a1.deposit(10)
        assert pytest.approx(10) == self.a1.get_balance()

        # Float
        assert True == self.a1.deposit(.5)
        assert pytest.approx(10.5) == self.a1.get_balance()

        # Bad amounts w/ non-zero balance
        assert False == self.a1.deposit(-1)
        assert pytest.approx(10.5) == self.a1.get_balance()
        
        assert False == self.a1.deposit(0)
        assert pytest.approx(10.5) == self.a1.get_balance()

        assert True == self.a1.withdraw(10.5)
        assert pytest.approx(0) == self.a1.get_balance()

        
    def test_withdraw(self):
        print("Running test_withdraw")


        # large withdraw w/ 0 balance
        assert False == self.a1.withdraw(1)
        assert pytest.approx(0) == self.a1.get_balance()

        # Negative withdraw
        assert False == self.a1.withdraw(-1)
        assert pytest.approx(0) == self.a1.get_balance()

        # Zero withdraw
        assert False == self.a1.withdraw(0)
        assert pytest.approx(0) == self.a1.get_balance()

        self.a1.deposit(10)
        # Negative withdraw w/ non-zero balance
        assert False == self.a1.withdraw(-1)
        assert pytest.approx(10) == self.a1.get_balance()

        # Zero withdraw w/ non-zero balance
        assert False == self.a1.withdraw(0)
        assert pytest.approx(10) == self.a1.get_balance()

        # Int withdraw
        assert True == self.a1.withdraw(1)
        assert pytest.approx(9) == self.a1.get_balance()

        # Float withdraw
        assert True == self.a1.withdraw(1.5)
        assert pytest.approx(7.5) == self.a1.get_balance()

        # Large float withdraw
        assert False == self.a1.withdraw(10.5)
        assert pytest.approx(7.5) == self.a1.get_balance()

        # Large int withdraw
        assert False == self.a1.withdraw(10)
        assert pytest.approx(7.5) == self.a1.get_balance()
        
        # Back to 0 withdraws
        assert True == self.a1.withdraw(.5)
        assert True == self.a1.withdraw(7.0)
        assert pytest.approx(0) == self.a1.get_balance()

        assert False == self.a1.withdraw(0)
        assert pytest.approx(0) == self.a1.get_balance()
        

    def test_get_balance(self):
        print("Running test_get_balance")


        # Initial bal
        assert pytest.approx(0) == self.a1.get_balance()

        # Float deposit
        assert True == self.a1.deposit(5.5)
        assert pytest.approx(5.5) == self.a1.get_balance()

        # Int deposit
        assert True == self.a1.deposit(5)
        assert pytest.approx(10.5) == self.a1.get_balance()

        # Int withdraw
        assert True == self.a1.withdraw(1)
        assert pytest.approx(9.5) == self.a1.get_balance()

        # Float withdraw
        assert True == self.a1.withdraw(1.0)
        assert pytest.approx(8.5) == self.a1.get_balance()

        # Float large withdraw
        assert False == self.a1.withdraw(99.99)
        assert pytest.approx(8.5) == self.a1.get_balance()

        # int large withdraw
        assert False == self.a1.withdraw(11)
        assert pytest.approx(8.5) == self.a1.get_balance()

        # Zeroing
        assert True == self.a1.withdraw(8.5)
        assert pytest.approx(0) == self.a1.get_balance()

        # Non-zeroing
        assert True == self.a1.deposit(5)
        assert pytest.approx(5) == self.a1.get_balance()

        # Negative amount w/ non-zero balance
        assert False == self.a1.deposit(-5)
        assert pytest.approx(5) == self.a1.get_balance()
        assert False == self.a1.withdraw(-5)
        assert pytest.approx(5) == self.a1.get_balance()

        # zero amount w/ non-zero balance
        assert False == self.a1.deposit(0)
        assert pytest.approx(5) == self.a1.get_balance()
        assert False == self.a1.withdraw(0)
        assert pytest.approx(5) == self.a1.get_balance() 

        assert True == self.a1.withdraw(5)
        assert pytest.approx(0) == self.a1.get_balance()
        

    def test_get_name(self, *args):
        print("Running test_get_name")


        for nameTest in args:
            t = Account(nameTest)
            assert nameTest == t.get_name()
            del t


if __name__ == "__main__":
    t = TestAccount()