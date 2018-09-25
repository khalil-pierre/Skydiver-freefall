# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 14:49:54 2018

@author: user
"""

import matplotlib.pyplot as plt 
import numpy as np
import math




def freefall(heghit,velocity,dt,mass=73,cross_sectional_area=0.75,drag_coefficant=1,Plot=True,Error_plots=False,Modiefied_euler_method=False,Variable_air_density=False,compare=False):
    '''A function that predicts the behaviour of an object in free fall using the Euler and modified Euler method.\
     Takes as arguments the starting heghit, the inital velocity, the size of the time step, the mass of the object,\
      the cross sectional area of the object, the drag coefficent, whether to plot the y(t) and v(t), whether to plot the error\
     on the euler method by comparing it to the anayltical soultions, wether to use the standard or modified euler method,\
      wether or not air density should be vairable in the soultion and wether you want the anaylitical models to be plotted or not.\
       Note that the cross sectional area, drag coefficant and mass already have inputs, these are based on Felix Baumgartner'''
    
    time=0
    position=heghit
    
    time_graph=[]
    position_graph=[]
    velocity_graph=[]
    airdensity_plot=[]
    analytical_position=[]
    analytical_velocity=[]
    
    
    while position>0:
        time+=dt
        g=(6.67e-11)*(5.972e24)/(6.371e6+position)**2
        
        #if and else statments used to change how free fall is modeled i.e. 
        #is air density variable and what numerical soultion should be used
        
        if Variable_air_density==True:
            airdensity=1.2*np.exp(-position/7640)
            airdensity_plot+=[airdensity]
        else:
            airdensity=1.2
        k=(drag_coefficant*airdensity*cross_sectional_area)/2
       
        if Modiefied_euler_method==True:
            velocity_mid=velocity-(dt/2)*(g+(k/mass)*abs(velocity)*velocity) 
        else:
            velocity_mid=velocity
        
        #Euler or modified Euler method used to calculate postion and velocity
        
        position+=dt*velocity_mid
        velocity=velocity-dt*(g+(k/mass)*abs(velocity_mid)*velocity_mid)
        
        #Results stored in graphs so they can be plotted later
        velocity_graph+=[velocity]     
        time_graph+=[time]
        position_graph+=[position]
        
        
        if Error_plots == True or compare ==True:
            analytical_position+=[heghit-(mass/(2*k))*math.log(math.cosh((k*g/mass)**(0.5)*time)**2)]
            analytical_velocity+=[-(mass*g/k)**(0.5)*math.tanh((k*g/mass)**(0.5)*time)]
            
    #Function plots graphs depending on what model is used
    #Was designed so it would print out the aproprate graphs for each section in exercise
    
    if Plot==True:
        if Modiefied_euler_method==True:
            plt.title('Distacnce time graph Modifeied Euler method')
        else:
            plt.title('Distacnce time graph Euler method')
        
        plt.xlabel('Time (s)')
        plt.ylabel('Heghit (m)')        
        plt.plot(time_graph,position_graph,label='Euler method')
        if compare ==True:
            plt.plot(time_graph,analytical_position,label='Analytical model')
            plt.legend()
        plt.show()
        plt.clf()
        
        if Modiefied_euler_method==True:
            plt.title('Velocity time graph Modifeied Euler method')
        else:
            plt.title('Velocity time graph Euler method')           
    
        plt.xlabel('Time (s)')
        plt.ylabel('Speed (m/s)')
        plt.plot(time_graph,velocity_graph,label='Euler method')
        if compare ==True:
            plt.plot(time_graph,analytical_velocity,label='Analytical model')
            plt.legend()
        plt.show()
        plt.clf()
    
    if Variable_air_density == True:
        plt.title('Air density as a funciton of heghit')
        plt.xlabel('Heghit (m)')
        plt.ylabel('Air denity (kg/m^3)')
        plt.plot(position_graph,airdensity_plot)
        plt.show()
        plt.clf()
        
    if Error_plots == True:
        #numpy arrays used to calculate the diffrence bettween the anaylitical and numerical soultions
        dif_position=-np.array(analytical_position)+np.array(position_graph)
        dif_velocity=np.array(analytical_velocity)-np.array(velocity_graph)
           
        plt.title('Position diffrence')
        plt.xlabel('Time (s)')
        plt.ylabel('Position error (m)')
        plt.plot(time_graph,dif_position)
        plt.show()
        plt.clf()
           
        plt.title('Velocity diffrence')
        plt.xlabel('Time (s)')
        plt.ylabel('Position error (m/s)')
        plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
        plt.plot(time_graph,dif_velocity)
        plt.show()
        plt.clf()
           
   
    return print('Time taken to fall was ' + str(time) + 's') \
           ,print('Speed at impact was ' + str(abs(velocity)) + 'm/s' )\
           ,print('Max Speed was ' + str(np.amin(velocity_graph)) + 'm/s')
      

    
    
    
MyInput = '0'
while MyInput != 'q':
    MyInput = input('Enter a choice, "a","b","c","d","e", or "q" to quit: ')
    if MyInput == 'a':
        print('You have chosen part (a)')
        print('In this section the behaviour of a freefalling skydiver is modeled using the Euler method')
        
        pos=float(input('Please select a starting heghit for the skydiver (m): '))
        vel=float(input('Please select a inital velocity for the skydiver (m/s): '))
        delta=float(input('Please select the time step the euler method will use: '))
        
        freefall(pos,vel,delta)
        
        
    elif MyInput == 'b':
        print('You have chosen part (b)')
        print('In this section the Euler method\'s numerical soultions are compared to the analytical models for a skydiver in freefall.')
        print('The diffrence between the two at each point t is plotted.')
        print('To get an idea of how the accuracy of the euler method changes with the time step you should try multiple time steps and see how this effects the results.')
        
        
        delta=float(input('Please select the time step the euler method will use: '))
        freefall(1000,0,delta,Plot=False,Error_plots=True)
        
        print('The graph is generated from an inital heghit of 1km and an inital velocity of 0')
        
        
    
    elif MyInput == 'c':
        print('You have chosen part (c)')
        print('In this section the Euler method was modified')
        print('The resulting numerical soultions where can be compared to the anaylitical soultions.')
        
        pos=float(input('Please select a starting heghit for the skydiver (m): '))
        vel=float(input('Please select a inital velocity for the skydiver (m/s): '))
        delta=float(input('Please select the time step the euler method will use: '))
       
        #Allow the user to have some input into what graphs they see        
        comparison=input('Do you want to overlay the analytical model on the y(t) and v(t) plots (y) or (n): ')
        if comparison=='y':
            comp=True
        elif comparison=='n':
            comp=False
        else:
            print(str(comparison)+ 'not a valid input your answer has been taken to be no')
            comp=False
        Error=input('Do you want to see the Error plots (y) or (n): ')
        
        if Error=='y':
            Error=True
        elif Error=='n':
            Error=False
        else:
            print(str(Error) + ' is not a valid choice, your answer has been taken to be no')
            Error=False
        
        freefall(pos,vel,delta,Error_plots=Error,Modiefied_euler_method=True,compare=comp)
        
        

  
        
    elif MyInput == 'd':
        print('You have chosen part (d)')
        print('In this section variable air density has been added to make the model more accurate')
        
        pos=float(input('Please select a starting heghit for the skydiver (m): '))
        vel=float(input('Please select a inital velocity for the skydiver (m/s): '))
        delta=float(input('Please select the time step the euler method will use: '))
        Error=str(input('Do you want to see the Error plots (y) or (n): '))
        
        
        if Error=='y':
            E=True
        elif Error=='n':
            E=False
        else:
            print(str(Error) + ' is not a valid choice, your answer has been taken to be no')
            E=False
        
        comparison=str(input('Do you want to overlay the analytical model on the y(t) and v(t) plots (y) or (n): '))
        if comparison=='y':
            comp=True
        elif comparison=='n':
            comp=False
        else:
            print(str(comparison)+ 'not a valid input your answer has been taken to be no')
            comp=False
        
        freefall(pos,vel,delta,Plot=True,Error_plots=E,Modiefied_euler_method=True,Variable_air_density=True,compare=comp)
        
        

    elif MyInput =='e':
        print('You have chosen part (e)')
        print('In this section you can see how changing the parameters of the system changes the end results')
        delta=float(input('Please select the time step the euler method will use: '))
        
        Mass=float(input('Please select a value for the mass of the object (kg): '))
        CrossSectionalArea=float(input('Please select a cross sectional area for the object (m^2): '))
        DragCoefficant=float(input('please select a value for the drag coefficant: '))
        
        comparison=input('Do you want to overlay the analytical model on the y(t) and v(t) plots (y) or (n): ')
        if comparison=='y':
            comparison=True
        elif comparison=='n':
            comparison=False
        else:
            print(str(comparison)+ 'not a valid input your answer has been taken to be no')
            comparison=False
        
        
        freefall(39045,0,delta,mass=Mass,cross_sectional_area=CrossSectionalArea,drag_coefficant=DragCoefficant,\
                 Modiefied_euler_method=True,Variable_air_density=True,compare=comparison)
        
        

    elif MyInput != 'q':
        print('This is not a valid choice')
    
print('You have chosen to finish - goodbye.')
               
        
   