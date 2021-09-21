def add_values(list1, list2, list3):
    """ Write a code to add three given lists using Python map and lambda. """
    result = map(lambda x, y, z: x + y + z, nums1, nums2, nums3) 
    print("\nNew list after adding above three lists:")
    print(list(result))



nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
nums3 = [7, 8, 9]
print(add_values(nums1, nums2, nums3))
# Expected Result: [12, 15, 18]
