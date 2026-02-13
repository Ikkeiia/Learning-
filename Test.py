data = """SKU: 32515151jDJASD1924
SKU: 12389719287498124
SKU: JKDFLK893479831749
SKU: fdakf998u3498U(jD(
SKU: aSDJALKSJD189432719
"""

ids = []

# .splitlines() automatically splits by the hidden \n (newline)
for line in data.splitlines():
    # Only process lines that actually contain data
    if line.strip():
        # Option A: Slicing (We know "SKU: " is 5 characters long)
        clean_id = line[5:] 
        
        # Option B: Replace (Better if you don't want to count indices)
        # clean_id = line.replace("SKU: ", "")
        
        ids.append(clean_id)

print(ids)