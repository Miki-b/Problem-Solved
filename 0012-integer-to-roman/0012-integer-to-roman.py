class Solution:
    def intToRoman(self, num: int) -> str:
        temp = num
        new_string =""
        while(temp != 0):
            if str(temp)[0] != "4" and str(temp)[0] != "9":
                if temp >= 1000:
                    temp = temp - 1000
                    new_string += "M"
                elif temp >= 500:
                    temp = temp - 500
                    new_string += "D"
                elif temp >= 100:
                    temp = temp - 100
                    new_string += "C"   
                elif temp >= 50:
                    temp = temp - 50
                    new_string += "L"               
                elif temp >= 10:
                    temp = temp - 10
                    new_string += "X"
                elif temp >= 5:
                    temp = temp - 5
                    new_string += "V"
                elif temp >= 1:
                    temp = temp - 1
                    new_string += "I"
            else:
                if temp >= 900:
                    temp = temp - 900
                    new_string += "CM"
                elif temp >= 400:
                    temp = temp - 400
                    new_string += "CD"
                elif temp >= 90:
                    temp = temp - 90
                    new_string += "XC"   
                elif temp >= 40:
                    temp = temp - 40
                    new_string += "XL"               
                elif temp >= 9:
                    temp = temp - 9
                    new_string += "IX"
                elif temp >= 4:
                    temp = temp - 4
                    new_string += "IV"
        return new_string