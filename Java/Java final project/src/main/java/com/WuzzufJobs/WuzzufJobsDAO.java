package com.WuzzufJobs;

import org.apache.commons.csv.CSVFormat;
import org.knowm.xchart.*;
import org.knowm.xchart.style.Styler;
import smile.data.DataFrame;
import smile.io.Read;

import java.awt.*;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.net.URISyntaxException;
import java.util.*;
import java.util.List;
import java.util.function.Function;
import java.util.stream.Collectors;

/*******************************************************************************************************************/
public class WuzzufJobsDAO {
    private List<WuzzufJob> jobsData = new ArrayList<WuzzufJob>();
    private DataFrame jobsDataFrame = null;
    /*******************************************************************************************************************/
    //Read the data from a CSV file and create object for each row of the data then returns a list of objects
    public List<WuzzufJob> getObjectsList(String filePath) {
        BufferedReader br = null;
        try {
            br = new BufferedReader(new FileReader(filePath));
            Iterator<String> lineIterator = br.lines().iterator();
            //To skip the headers of the csv file
            lineIterator.next();
            while (lineIterator.hasNext()) {
                String line = lineIterator.next();
                String[] splitedData = line.split(",(?=(?:[^\"]*\"[^\"]*\")*[^\"]*$)");

                if (!splitedData[0].isBlank() && !splitedData[1].isBlank() && !splitedData[2].isBlank() && !splitedData[3].isBlank() &&
                        !splitedData[4].isBlank() && !splitedData[5].isBlank() && !splitedData[6].isBlank() && !splitedData[7].isBlank()) {
                    jobsData.add(new WuzzufJob(splitedData[0].strip(), splitedData[1].strip(), splitedData[2].strip(),
                            splitedData[3].strip(), splitedData[4].strip(), splitedData[5].strip(), splitedData[6].strip(), splitedData[7].strip()));
                }
            }
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        return jobsData;
    }
    /*******************************************************************************************************************/
    public void readFileToDataFrame(String filePath){
        CSVFormat format = CSVFormat.DEFAULT.withFirstRecordAsHeader ();
        try {
            jobsDataFrame = Read.csv (filePath, format);
        } catch (IOException | URISyntaxException e) {
            e.printStackTrace();
        }
    }

    /*******************************************************************************************************************/
    //Remove Null values and duplicates then Returns Data structure as JSON String
    public void DataCleaning(){
        // Remove Null values
        jobsDataFrame = jobsDataFrame.omitNullRows();

        // Remove rows with null word in years of experience
        jobsDataFrame = DataFrame.of(jobsDataFrame.stream().filter(r-> r.toString().indexOf("null")==-1));

        // Remove duplicates
        jobsDataFrame = DataFrame.of(jobsDataFrame.stream().distinct());

    }
    /*******************************************************************************************************************/
    public Map<String, String> structure(){
        // Get the Data Structure
        DataFrame structure = jobsDataFrame.structure();
        Map<String, String> structureMap= new HashMap<String, String>();
        String[] col = structure.column("Column").toStringArray();
        String[] type = structure.column("Type").toStringArray();
        for(int i = 0; i < col.length;i++){
            structureMap.put(col[i], type[i]);
        }

        return structureMap;
    }
    /*******************************************************************************************************************/
    public String count(){
        return String.valueOf(jobsDataFrame.stream().count());
    }
    /*******************************************************************************************************************/
    // Count each Company jobs and visualize using pie chart
    public void CompaniesEDA(){
        // Get a map
        Map<String, Long> companies = Arrays.stream(jobsDataFrame.column("Company").toStringArray())
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Sort a map and add to finalMap
        Map<String, Long> companiesSorted = new LinkedHashMap<String, Long>();
        companies.entrySet().stream()
                .sorted(Map.Entry.<String, Long>comparingByValue()
                        .reversed()).forEachOrdered(e -> companiesSorted.put(e.getKey(), e.getValue()));

        //  Take top 10 companies in jobs count and other companies sum
        List<String> top10Companies = new ArrayList<String>();
        List<Long> top10CompaniesCount = new ArrayList<Long>();

        int i = 0;
        long otherCompaniesSum = 0;
        Iterator keys= companiesSorted.keySet().iterator();
        while(keys.hasNext()){
            String key = keys.next().toString();
            if(i > 10) {
                otherCompaniesSum += companiesSorted.get(key);
            }
            else{
                top10Companies.add(key);
                top10CompaniesCount.add(companiesSorted.get(key));
            }
            i++;
        }
        top10Companies.add("Other companies");
        top10CompaniesCount.add(otherCompaniesSum);

        // Create Chart
        PieChart chart = new PieChartBuilder().width(800).height(600).build();

        // Customize Chart
        Color[] sliceColors = new Color[] { new Color(224, 68, 14), new Color(230, 105, 62),
                new Color(236, 143, 110), new Color(243, 180, 159)};

        chart.getStyler().setSeriesColors(sliceColors);

//      // Series
        for (int j=0; j < top10Companies.size();j++){
            chart.addSeries(top10Companies.get(j), top10CompaniesCount.get(j));
        }

        //save the Chart
        try {
            BitmapEncoder.saveBitmap(chart, "src\\main\\resources\\public\\images\\Sample_ChartPie", BitmapEncoder.BitmapFormat.PNG);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    /*******************************************************************************************************************/
    // Count each job title and visualize using bar chart
    public void JobTitlesEDA(){
        // Get a map
        Map<String, Long> jobTitles = Arrays.stream(jobsDataFrame.column("Title").toStringArray())
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Sort a map and add to finalMap
        Map<String, Long> jobTitlesSorted = new LinkedHashMap<String, Long>();
        jobTitles.entrySet().stream()
                .sorted(Map.Entry.<String, Long>comparingByValue()
                        .reversed()).forEachOrdered(e -> jobTitlesSorted.put(e.getKey(), e.getValue()));

        //  Take top 10 jobTitles in count
        List<String> top10jobTitles = new ArrayList<String>();
        List<Long> top10jobTitlesCount = new ArrayList<Long>();
        int i = 0;
        Iterator keys= jobTitlesSorted.keySet().iterator();
        while(i < 10 & keys.hasNext()){
            String key = keys.next().toString();
            top10jobTitles.add(key);
            top10jobTitlesCount.add(jobTitlesSorted.get(key));
            i++;
        }

        // Create Chart
        CategoryChart chartHistJobs = new CategoryChartBuilder().width(800).height(600).title("most popular job titles").xAxisTitle("Jobs").yAxisTitle("Count").build();

        // Customize Chart
        chartHistJobs.getStyler().setLegendPosition(Styler.LegendPosition.InsideNW);
        chartHistJobs.getStyler().setHasAnnotations(true);

        // Series
        chartHistJobs.addSeries("Jobs count", top10jobTitles, top10jobTitlesCount);

        // Save the chart
        try {
            BitmapEncoder.saveBitmap(chartHistJobs, "src//main//resources//public//images//Sample_ChartHistJobs", BitmapEncoder.BitmapFormat.PNG);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    /*******************************************************************************************************************/
    // Count each job location and visualize using bar chart
    public void JobLocationsEDA(){
        // Get a map
        Map<String, Long> jobLocations = Arrays.stream(jobsDataFrame.column("Location").toStringArray())
                .collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Sort a map and add to finalMap
        Map<String, Long> jobLocationsSorted = new LinkedHashMap<String, Long>();
        jobLocations.entrySet().stream()
                .sorted(Map.Entry.<String, Long>comparingByValue()
                        .reversed()).forEachOrdered(e -> jobLocationsSorted.put(e.getKey(), e.getValue()));

        //  Take top 10 jobTitles in count
        List<String> top10jobLocations = new ArrayList<String>();
        List<Long> top10jobLocationsCount = new ArrayList<Long>();
        int i = 0;
        Iterator keys= jobLocationsSorted.keySet().iterator();
        while(i < 10 & keys.hasNext()){
            String key = keys.next().toString();
            top10jobLocations.add(key);
            top10jobLocationsCount.add(jobLocationsSorted.get(key));
            i++;
        }

        // Create Chart
        CategoryChart chartHistLocation = new CategoryChartBuilder().width(800).height(600).title("most popular areas").xAxisTitle("Location").yAxisTitle("Count").build();

        // Customize Chart
        chartHistLocation.getStyler().setLegendPosition(Styler.LegendPosition.InsideNW);
        chartHistLocation.getStyler().setHasAnnotations(true);

        // Series
        chartHistLocation.addSeries("Locations count", top10jobLocations, top10jobLocationsCount);

        // Save the chart
        try {
            BitmapEncoder.saveBitmap(chartHistLocation, "src//main//resources//public//images//Sample_ChartHistLocations", BitmapEncoder.BitmapFormat.PNG);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    /*******************************************************************************************************************/
    // Count each Skill and visualize using bar chart
    public Map<String, Long> SkillsEDA(){
        // Split each skill from skills column
        List<String> skillsList = new ArrayList<>();
        Arrays.stream(jobsDataFrame.column("Skills").toStringArray()).forEach(row->{
            String[] Skills = row.split(",");
            for(String skill : Skills){
                skillsList.add(skill.strip());
            }
        });
        // Get a map
        Map<String, Long> skills = skillsList.stream().collect(Collectors.groupingBy(Function.identity(), Collectors.counting()));

        // Sort a map and add to finalMap
        Map<String, Long> skillsSorted = new LinkedHashMap<String, Long>();
        skills.entrySet().stream()
                .sorted(Map.Entry.<String, Long>comparingByValue()
                        .reversed()).forEachOrdered(e -> skillsSorted.put(e.getKey(), e.getValue()));

        //  Take top 10 jobTitles in count
        List<String> top10Skills = new ArrayList<String>();
        List<Long> top10SkillsCount = new ArrayList<Long>();
        int i = 0;
        Iterator keys= skillsSorted.keySet().iterator();
        while(i < 10 & keys.hasNext()) {
            String key = keys.next().toString();
            top10Skills.add(key);
            top10SkillsCount.add(skillsSorted.get(key));
            i++;
        }

        // Create chart
        CategoryChart chartHistSkills = new CategoryChartBuilder().width(800).height(600).title("most popular Skills").xAxisTitle("Skills").yAxisTitle("Count").build();

        // Customize Chart
        chartHistSkills.getStyler().setLegendPosition(Styler.LegendPosition.InsideNW);
        chartHistSkills.getStyler().setHasAnnotations(true);

        // Series
        chartHistSkills.addSeries("Skills count", top10Skills, top10SkillsCount);

        // Save the chart
        try {
            BitmapEncoder.saveBitmap(chartHistSkills, "src//main//resources//public//images//Sample_ChartHistSkills", BitmapEncoder.BitmapFormat.PNG);
        } catch (IOException e) {
            e.printStackTrace();
        }
        skillsSorted.forEach((k,v)->System.out.println(k + " | "+v));
        return skillsSorted;
    }
    /*******************************************************************************************************************/
    public Map<String, Long> EDA (){
        DataCleaning();
        CompaniesEDA();
        JobTitlesEDA();
        JobLocationsEDA();
        return SkillsEDA();
    }
    /*******************************************************************************************************************/
}
