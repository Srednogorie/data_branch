function single_line_econ(data) {

    let dataTable = anychart.data.table('period');

    // Adds data.
    dataTable.addData(data);
    let mapping = dataTable.mapAs({x: 'period', value: 'value'});

    let chart = anychart.stock();

    let plot = chart.plot();


    //COLOR SCHEMA AND VISUAL SETTINGS
    // adjust chart background fill
    let background = chart.background();
    background.fill("rgb(195, 215, 227)");

    // Y axis
    let yAxis = plot.yAxis();
    yAxis.stroke(null);
    yAxis.ticks(true);
    let yLabels = plot.yAxis().labels();
    yLabels.fontColor("rgb(8, 63, 90)");

    // X Axis
    let xLabels = plot.xAxis().labels();
    xLabels.fontColor("rgb(8, 63, 90)");

    //Scroller
    chart.scroller().xAxis(false);
    chart.scroller().fill("rgb(195, 215, 227)");
    chart.scroller().selectedFill("rgb(230, 0, 25)");
    chart.scroller().height(1);
    chart.scroller().thumbs(true);
    //chart.scroller().orientation("right");
    //chart.scroller().outlineStroke("rgb(230, 0, 25)");

    // disable or enable major grid; minor grid available
    let grid = plot.grid();
    grid.enabled(true);
    grid.stroke("1 White");

    // Name the series mainlly because of the tooltip
    let series = plot.line(mapping);
    series.name("Index");
    series.stroke("2 rgb(8, 63, 90)");

    //chart.title("Australia AIG Construction PMI");

    // disable or enable tooltip
    let tooltip = chart.tooltip();
    tooltip.enabled(true);

    //Legent
    plot.legend(false);

    chart.container("chartContainer");
    chart.draw();
}




