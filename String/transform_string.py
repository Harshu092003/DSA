class Solution :
    def min_operation(self, A:str , B:str ) -> int :
        a = list(A)
        b = list(B)
        print(a,b)
        count = 0
        if a == b :
            pass
        
        for i in range (len(a)) :
            if a[i] != b[i] :
                a[i] = b[i]
                count +=1
                
        
        
                    
        return  count,a
                
                
                  
print(Solution().min_operation('ABD','BAD'))
print(Solution().min_operation('EACBD','EABCD'))