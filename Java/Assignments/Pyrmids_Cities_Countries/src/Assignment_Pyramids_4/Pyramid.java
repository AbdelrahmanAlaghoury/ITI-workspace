package Assignment_Pyramids_4;

public class Pyramid {
	String pharaoh;
	String modern_name;
	String site;
	double height;
	
	public Pyramid(String pharaoh, String modern_name, String site, double height) {
		 this.pharaoh =  pharaoh;
		 this.modern_name =  modern_name;
		 this.site =  site;
		 this.height =  height;
	}
	public void setPharaoh(String pharaoh) {
		this.pharaoh =  pharaoh;
	}
	public void setModern_name(String modern_name) {
		this.modern_name =  modern_name;
	}
	public void setSite(String site) {
		this.site =  site;
	}
	public void setHeight(double height) {
		this.height =  height;
	}
	
	public String getPharaoh() {
		return this.pharaoh;
	}
	public String getModern_name() {
		return this.modern_name;
	}
	public String getSite() {
		return this.site;
	}
	public double getHeight() {
		return this.height;
	}
}