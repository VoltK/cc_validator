package com.company;
import javax.swing.JOptionPane;

public class CardValidator {

    public static void main(String[] args) {

        String card = JOptionPane.showInputDialog("Enter card number to validate: ");

        if(card.matches("[0-9]+")){

            int [] cardArr = getNumbers(card);

            int sum = calculateSum(cardArr);

            showResult(sum, card);
        }
        else{
            JOptionPane.showMessageDialog(null, "You are not allowed to enter characters!",
                    "Invalid Input", JOptionPane.ERROR_MESSAGE);
        }

    }

    // Convert string to Int array
    public static int [] getNumbers(String number){
        int [] numbers_arr = new int[number.length()];

        for (int x = 0; x < numbers_arr.length; x++){
            numbers_arr[x] = Character.getNumericValue(number.charAt(x));
        }

        return numbers_arr;
    }

    public static int calculateSum(int [] numbers){
        int sum = 0;

        for (int x = numbers.length - 2; x >= 0; x-=2){
            int evenNumber = numbers[x] * 2;
            int oddNumber = numbers[x+1];

            // if doubled number is 2 digits number we add those 2 digits together( or just subtract 9)
            sum += evenNumber > 9 ? evenNumber - 9 + oddNumber: evenNumber + oddNumber;

        }

        return sum;
    }

    public static void showResult(int sum, String card){

        if(sum % 10 == 0){
            JOptionPane.showMessageDialog(null,"Valid Card Number: " + card,
                    "Valid",JOptionPane.INFORMATION_MESSAGE);
        }
        else{
            JOptionPane.showMessageDialog(null,"Invalid Card Number: " + card,
                    "Invalid", JOptionPane.ERROR_MESSAGE);
        }

    }
}
