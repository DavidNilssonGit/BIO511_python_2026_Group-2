##Load the ‘penguins’ dataset using seaborn. Remove any rows with missing values. Hint: Check out how to use the dropna() function.
"""
import seaborn as sns

# 1. Load the penguins dataset
penguins = sns.load_dataset('penguins')

# 2. Remove rows with missing values (NaN)
penguins_clean = penguins.dropna()

# Verify the results
print("Original dataset shape:", penguins.shape)
print("Cleaned dataset shape:", penguins_clean.shape)

#############################################################

##Plot a scatterplot using matplotlib. The plot should show flipper length on the x-axis and body mass on the y-axis. Add an informative title, xlabel and ylabel. Save the plot.


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')


plt.scatter(
    penguins["flipper_length_mm"],
    penguins["body_mass_g"]
)

plt.title("Penguin Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")

plt.savefig("flipper_vs_body_mass.png")
plt.show()

#######################################################

##Create the same plot but using plotly. Save an interactive file (.html).

import pandas as pd
import plotly.express as px

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

penguins = sns.load_dataset('penguins')

fig = px.scatter(
    penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    title="Penguin Flipper Length vs Body Mass",
    labels={
        "flipper_length_mm": "Flipper Length (mm)",
        "body_mass_g": "Body Mass (g)"
    }
)

fig.write_html("flipper_vs_body_mass.html")
fig.show()

########################################################


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


penguins = sns.load_dataset('penguins')

sns.scatterplot(
    data=penguins,
    x="flipper_length_mm",
    y="body_mass_g",
    hue="species"
)

plt.title("Penguin Flipper Length vs Body Mass")
plt.xlabel("Flipper Length (mm)")
plt.ylabel("Body Mass (g)")

plt.savefig("flipper_vs_body_mass_seaborn.png")
plt.show()

#########################################################

"""

##Finally, try it out using plotnine. To save the plot you will need to import and use the function ggsave. (A good practice is to always import any packages or functions at the top of your script.)

import pandas as pd
from plotnine import (
    ggplot, aes, geom_point,
    labs, theme_minimal, ggsave
)
import seaborn as sns
import matplotlib.pyplot as plt

penguins = sns.load_dataset('penguins')


p = (
    ggplot(
        penguins,
        aes(
            x="flipper_length_mm",
            y="body_mass_g",
            color="species"
        )
    )
    + geom_point()
    + labs(
        title="Penguin Flipper Length vs Body Mass",
        x="Flipper Length (mm)",
        y="Body Mass (g)",
        color="Species"
    )
    + theme_minimal()
)

ggsave(
    self=p,
    filename="flipper_vs_body_mass_plotnine.png",
    verbose=False
)

print(p)