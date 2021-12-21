package javageofiguren;

public class kugel {

    //Eigenscaften
    int radius;
    int umfang;
    int durchmesser;
    double volumen;
    String name;
    
    //Methoden
    
    public kugel(int a){
        this.radius = a;
        durchmesser = a * 2;
        umfang = (int) (2 * Math.PI * a);
        volumen = (4.0 / 3) * Math.PI * Math.pow(a, 3);
    }
    
    public void sayall(){
        System.out.println("Radius : " + radius + " Durchmesser : " + durchmesser + " Umfang : " + umfang + " Volumen : " + volumen + ".");
    }
    
}
