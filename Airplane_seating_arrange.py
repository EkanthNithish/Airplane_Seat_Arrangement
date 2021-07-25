import math
import random

class Airplane_seating_arrangement:
    
    def __init__(self):
        self.n=int(input("Number of Matrices : "))
        self.dim=[]
        self.temp=()
        self.Seat=[]
        self.Prime=[]
        self.Power=[]
        self.Other=[]
        self.Window_seat=[] 
        self.Aisle_seat=[]
        self.Middle_seat=[]
        print("Passenger's id : ",end=" ")
        self.passenger=list(map(int,input().split(' ')))
        for i in range(self.n):
          print("Number of rows in ",i+1," matrix : ",end=" ")
          row=int(input())
          print("Number of columns in ",i+1," matrix : ",end=" ")
          col=int(input())
          self.temp=(row,col)
          self.dim.append(self.temp)
          self.temp=()
    
    def findPrime(self, num):
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
        Log=math.log(n,2)
        AbsoltueValue=int(Log)
        Sol = True if Log==AbsoltueValue else False
        return Sol
    
    def Seat_init(self):
        for i in range(self.n):
          mat=[]
          Row=self.dim[i][0]
          Col=self.dim[i][1]
          for j in range(Row):
            rows=[0]*Col
            mat.append(rows)
          self.Seat.append(mat)
    
    def PPO_spliter(self):
        for i in self.passenger:
            if(self.findPrime(i)):
              self.Prime.append(i)
            elif(self.multiple_of_2_power_n(i)):
              self.Power.append(i)
            else:
              self.Other.append(i)
    
    def Seat_finder(self):
        for i in range(self.n):
          if(i==0):
            Row=self.dim[i][0]
            Col=self.dim[i][1]
            for j in range(Row):
              for k in range(Col): 
                if(k==0):
                  self.temp=(i,j,k)
                  self.Window_seat.append(self.temp)
                elif(k==Col-1):
                  self.temp=(i,j,k)
                  self.Aisle_seat.append(self.temp)
                #else part
                else :
                  self.temp=(i,j,k)
                  self.Middle_seat.append(self.temp)
                  
          elif(i==self.n-1):
            Row=self.dim[i][0]
            Col=self.dim[i][1]
            for j in range(Row):
              for k in range(Col): 
                #checking if first column
                if(k==0):
                  self.temp=(i,j,k)
                  self.Aisle_seat.append(self.temp)
                #checking if last column
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
    
    def Prime_passengers(self):
        while(len(self.Prime)!=0):
            if(len(self.Aisle_seat)!=0):
    
              passenger_id=random.choice(self.Prime)
              self.temp=random.choice(self.Aisle_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Prime.remove(passenger_id)
              self.Aisle_seat.remove(self.temp)
    
            elif(len(self.Window_seat)!=0):
              
              passenger_id=random.choice(self.Prime)
              self.temp=random.choice(self.Window_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Prime.remove(passenger_id)
              self.Window_seat.remove(self.temp)  
    
            else :
              
              passenger_id=random.choice(self.Prime)
              self.temp=random.choice(self.Middle_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Prime.remove(passenger_id)
              self.Middle_seat.remove(self.temp)
    
    def Power_0f_2_passenger(self):
        
        while(len(self.Power)!=0):
             #alloting in Aisle seats    
            if(len(self.Aisle_seat)!=0):
              passenger_id=random.choice(self.Power)
              self.temp=random.choice(self.Aisle_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Power.remove(passenger_id)
              self.Aisle_seat.remove(self.temp)
            
                
            elif(len(self.Window_seat)!=0):
              passenger_id=random.choice(self.Power)
              self.temp=random.choice(self.Window_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Power.remove(passenger_id)
              self.Window_seat.remove(self.temp)
        
               
            else :
              passenger_id=random.choice(self.Power)
              self.temp=random.choice(self.Middle_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Power.remove(passenger_id)
              self.Middle_seat.remove(self.temp)
       
    def other_passengers(self):        
        while(len(self.Other)!=0):
            #alloting in Aisle seats
            if(len(self.Aisle_seat)!=0):
        
              passenger_id=random.choice(self.Other)
              self.temp=random.choice(self.Aisle_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Other.remove(passenger_id)
              self.Aisle_seat.remove(self.temp)
        
            elif(len(self.Window_seat)!=0):
              passenger_id=random.choice(self.Other)
              self.temp=random.choice(self.Window_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Other.remove(passenger_id)
              self.Window_seat.remove(self.temp)  
        
            else :
              passenger_id=random.choice(self.Other)
              self.temp=random.choice(self.Middle_seat)
              self.Seat[self.temp[0]][self.temp[1]][self.temp[2]]=passenger_id
              self.Other.remove(passenger_id)
              self.Middle_seat.remove(self.temp)
    
    def Final_seat_arrangement_vis(self):
        for i in range(self.n):
          Row=self.dim[i][0]
          for j in range(Row):
            print(self.Seat[i][j]) 
          print(' ')
    
    def Main(self):
        self.Seat_init()
        self.PPO_spliter()
        self.Seat_finder()
        self.Prime_passengers()
        self.Power_0f_2_passenger()
        self.other_passengers()
        self.Final_seat_arrangement_vis()
        
# =============================================================================
# DoneBY: Ekanth Nithish PGV
# =============================================================================

if __name__ == '__main__':
    try:
        KF = Airplane_seating_arrangement()
        KF.Main()
    except Exception as e:
        print(e)

    
