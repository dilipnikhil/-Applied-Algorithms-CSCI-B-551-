def convertToTitle(col_num ):
    title = ''
    
    while col_num > 0:
        col_num = col_num - 1
        remainder = col_num % 26
        
        # Append the corresponding character to the title
        title = chr(ord('A') + remainder) + title
        
        # Update col_num for the next iteration
        col_num //= 26
    
    return title
