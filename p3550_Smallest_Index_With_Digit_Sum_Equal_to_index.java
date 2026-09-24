class Solution {
    public int smallestIndex(int[] nums) {
        int index = -1;
        for (int i = 0; i < nums.length; i++) {
            int digitSum = 0;
            int num = nums[i];
            while (num > 0) {
                digitSum += num % 10;
                num /= 10;
            }
            if (i == digitSum) {
                index = i;
                break;
            }
        }
        return index;
    }
}

public class p3550_Smallest_Index_With_Digit_Sum_Equal_to_index {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums = { 1, 3, 2 };
        int result = solution.smallestIndex(nums);
        System.out.println("Smallest index with digit sum equal to index: " + result);
    }
}