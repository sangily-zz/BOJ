class Repo:
    cnt = 0
    def devision(self, a):
        num_list = []
        while a>0:
            num_list.insert(0, a%10)
            a = (a - a%10)/10
        if num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            return True
        else: return False
    def research(self, b):
        if b<100: return self.cnt + b
        if self.devision(b):
            self.cnt += 1
        return self.research(b-1)

c = int(input())
sol = Repo()
print(sol.research(c))
