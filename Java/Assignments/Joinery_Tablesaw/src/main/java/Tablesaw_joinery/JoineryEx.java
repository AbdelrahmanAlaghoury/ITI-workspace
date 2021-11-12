package Tablesaw_joinery;

import java.io.IOException;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import joinery.DataFrame;
import cyclops.async.LazyReact;
import org.apache.commons.math3.stat.descriptive.SummaryStatistics;
import org.jooq.lambda.tuple.Tuple2;
public class JoineryEx {
	public static void main(String[] args) throws IOException {
		DataFrame<Object> df = DataFrame.readCsv("src\\main\\resources\\data\\randomDataset.csv");
		System.out.println(df.describe());
		System.out.println("=======================================================================================================================");
		
		List<Object> country = df.col("country");
		List<Object> salary = df.col("salary");
		//dest.forEach(c-> System.out.println(c));
		System.out.println("=======================================================================================================================");

		Map<String, Long> map = LazyReact.sequentialBuilder()
								.from(country)
								.cast(String.class)
								.distinct()
								.zipWithIndex()
								.toMap(Tuple2::v1, Tuple2::v2);
		List<Object> indexes = country.stream().map(map::get).sorted()
							   .collect(Collectors.toList());
		//map.forEach((k,v)->System.out.println(k + " -> " + v));
		System.out.println("=======================================================================================================================");
		country.forEach((v)->System.out.println(" -> " + map.get(v)));
		System.out.println("=======================================================================================================================");
		DataFrame<Object> df_2 = DataFrame.readCsv("src\\main\\resources\\data\\vgsales.csv")
								.retain("Year", "NA_Sales", "EU_Sales", "JP_Sales")
								.sortBy("Year")
								.groupBy(row->row.get(0))
								
								.mean();
		System.out.println(df_2.head(df_2.length()));						
		
		System.out.println("=======================================================================================================================");
		df_2.iterrows().forEachRemaining((row)->System.out.println(row));
		System.out.println("=======================================================================================================================");
		
		SummaryStatistics statistics = new SummaryStatistics();
		salary.forEach(s->statistics.addValue((double) s));
		System.out.println (statistics.getSummary());
	}
}