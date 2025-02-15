class Solution {
    public String solution(String phone_number) {
        
        String str1 = "";
        int length = phone_number.length();
        str1 = phone_number.substring(length-4);
        String str2 = phone_number.substring(0, length-4);
        int length2 = str2.length();
        String str3 = "*";
        return str3.repeat(length2) + str1;
    }
}