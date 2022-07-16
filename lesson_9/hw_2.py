class Road():
    def m_asf(self, lenght, weight):
        mas_asf = (lenght * weight * 25 * 5)//100
        print('массa асфальта, необходимого для покрытия всей дороги: ', mas_asf, 'тонн')

r = Road()
r.m_asf(20, 500)