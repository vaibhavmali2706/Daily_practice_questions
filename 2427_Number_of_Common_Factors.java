class Solution {
    public int commonFactors(int a, int b) {
        int cnt=0;
        int low =0;
            if (a<b){
            low=a;
        }
        else{
            low =b;
        }
        for (int i =0;i<=low;i++){
            if (i==0){
                
            }
            else if (a%i==0 && b%i ==0){
                cnt+=1;
            }
        }
        return cnt;
        
    }
}
public class 2427_Number_of_Common_Factors {
    public static void main(String[] args) {
        Solution solution = new Solution();
        int a = 12;
        int b = 18;
        int result = solution.commonFactors(a, b);
        System.out.println("Number of common factors between " + a + " and " + b + ": " + result);
    }
}
