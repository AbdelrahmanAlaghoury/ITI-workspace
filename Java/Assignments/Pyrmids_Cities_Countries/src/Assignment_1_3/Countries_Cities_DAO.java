package Assignment_1_3;
import java.util.*;
import java.io.*;
import java.util.stream.*;

public class Countries_Cities_DAO{
	
	private List<City> Cities = new ArrayList<City>();
	private List<Country> Countries = new ArrayList<Country>();
	//method to read Countries CSV file
	public List<City> readCitiesFile(String filePath){
		try {
			Scanner sc =new Scanner(new File(filePath));
			int linePointer = 0;
			while(sc.hasNextLine()) {
				String[] Line = sc.nextLine().split(",");
				if(linePointer >= 1) {
					Cities.add(new City(Line[0], Integer.parseInt(Line[1]), Double.parseDouble(Line[2]),
										Line[3], Line[4], Boolean.parseBoolean(Line[5])));
				}
				linePointer++;
			}
		}
		catch(Exception e){
			System.out.println("An Error Occured.");
			e.printStackTrace();
		}
		return Cities;
	}
	//method to read Cities CSV file
	public List<Country> readCountriesFile(String filePath){
		try {
			Scanner sc =new Scanner(new File(filePath));
			int linePointer = 0;
			while(sc.hasNextLine()) {
				String[] Line = sc.nextLine().split(",");
				if(linePointer >= 1) {
					Countries.add(new Country(Line[0],Line[1]));
				}
				linePointer++;
			}
		}
		catch(Exception e){
			System.out.println("An Error Occured.");
			e.printStackTrace();
		}
		return Countries;
	} 
	//Method to sort a given Country cities from a given HashMap based on population
	public void sortCountry(HashMap<String,List<City>> countries, String key) {
		countries.get(key).sort(Comparator.comparingInt(City::getPopulation));
		
		countries.get(key).forEach((city)->System.out.println(city.getPopulation()));
	}
	//Method to get the highest population city in each country
	public void getHighestPopInEachCountry(HashMap<String, List<City>> countries){
		countries.forEach((k, v)-> System.out.println("Key -> "+ k + "  |  Value -> " + 
													   v.stream().map(City::getPopulation)
													   .max(Comparator.comparingInt((maxVal)->maxVal)))); 
	}
	//Method to get the highest population city in each continent
	public void getHighestPopInEachContient(List<City> cities) {
		HashMap<String, Integer> hContinents = new HashMap<>();
		Set<String> sContinents = cities.stream().map(City::getContinent).collect(Collectors.toSet());
		for(String continent : sContinents) {
			int max = cities.stream().filter((city)->city.getContinent().equalsIgnoreCase(continent))
								 .map(City::getPopulation)
								 .max(Comparator.comparingInt((maxVal)->maxVal)).get();
			hContinents.put(continent, max);
		}
		hContinents.forEach((k, v)-> System.out.println("Key -> " + k + "   |  Value -> " + v));
	}
	//Method to get the highest population capital
	public void getHighestPopCapital(List<City> cities) {
		System.out.println("Heighest Pop Capital = " + cities.stream().filter((city)->city.isCapital()==true)
					   												  .map(City::getPopulation)
					   												  .max(Comparator.comparingInt((maxVal)->maxVal)).get());
	}
}