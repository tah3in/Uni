from math import cos,sin,radians

def main():
    Parameters = list(map(int,input("Enter Gama , Beta , Alfa Parameters : ").split(' ')))
    Gama , Beta , Alfa = radians(Parameters[0]) , radians(Parameters[1]) , radians(Parameters[2])
    RotationMatrix = [[],[],[]]

    RotationMatrix[0]= [    cos(Alfa)*cos(Beta)   ,   cos((Alfa)*sin(Beta)-sin(Alfa)*cos(Gama))            ,   cos(Alfa)*sin(Beta)*cos(Gama)+sin(Alfa)*sin(Beta)  ]
    RotationMatrix[1]= [    sin(Alfa)*cos(Beta)   ,   sin((Alfa)*sin(Beta)*sin(Gama)+cos(Gama)*cos(Alfa))  ,   sin(Alfa)*sin(Beta)*cos(Gama)-cos(Alfa)*sin(Gama)  ]
    RotationMatrix[2]= [    -sin(Beta)            ,   cos(Beta)*sin(Gama)                                  ,   cos(Beta)*cos(Gama) ]
    print(f"\nRotationMatrix :\n\n {RotationMatrix[0]} \n {RotationMatrix[1]} \n {RotationMatrix[2]} \n\n")

    P = list(map(int,input("Enter Px , Py , Pz Parameters : ").split(' ')))
    Px , Py , Pz = P[0] , P[1] , P[2]

    for i in range(3):
        RotationMatrix[i].append(P[i])

    RotationMatrix.append([0,0,0,1])

    print(f"\nTransformation matrix_B_to_A :\n\n {RotationMatrix[0]} \n {RotationMatrix[1]} \n {RotationMatrix[2]} \n {RotationMatrix[3]}\n\n")

if __name__ == "__main__":
    main()