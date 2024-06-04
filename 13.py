from typing import List


class Solution:
    def romanToInt(self, s: str) -> int:
        unique_roman_symbols_map = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "III": 3,
            "II": 2,
            "I": 1,
        }

        mixed_roman_symbols_map = {
            "CM": 900,
            "CD": 400,
            "XC": 90,
            "XL": 40,
            "IX": 9,
            "IV": 4,
        }

        total = 0
        for mixed_symbol, value in mixed_roman_symbols_map.items():
            total += s.count(mixed_symbol) * value
            s = s.replace(mixed_symbol, "")
            if len(s) == 0:
                break


        for unique_symbol, value in unique_roman_symbols_map.items():
            total += s.count(unique_symbol) * value
            s = s.replace(unique_symbol, "")
            if len(s) == 0:
                break
        
        return total




solution = Solution()

print(solution.romanToInt(s="III")) # 3
print(solution.romanToInt(s="LVIII")) # 58
print(solution.romanToInt(s="MCMXCIV")) # 1994
print(solution.romanToInt(s="DCXXI")) # 621