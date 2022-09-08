"""
Escribir un programa que lea un entero positivo, n , introducido por el usuario 
y después muestre en pantalla la suma de todos los enteros desde 1 hasta n.
 La suma de los  primeros enteros positivos puede ser calculada de la siguiente forma:

 suma= n(n+1)/2

"""
suma=0
n=int(input("Introduce un numero entero positivo: "))
suma= n*(n+1)/2
print(suma)

"""
 public static void main(String [] args){
        Scanner sc = new Scanner(System.in);
        int n = 0;
        long s = 0;
        do{
            n = sc.nextInt();
            s = n*(n+1)/2;
           
            for(int i=1; i<n;i++){
                s = s - sc.nextInt();
            }
         
            int i = 1;
            while(i<n){
              s = s - sc.nextInt();
              i++;
            }
            
            System.out.println(s);
        }while(sc.hasNext());
    }

"""