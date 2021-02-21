import pytest

from util.web_login import web_login


class Test_登录Login:

    def setup_method(self):
        pass

    def tear_method(self):
        dr = web_login()
        dr.quit()


    @pytest.mark.parametrize('loginName, password, expected',[
        (31683999, 'leke1234', '用户名不存在'),
        (3168399, 'leke12345', '用户名密码错误')
    ])
    def test_登录case01(self, loginName, password, expected):
        text = web_login(loginName, password)
        assert text == expected

    # def test_case02(self):
    #     text = web_login()
    #     assert text == '用户密码错误'
    #
    # def test_case03(self):
    #     assert 1 == 2
