class FizzBuzz:
    def __init__(self, number):
        self.n = number
        self.f = 'Fizz'
        self.b = 'Buzz'
        self.fb = 'FizzBuzz'
        self.res = []
        
    def calc_fb(self):
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                self.res.append(self.fb)
                continue
            elif i % 3 == 0:
                self.res.append(self.f)
                continue
            elif i % 5 == 0:
                self.res.append(self.b)
                continue
            else:
                self.res.append(str(i))
                
        return self.res

class DefangIPAddress:
    def __init__(self, ip_address):
        self.ipa = ip_address
        self.len_ipa = len(ip_address)
        self.ip_dot_count = ip_address.count('.')
    
    def defang(self):
        if self.len_ipa > 15 or self.ip_dot_count != 3:
            return (f'[ERROR]: INVALID IP ADDRESS --> {self.ipa}')
        defanged = '[.]'.join(self.ipa.split('.'))
        return (f'Defanged IP Address {self.ipa} --> {defanged}')
        
        
def main():

    for num in [10, 20, 30]:
        fizzbuzz = FizzBuzz(num)
        print(f'Calc FizzBuzz for {num}:\n{fizzbuzz.calc_fb()}\n')
    
    for ip in ['0.0.0.0', '127.092.2.1', '127.0.0.1', '1', '10293801923809']:
        defang_ip = DefangIPAddress(ip)
        print(defang_ip.defang())
        
        
if __name__ == "__main__":
    main()