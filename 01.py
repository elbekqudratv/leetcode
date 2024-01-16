
class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Elementlar soni
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
solution = Solution()
input_nums = [3, 2, 2, 3]
value_to_remove = 3

result = solution.removeElement(input_nums, value_to_remove)
print("Natija:", result)
print("Yangi ro'yxat:", input_nums[:result])


#ikkinchi ko'rinishi

#def removeElement(nums, val):
#    k = 0
#    for i in range(len(nums)):
#        if nums[i] != val:
#            nums[k] = nums[i]
#            k += 1
#    return k
#
# Test uchun funksiya
#def test_removeElement():
#    nums1 = [3, 2, 2, 3]
#    val1 = 3
#    expectedNums1 = [2, 2]
#    k1 = removeElement(nums1, val1)
#    nums1 = nums1[:k1]  # Foydalanilmagan elementlarni olib tashlash
#    assert k1 == len(expectedNums1)
#    assert sorted(nums1) == sorted(expectedNums1)
#
#    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
#    val2 = 2
#    expectedNums2 = [0, 1, 4, 0, 3]
#    k2 = removeElement(nums2, val2)
#    nums2 = nums2[:k2]  # Foydalanilmagan elementlarni olib tashlash
#    assert k2 == len(expectedNums2)
#    assert sorted(nums2) == sorted(expectedNums2)
#
#    print("Testlar muvaffaqiyatli yakunlandi!")
#
# Testlarni ishga tushurish
#test_removeElement()
