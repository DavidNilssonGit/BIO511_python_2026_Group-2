# Import the required external libraries
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from plotnine import ggplot, aes, geom_point, ggtitle

# Load the 'penguins' dataset using Seaborn
penguins = sns.load_dataset("penguins")

# Remove any rows containing missing values (NaN)

penguins_trimmed = penguins.dropna()

# Plot a scatterplot using matplotlib
# The plot should show flipper length on the x-axis and body mass on the y-axis
# Add an informative title, xlabel and ylabel, then save the plot

plt.scatter(penguins_trimmed['flipper_length_mm'], penguins_trimmed['body_mass_g'])
plt.title('Flipper Length in mm vs Body Mass in g')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Body Mass (g)')


plt.savefig("FLipper_Length_vs_Body_Mass.png")
plt.show()


# Create the same scatterplot using Plotly

plotly_penguins = px.scatter(
    penguins_trimmed,
    x="flipper_length_mm",
    y="body_mass_g",
    title="Flipper Length (mm) VS Body Mass (g)",
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)"
    }
)
plotly_penguins.write_html("F.html")
plotly_penguins.show()


# Create the scatterplot using Seaborn

