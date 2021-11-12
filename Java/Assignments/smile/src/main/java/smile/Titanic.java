package smile;

import java.lang.reflect.InvocationTargetException;
import java.util.Arrays;
import java.util.Collection;
import java.util.Map;
import java.util.stream.Collectors;

import smile.classification.RandomForest;
import smile.data.*;
import smile.data.measure.NominalScale;
import smile.data.vector.IntVector;
import smile.plot.swing.Histogram;
import smile.validation.metric.Accuracy;
import smile.data.formula.Formula;

public class Titanic {
	public static void main(String[] args) throws InvocationTargetException, InterruptedException{
		PassengerProvider passengerProvider = new PassengerProvider();
		DataFrame testData = passengerProvider.ReadCSV("src/main/resources/data/titanic_test.csv");
		DataFrame trainData = passengerProvider.ReadCSV("src/main/resources/data/titanic_train.csv");
		System.out.println(testData.structure());
		System.out.println(trainData.structure());
		//System.out.println(testData.summary());
		//System.out.println(testData.structure());
		//System.in.read();
		
		System.out.println ("=======Encoding Non Numeric Data==============");
		testData = testData.merge(IntVector.of("SexValue",encodeCategory(testData, "Sex")));
		trainData = trainData.merge(IntVector.of("SexValue",encodeCategory(trainData, "Sex")));
		//System.out.println(testData.structure());
		//System.out.println(testData);
		//System.in.read();
		
		System.out.println ("=======Dropping the Name and Sex Column==============");
		testData = testData.drop("Name","Sex");
		trainData = trainData.drop("Name","Sex");
		//System.out.println(testData.structure());
		//System.out.println(testData.summary());
		//System.out.println(testData);
		//System.in.read();
		
		System.out.println ("=======After Omitting null Rows==============");
		testData= testData.omitNullRows();
		trainData= trainData.omitNullRows();
		
		System.out.println("TestData" +testData.structure());
		System.out.println("TestData" +testData.summary());

		System.out.println("TrainData" + trainData.structure());
		System.out.println("TrainData" +trainData.summary());
		
		EDA(trainData);
		
		System.out.println("==========Fitting A model===========");
		
		RandomForest model = RandomForest.fit(Formula.lhs("Survived"), trainData);
        //System.out.println("feature importance:");
        //System.out.println(Arrays.toString(model.importance()));
        //System.out.println(model.metrics ());
		
		System.out.println("==========Evaluating the model===========");

		int[] act = testData.intVector("Survived").toIntArray();
		
		int[] pred = model.predict(testData);
		System.out.println(Accuracy.of(act, pred));

	}
	
    public static int[] encodeCategory(DataFrame df, String columnName) {
        String[] values = df.stringVector(columnName).distinct().toArray(new String[] {});
        int[] retValues = df.stringVector(columnName).factorize(new NominalScale(values)).toIntArray();
        return retValues;
    }
    public static void EDA (DataFrame titanic) throws InvocationTargetException, InterruptedException {
    	System.out.println(titanic.summary());
    	DataFrame titanicSurvived = DataFrame.of(titanic.stream().filter(t -> t.get("Survived").equals(1)));
    	DataFrame titanicNotSurvived = DataFrame.of(titanic.stream().filter(t -> t.get("Survived").equals(0)));
    	titanicSurvived = titanicSurvived.omitNullRows();
    	titanicNotSurvived = titanicNotSurvived.omitNullRows();
    	System.out.println(titanicSurvived.summary());
    	
    	int survivedSize = titanicSurvived.size();
    	int notSurvivedSize = titanicNotSurvived.size();
    	System.out.println(survivedSize);
    	System.out.println(notSurvivedSize);
    	
    	double survivedAverageAge = titanicSurvived.stream().mapToDouble(t -> t.isNullAt("Age") ? 0.0 : t.getDouble("Age"))
    			.average()
    			.orElse(0);
    	double notSurvivedAverageAge = titanicNotSurvived.stream().mapToDouble(t -> t.isNullAt("Age") ? 0.0 : t.getDouble("Age"))
    			.average()
    			.orElse(0);
    	
        Map<Integer, Long> map = titanicSurvived.stream ()
                .collect (Collectors.groupingBy (t -> Double.valueOf (t.getDouble ("Age")).intValue (), Collectors.counting ()));
    	//map.forEach((k,v)-> System.out.println(k + "->>>>>" + v));
    	
        double[] breaks = ((Collection<Integer>) map.keySet())
        		.stream()
        		.mapToDouble(v -> Double.valueOf(v))
        		.toArray();
        int[] values = ((Collection<Long>) map.values())
        		.stream()
        		.mapToInt(v -> v.intValue())
        		.toArray();
        
//        Histogram.of (titanicSurvived.doubleVector ("Age").toDoubleArray (), 15, false)
//        	.canvas ().setAxisLabels ("Age", "Count")
//        	.setTitle ("Age frequencies among surviving passengers")
//        	.window ();    
//        
//        Histogram.of(values, map.size(), false).canvas().window();
        System.out.println (titanicSurvived.schema ());
    }
    //public static void eda()
}
