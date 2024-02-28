from flask import Flask, send_file
import matplotlib.pyplot as plt
import io
import numpy as np

app = Flask(__name__)

# Predefined background color choices
background_colors = ['lightblue', 'lightgreen', 'lightcoral']

@app.route('/')
def generate_image():
    # Define text
    name = "John Doe"
    position = "Tanzania: "
    position_number = "12345"

    # Create a plot with text
    fig, ax = plt.subplots()

    # Set background color randomly from the choices
    background_color = np.random.choice(background_colors)
    fig.patch.set_facecolor(background_color)

    # Set figure size with longer width and smaller height
    fig.set_size_inches(2, 0.5)  # Adjust width and height as needed

    # Set font size for name and position
    font_size = 10

    # Set text color to white
    text_color = 'white'

    # Name
    ax.text(0.05, 0.5, name, ha='left', va='center', fontsize=font_size, color=text_color)
    
    # Position
    ax.text(0.5, 0.5, position, ha='left', va='center', fontsize=font_size, color=text_color)
    
    # Position number
    ax.text(0.95, 0.5, position_number, ha='right', va='center', fontsize=font_size, color=text_color)

    # Remove axes
    ax.axis('off')

    # Save the plot to a BytesIO object
    img_io = io.BytesIO()
    plt.savefig(img_io, format='png', bbox_inches='tight', pad_inches=0)
    img_io.seek(0)

    # Close the plot to free memory
    plt.close()

    # Return the image to the user
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)
