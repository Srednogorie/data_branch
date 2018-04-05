function highcharts_multiline(datata) {
    console.log(datata);
    // Create the chart

    let firstRecord = datata[0]; // Get the first record for reference!
    let numOfSeries = Object.keys(firstRecord).length - 1; // Return how many series your chart will be!
    let allKeys = Object.keys(firstRecord);  // Get the object keys!
    let periodOrPeriod = allKeys[0];  // Period or period! This is the question.
    let namesOfSeries = allKeys.slice(-numOfSeries); // Series Names only

    let chartSeriesSetting = [];
    for (let i = 0; i < numOfSeries; i++) {
        let seriesObj = {};
        seriesObj.name = _u.capitalize(namesOfSeries[i]);
        seriesObj.data = [];
        chartSeriesSetting.push(seriesObj)
    }

    // function getMinY() {
    //     return datata.reduce((min, p) => p.period < min ? p.period : min, datata[0].period);
    // }
    //
    // function getMaxY() {
    //     return datata.reduce((max, p) => p.period > max ? p.period : max, datata[0].period);
    // }
    //
    // let chartYmin = getMinY();
    // let chartYmax = getMaxY();
    // console.log(chartYmin);
    // console.log(chartYmax);

    let chart;
    chart = new Highcharts.stockChart({
        chart: {
            renderTo: 'chartContainer',
            zoomType: 'x'
        },
        yAxis: {
            type: 'double',
            // endOnTick: false,
            // startOnTick: false
            plotLines: [{
                color: '#C0C0C0',
                width: 5,
                value: 50
            }]
        },
        xAxis: {
            type: 'datetime',
            labels: {
                formatter: function () {
                    return Highcharts.dateFormat('%b %Y', this.value);
                },
                dateTimeLabelFormats: {
                    minute: '%H:%M',
                    hour: '%H:%M',
                    day: '%e. %b',
                    week: '%e. %b',
                    month: '%b \'%y',
                    year: '%Y'
                }
            }
        },
        series: chartSeriesSetting

    });

    let minValueHC = Number.MAX_VALUE;
    let maxValueHC = Number.MIN_VALUE;
    for (let i = 0; i < numOfSeries; ++i) {
        let chartSeries = [];
        datata.forEach(function (element) {
            let p = Date.parse(eval('element.' + periodOrPeriod));
            let v = parseInt(eval('element.' + namesOfSeries[i]));
            if (v < minValueHC) {
                minValueHC = v
            }
            if (v > maxValueHC) {
                maxValueHC = v
            }
            chartSeries.push([p, v]);
        });
        console.log(chartSeries);
        chart.series[i].setData(chartSeries);

        // const maxValue = Math.max(...[].concat(...chartSeries));
        //
        // const minValue = Math.min(...[].concat(...chartSeries));
        // console.log(maxValue);
        // console.log(minValue);

    }
    console.log(minValueHC);
    console.log(maxValueHC);
    //chart.yAxis[0].setExtremes((minValueHC - minValueHC * 0.1), (maxValueHC + maxValueHC * 0.1));
}
