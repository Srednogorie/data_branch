function d3_multiline(SomeData) {
    let dataset = [
        // {period: "2009-09-01", manufacturing: null, services: "52.00", construction: null},
        // {period: "2009-10-01", manufacturing: "54.80", services: "51.70", construction: null},
        // {period: "2009-11-01", manufacturing: "52.50", services: "51.20", construction: null},
        // {period: "2009-12-01", manufacturing: "50.00", services: "48.50", construction: null},
        {period: "2010-01-01", manufacturing: "47.40", services: "51.00", construction: "57.70"},
        {period: "2010-02-01", manufacturing: "48.30", services: "53.80", construction: "52.80"},
        {period: "2010-03-01", manufacturing: "48.90", services: "50.50", construction: "51.00"},
        {period: "2010-04-01", manufacturing: "52.30", services: "59.80", construction: "55.80"},
        {period: "2010-05-01", manufacturing: "47.50", services: "56.30", construction: "53.20"},
        {period: "2010-06-01", manufacturing: "48.80", services: "52.90", construction: "46.40"},
        {period: "2010-07-01", manufacturing: "46.60", services: "54.40", construction: "43.30"},
        {period: "2010-08-01", manufacturing: "47.50", services: "51.70", construction: "43.20"},
        {period: "2010-09-01", manufacturing: "45.60", services: "47.30", construction: "40.80"},
        {period: "2010-10-01", manufacturing: "50.70", services: "49.40", construction: "44.00"},
        {period: "2010-11-01", manufacturing: "46.20", services: "47.60", construction: "42.20"},
        {period: "2010-12-01", manufacturing: "46.40", services: "46.30", construction: "43.80"},
        {period: "2011-01-01", manufacturing: "45.50", services: "46.70", construction: "40.20"},
        {period: "2011-02-01", manufacturing: "48.70", services: "51.10", construction: "44.60"},
        {period: "2011-03-01", manufacturing: "46.50", services: "47.90", construction: "39.40"},
        {period: "2011-04-01", manufacturing: "51.50", services: "48.40", construction: "37.90"},
        {period: "2011-05-01", manufacturing: "49.90", services: "47.70", construction: "39.60"},
        {period: "2011-06-01", manufacturing: "48.50", services: "52.90", construction: "35.80"},
        {period: "2011-07-01", manufacturing: "48.80", services: "43.40", construction: "36.10"},
        {period: "2011-08-01", manufacturing: "52.10", services: "43.30", construction: "32.10"},
        {period: "2011-09-01", manufacturing: "50.30", services: "42.30", construction: "30.00"},
        {period: "2011-10-01", manufacturing: "48.80", services: "47.40", construction: "34.70"},
        {period: "2011-11-01", manufacturing: "47.70", services: "47.80", construction: "39.60"},
        {period: "2011-12-01", manufacturing: "49.00", services: "50.20", construction: "41.00"},
        {period: "2012-01-01", manufacturing: "51.90", services: "51.60", construction: "39.80"},
        {period: "2012-02-01", manufacturing: "46.70", services: "51.30", construction: "35.60"},
        {period: "2012-03-01", manufacturing: "47.00", services: "49.50", construction: "36.20"}
    ];


    // 2. Use the margin convention practice
    var margin = {top: 200, right: 200, bottom: 200, left: 200}
        , width = window.innerWidth - margin.left - margin.right // Use the window's width
        , height = window.innerHeight - margin.top - margin.bottom; // Use the window's height

// The number of datapoints
    var n = 21;
    var mindate = new Date(2012, 0, 1),
        maxdate = new Date(2012, 0, 31);
// 5. X scale will use the index of our data
    var xScale = d3.scaleLinear()
        .domain([0, n - 1]) // input
        .range([0, width]); // output

// 6. Y scale will use the randomly generate number
    var yScale = d3.scaleLinear()
        .domain([0, 100]) // input
        .range([height, 0]); // output

// 7. d3's line generator
    var line = d3.line()
        .x(function (d, i) {
            return xScale(i);
        }) // set the x values for the line generator
        .y(function (d) {
            return yScale(d.manufacturing);
        }) // set the y values for the line generator
        .curve(d3.curveMonotoneX) // apply smoothing to the line
    // 7. d3's line generator
    var line1 = d3.line()
        .x(function (d, i) {
            return xScale(i);
        }) // set the x values for the line generator
        .y(function (d) {
            return yScale(d.services);
        }) // set the y values for the line generator
        .curve(d3.curveMonotoneX) // apply smoothing to the line
    // 7. d3's line generator
    var line2 = d3.line()
        .x(function (d, i) {
            return xScale(i);
        }) // set the x values for the line generator
        .y(function (d) {
            return yScale(d.construction);
        }) // set the y values for the line generator
        .curve(d3.curveMonotoneX) // apply smoothing to the line

// //8. An array of objects of length N. Each object has key -> value pair, the key being "y" and the value is a random number
//     var dataset = d3.range(n).map(function (d) {
//         return {"y": d3.randomUniform(1)()}
//     })
//     console.log(dataset);

// 1. Add the SVG to the page and employ #2
    var svg = d3.select("#chartContainer").append("svg")
        .attr("width", width + margin.left + margin.right)
        .attr("height", height + margin.top + margin.bottom)
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

// 3. Call the x axis in a group tag
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

// 4. Call the y axis in a group tag
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

// 9. Append the path, bind the data, and call the line generator
    svg.append("path")
        .datum(dataset) // 10. Binds data to the line
        .attr("class", "line") // Assign a class for styling
        .attr("d", line) // 11. Calls the line generator
        .attr("d", line1) // 11. Calls the line generator
        .attr("d", line2); // 11. Calls the line generator

// // 12. Appends a circle for each datapoint
//     svg.selectAll(".dot")
//         .data(dataset)
//         .enter().append("circle") // Uses the enter().append() method
//         .attr("class", "dot") // Assign a class for styling
//         .attr("cx", function (d, i) {
//             return xScale(i)
//         })
//         .attr("cy", function (d) {
//             return yScale(d.y)
//         })
//         .attr("r", 5);

}

