def letterCombinations(digits: str):
    if not digits:
        return []

    # Mapping of digits to letters
    phone_map = {
        "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
        "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
    }
    
    res = []

    def backtrack(index, path):
        # Base case: if the path is the same length as digits
        if len(path) == len(digits):
            res.append("".join(path))
            return
        
        # Get letters for the current digit and iterate
        letters = phone_map[digits[index]]
        for letter in letters:
            path.append(letter)       # Choose
            backtrack(index + 1, path) # Explore
            path.pop()                # Un-choose (backtrack)

    backtrack(0, [])
    return res
