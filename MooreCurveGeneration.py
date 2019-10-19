# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 22:08:06 2019
@author: jiayi
"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib


#iteration number: 0, 1, 2, 3...
n=5;

#store previous position
pre = np.array((n-1, 0))

#store current position
#initially start at lower left corner
cur = np.array(( len(grid[0])-1, int((2**(n+1)*2-1)/2)-1 ))

#create grid size of 2**(n+1)*2-1
grid = np.zeros((2**(n+1)*2-1, 2**(n+1)*2-1));

#Moore Curve Generating rules:
#Constants: F, +, −
#Axiom: LFL+F+LFL
#Production rules:
#L → −RF+LFL+FR−
#R → +LF−RFR−FL+
def F(i, j,opct):
    if opct==0:
        grid[i-2:i+1, j]=1;
        pre[0] = i-1;
        pre[1] = j;
        cur[0] = i-2;
        cur[1] = j;
    else:
        if pre[1]==cur[1]:
            if(cur[0]==pre[0]-1):
                grid[i-2:i+1, j]=1;
                pre[0] = i-1;
                pre[1] = j;
                cur[0] = i-2;
                cur[1] = j;
                
            else:
                grid[i:i+3, j]=1;
                pre[0] = i+1;
                pre[1] = j;
                cur[0] = i+2;
                cur[1] = j;
                
        else:
            if(cur[1]==pre[1]-1):
                grid[i, j-2:j+1]=1;
                pre[0] = i;
                pre[1] = j-1;
                cur[0] = i;
                cur[1] = j-2;
                
            else:
                grid[i, j:j+3]=1;
                pre[0] = i;
                pre[1] = j+1;
                cur[0] = i;
                cur[1] = j+2;

def nF(i,j,opct):  #negative of F, move backward
    if opct==0:
        grid[i:i+3, j]=1;
        pre[0] = i+1;
        pre[1] = j;
        cur[0] = i+2;
        cur[1] = j;
    else:
        if pre[1]==cur[1]:
            if(cur[0]==pre[0]-1):
                grid[i:i+3, j]=1;
                pre[0] = i+1;
                pre[1] = j;
                cur[0] = i+2;
                cur[1] = j;
                
                
            else:
                grid[i-2:i+1, j]=1;
                pre[0] = i-1;
                pre[1] = j;
                cur[0] = i-2;
                cur[1] = j;
                
        else:
            if(cur[1]==pre[1]-1):
                grid[i, j:j+3]=1;
                pre[0] = i;
                pre[1] = j+1;
                cur[0] = i;
                cur[1] = j+2;
                
            else:
                grid[i, j-2:j+1]=1;
                pre[0] = i;
                pre[1] = j-1;
                cur[0] = i;
                cur[1] = j-2;
            


def pF(i, j,opct):
    if opct==0:
        grid[i, j:j+3]=1;
        pre[0] = i;
        pre[1] = j+1;
        cur[0] = i;
        cur[1] = j+2;
    else:
        if pre[1]==cur[1]:
            if(cur[0]==pre[0]-1):
                grid[i, j:j+3]=1;
                pre[0] = i;
                pre[1] = j+1;
                cur[0] = i;
                cur[1] = j+2;
                
            else:
                grid[i, j-2:j+1]=1;
                pre[0] = i;
                pre[1] = j-1;
                cur[0] = i;
                cur[1] = j-2;
                
        else:
            if(cur[1]==pre[1]-1):
                grid[i-2:i+1, j]=1;
                pre[0] = i-1;
                pre[1] = j;
                cur[0] = i-2;
                cur[1] = j;
                
            else:
                grid[i:i+3, j]=1;
                pre[0] = i+1;
                pre[1] = j;
                cur[0] = i+2;
                cur[1] = j;

def ppF(i,j,opct):
    nF(i,j,opct);

def pppF(i,j,opct):
    mF(i,j,opct);

def ppppF(i,j,opct):
    F(i,j,opct);
              
            
def mF(i, j,opct):
    if opct==0:
        grid[i, j-2:j+1]=1;
        pre[0] = i;
        pre[1] = j-1;
        cur[0] = i;
        cur[1] = j-2;
    else:
        if pre[1]==cur[1]:
            if(cur[0]==pre[0]-1):
                grid[i, j-2:j+1]=1;
                pre[0] = i;
                pre[1] = j-1;
                cur[0] = i;
                cur[1] = j-2;
                
            else:
                grid[i, j:j+3]=1;
                pre[0] = i;
                pre[1] = j+1;
                cur[0] = i;
                cur[1] = j+2;
                
        else:
            if(cur[1]==pre[1]-1):
                grid[i:i+3, j]=1;
                pre[0] = i+1;
                pre[1] = j;
                cur[0] = i+2;
                cur[1] = j;
                
            else:
                grid[i-2:i+1, j]=1;
                pre[0] = i-1;
                pre[1] = j;
                cur[0] = i-2;
                cur[1] = j;

def mmF(i,j,opct):
    nF(i,j,opct);
    
def mmmF(i,j,opct):
    pF(i,j,opct);

def mmmmF(i,j,opct):
    F(i,j,opct);

         
def L(m):
    if m==0:
        return ["m", F, "p", F, "p", F, "m"];
    else:
        return ["m"]+R(m-1)+[F, "p"]+L(m-1)+[F]+L(m-1)+["p", F]+R(m-1)+["m"];   

def R(m):
    if m==0:
        return ["p", F, "m", F, "m", F, "p"];
    else:
        return ["p"]+L(m-1)+[F, "m"]+R(m-1)+[F]+R(m-1)+["m", F]+L(m-1)+["p"];   

    

def Moore(n):
    m = n;
    if m==0:
        operation = [F, "p", F, "p", F]
        
    else:
        operation = L(m-1)+[F]+L(m-1)+["p",F]+["p"]+L(m-1)+[F]+L(m-1);
    
    opct=0;
    
    for i in range(0, len(operation)):
        mct=0;
        pct=0;
        if operation[i]!="m" and operation[i]!="p":
            if i==0:
                operation[i](cur[0],cur[1],opct);
                opct=opct+1;
            else:
                if operation[i-1]!="m" and operation[i-1]!="p":
                    operation[i](cur[0],cur[1],opct);
                    opct=opct+1;
                else: 
                    j=i-1;
                    while (operation[j]=="m" or operation[j]=='p') and j >=0:
                        if operation[j]=="m":
                            mct=mct+1;
                        else:
                            pct=pct+1;
                        j=j-1;
                    mpnet=mct-pct;
                    
                    
                    if mpnet==0:
                        operation[i](cur[0],cur[1],opct);
                        opct=opct+1;
                    elif mpnet>0:
                        if mpnet%4==1:
                            mF(cur[0],cur[1],opct);
                            opct=opct+1;
                        if mpnet%4==2:
                            mmF(cur[0],cur[1],opct);
                            opct=opct+1;
                        if mpnet%4==3:
                            mmmF(cur[0],cur[1],opct);
                            opct=opct+1;
                        if mpnet%4==0:
                            mmmmF(cur[0],cur[1],opct);
                            opct=opct+1;
                            
                    else: #mpnet<0
                        if -mpnet%4==1:
                            pF(cur[0],cur[1],opct);
                            opct=opct+1;
                        if -mpnet%4==2:
                            ppF(cur[0],cur[1],opct);
                            opct=opct+1;
                        if -mpnet%4==3:
                            pppF(cur[0],cur[1],opct);
                            opct=opct+1;
                        if -mpnet%4==0:
                            ppppF(cur[0],cur[1],opct);
                            opct=opct+1;
                        

                    
                
     


#run
Moore(n);

grid

plt.figure(figsize=(30, 30))
plt.imshow(grid)
