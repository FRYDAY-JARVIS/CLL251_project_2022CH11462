import matplotlib.pyplot as plt
import numpy as np

x0 = 3.4e-4

# Create an array with the specified elements
array_elements=[2*x0,5*x0,x0,x0,x0,x0,2*x0]

second_array = [0.35, 0.3, 3, 0.2725, 0.19, 0.285, 0.135, 0.17]

def draw_gradient(input_float):
    # Find the absolute difference between the input float and 310
    absolute_difference = abs(input_float - 310)
    
    # Calculate q_by_a
    q_by_a = 40.16 * absolute_difference
    
    # Create an array with only one element, which is the input to the function
    array = [input_float]
    
    # Run a loop six times, adding one value to the array in each iteration
    for i in range(6):
        # Calculate the sum of array_elements[k]/second_array[k] for k up to the current iteration
        sum_elements = sum(array_elements[k] / second_array[k] for k in range(i + 1))
        
        # Calculate the final value using the sum, q_by_a, and the input float
        final_value = input_float + q_by_a * sum_elements
        
        # Add the final value to the array
        array.append(final_value)
    
    # Append the final value of 310 to the array
    array.append(310)
    print(array)
    # Initialize the initial x-coordinate
    initial_x = 0
    
    # Plot the gradient lines
    for i in range(7):  # There are 7 segments in the array
        # Calculate the final x-coordinate for the current segment
        final_x = initial_x + array_elements[i]
        
        # Calculate the temperature for the current segment
        initial_temp = array[i]
        final_temp = array[i + 1]
        
        # Divide the segment into 500 points
        x_values = np.linspace(initial_x, final_x, num=500)
        
        # Calculate the color intensity (proportional to temp) for each point
        
        color_intensity1 = 0.3+(initial_temp - input_float) *0.7/ (310 - input_float)
        color_intensity2 = 0.3+(final_temp- input_float) *0.7/ (310 - input_float)
        color_intensity_values = np.linspace(color_intensity1, color_intensity2, num=500)
        # Clip values to [0, 1] range
        
        # Iterate over each point and draw a vertical line
        for x, color_intensity in zip(x_values, color_intensity_values):
            # Calculate the color based on color intensity
            color = (color_intensity, 0, 0)  # Red color with intensity proportional to temp
            
            # Draw a vertical line segment with color intensity proportional to temp
            plt.vlines(x=x, ymin=0, ymax=310, color=color, linewidth=1)
        
        # Update the initial x-coordinate for the next segment
        initial_x = final_x
    
    initial_x = 0
    
    # Plot the gradient lines
    for i in range(7):  # There are 7 segments in the array
        # Calculate the final x-coordinate for the current segment
        final_x = initial_x + array_elements[i]
        initial_x=final_x
        plt.axvline(x=final_x, color='black', linestyle='-', linewidth=1)
    
    # Set plot labels and remove y-axis ticks and labels
    plt.xlabel('Distance from outer layer to inner layer')
    plt.gca().axes.yaxis.set_visible(False)
    
    # Show the plot
    plt.show()

# Test the function
draw_gradient(280)