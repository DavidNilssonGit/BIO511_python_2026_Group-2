# Import seaborn, matplotlib, plotly, plotnine
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from plotnine import *

# Apply the default theme
sns.set_theme()

# Load an example dataset
penguins = sns.load_dataset("penguins")

# remove rows with missing values, penguins_clean has the new stuff
penguins_clean = penguins.dropna()
print(penguins_clean)

# make scatterplot
plt.scatter(penguins_clean["flipper_length_mm"], penguins_clean["body_mass_g"])
plt.title("Penguin flipper length vs body mass")
plt.xlabel("Flipper length (mm)")
plt.ylabel("Body mass (g)")
plt.savefig("penguin_scatterplot.png")
plt.show()

# Make an scatterplot with plotly
df = penguins_clean

fig = px.scatter(
    df,
    x="flipper_length_mm",
    y="body_mass_g",
    title="Penguin flipper length vs body mass"
)

fig.write_html("penguin_scatterplot.html")

# make scatterplot med seaborn
sns.scatterplot(
    data=df,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species"
)
plt.savefig("penguin_seaborn.png")
plt.close()

# make scatterplot with plotnine
plot = (
    ggplot(penguins_clean, aes(x="flipper_length_mm", y="body_mass_g"))
    + geom_point()
)
ggsave(plot, "penguin_plotnine.png")