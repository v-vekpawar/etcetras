public class PracticeAbstractInterface {
    public static void main(String[] args) {
        //1. 
        AreaPerimeterCircle circle = new AreaPerimeterCircle(23);
        System.out.println(circle.area());
        System.out.println(circle.perimeter());
        AreaPerimeterRectangle rectangle = new AreaPerimeterRectangle(43,21);
        System.out.println(rectangle.area());
        System.out.println(rectangle.perimeter());
        AreaPerimeterTriangle triangle = new AreaPerimeterTriangle(21,12);
        System.out.println(triangle.area());
        System.out.println(triangle.perimeter(4,7,13));
        //2.
        AudioPlayerSystem audio = new AudioPlayerSystem();
        audio.play();
        audio.pause();
        audio.stop();
        VideoPlayerSystem video = new VideoPlayerSystem();
        video.play();
        video.pause();
        video.stop();
        //3.
        PDFDocument pdf = new PDFDocument("PDFDocument.pdf");
        pdf.compressDocument();
        pdf.printDocument();
        pdf.scanDocument();
        WORDDocument word = new WORDDocument("WORDDocument.txt");
        word.printDocument();
        word.convertType("text");
        SpreadSheetDocument spd = new SpreadSheetDocument("SpreadSheet.xlsx");
        spd.editDocument();
        spd.reduceSize(100);
    }
}

//1. abstract shape hierarchy
abstract class AreaPerimeter{
    abstract float area();
    abstract float perimeter();
}
class AreaPerimeterCircle extends AreaPerimeter{
    float radius;
    //constructor
    AreaPerimeterCircle(float rad){
        this.radius=rad;
    }

    @Override
    float area(){
        return ((float) Math.PI*this.radius*this.radius);
    }
    @Override
    float perimeter(){
        return (2*(float) Math.PI*this.radius);
    }
}
class AreaPerimeterRectangle extends AreaPerimeter{
    float length;
    float breadth;
    //constructor
    AreaPerimeterRectangle(float l,float b){
        this.length=l;
        this.breadth=b;
    }

    @Override
    float area(){
        return (this.length*this.breadth);
    }
    @Override
    float perimeter(){
        return (2*(this.length+this.breadth));
    }
}
class AreaPerimeterTriangle extends AreaPerimeter{
    float base;
    float height;
    //constructor
    AreaPerimeterTriangle(float b,float h){
        this.base=b;
        this.height=h;
    }

    @Override
    float area(){
        return ((1/2)*this.base*this.height);
    }
    @Override
    float perimeter(){
        return 0;
    }
    //overloaded method perimeter
    float perimeter(float a, float b, float c){
        return (a+b+c);
    }
}

//2. interface player system
interface PlayerSystem{
    void play();
    void pause();
    void stop();
}
class AudioPlayerSystem implements PlayerSystem{
    public void play(){
        System.out.println("playing audio.....");
    }
    public void pause(){
        System.out.println("paused audio......");
    }
    public void stop(){
        System.out.println("...stopped audio player system...");
    }
}
class VideoPlayerSystem implements PlayerSystem{
    public void play(){
        System.out.println("playing video.....");
    }
    public void pause(){
        System.out.println("paused video......");
    }
    public void stop(){
        System.out.println("...stopped video player system...");
    }
}

//3. complex system applying abstract class and interfaces
abstract class Document{
    abstract void reduceSize(int tosize);
    abstract void convertType(String type);
    abstract void compressDocument();
}
interface Printable{
    void printDocument();
}
interface Scanable{
    void scanDocument();
}
interface Editable{
    void editDocument();
}
class PDFDocument extends Document implements Printable,Scanable,Editable {
    String doc;
    PDFDocument(String document){
        this.doc=document;
    }
    void reduceSize(int size){
        System.out.println("reduce document size to "+size+" kb");
    }
    void convertType(String type){
        int index = doc.indexOf('.');
        String otype= doc.substring(index+1);
        System.out.println("converted type of document from "+otype+" to "+type);
        this.doc=this.doc.replace(otype,type);
    }
    void compressDocument(){
        int index = doc.indexOf('.');
        String otype= doc.substring(index+1);
        System.out.println("compressed document to zip file");
        this.doc=this.doc.replace(otype,"zip");
    }
    public void printDocument(){
        System.out.println(this.doc);
    }
    public void scanDocument(){
        System.out.println("scanning "+ this.doc);
    }
    public void editDocument(){
        System.out.println("editing "+ this.doc);
    }
}
class SpreadSheetDocument extends Document implements Printable,Scanable,Editable {
    String doc;
    SpreadSheetDocument(String document){
        this.doc=document;
    }
    void reduceSize(int size){
        System.out.println("reduce document size to "+size+" kb");
    }
    void convertType(String type){
        int index = doc.indexOf('.');
        String otype= doc.substring(index+1);
        System.out.println("converted type of document from "+otype+" to "+type);
        this.doc=this.doc.replace(otype,type);
    }
    void compressDocument(){
        int index = doc.indexOf('.');
        String otype= doc.substring(index+1);
        System.out.println("compressed document to zip file");
        this.doc=this.doc.replace(otype,"zip");
    }
    public void printDocument(){
        System.out.println(this.doc);
    }
    public void scanDocument(){
        System.out.println("scanning "+ this.doc);
    }
    public void editDocument(){
        System.out.println("editing "+ this.doc);
    }
}
class WORDDocument extends Document implements Printable,Scanable,Editable {
    String doc;
    WORDDocument(String document){
        this.doc=document;
    }
    void reduceSize(int size){
        System.out.println("reduce document size to "+size+" kb");
    }
    void convertType(String type){
        int index = doc.indexOf('.');
        String otype= doc.substring(index+1);
        System.out.println("converted type of document from "+otype+" to "+type);
        this.doc=this.doc.replace(otype,type);
    }
    void compressDocument(){
        int index = doc.indexOf('.');
        String otype= doc.substring(index+1);
        System.out.println("compressed document to zip file");
        this.doc=this.doc.replace(otype,"zip");
    }
    public void printDocument(){
        System.out.println(this.doc);
    }
    public void scanDocument(){
        System.out.println("scanning "+ this.doc);
    }
    public void editDocument(){
        System.out.println("editing "+ this.doc);
    }
}