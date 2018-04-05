function dummy(data) {

// create a data set
    var dataSet = anychart.data.set(data);

// create a line chart using the data set
    var lineChart = anychart.line(dataSet);

// set container id for the chart
    lineChart.container('chartContainer');
    lineChart.title('New York weather');
    lineChart.getSeries(0).name('New York');

// initiate chart drawing
    lineChart.draw();
}
