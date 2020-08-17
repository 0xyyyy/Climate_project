
// ######  code block for SVG animation  ######
const logo = document.querySelectorAll('#logo path')

for (let i = 0; i < logo.length; i++)
  console.log(`Letter ${i} is & ${logo[i].getTotalLength()}`)
// #####  end SVG code  ######



    // D3 code block
    var url = {
        greenhouseGas_url: "http://127.0.0.1:5000/api/v1.0/greenhouseGas",
        bp_url: "http://127.0.0.1:5000/api/v1.0/bpdata",
        oil_url: "http://127.0.0.1:5000/api/v1.0/tempOil"
    }

        const greenhouseGas_df = d3.json(url.greenhouseGas_url).then(data=> console.log(data))

        const bp_df = d3.json(url.bp_url).then(data=> console.log(data))

        // svg container 
        var height = 600;
        var width = 1000;


        // margins 
        var margins = {
            top: 50, 
            right: 50, 
            bottom: 50, 
            left: 80
        }

        // chart area minus margins 
        var chartHeight = height - margins.top - margins.bottom;
        var chartWidth = width - margins.left - margins.right;

        //create svg container 
        var svg = d3.select("#scatter").append("svg")
            .attr("height", height)
            .attr("width", width);

        var chartGroup = svg.append('g')
            .attr('transform', `translate(${margins.left}, ${margins.top})`)

        d3.json(url.oil_url).then(function (oilData) {
            oilData.forEach(function (data) {
                data.ID = +data.ID
                data.Avg_Temp = +data.Avg_Temp
                data.Year = +data.Year
                data.Thousand_Barrels_Daily = +data.Thousand_Barrels_Daily
            })
            console.log(oilData)

            var xLinearScale = d3.scaleLinear()
            .domain([10000, d3.max(oilData, d => d.Thousand_Barrels_Daily)])
            .range([0, chartWidth]);

            var yLinearScale = d3.scaleLinear()
            .domain([7.5, d3.max(oilData, d => d.Avg_Temp)])
            .range([chartHeight, 0]);

            var bottomAxis = d3.axisBottom(xLinearScale);
            var leftAxis = d3.axisLeft(yLinearScale);

            chartGroup.append("g")
            .attr("transform", `translate(0, ${chartHeight})`)
            .call(bottomAxis);

            chartGroup.append("g")
            .call(leftAxis);

            var circlesGroup = chartGroup.selectAll("circle")
            .data(oilData)
            .enter()
            .append("circle")
            .attr("cx", d => xLinearScale(d.Thousand_Barrels_Daily))
            .attr("cy", d => yLinearScale(d.Avg_Temp))
            .attr('class', 'circle')
            .attr("r", "14")
            .attr("opacity", "0.7")
            

            var textGroup = chartGroup.selectAll("yearText")
                .data(oilData)
                .enter()
                .append('text')
                .attr('x', d => xLinearScale(d.Thousand_Barrels_Daily))
                .attr('y', d => yLinearScale(d.Avg_Temp))
                .text(d => d.Year)
                .attr('class', 'yearText')
                .attr('font-size', '11px')
                .attr('text-anchor', 'middle')
                .attr("dy", ".3em");
            


                    // // y axis gp ADDED
                    var yLabelsGp = chartGroup
                    .append('g')
                    .attr('transform', `translate(-20, ${chartHeight / 2})`)

                    // // Append yAxis ADDED
                    var tempLabel = yLabelsGp
                    .append('text')
                    .attr('transform', 'rotate(-90)')
                    .attr('y', -45)
                    .attr('x', 0)
                    .attr('dy', '1em')
                    .classed('axis-text', true)
                    .classed('active', true)
                    .text('Average Temperature by Year US')



            
            // chartGroup.append('text')
            //     .attr("transform", `rotate(-90)`)
            //     .attr("y", 0 - margins.left + 20)
            //     .attr("x", 0 - (chartHeight/2))
            //     .attr("dy", "1em")
            //     .attr('class', 'axisText')
            //     .text("Average Temperature by Year US")
            
            chartGroup.append("text")
                .attr('transform', `translate(400, ${chartHeight + 40})`)
                .attr("class", "axisText")
                .classed('active', true)
                .text("Barrels Consumed Daily in Thousands");
        })





// __________________________________________________________________
// d3.json(url.bp_url).then(function (iData) {
//     iData.forEach(function (data) {
//         data.ID = +data.ID
//         data.Year = +data.Year
//         data.pop = +data.pop
//         data.ISO3166_numeric = +data.ISO3166_numeric
//         data.OPEC = +data.OPEC
//         data.EU = +data.EU
//         data.OECD = +data.OECD
//         data.CIS = +data.CIS        
//         data.oilcons_ej = +data.oilcons_ej
//         data.oilcons_kbd = +data.oilcons_kbd
//         data.oilcons_mt = +data.oilcons_mt
//         data.oilcons_mtoe = +data.oilcons_mtoe
//     })
//     console.log(iData)

//     var xLinearScale = xScale(iData, xValue)
//     var yLinearScale = yScale(iData, yValue)

//     var bottomAxis = d3.axisbottom(xLinearScale)
//     var leftAxis = d3.axisleft(yLinearScale)

//     var xAxis = chartgroup.append('g')
//         .classed('y-axis', true)
//         .attr('transform', `translate(0, ${chartHeight})`)
//         .call(bottomAxis)
    
//     var yAxis = chartgroup.append('g')
//         .classed('x-axis', true)
//         .call(leftAxis)
// })

// function xScale (iData, xValue) {
//     var xLinearScale = d3.scaleLinear().domain([
//         d3.min(iData, d=> d[xValue]) * .5, 
//         d3.max(iData, d=> d[xValue]) * 1.0
//         ]).range(0, chartWidth)
//     return xLinearScale
// }

// function yScale (iData, yValue) {
//     var yLinearScale = d3.scaleLinear().domain([
//         d3.min(iData, d=> d[yValue]) * .5,
//         d3.max(iData, d=> d[yValue]) * 1.0
//     ]).range(chartHeight, 0)
//     return yLinearScale
// }

// function updateXAxes (newXScale, xAxis) {
//     var bottomaxis = d3.axisbottom(newXScale)
//     xAxis.transition().duration(1500).call(bottomaxis)
//     return xAxis
// }

// function updateYAxes (newYScale, yAxis) {
//     var leftAxis = d3.axisleft(newYScale)
//     yAxis.transition().duration(1500).call(leftAxis)
//     return yAxis
// }

// function renderCircles (circlesGroup, newXScale, xValue, newYScale, yValue) {
//     circlesGroup
//       .transition()
//       .duration(1500)
//       .attr('cx', d => newXScale(d[xValue]))
//       .attr('cy', d => newYScale(d[yValue]))
//     return circlesGroup
//   }

// function renderText (textGroup, newXScale, xValue, newYScale, yValue) {
// textGroup
//     .transition()
//     .duration(1500)
//     .attr('x', d => newXScale(d[xValue]))
//     .attr('y', d => newYScale(d[yValue]))
//     .attr('text-anchor', 'middle')
// return textGroup
// }

