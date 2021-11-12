package Tablesaw_joinery;

import java.io.IOException;

import joinery.DataFrame;

public class eda_Joinery {
	
	public DataFrame readCSV(String path) {
		DataFrame data = new DataFrame<>();
		try {
			data = DataFrame.readCsv(path);
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return data;
	}

	public DataFrame getStatistics(DataFrame data) {
		return data.describe();
	}
}
