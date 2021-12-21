package javageofiguren;

public class allgemeinesdreieck {
    
    //Eigenschaften
    int seite1;
    int seite2;
    int seite3;
    double umfang;
    double flaeche;
    
    //Methoden
    public allgemeinesdreieck(int a, int b, int c){
        this.seite1 = a;
        this.seite2 = b;
        this.seite3 = c;
        umfang = a + b + c;
        flaeche = Math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(c+a-b))/4;
    }
    
    public void sayall(){
        System.out.println("Seite 1 : "+seite1+" Seite 2 : "+seite2+" Seite 3 : "+seite3+" Umfang : "+umfang+" Fläche : "+flaeche+".");
    }
    
}
