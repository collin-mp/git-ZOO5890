"""Create a two-panel box plot of fish abundance by month and reef."""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


# This line tells Python where the CSV file is stored.
# We go up one folder from this script's location, then into the data folder.
data_path = Path(__file__).resolve().parent.parent / "data" / "ReefFish.csv"

# This folder will hold the generated plot output file.
plots_dir = Path(__file__).resolve().parent / "plots"
plots_dir.mkdir(exist_ok=True)


# This function reads the CSV file into a table so we can work with it easily.
def load_fish_data():
    """Load the reef fish data from the data folder."""
    # pd.read_csv opens the CSV file and turns its rows and columns into a DataFrame.
    # A DataFrame is a pandas table that lets us filter, group, and analyze data.
    return pd.read_csv(data_path)


# This creates a two-panel box plot, with one panel for each month.
# Within each panel, the reefs are shown side-by-side so similar species remain adjacent.
# For example, BlueFish has one box for Reef1 next to one box for Reef2.
def make_monthly_reef_box_plots(df):
    """Create a two-panel box plot split by month, with reef boxes side-by-side for each species."""
    # Use a 1-by-2 layout so each panel can highlight one month.
    # fig represents the whole image, while axes contains the two graph panels.
    fig, axes = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

    # Match the same species colors as the other plots for visual consistency.
    species_colors = {
        "BlackFish": "#4a4a4a",
        "BlueFish": "#5b8db8",
        "RedFish": "#d97777",
    }

    # Lists give us a predictable order instead of relying on the order in the CSV file.
    species_order = ["BlackFish", "BlueFish", "RedFish"]
    month_order = ["January", "February"]
    reefs = ["Reef1", "Reef2"]

    # Loop through each month to build a panel for that time point.
    # zip pairs the first axis with January and the second axis with February.
    for ax, month in zip(axes, month_order):
        # df["Month"] == month creates True/False values for every row.
        # The brackets keep only the rows belonging to the current month.
        month_data = df[df["Month"] == month]

        # These empty lists will collect the values and labels for this panel.
        box_data = []
        labels = []

        # The nested loops create boxes in species order, with one box per reef.
        for species in species_order:
            for reef in reefs:
                # Each condition selects one species and one reef from this month.
                reef_species_data = month_data[
                    (month_data["Species"] == species)
                    & (month_data["Site"] == reef)
                ]

                # Select only the abundance numbers because those are the values to plot.
                box_data.append(reef_species_data["Abundance"])

                # \n puts the reef name on a second line below the species name.
                labels.append(f"{species}\n{reef}")

        # Each box represents one species-by-reef combination for that month.
        # patch_artist=True allows us to fill the boxes with color.
        # widths controls how wide each box appears.
        box_plot = ax.boxplot(box_data, patch_artist=True, widths=0.5)

        # Give each box the matching species color.
        # zip pairs each drawn box with its corresponding text label.
        for box, label in zip(box_plot["boxes"], labels):
            # Split the two-line label and keep its first part, the species name.
            species_name = label.split("\n")[0]
            # set changes the box's fill color and makes it slightly transparent.
            box.set(facecolor=species_colors[species_name], alpha=0.7)

        # A black dashed median line makes the center of each distribution easy to read.
        # box_plot["medians"] contains the median line created for every box.
        for median_line in box_plot["medians"]:
            median_line.set(color="black", linestyle="--", linewidth=1.5)

        # There is one x-axis position for every label, starting at position 1.
        ax.set_xticks(range(1, len(labels) + 1))
        # Replace numeric positions with readable species and reef names.
        ax.set_xticklabels(labels, rotation=0)
        # f"{month}" inserts the current month into the panel title.
        ax.set_title(f"{month}")
        ax.set_xlabel("Species and Reef")
        ax.set_ylabel("Abundance")
        # Add faint horizontal lines to help compare the heights of the boxes.
        ax.grid(True, axis="y", alpha=0.3)

    # Adjust spacing so labels and titles do not overlap.
    plt.tight_layout()

    # Save the monthly reef box plot in the plots folder.
    # / joins folder and filename in a way that works across operating systems.
    output_path = plots_dir / "final_reef_species_boxplot_by_month.png"
    # bbox_inches="tight" prevents labels near the edges from being cut off.
    plt.savefig(output_path, bbox_inches="tight")
    print(f"Saved monthly reef box plot to: {output_path}")

    # Returning the path lets another part of a program use the saved file location.
    return output_path


# This function runs the workflow from start to finish.
def main():
    """Load the data and generate only the monthly two-panel box plot."""
    # Call the loading function and store its returned DataFrame in df.
    df = load_fish_data()

    # Print a quick preview so we can confirm the data loaded correctly.
    print("Loaded fish data:")
    print(df.head())

    # Create the figure produced by this script.
    # Pass df into the plotting function so it can use the loaded data.
    make_monthly_reef_box_plots(df)


# __name__ is "__main__" only when this file is run directly.
# This prevents main() from running automatically if another script imports this file.
if __name__ == "__main__":
    main()
