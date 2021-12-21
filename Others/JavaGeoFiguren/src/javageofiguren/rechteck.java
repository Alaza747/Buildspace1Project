package javageofiguren;

public class rechteck {

    //Eigenschaften
    int laenge;
    int breite;
    int umfang;
    int flaeche;
    
    //Methoden 
    
    public rechteck(int a, int b){
    this.laenge = a;
    this.breite = b;
    umfang = (a + b) * 2;
    flaeche = a * b;
    }
    
    public void sayall(){
        System.out.println("Länge : "+ laenge + " Breite : " + breite + " Umfang : " +umfang + " Flaeche :" + flaeche + ".");
    }
    
    
}
