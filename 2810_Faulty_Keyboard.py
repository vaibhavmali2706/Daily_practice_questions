class solution:
    def faulty_keyboard(self,s):
        sr=""
        for a in s:
            if a != "i" :
                sr=sr+a
            if a == "i" :
                sr=sr[::-1]
                
        return sr
st="poiinter"

sol=solution()
print(sol.faulty_keyboard(st))
        