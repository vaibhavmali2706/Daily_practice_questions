publis class solution {
    public int sumOfMultiples(int n) {
        int sum = 0;
        for (int i = 0; i <= n; i++) {
            if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
                sum += i;
            }
        }
        return sum;
    }
}


public class 2652_Sum_Multiples {
    public static void main(String[] args) {
        solution s = new solution();
        int n = 9;
        int result = s.sumOfMultiples(n);
        System.out.println("Sum of multiples of 3, 5, or 7 up to " + n + ": " + result);
    }
}

    }
}
