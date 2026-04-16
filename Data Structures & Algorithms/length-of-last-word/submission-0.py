class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cleaned_str =" ".join(s.split())
        str_array = cleaned_str.split(" ")
        return len(str_array[len(str_array)-1])