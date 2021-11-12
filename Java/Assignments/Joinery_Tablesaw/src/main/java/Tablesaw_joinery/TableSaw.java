package Tablesaw_joinery;
import java.io.IOException;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

import tech.tablesaw.api.DateColumn;
import tech.tablesaw.api.DoubleColumn;
import tech.tablesaw.api.NumberColumn;
import tech.tablesaw.api.StringColumn;
import tech.tablesaw.api.Table;
import tech.tablesaw.joining.DataFrameJoiner;

public class TableSaw {
	public static void main(String[] args) throws IOException{
		Table table = Table.read().csv("src\\main\\resources\\data\\titanic.csv");
		Table table_2 = Table.read().csv("src\\main\\resources\\data\\Titanic_2.csv");
		System.out.println("====================================================================================================================================================================================");
		
		Table dataStructure = table.structure();
		Table dataStructure_2 = table_2.structure();
		System.out.println(dataStructure);
		System.out.println(dataStructure_2);
		System.out.println("====================================================================================================================================================================================");
		
		Table summary = table.summary();
		Table summary_2 = table_2.summary();
		System.out.println(summary);
		System.out.println(summary_2);
		System.out.println("====================================================================================================================================================================================");
		
		int rowCount = table.rowCount();
		List<LocalDate> dateList = new ArrayList<>();
		for(int i=0; i<rowCount; i++) {
			dateList.add(LocalDate.of(2021, 3, i%31==0?1:i%31));
		}
		DateColumn dateColumn = DateColumn.create("Fake Date",dateList);
		Table editedData = table.insertColumn(table.columnCount(), dateColumn);
		System.out.println(editedData);
		System.out.println("====================================================================================================================================================================================");
		
		NumberColumn mappedGenderColumn = null;
		StringColumn gender = (StringColumn)table.column("sex");
		List<Number> mappedGenderValue = new ArrayList<>();
		for(String value : gender) {
			if((value != null) && (value.equalsIgnoreCase("female"))) {
				mappedGenderValue.add(new Double(1));
			}
			else {
				mappedGenderValue.add(new Double(0));		
			}
		}
		mappedGenderColumn = DoubleColumn.create("Gender", mappedGenderValue);
		Table editedGenderData = table.addColumns(mappedGenderColumn);
		editedGenderData = (Table) editedGenderData.removeColumns("Sex");
		System.out.println(editedGenderData);
		System.out.println("====================================================================================================================================================================================");
		Table newMergedData = table.addColumns(table_2.column("PassengerId"));
		System.out.println(newMergedData);
		
		System.out.println("====================================================================================================================================================================================");
		DataFrameJoiner dfj = new DataFrameJoiner(table,"name");
		System.out.println(dfj.inner(true, table_2));
		
	}
}
