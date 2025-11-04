class Solution:
    def palindromic_subsequence(self, s : str) -> int :
        sub_sequence_of_1 = []
        sub_sequence_of_2 = []

        for i in range (len(s)):
            sub_sequence_of_1.append(s[i])
            sub_sequence_of_2.append(s[i:i+2])

        union_list= list(set(sub_sequence_of_1) | set(sub_sequence_of_2))
        count =0
        for i in range(len(union_list)):
            substring = union_list[i]
            if substring == substring[::-1]:
                count +=1

        return count
    
s ="abcd"
print(Solution().palindromic_subsequence(s))