# Circular Dichroism and Optical Rotatory Dispersion Kramers Kronig numerical transformation
A python script that performs a numerical Kramers-Kronig transformation from Circular Dichroism into Optical Rotatory Dispersion. A "leap frog" method is used for the numerical integration. The script outputs a plot .png file. The data used is from a Lorentzian function, but raw data can be used as well.


# Kramers-Kronig numerical integration
The Kramers-Kronig relation can be used relate two physical quantities to each other and in this script it was used to calculate Optical Rotatory Dispersion from a simulated Circular Dichroism measurement.

The relation is expressed with the equations [1]

![image](https://user-images.githubusercontent.com/48471512/179350156-1746d795-4a4a-4790-80b9-91e925042e49.png)

and they can be expressed numerically with the equations

![image](https://user-images.githubusercontent.com/48471512/179350190-200d375c-7877-43ab-a125-61dfceaec59e.png)

To avoid a situation where there is a zero in the denominator of these equations, a "leap frog" method is used. For odd i we use even j, and for even i we use odd j. So when i is odd

![image](https://user-images.githubusercontent.com/48471512/179350224-3a3c13d4-a98b-42b5-9480-7a7af42e0b9e.png)

and when i is even [2]

![image](https://user-images.githubusercontent.com/48471512/179350237-1049c1da-29fb-4270-815c-1defcdee3cb8.png)


# Output
The script outputs the following plot, showing the original Lorentzian peak in blue, the initial transformation in orange and a twice transformed data in red. We can see that the transformation is qualitatively valid, as the original peak and ord-to-cd-to-ord data matches the original plot. 

![test_run_plot2](https://user-images.githubusercontent.com/48471512/179350260-7adaaeb6-5c08-40f9-8637-53d1c5a04ccf.png)

# Used sources
[1] C. A. Emeis, L. J. Oosterhoff and G. D. Vries, Numerical evaluation of Kramers—Kronig relations, Royal Society, 1967. 

[2] K. Ohta and H. Ishida, Comparison Among Several Numerical Integration Methods for Kramers-Kronig Transformation, Applied Spectroscopy, 1988. 
