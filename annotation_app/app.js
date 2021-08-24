


var canvas = new fabric.Canvas("canvas");

var rects = [];

var csv = []
var currentImg = " "
// har aks chand rect dare 
// har csv file chand ta aks 
// har rect bayad dakhele aks marbot be khodesh bashe 
/*
{
csv[{image 1  , bounds : [{label, xmin , ymin , xmax , ymax },{},{}] } , {image 2  , bounds : []} , {image 3 , bounds : []}]
}
*/
loadImageFromUrl("horse.jpg");
// addNewRectToCanvas("red");
getCoordiantes();
onAddClicked();
onCsvExport();
oncsvImport();

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
    dirty: true
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

function addLoadedRectToCanvas(color, rectName,xmin,ymin,xmax,ymax) {
  console.log("xmin",xmin , "ymin",ymin,"xmax",xmax , "ymax" , ymax)
  var rawWidth = Math.trunc( xmax - xmin )
  var rawheight = Math.trunc( ymax - ymin )
  var width = isEven(rawWidth) ? rawWidth : rawWidth + 1 
  var height = isEven(rawheight) ? rawheight : rawheight + 1 

 
//width and height should be even
  var rect = new fabric.Rect({
    top:  ymin,
    left: xmin,
    width: width,
    height:height,
    fill: "transparent",
    strokeWidth: 10,
    stroke: color,
    lockRotation: true,
  });
 
// console.log(rect.x)

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

      // editTableData(object.name, object.aCoords);
    }
  });
}
function onAddClicked() {
  document.getElementById("addrect").addEventListener("click", function () {
    // TODO : we should get input label from here
    var rectName = document.getElementById("rectname").value.trim();
    // TODO : we should get color for
   var color  =  document.getElementById("colorpalette").value
   console.log(color)
    if (rectName === "") {
      alert("label should not be empty ! ! ! ");
      return;
    }
    addNewRectToCanvas(color, rectName);
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


function previewImages() {

  
  
  if (this.files) {
    [].forEach.call(this.files, readAndPreview);
  }
  
  function readAndPreview(file) {
  
  
    if (!/\.(jpe?g|png|gif)$/i.test(file.name)) {
      return 
    } // else...
    
    var reader = new FileReader();
    
    reader.addEventListener("load", function() {
     console.log(file.name, this.result)
     var li = document.createElement("li");
             li.innerHTML = file.name;
             li.onclick =  onfilenameClicked
             li.id= this.result
             document.getElementById("filenames").appendChild(li)
             loadImageFromUrl(this.result);
     
    });
    
    reader.readAsDataURL(file);
    
  }
  
  }
  
  document.querySelector('#files').addEventListener("change", previewImages);


function onfilenameClicked(event){
 loadImageFromUrl(event.target.id)
 var filenames = document.getElementById("filenames")

 loadRectFromCSV(event.target.textContent)

 filenames.childNodes.forEach(function(item){
  item.style = "color: black;"
 })
 event.target.style.color = "#69FF00"

}
function onCsvExport(){
 var downloadBtn = document.getElementById("downloadcsv")
 downloadBtn.addEventListener("click",function(){

var excelRows  = []
var table = document.getElementById("t01")
var tableRows = table.rows
for (var i = 0; i < tableRows.length; i++) {
  var rectInfoTr = tableRows[i];
  var label = rectInfoTr.cells[0].innerHTML;
  var xmin = rectInfoTr.cells[1].innerHTML;
  var ymin = rectInfoTr.cells[2].innerHTML;
  var xmax = rectInfoTr.cells[3].innerHTML;
  var ymax = rectInfoTr.cells[4].innerHTML;
excelRows.push([label,xmin,ymin,xmax,ymax])   

}
console.log(excelRows)
let csvContent = "data:text/csv;charset=utf-8,";

excelRows.forEach(function(rowArray) {
    let row = rowArray.join(",");
    csvContent += row + "\r\n";
});

var encodedUri = encodeURI(csvContent);
window.open(encodedUri);

 })
}


function csvToArray(str, delimiter = ",") {
  // slice from start of text to the first \n index
  // use split to create an array from string by delimiter
  const headers = str.slice(0, str.indexOf("\n")).split(delimiter);
  const cleanHeaders =  headers.map(function(item){
   return item.replace(/[^\w\s]/gi, '')
  })
  // slice from \n index + 1 to the end of the text
  // use split to create an array of each csv value row
  const rows = str.slice(str.indexOf("\n") + 1).split("\n");
 
  // Map the rows
  // split values from each row into an array
  // use headers.reduce to create an object
  // object properties derived from headers:values
  // the object passed as an element of the array
  const arr = rows.map(function (row,index) {
    
    const values = row.replace(/[\"]/g, '').split(delimiter)
    const el = cleanHeaders.reduce(function (object, header, index) 
    {   
      object[header] = values[index];
      return object;
    }, {});
    return el;
  });

  // return the array
  return arr;
}

// function makeListFromImages() {}
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
function oncsvImport(){

 
    var fileInput = document.getElementById("files").addEventListener('change', function(event){
      if(event.target.files[0].type.match("csv")){
        var reader = new FileReader();
        reader.onload = function (event) {
            // alert(reader.result)
            
           
          var importedCSV = csvToArray(reader.result)
           
            csv = importedCSV
            console.log(csv)
           
       
        };
        var fileInput = document.getElementById("files")
        // start reading the file. When it is done, calls the onload event defined above.
        reader.readAsText(fileInput.files[0]);
      }
      
      
    });
   
}

function loadRectFromCSV(imgName){
  
var rects = csv.filter(function(row){
  return row.image == imgName.trim()
})
console.log(imgName)
console.log(csv)
console.log(rects)
rects.forEach(function(item){

  // addLoadedRectToCanvas("red",item.label,item.xmin,item.ymin,item.xmax,item.ymax)
  // this will only return number part of value 
  var  x = Math.trunc( item.xmin )
  var  y = Math.trunc( item.ymin )
addLoadedRectToCanvas("red",item.label,x,y,item.xmax,item.ymax)

  // console.log(`Xmin ${item.xmin} Ymin ${item.ymin} Xmax ${item.xmax} YMax ${item.ymax}`)
})



canvas.requestRenderAll()
canvas.renderAll()
}

function isEven(value) {
    return !(value % 2)
}
//isue number 1 when we load canvas stuck on cursor and some object are negative x or y
// isue number 2 the position is not accurate 