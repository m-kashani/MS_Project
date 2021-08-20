var canvas = new fabric.Canvas("canvas");
var rects = [];

loadImageFromUrl("horse.jpg");
// addNewRectToCanvas("red");
getCoordiantes();
onAddClicked();

function loadImageFromUrl(url) {
  fabric.Image.fromURL(url, function (img) {
    canvas.setBackgroundImage(img, canvas.renderAll.bind(canvas));
  });
}

function addNewRectToCanvas(color, rectName) {
  var rect = new fabric.Rect({
    top: 0,
    left: 0,
    width: 60,
    height: 70,
    fill: "transparent",
    strokeWidth: 2,
    stroke: color,
    lockRotation: true,
  });
  //test

  rect.toObject = (function (toObject) {
    return function () {
      return fabric.util.object.extend(toObject.call(this), {
        name: this.name,
      });
    };
  })(rect.toObject);

  rect.name = rectName;
  //
  rect.setControlsVisibility({ mtr: false });

  canvas.add(rect);

  addDataToTable(rect, rectName, color);

  rects.push(rect);

  console.log(rects);
}

function getCoordiantes() {
  canvas.on("mouse:up", function (e) {
    //check if user clicked an object
    if (e.target) {
      //clicked on object
      console.log("clicked on object ");
      console.log(e.target);
      //this is the position of rect

      // console.log("all objects",canvas.getObjects())

      var object = canvas.getActiveObject();
      var objectCenter = object.getCenterPoint();
      var translatedPoints = object.get("points");
      //  console.log(object);
      //  console.log(translatedPoints);
      //  console.log("active objects" ,canvas.getActiveObjects());
      console.log(object);

      editTableData(object.name, object.aCoords);
    }
  });
}
function onAddClicked() {
  document.getElementById("addrect").addEventListener("click", function () {
    // TODO : we should get input label from here
    var rectName = document.getElementById("rectname").value.trim();
    // TODO : we should get color for
    if (rectName === "") {
      alert("label should not be empty ! ! ! ");
      return;
    }
    addNewRectToCanvas("red", rectName);
  });
}

function addDataToTable(data, rectName, rectColor) {
  var label = document.createElement("td");
  var Xmin = document.createElement("td");
  var Ymin = document.createElement("td");
  var Xmax = document.createElement("td");
  var Ymax = document.createElement("td");
  var tableRow = document.createElement("tr");
  tableRow.id = rectName;
  label.style.color = rectColor;
  label.innerHTML = rectName;
  Xmin.innerHTML = data.aCoords.tl.x;
  Ymin.innerHTML = data.aCoords.tl.y;
  Xmax.innerHTML = data.aCoords.br.x;
  Ymax.innerHTML = data.aCoords.br.y;

  tableRow.appendChild(label);
  tableRow.appendChild(Xmin);
  tableRow.appendChild(Ymin);
  tableRow.appendChild(Xmax);
  tableRow.appendChild(Ymax);

  document.getElementById("t01").appendChild(tableRow);
}

//we shoud getactive object on mouse down and update the edited objectdata  on mouse up
function editTableData(targetRowId, newaCoords) {
  var tablerow = document.getElementById(targetRowId);
  var tdList = tablerow.childNodes;
  tdList[1].innerHTML = newaCoords.tl.x.toFixed(2);
  tdList[2].innerHTML = newaCoords.tl.y.toFixed(2);
  tdList[3].innerHTML = newaCoords.br.x.toFixed(2);
  tdList[4].innerHTML = newaCoords.br.y.toFixed(2);
}

window.onload = function () {
  //Check File API support
  if (window.File && window.FileList && window.FileReader) {
    var filesInput = document.getElementById("files");
    filesInput.addEventListener("change", function (event) {
      var files = event.target.files; //FileList object

      var filenameTag = document.getElementById("filenames");
      for (var i = 0; i < files.length; i++) {
        var file = files[i];

        console.log(file);
        var li = document.createElement("li");
        li.innerHTML = file.name;

        //Only pics
        if (!file.type.match("image")) continue;

        var picReader = new FileReader();
        picReader.addEventListener("load", function (event) {
          var picFile = event.target;

          console.log(picFile);

          li.id = picFile.result;
          loadImageFromUrl(picFile.result);
        });
        //Read the image
        filenameTag.appendChild(li);
        picReader.readAsDataURL(file);
      }
    });
  } else {
    console.log("Your browser does not support File API");
  }
};

function makeListFromImages() {}
// var rect = new fabric.Rect({
//     top : 100,
//     left : 100,
//     width : 60,
//     height : 70,
//     fill : 'transparent',
//     strokeWidth : 1,
//     stroke : 'black',
//     lockRotation: true,
// });
// we should add tl and br x and ys to table
// where we should update our table ? 1 when we add a new rect and 2. where we edit a new rect
