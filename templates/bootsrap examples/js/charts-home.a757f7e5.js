"use strict";

document.addEventListener("DOMContentLoaded", function () {
    // ------------------------------------------------------- //
    // Line Chart
    // ------------------------------------------------------ //

    var lineChart1 = new Chart(document.getElementById("lineChart1"), {
        type: "line",
        options: {
            tooltips: {
                mode: "index",
                intersect: false,
                callbacks: {
                    label: function (tooltipItems, data) {
                        return "$" + tooltipItems.yLabel.toString();
                    },
                },
            },
            hover: {
                mode: "nearest",
                intersect: true,
            },
            scales: {
                xAxes: [
                    {
                        gridLines: {
                            display: false,
                            drawBorder: false,
                        },
                    },
                ],
                yAxes: [
                    {
                        ticks: {
                            max: 30,
                            min: 0,
                        },
                        gridLines: {
                            display: false,
                            drawBorder: false,
                        },
                    },
                ],
            },

            legend: {
                display: false,
            },
        },
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [
                {
                    label: "Your Account Balance",
                    fill: true,
                    lineTension: 0.4,
                    backgroundColor: "transparent",
                    borderColor: window.colors.blue,
                    pointBorderColor: window.colors.blue,
                    pointHoverBackgroundColor: window.colors.blue,
                    borderCapStyle: "butt",
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: "miter",
                    borderWidth: 3,
                    pointBackgroundColor: "blue",
                    pointBorderWidth: 5,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 1,
                    pointRadius: 0,
                    pointHitRadius: 1,
                    data: [20, 14, 21, 15, 22, 8, 18],
                    spanGaps: false,
                },
            ],
        },
    });

    // ------------------------------------------------------- //
    // Line Chart
    // ------------------------------------------------------ //

    var lineChart2 = new Chart(document.getElementById("lineChart2"), {
        type: "line",
        options: {
            tooltips: {
                mode: "index",
                intersect: false,
            },
            scales: {
                xAxes: [
                    {
                        gridLines: {
                            display: false,
                            drawBorder: false,
                        },
                        ticks: {
                            fontColor: "#adb5bd",
                        },
                    },
                ],
                yAxes: [
                    {
                        ticks: {
                            max: 30,
                            min: 0,
                        },
                        gridLines: {
                            display: false,
                            drawBorder: false,
                        },
                    },
                ],
            },
            legend: {
                display: false,
            },
        },
        data: {
            labels: ["January", "February", "March", "April", "May", "June", "July"],
            datasets: [
                {
                    label: "Referrals",
                    fill: true,
                    lineTension: 0.4,
                    backgroundColor: "transparent",
                    borderColor: window.colors.primary,
                    pointBorderColor: window.colors.primary,
                    pointHoverBackgroundColor: window.colors.primary,
                    borderCapStyle: "butt",
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: "miter",
                    borderWidth: 3,
                    pointBackgroundColor: window.colors.primary,
                    pointBorderWidth: 5,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: window.colors.primary,
                    pointHoverBorderWidth: 1,
                    pointRadius: 0,
                    pointHitRadius: 1,
                    data: [13, 21, 13, 17, 13, 20, 15],
                    spanGaps: false,
                },
            ],
        },
    });

    // ------------------------------------------------------- //
    // Line Chart 3
    // ------------------------------------------------------ //

    var lineChart3 = new Chart(document.getElementById("lineChart3"), {
        type: "line",
        options: {
            scales: {
                xAxes: [
                    {
                        display: false,
                    },
                ],
                yAxes: [
                    {
                        ticks: {
                            max: 30,
                            min: 0,
                        },
                        display: false,
                    },
                ],
            },
            legend: {
                display: false,
            },
            tooltips: {
                mode: "index",
                intersect: false,
            },
        },
        data: {
            labels: [
                "Jun 1",
                "Jun 2",
                "Jun 3",
                "Jun 4",
                "Jun 5",
                "Jun 6",
                "Jun 7",
                "Jun 8",
                "Jun 9",
                "Jun 10",
                "Jun 11",
                "Jun 12",
                "Jun 13",
                "Jun 14",
            ],
            datasets: [
                {
                    label: "Profile Visitors",
                    fill: true,
                    lineTension: 0.4,
                    backgroundColor: "transparent",
                    borderColor: window.colors.red,
                    pointBorderColor: window.colors.red,
                    pointHoverBackgroundColor: window.colors.red,
                    borderCapStyle: "butt",
                    borderDash: [],
                    borderDashOffset: 0.0,
                    borderJoinStyle: "miter",
                    borderWidth: 3,
                    pointBackgroundColor: "#fff",
                    pointBorderWidth: 5,
                    pointHoverRadius: 5,
                    pointHoverBorderColor: "#fff",
                    pointHoverBorderWidth: 1,
                    pointRadius: 0,
                    pointHitRadius: 1,
                    data: [20, 14, 21, 15, 22, 8, 18, 13, 21, 13, 17, 13, 20, 15],
                    spanGaps: false,
                },
            ],
        },
    });

    // ------------------------------------------------------- //
    // Pie Chart
    // ------------------------------------------------------ //

    var pieChartHome1 = new Chart(document.getElementById("pieChartHome1"), {
        type: "doughnut",
        options: {
            cutoutPercentage: 90,
            legend: {
                display: false,
            },
        },
        data: {
            labels: ["Hours Worked", "Hours Remaining"],
            datasets: [
                {
                    data: [250, 200],
                    borderWidth: [0, 0],
                    backgroundColor: [window.colors.green, "#eee"],
                    hoverBackgroundColor: [window.colors.green, "#eee"],
                },
            ],
        },
    });

    // ------------------------------------------------------- //
    // Pie Chart
    // ------------------------------------------------------ //

    var pieChartHome2 = new Chart(document.getElementById("pieChartHome2"), {
        type: "doughnut",
        options: {
            cutoutPercentage: 90,
            legend: {
                display: false,
            },
        },
        data: {
            labels: ["Completed", "Remaining"],
            datasets: [
                {
                    data: [300, 50],
                    borderWidth: [0, 0],
                    backgroundColor: [window.colors.indigo, "#eee"],
                    hoverBackgroundColor: [window.colors.indigo, "#eee"],
                },
            ],
        },
    });

    // ------------------------------------------------------- //
    // Pie Chart
    // ------------------------------------------------------ //

    var pieChartHome3 = new Chart(document.getElementById("pieChartHome3"), {
        type: "doughnut",
        options: {
            cutoutPercentage: 90,
            legend: {
                display: false,
            },
        },
        data: {
            labels: ["Credit Used", "Remaining"],
            datasets: [
                {
                    data: [300, 50],
                    borderWidth: [0, 0],
                    backgroundColor: [window.colors.pink, "#eee"],
                    hoverBackgroundColor: [window.colors.pink, "#eee"],
                },
            ],
        },
    });

    // ------------------------------------------------------- //
    // Pie Chart
    // ------------------------------------------------------ //

    var pieChartHome4 = new Chart(document.getElementById("pieChartHome4"), {
        type: "doughnut",
        options: {
            cutoutPercentage: 90,
            legend: {
                display: false,
            },
        },
        data: {
            labels: ["First", "Second"],
            datasets: [
                {
                    data: [200, 80],
                    borderWidth: [0, 0],
                    backgroundColor: [window.colors.green, "#eee"],
                    hoverBackgroundColor: [window.colors.green, "#eee"],
                },
            ],
        },
    });
});
