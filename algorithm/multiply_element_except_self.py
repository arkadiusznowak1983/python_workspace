# My, I think better version for https://www.youtube.com/watch?v=riBWq1DvVb8
# Coding Mock Interview: Product of Array Except for Self (with Google Software Engineer)
# time complexity: O(2n)
def get_product_array(array):
    all_elements = 1
    for index, element in enumerate(array):
        if not element:
            for right_element in array[index+1:]:
                if not right_element:
                    return [0 for x in range(len(array))]
                all_elements *= right_element
            return [0 for x in range(index)] + [all_elements] + [0 for x in range(len(array)-index-1)]
        all_elements *= element
    return [all_elements/element for element in array]


assert get_product_array([1, 2, 3, 4]) == [24, 12, 8, 6]
assert get_product_array([2]) == [1]
assert get_product_array([2, 0, 3]) == [0, 6, 0]
assert get_product_array([2, 0, 3, 0, 9]) == [0, 0, 0, 0, 0]