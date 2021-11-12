package Assignment_Pyramids_4;

import static java.util.stream.Collectors.toList;
import java.io.File;
import java.util.*;
import java.util.stream.*;

public class PyramidCSDAO{
	
	private List<Pyramid> Pyrmids = new ArrayList<Pyramid>();
	
	public List<Pyramid> readPyrmidsFromCSV(String filePath) {
		try{
			List<String> a = new ArrayList<String>();
			Scanner Sc = new Scanner(new File(filePath));
			int i = 0;
			while(Sc.hasNextLine()) {
				a.add(Sc.nextLine());
				if(i >= 1) {
					String[] row = a.get(i).split(",");
					if(!row[0].isEmpty() && !row[2].isEmpty() && !row[4].isEmpty() && !row[7].isEmpty()) {
						Pyrmids.add(new Pyramid(row[0], row[2], row[4], Double.parseDouble(row[7])));
					
					}
				}
				i++;
			}
			Sc.close();
			}
			
		catch(Exception e){
				System.out.println("An Error Occured.");
				System.out.println(e);
				e.printStackTrace();
		}
		return Pyrmids;
	}
	
	public HashMap<String, Double> getStatistics(List<Pyramid> p) {
		HashMap<String,Double> RetVal = new HashMap<>();
		List<Double> Heights = p.stream().map(Pyramid::getHeight).sorted().collect(toList());
		double median = Heights.size()%2 != 0 ? Heights.get(Heights.size()/2) : (Heights.get((Heights.size()/2)-1) + Heights.get(Heights.size()/2))/2;
		RetVal.put("Median",median);
		
		double average = (Heights.stream().collect(Collectors.summingDouble(i->i)))/Heights.size();
		RetVal.put("Average", average);
		
		List<Double> Q1 = new ArrayList<>(Heights.subList(0, Heights.size()/2));
		List<Double> Q2 = new ArrayList<>(Heights.subList(Heights.size()%2 == 0 ? Heights.size()/2 : (Heights.size()/2)+1, Heights.size()));
		
		double q1 = Q1.size()%2 != 0 ? Q1.get(Q1.size()/2) : (Q1.get((Q1.size()/2)-1) + Q1.get(Q1.size()/2))/2;
		double q2 = Q2.size()%2 != 0 ? Q2.get(Q2.size()/2) : (Q2.get((Q2.size()/2)-1) + Q2.get(Q2.size()/2))/2;
		RetVal.put("Q1", q1);
		RetVal.put("Q2", q2);
		
		RetVal.forEach((k, v)-> System.out.println("KEY = "+ k + "|   VALUE = "+v));
		return RetVal;
	}
}