package Assignment_2;

public class EntryPoint {

	public static void main(String[] args) {
		stringUtils su = new stringUtils();
		
		System.out.println(su.betterStringLength("Test_String_1", "TestString_2", 
												(s1,s2)->s1.length()>s2.length() ? true : false));
		
		System.out.println(su.isOnlyAlphabets("StringTest", stringUtils::checkString));
		
		System.out.println(su.isOnlyAlphabets("String_Test", stringUtils::checkString));		
	}
}
