package com.company;
import javax.swing.JOptionPane;

public class CardValidator {

    public static void main(String[] args) {

        String card = JOptionPane.showInputDialog("Enter card number to validate: ");

        if(card.matches("[0-9]+")){
            int sum = calculateSum(card);

            showResult(sum, card);
        }
        else{
            JOptionPane.showMessageDialog(null, "You are not allowed to enter characters!",
                    "Invalid Input", JOptionPane.ERROR_MESSAGE);
        }

    }
    
    public static int calculateSum(String numbers){
        int sum = 0;

        for (int x = numbers.length() - 2; x >= 0; x-=2){
            int evenNumber = Character.getNumericValue(numbers.charAt(x)) * 2;
            int oddNumber = Character.getNumericValue(numbers.charAt(x+1));

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
