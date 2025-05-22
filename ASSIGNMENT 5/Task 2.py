first_10_nums = list(range(1, 11))
print("Original list: %s" % (first_10_nums,))
extract_5_elems = first_10_nums[:5]
print("Extracted first five elements: %s" % (extract_5_elems,))
reversed_5_elems = extract_5_elems[::-1]
print("Reversed extracted elements: %s" % (reversed_5_elems,))