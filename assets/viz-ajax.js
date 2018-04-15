// initialize globals

// just opening index.html with viz-ajax.js will give cross origin error due to security issues
// Run the following command to open a server
// python -m SimpleHTTPServer 8080

// ` ` string templating
// var x = 5;
// var m = `${x} feet`; // 5 feet

// Lecture length (y-axis) vs size of lecture (x-axis)
d3.json("assets/data.json", function(error, data) {
	if (error) return;
	console.log(data);
	makeVis(data);
});

var makeVis = function(data) {
	var margin = { top: 20, right: 20, bottom: 30, left: 40 },
			width = 960 - margin.left - margin.right,
			height = 500 - margin.top - margin.bottom;

	var canvas = d3.select('#vis-container').append('svg')
		.attr('width', width + margin.left + margin.right)
		.attr('height', height + margin.top + margin.bottom)
		.append('g')
		.attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');

	// Define scales
	//var colorScale = d3.scale.category10();
	var xScale = d3.scale.linear()
		.domain([0, 500]) // TODO: set a better bound through the max function
		.range([0, width])
	var yScale = d3.scale.linear()
		.domain([0, 600]) // TODO: set a better bound through the max function
		.range([height, 0]); // y-axis is upper left downwards

	// Define axes
	var xAxis = d3.svg.axis()
		.scale(xScale)
		.orient('bottom');
	var yAxis = d3.svg.axis()
		.scale(yScale)
		.orient('left');

	// Add x-axis to canvas
	canvas.append('g')
		.attr('class', 'x axis')
		// move axis to bottom of canvas
		.attr('transform', 'translate(0,' + height + ')')
		.call(xAxis)
		.append('text')
		.attr('class', 'label')
		.attr('x', width) // x-offset from xAxis
		.attr('y', -6) // y-offset from xAxis
		.style('text-anchor', 'end') // right-justify
		.text('Lecture Size');

	// Add y-axis to canvas
	canvas.append('g')
		.attr('class', 'y axis')
		.call(yAxis)
		.append('text')
		.attr('class', 'label')
		.attr('transform', 'rotate(-90)') // rotate text
		.attr('y', 15) // y-offset from yAxis
		.style('text-anchor', 'end')
		.text('Lecture Length');

	// Add tooltip to vis-container, visible on mouseover
	var tooltip = d3.select('#vis-container').append('div')
		.attr('class', 'tooltip')
		.style('opacity', 0);

	// Tooltip mouseover event handler
	var tipMouseover = function(d) {
		var html = "hello";
		tooltip.html(html)
			.style('left', (d3.event.pageX + 15) + 'px')
			.style('top', (d3.event.pageY - 28) + 'px')
			.transition()
			.duration(200) // 200ms
			.style('opacity', 0.9)
	};

	// Tooltip mouseout event handler
	var tipMouseover = function(d) {
		tooltip.transition()
			.duration(300)
			.style('opacity', 0);
	};

	// Add data points
	canvas.selectAll('dot')
		.data(data)
		.enter().append('circle')
		.attr('class', 'dot')
		.attr('r', 5.5); // radius size
}
