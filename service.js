let x = 4000; // this is input field from html
let y = 4008; // this is input field from html
let z = 100; // this is input field from html
let w = x * z;
let r = y * z;
let e = Math.abs((Math.sqrt(w) - Math.sqrt(r)) / 0.005555);
while (!(43 <= e && e < 180)) {
  z = parseInt(prompt());
  w = x * z;
  r = y * z;
  e = Math.abs((Math.sqrt(w) - Math.sqrt(r)) / 0.005555);
}

let a = null;
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

let levels = [.25, .383, .5, .618, .75, 1];
let cs = [];
for (let l of levels) {
  cs.push((a * 4 * l) / 180);
}

let results = [];
for (let c of cs) {
  if (x / y > 1) {
    results.push(Number(Math.pow(Math.sqrt(w) - c, 2) / z).toFixed(5));
  } else {
    results.push(Number(Math.pow(Math.sqrt(w) + c, 2) / z).toFixed(5));
  }
}
