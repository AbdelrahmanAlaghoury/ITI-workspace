package com;

import com.WuzzufJobs.WuzzufJobsDAO;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.HashMap;
import java.util.Map;


@SpringBootApplication
@RestController
@RequestMapping
public class JavaFinalProjectApplication {
	static Map<String, String> dataStructure = new HashMap<String, String>();
	static String dataCount;
	static Map<String, Long> skills = new HashMap<String, Long>();
	public static void main(String[] args) {
		SpringApplication.run(JavaFinalProjectApplication.class, args);
		WuzzufJobsDAO dao = new WuzzufJobsDAO();
		dao.readFileToDataFrame("D:\\ITI_AI-Pro\\Java\\Final Java Project\\JavaFinalProject_2.3.12\\JavaFinalProject\\src\\main\\resources\\Wuzzuf_Jobs.csv");
		skills = dao.EDA();
		dataStructure = dao.structure();
		dataCount = dao.count();
	}
	@GetMapping
	public StringBuilder DataStructure(){
		StringBuilder builder = new StringBuilder();
		builder.append("<h3>Data structure : </h3>").append(dataStructure);
		builder.append("<h3>Count : </h3>").append(dataCount);
		return builder;
	}
	@GetMapping("/companies")
	public StringBuilder companies(){
		StringBuilder builder = new StringBuilder();
		builder.append("<h1>Companies Pie Chart</h1>");
		builder.append("<img src=").append("\"src/main/resources/public/images/Sample_ChartPie.png\"").append("width=\"1800\" height=\"800\"").append("/>");
		return builder;
	}
	@GetMapping("/jobs")
	public StringBuilder jobs(){
		StringBuilder builder = new StringBuilder();
		builder.append("<h1>Jobs Bar Chart</h1>");
		builder.append("<img src=").append("\"src/main/resources/public/images/Sample_ChartHistJobs.png\"").append("width=\"1800\" height=\"800\"").append("/>");
		return builder;
	}
	@GetMapping("/location")
	public StringBuilder location(){
		StringBuilder builder = new StringBuilder();
		builder.append("<h1>Location Bar Chart</h1>");
		builder.append("<img src=").append("\"src/main/resources/public/images/Sample_ChartHistLocations.png\"").append("width=\"1800\" height=\"800\"").append("/>");
		return builder;
	}
	@GetMapping("/skills")
	public StringBuilder skills() {
		StringBuilder builder = new StringBuilder();
		builder.append("<h1>Skills Bar Chart</h1>");
		builder.append("<img src=").append("\"src/main/resources/public/images/Sample_ChartHistSkills.png\"").append("width=\"1800\" height=\"800\"").append("/>");
		builder.append("<h3>Skills : </h3>").append(skills);
		return builder;
	}
}
