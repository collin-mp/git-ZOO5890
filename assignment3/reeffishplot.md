## What figure did you set out to make? In words, what do you want this figure to show?
I wanted to create a fairly comprehensive plot (or set of plots) to help visualize species composition according to both spatial differentiation between reefs and temporal changes between the two months. I also wanted to implement data from transects within each reef to refine representation of overall composition in the reefs.

## How easy or hard was it to actually make this figure? What went smoothly, what didn’t. How were you able to solve any difficulties?
It took some time to understand and refine what certain aspects (e.g. panels, grouped x-axis items) were displaying based on my limited familiarity with matplotlib. Most refining to work towards my target involved discrete and clear language about what certain things should portray. For example, the agent struggled at first to group like species together by reef until I was very explicit about positioning and categorization.

## How much do you feel like you understand the code used to generate the figure?
I feel like I understand the general flow of the script and am continuing to gain an understanding of individual commands and arguments for data grouping and constructing the plots. The general python structure of grouping together functions and executing at once took me by surprise, but the exercise in general helped my familiarity with the structure.

## Was anything particularly useful for better understanding the code that was generated?
I had the agent include detailed information about each line to help understand what individual commands and unfamiliar arguments (such as \n) are doing, both for the purposes of this script and for future understanding. The comments are a little dense with this structure, however, and I want to continue exploring how I can learn from detailed comments while not interrupting my ability to read the code itself.

## What steps did you use to try and verify for yourself that the figure you created is correctly showing what you want it to?
I relied primarily on visual comparison with the raw csv to verify that ranges portrayed by the boxplots are accurate to the data recorded. Independently from this code, I also asked the agent to report summary statistics to verify that they aligned with the range and medians shown on the plots.