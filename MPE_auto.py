# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:05:34 2022

@author: ldavidov
"""

import tkinter as tk
import numpy as np


# Dimensions of the GUI window
WIDTH = 600;
HEIGHT = 500;





def I_col(P,D):                          # Calculates irradiance for power and a diameter
    A_colimated = (np.pi*D**2)/4;
    I_colimated = P/A_colimated;
    return I_colimated;

    
def message_return(ratio_MPE):
    if ratio_MPE > 1.0 and ratio_MPE < 5:
        laser_advice = "MPE value exceeded!";
    elif ratio_MPE >= 5:
        laser_advice = "WARNING: MPE value exceeded \n by more than 5 times!"
    elif ratio_MPE <= 1.0:
        laser_advice = "SAFE!";
    return laser_advice;

    

def calc(wavel,P,BD):                 # Determines the irradiance to MPE ratio based on the laser safety table per wavelength
    if wavel > 400 and wavel <= 700:
        t_eye = 0.25;                    # Eye response time [s]
        MPE = 18*t_eye**(0.75)/t_eye;    # MPE value [W/m^2]
        I_calc = I_col(P,BD);            # Calculated irradiance [W/m^2]
        ratio = I_calc/MPE;              # Ratio I_calc to MPE
    elif wavel < 400:
        ratio = "NaN";
    elif wavel > 700 and wavel <= 1050:
        MPE = 10*10**(0.002*(wavel-700));
        I_calc = I_col(P,BD);            # Calculated irradiance [W/m^2]
        ratio = I_calc/MPE;              # Ratio I_calc to MPE
    elif wavel > 1050 and wavel <= 1150:
        MPE = 10*5*1;
        I_calc = I_col(P,BD);            # Calculated irradiance [W/m^2]
        ratio = I_calc/MPE;              # Ratio I_calc to MPE
    elif wavel > 1150 and wavel <= 1200:
        MPE = 10*5*10**(0.018*(wavel-1150));
        I_calc = I_col(P,BD);            # Calculated irradiance [W/m^2]
        ratio = I_calc/MPE;              # Ratio I_calc to MPE
    elif wavel > 1200 and wavel <= 1250:
        MPE  = 10*5*(8+10**(0.04*(wavel-1250)));
        I_calc = I_col(P,BD);            # Calculated irradiance [W/m^2]
        ratio = I_calc/MPE;              # Ratio I_calc to MPE
    elif wavel > 1250  and wavel <= 1400:
        MPE = 2000*5;
        I_calc = I_col(P,BD);            # Calculated irradiance [W/m^2]
        ratio = I_calc/MPE;              # Ratio I_calc to MPE
    elif wavel > 1400 and wavel <= 10**6:
        MPE = 1000;
        I_calc = I_col(P,BD);            # Calculated irradiance [W/m^2]
        ratio = I_calc/MPE;              # Ratio I_calc to MPE
    ratio = round(ratio, 3);
    label_output_MPE.config(text = ratio);
    label_output.config(text = message_return(ratio))
    return ratio;
 


 


# Here starts the root for the GUI
root = tk.Tk()

root.title('MPE Calculation Software for CW laser')
photo = tk.PhotoImage(file = "logo_small1.png")
root.iconphoto(False, photo)

root.geometry("600x500")
root.resizable(0, 0)


canvas = tk.Canvas(root, height = HEIGHT, width = WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='background.png')
background_label=tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)



frame1 = tk.Frame(root, bg = '#3c5bb0', bd=5)
frame1.place(relx=0.95, rely=0.5, relwidth=0.30, relheight=0.5, anchor = 'e')





entry1 = tk.Entry(frame1, font=("Calibri 10"))
entry1.place(relwidth=0.5, relheight=0.075)

label1 = tk.Label(frame1, text = " \u03BB [nm]", bg = '#80c1ff')
label1.place(relx=0.55, relheight=0.075, relwidth=0.45)





entry2 = tk.Entry(frame1, font=("Calibri 10"))
entry2.place(rely=0.2, relwidth=0.5, relheight=0.075)

label2 = tk.Label(frame1, text = "Power [W]", bg = '#80c1ff')
label2.place(relx=0.55, rely=0.2, relheight=0.075, relwidth=0.45)





entry3 = tk.Entry(frame1, font=("Calibri 10"))
entry3.place(rely=0.4, relwidth=0.5, relheight=0.075)

label3 = tk.Label(frame1, text = "BD [m]", bg = '#80c1ff')
label3.place(relx=0.55, rely=0.4, relheight=0.075, relwidth=0.45)





button = tk.Button(frame1, text = "CALCULATE", command=lambda: [calc(float(entry1.get()),float(entry2.get()),float(entry3.get()))])
button.place(relx=0.05,rely=0.8, relheight=0.1, relwidth=0.9)



lower_frame = tk.Frame(root, bg='#3c5bb0', bd=5)
lower_frame.place(relx=0.05, rely=0.5, relwidth=0.5, relheight=0.5, anchor = 'w')


label = tk.Label(lower_frame, text = "Calculated values", bg = '#bdecfc')
label.place(relx=0.1, rely=0, relheight=0.1, relwidth=0.8)



label = tk.Label(lower_frame, text = "MPE Ratio", bg = '#80c1ff')
label.place(relx=0.025, rely=0.2, relheight=0.1, relwidth=0.45)


label_output_MPE = tk.Label(lower_frame, text = "", bg = '#80c1ff')
label_output_MPE.place(relx=0.525, rely=0.2, relheight=0.1, relwidth=0.45)

label_output = tk.Label(lower_frame, text = "", bg = '#80c1ff')
label_output.place(relx=0.05, rely=0.4, relheight=0.3, relwidth=0.90)






lowest_frame = tk.Frame(root, bg='#3c5bb0', bd=5)
lowest_frame.place(relx=0.5, rely=0.95, relwidth=0.9, relheight=0.15, anchor = 's')

label = tk.Label(lowest_frame, text = "Please choose a value ABOVE 400 nm \n BD = Bundel Diameter \n 1 inch = 0.0254 m \n For visible light the exposure time is t = 0.25s. For \u03BB > 700nm maximum exposure time is taken ", bg = '#80c1ff')
label.place(relheight=1, relwidth=1)





root.mainloop()