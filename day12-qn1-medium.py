# Qn. Given a sentence in the form of a string, convert it into its equivalent mobile numeric keypad sequence. 

# Unoptimized easy solution
def map_letter_to_num() -> dict:
    # Each index corresponds a letter in English from A to Z
    letter_to_num = {}
    idx = 0
    for i in range(2, 10):
        # Set the inner bound
        if i == 7 or i == 9:
            lower = 4
        else:
            lower = 3
        # Initialize current num pad equivalent
        num_equiv = i
        for j in range(0, lower):
            letter_to_num[chr(65 + idx)] = {"equiv": num_equiv, "raise": j + 1}
            num_equiv = num_equiv * 10 + i
            idx += 1
    return letter_to_num
            
def main(sentence: str) -> int:
    size = len(sentence)
    if size == 0:
        return 0
    letter_to_num = map_letter_to_num()
    num_equiv = letter_to_num[sentence[-1]]["equiv"]
    curr_raise = letter_to_num[sentence[-1]]["raise"]
    for idx in range(size - 2, -1, -1):
        char = sentence[idx]
        if ord(char) >= 65 and ord(char) <= 90:
            num_equiv = letter_to_num[char]["equiv"] * (10 ** curr_raise) + num_equiv
            curr_raise += letter_to_num[char]["raise"]
        else:
            curr_raise += 1
    return num_equiv

        
        
        
        
    
    
    
