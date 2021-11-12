package Assignment_1_3;

public class City{
	private String countryCode;
	private String name;
	private String continent;
	private double surfaceArea;
	private int population;
	private boolean isCapital;
	public City(String name, int population, double surfaceArea, String countryCode, String continent,boolean isCapital){
		this.name = name;
		this.countryCode = countryCode;
		this.continent = continent;
		this.surfaceArea = surfaceArea;
		this.population = population;
		this.isCapital = isCapital;
	}
	
	public String getCountryCode() {
		return this.countryCode;
	}
	public String getName() {
		return this.name;
	}
	public String getContinent() {
		return this.continent;
	}
	public double getSurfaceArea() {
		return this.surfaceArea;
	}
	public int getPopulation() {
		return this.population;
	}
	public boolean isCapital() {
		return this.isCapital;
	}
}