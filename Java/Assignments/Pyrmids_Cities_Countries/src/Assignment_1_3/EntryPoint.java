package Assignment_1_3;

import java.util.*;
import java.util.stream.Collectors;

public class EntryPoint{
	public static void main(String[] args) {
		/***************************************************************************************************************************/
		//Exercise 1
		/***************************************************************************************************************************/
		//create an object of Countries_Cities_DAO to read Countries and Cities files
		Countries_Cities_DAO CitiesCountriesDAO = new Countries_Cities_DAO();
		
		//using DAO methods to read the files 
		List<City> Cities = CitiesCountriesDAO.readCitiesFile("cities.csv");
		List<Country> Countries = CitiesCountriesDAO.readCountriesFile("countries.csv");
		
		//create an country Iterator to iterate the countries objects to get their codes for HashMap keys construction
		Iterator<Country> Countries_Iter = Countries.iterator();
		
		//create the HashMap of Countries and their Cities
		Map<String, List<City>> CountryCodes = new HashMap<>();
		
		CountryCodes = Cities.stream().collect(Collectors.groupingBy(City::getContinent
				));//.forEach((k,x)->x.forEach((c)->System.out.println(k+ "->>>" +c.getPopulation())));
		//for(String s : CountryCodes.keySet()) {
			//for(City c:s.get(s))
			
		//}
		CountryCodes.forEach((k, v)->v.forEach((x)->System.out.println(k+"-> "+x.getPopulation())));
		
		//create an temp list to extract the Cities of each country based on the country code 
		//List<City> Temp = new ArrayList<>();
		
		//looping on the Countries Objects
		//while(Countries_Iter.hasNext()){
			//Store the current object reference in a temp obj to use it in cities capturing out of cities list
			//Country currentCountryCodeObj = Countries_Iter.next();
			
			//compare the country code with each city code and if it was matched we will add it to the temp list
			
			//Cities.forEach((City) ->{
				//if(City.getCountryCode().equalsIgnoreCase(currentCountryCodeObj.getCountryCode())) {
					//Temp.add(City);				
				//}
			
			//}); 
			
			
			//put the country code as a key and the cities list as value in the HashMap
			//CountryCodes.put(currentCountryCodeObj.getCountryCode(), new ArrayList<City>(Temp));
			
			//reset the temp list to use it in next country code 
			//Temp.removeAll(Cities);
		//}
		
		//CountryCodes.forEach((k, v)->CountryCodes.get(k).forEach((x)->System.out.println(k+"-> "+x.getPopulation())));
		
		//CitiesCountriesDAO.sortCountry(CountryCodes, "BRA");
		
		/***************************************************************************************************************************/
		//Exercise 3
		/***************************************************************************************************************************/
		//CitiesCountriesDAO.getHighestPopInEachCountry(CountryCodes);
		
		CitiesCountriesDAO.getHighestPopInEachContient(Cities);
		
		CitiesCountriesDAO.getHighestPopCapital(Cities);
	}
}