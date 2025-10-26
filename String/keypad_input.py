class Solution:
    def keypad(self,arr : list[str] ,input : str) ->  int :
        result = ""
        input = input.upper()
        for i in range(len(input)):
            if input[i] == " ":
                result += "0"
            else:
                position = ord(input[i]) - ord('A') # ord method gets the ASCII value for upper A to Z is(65-90) , for lower(a-z) is (97-122)
                result += arr[position]
        
        return int(result)
    
arr = ["2", "22", "222",
       "3", "33", "333",
       "4", "44", "444",
       "5", "55", "555",
       "6", "66", "666",
       "7", "77", "777", "7777",
       "8", "88", "888",
       "9", "99", "999", "9999"]

input = "GEEkS FOR GEEKS"
print(Solution().keypad(arr,input))