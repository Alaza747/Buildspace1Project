package javageofiguren;

public class JavaGeoFiguren {

    public static void main(String[] args) {
        kugel Kugel = new kugel(3);
        Kugel.sayall();
        rechteck bla = new rechteck(4, 6);
        bla.sayall();
        allgemeinesdreieck blbl = new allgemeinesdreieck(3,4,5);
        blbl.sayall();
    }
    
}
