#Given Input = 29 59 14 11 3 13 15 18 12 16 6 17 7 47 61 5 21 2 41 9 10 8 19 1 4
# =============================================================================
# Importing required libraries
# =============================================================================
import math

class Airplane_seating_arrangement:
    
    def __init__(self):
# =============================================================================
#         This function will act as a constructor to get the input from the 
#         user for the respective class.
# =============================================================================
        self.n=int(input("Number of Matrices : "))
        self.dim=[]         #Stores number of rows and columns 
        self.temp=()        #Stores rows and column of ith matrix  
        self.Seat=[]        #Stores final allocated seat
        self.Prime=[]       #Stores the Prime number of the given input passenger's id
        self.Power=[]       #Stores the multiple of 2 number of the given input passenger's id
        self.Other=[]       #Stores the Other numbers of the given input passenger's id
        self.Window_seat=[] #Storing corresponding window seat as tuple
        self.Aisle_seat=[]  #Storing corresponding Aisle seat as tuple
        self.Middle_seat=[] #Storing corresponding Middle seat as tuple
        self.count = 0
        print("Passenger's id : ",end=" ")
        self.passenger=list(map(int,input().split(' ')))
        for i in range(self.n):
          print("Number of rows in ",i+1," matrix : ",end=" ")
          row=int(input())
          if row <= 0:
              print("Row cannot be zero or negative, kindly give positive values")
              exit(0)
          print("Number of columns in ",i+1," matrix : ",end=" ")
          col=int(input())
          if col <= 0 :
              print("Column cannot be zero or negative, kindly give positive values")
              exit(0)
          self.temp=(row,col)
          self.count =self.count + (row * col)
          self.dim.append(self.temp)
          self.temp=()
    
    def findPrime(self, num):
# =============================================================================
#         This function will help to find out the prime numbers from the given 
#         input.
# =============================================================================
        if (num==1):
              return False
        elif (num==2):
              return True
        else:
          for x in range(2,num):
            if(num % x==0):
              return False
          return True  
            
    def multiple_of_2_power_n(self, n):
# =============================================================================
#         This function will help to find out the multiple of 2 power n from
#         the given input
# =============================================================================
        Log=math.log(n,2)#n=65
        #6.02..
        AbsoltueValue=int(Log)
        #6=6.02
        Sol = True if Log==AbsoltueValue else False
                     #6.022==6.0 returns false
        return Sol
    
    def Seat_init(self):
# =============================================================================
#         This function will create a list of seats for the given 2D matrix.
# =============================================================================
        for i in range(self.n):
          mat=[] 
          Row=self.dim[i][0]
          Col=self.dim[i][1]
          #2D matrix which is the given matrix by user [(2,3),(3,4),(3,2),(4,3)]
          for j in range(Row):
            rows=['XX']*Col   #Allocating every seat as 'XX'
            mat.append(rows)
          self.Seat.append(mat)
    
    def PPO_spliter(self):
# =============================================================================
#         This function will split the given passenger’s id according to the 
#         given constraint.
# =============================================================================
        for i in self.passenger:
            if(self.findPrime(i)):
              self.Prime.append(i)
            elif(self.multiple_of_2_power_n(i)):
              self.Power.append(i)
            else:
              self.Other.append(i)
    
    def Seat_finder(self):
# =============================================================================
#         This function will create the list of seat as Window, Middle and Aisle.
# =============================================================================
        for i in range(self.n):
          if(i==0):
            Row=self.dim[i][0]
            Col=self.dim[i][1]
            for j in range(Row):
              for k in range(Col): 
                if(k==0):
                  self.temp=(i,j,k) #temp(matrix, row, column)
                  self.Window_seat.append(self.temp)
                elif(k==Col-1):
                  self.temp=(i,j,k)
                  self.Aisle_seat.append(self.temp)
                else :
                  self.temp=(i,j,k)
                  self.Middle_seat.append(self.temp)
          elif(i==self.n-1):
            Row=self.dim[i][0]
            Col=self.dim[i][1]
            for j in range(Row):
              for k in range(Col): 
                if(k==0):
                  self.temp=(i,j,k)
                  self.Aisle_seat.append(self.temp)
                elif(k==Col-1):
                  self.temp=(i,j,k)
                  self.Window_seat.append(self.temp)
                else :
                  self.temp=(i,j,k)
                  self.Middle_seat.append(self.temp)
          else :
            Row=self.dim[i][0]
            Col=self.dim[i][1]
            for j in range(Row):
              for k in range(Col):
                if(k==0 or k==Col-1):
                  self.temp=(i,j,k)
                  self.Aisle_seat.append(self.temp)
                else:
                  self.temp=(i,j,k)
                  self.Middle_seat.append(self.temp)
                  

    def Passengers_Rule(self, condition): #conditions are prime, multiple of 2 and remaining passenger id's
# =============================================================================
#         This function will take the prime passangers as a first priority for allocation.
# =============================================================================
        while(len(condition)!=0):
            if(len(self.Aisle_seat)!=0):
              
              passenger_id = condition[0]
              self.temp=self.Aisle_seat[0]
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
                       # matrix          row          column
              condition.remove(passenger_id)
              self.Aisle_seat.remove(self.temp)
    
            elif(len(self.Window_seat)!=0):
              passenger_id = condition[0]
              self.temp = self.Window_seat[0]
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              condition.remove(passenger_id)
              self.Window_seat.remove(self.temp)  
    
            else :
              
              passenger_id = condition[0]
              self.temp = self.Middle_seat[0]
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              condition.remove(passenger_id)
              self.Middle_seat.remove(self.temp)
              
    def output_format(self):
# =============================================================================
#         This Function displays Whether the seat is Window, Aisle, Middle
#         Window as 'WW'
#         Aisle as 'AA'
#         Middle as 'MM'
# =============================================================================
        Length = len(self.dim) #Length of the matrix 

        Final = [] # Example = [['WW' 'MM' 'AA']]
        
        for loc in range(Length):
            if loc == 0 or loc == (Length -1): # First and Last matrix
                Input = self.dim[loc][1] 
                LC = []
                for x in range(Input): # x is column
                    if (x == 0 and loc == 0) or (x == Input - 1 and loc == Length -1):
                        LC.append('WW')
                    elif (loc == 0 and x == Input -1) or (loc == Length -1 and x == 0):
                        LC.append('AA')
                    else:
                        LC.append('MM')
                Final.append(LC)        
            else:
                Input = self.dim[loc][1]
                LC = ["AA" if (x == 0 or x == Input - 1) else 'MM' for x in range(Input)]
                Final.append(LC) 
                
        return Final      
    
    def Final_seat_arrangement_vis(self):
# =============================================================================
#         This function will visualize the output of list of the seats.
# =============================================================================
        
        Final = self.output_format()
        for i in range(self.n):
          Row=self.dim[i][0]
          print(Final[i])
          for j in range(Row):
            print(list(map(str,(self.Seat[i][j]))))
          print(' ')

    def Input_Check(self):
      if self.count < len(self.passenger):
        print("The Passenger Id is more than the seat's available")
        exit()
    
    def Main(self):
        self.Seat_init()
        self.Input_Check()
        self.PPO_spliter()
        self.Seat_finder()
        self.Passengers_Rule(self.Prime)
        self.Passengers_Rule(self.Power)
        self.Passengers_Rule(self.Other)
        self.Final_seat_arrangement_vis()
        
if __name__ == '__main__':
    try:
# =============================================================================
#         Creating the object as KF for the created class.
# =============================================================================
        KF = Airplane_seating_arrangement()
        KF.Main()
    except Exception as e:
        print(e)


# =============================================================================
# DoneBY: Ekanth Nithish PGV
# =============================================================================
