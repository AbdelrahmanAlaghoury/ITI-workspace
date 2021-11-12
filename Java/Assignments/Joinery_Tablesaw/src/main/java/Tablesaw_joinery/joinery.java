package Tablesaw_joinery;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;

import joinery.DataFrame;
import joinery.DataFrame.JoinType;

public class joinery {
	public static void main(String[] args) {
		eda_Joinery eda = new eda_Joinery();
		DataFrame titanic = eda.readCSV("src\\main\\resources\\data\\titanic.csv");
		DataFrame titanic_2 = eda.readCSV("src\\main\\resources\\data\\Titanic_2.csv");
		System.out.println("Titanic" + eda.getStatistics(titanic));
		System.out.println("Titanic_2" + eda.getStatistics(titanic_2));
		System.out.println("=======================================================================================================================");

		System.out.println("Titanic \n" + titanic.columns());
		System.out.println("Titanic_2 \n" + titanic_2.columns());
		System.out.println("=======================================================================================================================");
		
		List gender = (List) titanic.col("sex").stream().map(g->g.toString().equalsIgnoreCase("male")? 1:0).collect(Collectors.toList());
		titanic.add("gender", gender);
		titanic = titanic.drop("sex");
		gender = (List) titanic_2.col("Sex").stream().map(g->g.toString().equalsIgnoreCase("male")? 1:0).collect(Collectors.toList());
		titanic_2.add("gender", gender);
		titanic_2 = titanic_2.drop("Sex");
		System.out.println("titanic\n==========\n" + titanic + "\n" + "titanic_2\n==========\n" + titanic_2);
		System.out.println("=======================================================================================================================");
		
		DataFrame mergedData = titanic.join(titanic_2);
		System.out.println(mergedData.columns());
		System.out.println("=======================================================================================================================");
	}
}
