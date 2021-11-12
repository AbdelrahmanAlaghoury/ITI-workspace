package Assignment_1_3;

public class Country{
	private String countryCode;
	private String name;
	
	public Country(String name, String countryCode) {
		this.countryCode = countryCode;
		this.name = name;
	}
	
	public String getCountryCode() {
		return this.countryCode;
	}
	public String getName() {
		return this.name;
	}
}