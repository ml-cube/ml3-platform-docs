# Analytics

The Analytics section provides a series of tools and visualizations to help users visualize data, model performance and drift scores over time. It's currently organized into 3 distinct sections, which can be accessed through the tabs at the top of the page: *Timeseries*, *Plots* and *Representation*.

!!! note
    The Analytics section is an old module that is currently being redesigned in a new interface.

## Timeseries

The *Timeseries* section provides a way to visualize different quantities over time. It's organized in *views*. A view is a collection of related timeseries charts. For instance, you could have a view for image metrics, containing image metrics values over time, and another view for the drift scores, containing drift scores of other quantities over time. You can select which view to display through the dropdown at the top left of the page. You can also edit existing views or create new ones by clicking on the buttons next to the view selector.

![Views Selection](../../imgs/analytics/timeseries-views-selection.png)

Data are filtered in a given time range (default is last 2 years), which can be changed through the time range selector at the top right of the page. There is also the option to make charts having a dot on each data point, so that it's easier to understand where data points are located.

The page itself then just contains the timeseries charts for the selected view. Each chart has its own title and usually displays both the raw data and a moving average, to help understand trends over time. You can zoom in a specific region of the chart by dragging and also download charts as svg or png by clicking on the menu at the top right of each chart.

![Timeseries Charts](../../imgs/analytics/timeseries.png)

## Plots

The *Plots* section provides a way to visualize distributions of data through univariate (boxplot, density, histogram) and bivariate (scatter) plots. 

The concept of *views* is also used here, to group related plots together. Notice that views are not shared between the Timeseries and Plots sections, since they contain different types of visualizations. 

There is an additional idea, the *graph configurations*. A configuration is just a time interval, associated with a color. The plots in the displayed view will show data only for the selected configurations, which will basically act as legends for the plot. This structure allows to easily compare distributions of data across different time intervals. Configurations can be created, modified and selected in the dropdown at the top right of the page.

![Plots](../../imgs/analytics/plots.png)

