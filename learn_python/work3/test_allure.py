import pytest
#pytest E:\pengketong_python\pengketong_lg3\learn_python\work3\test_allure.py --alluredir=./result/1  收集测试结果
#allure serve ./result/1  查看测试报告
#allure generate ./result/1 -o ./allure-report/5 --clean 用执行的数据./result/1在./allure-report/5生成报告
#allure open -h 127.0.0.1 -p 8883 ./allure-report/5 开启一个服务，打开测试报告


def test_success():
    """this test succeeds"""
    assert True


def test_failure():
    """this test fails"""
    assert False


def test_skip():
    """this test is skipped"""
    pytest.skip('for a reason!')


def test_broken():
    raise Exception('oops')

if __name__ == '__main__':
    pytest.main()



print(111111195%50)