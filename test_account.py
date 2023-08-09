from account import *
import pytest

class TestAccount():
    def test_deposit(self):
        t = Account("TEST_ACCOUNT")
        
        assert False == t.deposit(-1)
        assert False == t.deposit(0)

        assert True == t.deposit(10)
        assert True == t.deposit(.5)
        
        assert False == t.deposit(-1)
        assert False == t.deposit(0)

        with pytest.raises( TypeError ):
            t.deposit("H")
            t.deposit(None)
        
    def test_withdraw(self):
        t = Account("TEST_ACCOUNT")

        assert False == t.withdraw(1)
        assert False == t.withdraw(-1)

        t.deposit(999)
        assert False == t.withdraw(-1)
        assert False == t.withdraw(0)

        assert True == t.withdraw(1)
        assert True == t.withdraw(1.5)

        t.withdraw(.5)
        assert True == t.withdraw(996.0)
        assert pytest.approx(0) == t.get_balance()
        
        t.deposit(999)

        with pytest.raises( TypeError ):
            t.withdraw("H")
            t.withdraw(None)


    def test_get_balance(self):
        t = Account("TEST_ACCOUNT")

        assert pytest.approx(0) == t.get_balance()
        t.withdraw(1)
        assert pytest.approx(0) == t.get_balance()
        t.deposit(5.5)
        assert pytest.approx(5.5) == t.get_balance()
        t.deposit(5)
        assert pytest.approx(10.5) == t.get_balance()
        t.withdraw(11)
        assert pytest.approx(10.5) == t.get_balance()
        t.withdraw(10.5)
        assert pytest.approx(0) == t.get_balance()

        t.deposit(5)
        t.deposit(-5)
        assert pytest.approx(5) == t.get_balance()
        t.withdraw(-5)
        assert pytest.approx(5) == t.get_balance()        

    def test_get_name(self, *args):
        for nameTest in args:
            t = Account(nameTest)
            assert nameTest == t.get_name()


if __name__ == "__main__":
    tester = TestAccount()

    tester.test_get_name("t", "John Oliver", "", "5", 3.5, 1, None)
    tester.test_get_balance()
    tester.test_withdraw()
    tester.test_deposit()