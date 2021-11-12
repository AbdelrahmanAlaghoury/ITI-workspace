package Assignment_Pyramids_4;
import java.util.List;

public class EntryPoint{
	public static void main(String[] args){
		/***************************************************************************************************************************/
		//Pyramids Exercise
		/***************************************************************************************************************************/
		PyramidCSDAO PDAO = new PyramidCSDAO();
		
		//I read only the valid and full row's data so the pyramids list doesn't have any null values
		List<Pyramid> pyramids = PDAO.readPyrmidsFromCSV("pyramids.csv");
		
		pyramids.forEach((p)->System.out.println(p.getPharaoh()));
		
		/***************************************************************************************************************************/
		//Exercise 4
		/***************************************************************************************************************************/
		PDAO.getStatistics(pyramids);
	}
}