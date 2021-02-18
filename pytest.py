import pytest
#封装函数
def test_001():
    print('开始')
    assert 1+2==3 #断言
    print('结束')
def test_002():
    assert 1+3==1 #断言


#封装测试类
class Test_login:#类需以Test开头,登录类可以把登录相关的接口封装
    def test_003(self):
        assert 1+5==6 #断言


if __name__ == '__main__':
    pytest.main(['test_fc.py','-s'])#"-s"输出打印信息，如果不加这个参数，不能输出print内容
