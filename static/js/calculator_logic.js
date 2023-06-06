$(document).ready(function () {
  $('#slider-value').text($('#slider-ticks option:selected').text());
  // var calculateBtn = $('#calculate-btn');
  // calculateBtn.on('click', calculate);
  $('#slider').on('input', function () {
    var selectedOption = $('#slider-ticks option[value="' + this.value + '"]');
    $('#slider-value').text(selectedOption.text());
  });
  $('#slider-value').text($('#slider-ticks option:selected').text());
  var selectedValue = $('#slider-ticks option:selected').val();
  $('#slider').val(selectedValue);
  // $('#result-table tbody').empty();
  // for (var i = 0; i < results.length; i++) {
  //   $('#result-table tbody').append('<td>' + results[i] + '</td>');
  // }
});

function calculate() {
  var x = parseInt(document.getElementById('x-input').value);
  var y = parseInt(document.getElementById('y-input').value);
  var z = parseFloat(
    document.getElementById('slider-ticks').options[
      document.getElementById('slider').value
    ].text,
  );
  var w = x * z;
  var r = y * z;
  var e = Math.abs(Math.pow(w, 0.5) - Math.pow(r, 0.5)) / 0.005555;
  var a;
  if (43 <= e && e < 58) {
    a = 45;
  } else if (58 <= e && e < 70) {
    a = 60;
  } else if (70 <= e && e < 88) {
    a = 72;
  } else if (88 <= e && e < 106) {
    a = 90;
  } else if (106 <= e && e < 118) {
    a = 108;
  } else if (118 <= e && e < 126.57) {
    a = 120;
  } else if (126.57 <= e && e < 133) {
    a = 128.57;
  } else if (133 <= e && e < 138) {
    a = 135;
  } else if (138 <= e && e < 142) {
    a = 140;
  } else if (142 <= e && e < 145.27) {
    a = 144;
  } else if (145.27 <= e && e < 148) {
    a = 147.27;
  } else if (148 <= e && e < 151.31) {
    a = 150;
  } else if (151.31 <= e && e < 153.29) {
    a = 152.31;
  } else if (153.29 <= e && e < 155) {
    a = 154.29;
  } else if (155 <= e && e < 157.5) {
    a = 156;
  } else if (157.5 <= e && e < 158.2) {
    a = 157.5;
  } else if (158.2 <= e && e < 160) {
    a = 158.82;
  } else if (160 <= e && e < 161.06) {
    a = 160;
  } else if (161.06 <= e && e < 162) {
    a = 161.05;
  } else if (162 <= e && e < 178) {
    a = 162;
  } else if (178 <= e && e < 182) {
    a = 180;
  } else {
    a = 1;
  }
  //مستويات فيبوجان
  var levels = [0.25, 0.383, 0.5, 0.618, 0.75, 1];
  //معاملات الزاويه
  var cs = [];
  for (let l of levels) {
    cs.push((a * 4 * l) / 180);
  }
  //القيم
  let results = [];
  for (let c of cs) {
    if (x / y > 1) {
      results.push(Number(Math.pow(Math.sqrt(w) - c, 2) / z).toFixed(5));
    } else {
      results.push(Number(Math.pow(Math.sqrt(w) + c, 2) / z).toFixed(5));
    }
  }
  for (let i = 0; i < results.length; i++) {
    $(`#result-${i}`).text(results[i]);
  }
  let arr = [1, 1.5278, 2, 2.4722, 3, 4];
  for (let i = 0; i < arr.length; i++) {
    $(`#angle-${i}`).text(a * arr[i]);
  }
  console.log(a);
}
