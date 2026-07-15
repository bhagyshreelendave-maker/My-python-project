class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 1. Handle overflow edge case
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
            
        # 2. Determine the sign of the quotient
        # True if result is negative, False otherwise
        negative = (dividend < 0) ^ (divisor < 0)
        
        # 3. Work with absolute values
        abs_dividend = abs(dividend)
        abs_divisor = abs(divisor)
        
        quotient = 0
        
        # 4. Binary long division using bit shifting
        while abs_dividend >= abs_divisor:
            temp_divisor = abs_divisor
            multiple = 1
            
            # Find the largest multiple using left shifts
            while abs_dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
                
            # Subtract the largest found multiple and update quotient
            abs_dividend -= temp_divisor
            quotient += multiple
            
        # Apply sign and return
        return -quotient if negative else 
