

# binary search template
# int binary_search(int[] nums, int target) {
#     int left = 0, right = nums.length - 1; 
#     while(left <= right) {
#         int mid = left + (right - left) / 2;
#         if (nums[mid] < target) {
#             left = mid + 1;
#         } else if (nums[mid] > target) {
#             right = mid - 1; 
#         } else if(nums[mid] == target) {
#             // 直接返回
#             return mid;
#         }
#     }
#     // 直接返回
#     return -1;
# }

# int left_bound(int[] nums, int target) {
#     int left = 0, right = nums.length - 1;
#     while (left <= right) {
#         int mid = left + (right - left) / 2;
#         if (nums[mid] < target) {
#             left = mid + 1;
#         } else if (nums[mid] > target) {
#             right = mid - 1;
#         } else if (nums[mid] == target) {
#             // 别返回，锁定左侧边界
#             right = mid - 1;
#         }
#     }
#     // 最后要检查 left 越界的情况
#     if (left >= nums.length || nums[left] != target)
#         return -1;
#     return left;
# }


# int right_bound(int[] nums, int target) {
#     int left = 0, right = nums.length - 1;
#     while (left <= right) {
#         int mid = left + (right - left) / 2;
#         if (nums[mid] < target) {
#             left = mid + 1;
#         } else if (nums[mid] > target) {
#             right = mid - 1;
#         } else if (nums[mid] == target) {
#             // 别返回，锁定右侧边界
#             left = mid + 1;
#         }
#     }
#     // 最后要检查 right 越界的情况
#     if (right < 0 || nums[right] != target)
#         return -1;
#     return right;
# }

def binary_search(arr, target):
    left = 0
    right = len(arr)-1

    while left <= right:
        mid = (left + right)//2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        elif arr[mid] > target:
            right = mid -1
    
    return -1

if __name__ == '__main__':
    rst = binary_search([1], 2)
    print('binary search result: %d' %rst)
    rst = binary_search([1,2], 2)
    print('binary search result: %d' %rst)
    rst = binary_search([1,2,3,4,5], 2)
    print('binary search result: %d' %rst)

