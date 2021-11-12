package Assignment_2;
import java.util.function.*;

public class stringUtils{
	
	public String betterStringLength(String s1, String s2, BiPredicate<String, String> p) {
		if(p.test(s1, s2)) {
			return s1;
		}
		return s2;
	}
	
	public boolean isOnlyAlphabets(String s, Function<String, Boolean> f) {
		if(f.apply(s)) {
			return true;
		}
		return false;
	}
	
	public static boolean checkString(String s) {
		char[] sChars = s.toCharArray();
		for(int i = 0; i <sChars.length; i++) {
			if(! Character.isLetter(sChars[i])) {
				return false;
			}
		}
		return true;
	}
}
