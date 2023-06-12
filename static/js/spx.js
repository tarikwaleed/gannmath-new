/**
 * Stuff related to SPX
 */
const BASE_URL = 'https://api.gexbot.com/spx';
const url = `${BASE_URL}/all/gex?key=${apiKey}`;
const data = 0;

fetch(url)
  .then((response) => response.json())
  .then((data) => {
    /** Prepare the data */
    const strikes = data.strikes.map((strike) => strike.strike);
    const gexVolData = data.strikes.map((strike) => ({
      value: strike.gex_vol,
      label: 'labelRight',
    }));
    const gexOiData = data.strikes.map((strike) => ({
      value: strike.gex_oi,
      label: 'labelLeft',
    }));
    const zeroGamma = data.zero_gamma;
    const roundedZeroGamma = Math.round(zeroGamma / 5) * 5;
    const spot = data.spot;
    const majorPosVol = data.major_pos_vol;
    const majorPosOi = data.major_pos_oi;
    const majorNegVol = data.major_neg_vol;
    const majorNegOi = data.major_neg_oi;
    const roundedSpot = Math.round(data.spot / 5) * 5;
    const roundedMajorPosVol = Math.round(data.major_pos_vol / 5) * 5;
    const roundedMajorPosOi = Math.round(data.major_pos_oi / 5) * 5;
    const roundedMajorNegVol = Math.round(data.major_neg_vol / 5) * 5;
    const roundedMajorNegOi = Math.round(data.major_neg_oi / 5) * 5;

    /** */

    var dom = document.getElementById('chart-container');
    var myChart = echarts.init(dom, null, {
      renderer: 'canvas',
      useDirtyRect: false,
    });
    var app = {};
    var option;
    const labelLeft = {
      position: 'left',
    };
    const labelRight = {
      position: 'right',
    };

    option = {
      title: {
        textStyle: {
          color: '#ffffff',
        },
        left: 'center',
        top: 'middle',
      },
      tooltip: {
        trigger: 'axis',
        axisPointer: {
          type: 'shadow',
        },
      },
      grid: {
        top: 80,
        bottom: 30,
        left: 350,
      },
      xAxis: {
        type: 'value',
        position: 'bottom',
        splitLine: { show: false },
      },
      yAxis: {
        type: 'category',
        axisLine: {
          show: true,
        },
        axisLabel: {
          show: true,
        },
        axisTick: {
          show: true,
        },
        splitLine: {
          show: false,
        },
        minorTick: { show: false },
        label: {
          show: true,
          align: 'center',
        },
        onZero: true,
        onZeroAxisIndex: 1,
        data: strikes,
      },
      series: [
        {
          name: 'GEX By Vol',
          type: 'bar',

          markLine: {
            data: [
              {
                name: 'Spot',
                xAxis: 0,
                yAxis: roundedSpot.toString(),
                lineStyle: {
                  color: 'yello',
                  type: 'dashed',
                },
                symbol: 'circle',
                symbolSize: 10,
                label: {
                  show: true,
                  formatter: `Spot \n${spot}`,
                  backgroundColor: 'rgba(255, 255, 0, 0.7)',
                  color: '#fff',
                  padding: [5, 10],
                },
              },
              {
                name: 'Zero Gamma',
                xAxis: 0,
                yAxis: roundedZeroGamma.toString(),
                lineStyle: {
                  color: 'orange',
                  type: 'dashed',
                },
                symbol: 'circle',
                symbolSize: 10,
                label: {
                  show: true,
                  formatter: `Zero Gamma \n${zeroGamma}`,
                  backgroundColor: 'rgba(255, 165, 0, 0.7)',
                  color: '#fff',
                  padding: [5, 10],
                },
              },

              {
                name: 'MajorPosVol',
                xAxis: 0,
                yAxis: roundedMajorPosVol.toString(),
                lineStyle: {
                  color: 'green',
                  type: 'dashed',
                },
                symbol: 'circle',
                symbolSize: 10,
                label: {
                  show: true,
                  formatter: `Major Posiive Volume \n${majorPosVol}`,
                  backgroundColor: 'rgba(0, 128, 0, 0.7)',
                  color: '#fff',
                  padding: [5, 10],
                },
              },
              {
                name: 'MajorPosOi',
                xAxis: 0,
                yAxis: roundedMajorPosOi.toString(),
                lineStyle: {
                  color: 'red',
                  type: 'dashed',
                },
                symbol: 'circle',
                symbolSize: 10,
                label: {
                  show: true,
                  formatter: `Major Positive Oi \n${majorPosOi}`,
                  backgroundColor: 'rgba(255, 0, 0, 0.7)',
                  color: '#fff',
                  padding: [5, 10],
                },
              },
              {
                name: 'MajorNegVol',
                xAxis: 0,
                yAxis: roundedMajorNegVol.toString(),
                lineStyle: {
                  color: 'blue',
                  type: 'dashed',
                },
                symbol: 'circle',
                symbolSize: 10,
                label: {
                  show: true,
                  formatter: `Major Negative Vol \n${majorNegVol}`,
                  backgroundColor: 'rgba(0, 0, 0, 0.7)',
                  color: '#fff',
                  padding: [5, 10],
                },
              },
              {
                name: 'MajorNegOi',
                xAxis: 0,
                yAxis: roundedMajorNegOi.toString(),
                lineStyle: {
                  color: 'purple',
                  type: 'dashed',
                },
                symbol: 'circle',
                symbolSize: 10,
                label: {
                  show: true,
                  formatter: `Major Negative Oi \n${majorNegOi}`,
                  backgroundColor: 'rgba(128, 0, 128, 0.7)',
                  color: '#fff',
                  padding: [5, 10],
                },
              },
            ],
          },

          label: {
            show: false,
            position: function (params) {
              return params.value >= 0 ? labelRight : labelLeft;
            },
            align: 'center',
          },
          itemStyle: {
            normal: {
              barBorderRadius: 10,
              color: function (params) {
                var colorList = ['#8ef6e4', '#9896f1', '#F198C1'];
                return colorList[params.dataIndex % 3];
              },
            },
            emphasis: {
              barBorderRadius: 10,
            },
          },
          barWidth: 8,
          barCategoryGap: '0%',
          data: gexVolData,
        },

        {
          name: 'GEX By OI',
          type: 'bar',

          label: {
            show: false,
            position: function (params) {
              return params.value >= 0 ? labelRight : labelLeft;
            },
            align: 'center',
          },
          itemStyle: {
            normal: {
              barBorderRadius: 10,
              color: function (params) {
                var colorList = ['#8ef6e4', '#F198C1', '#9896f1'];
                return colorList[params.dataIndex % 3];
              },
            },
            emphasis: {
              barBorderRadius: 10,
            },
          },
          barWidth: 8,
          barCategoryGap: '0%',
          data: gexOiData,
        },
      ],
    };

    if (option && typeof option === 'object') {
      myChart.setOption(option);
    }

    window.addEventListener('resize', myChart.resize);
  })
  .catch((error) => {
    // Handle any errors
    console.error(error);
  });

/**
 * Stuff related to echarts
 */
