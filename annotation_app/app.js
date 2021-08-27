

var canvas = new fabric.Canvas("canvas");
var csv = []
var currentImg = " "

getCoordiantes();
onAddClicked();
onCsvExport();
oncsvImport();
onDeleteObject();

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


  rect.toObject = (function (toObject) {
    return function () {
      return fabric.util.object.extend(toObject.call(this), {
        name: this.name,
      });
    };
  })(rect.toObject);
  var newId = generateID()
  rect.name = newId;
  console.log(rect.aCoords , "this is width")
  //
  rect.setControlsVisibility({ mtr: false });

  canvas.add(rect);

  addDataToTable(rect, rectName, color, newId);
  addNewRecordToCsv({
    image : currentImg,
    label : rectName,
    xmin  : 0,
    ymin  : 0,
    xmax  : 0, 
    xmax  : 0, 
    id:newId
  })

}

function addLoadedRectToCanvas(color, rectName,xmin,ymin,xmax,ymax,id) {
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
 


  rect.toObject = (function (toObject) {
    return function () {
      return fabric.util.object.extend(toObject.call(this), {
        name: this.name,
      });
    };
  })(rect.toObject);

  rect.name = id;
  //
  rect.setControlsVisibility({ mtr: false });

  canvas.add(rect);

  addDataToTable(rect, rectName, color, id );


}


function getCoordiantes() {
  canvas.on("mouse:up", function (e) {
    //check if user clicked an object
    if (e.target) {
      //clicked on object
      console.log("clicked on object ");
      console.log(e.target);
      var object = canvas.getActiveObject();
      console.log(object);

      // here we should update our data with changed data 
      // to Table and csv Array 
      editRecordToCsv(object.name,object.aCoords)
      editTableData(object.name, object.aCoords);
    }
  });
}
function onAddClicked() {
  document.getElementById("addrect").addEventListener("click", function () {
    //  get input label from here
    var rectName = document.getElementById("rectname").value.trim();
    //  get color 
   var color  =  document.getElementById("colorpalette").value
    if (rectName === "") {
      alert("label should not be empty ! ! ! ");
      return;
    }
    addNewRectToCanvas(color, rectName);
  });
}

function addDataToTable(data, rectName, rectColor,rectID) {
  var label = document.createElement("td");
  var Xmin = document.createElement("td");
  var Ymin = document.createElement("td");
  var Xmax = document.createElement("td");
  var Ymax = document.createElement("td");
  var tableRow = document.createElement("tr");

  tableRow.id = rectID;
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
     console.log("this is the result of reading  a file  : " + file.name +" " +this.result)
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
 //remove all exisiting object in canvas 
 canvas.remove(...canvas.getObjects());
//remove all exisiting data in table  (but we keep the table header)
 var table = document.getElementById("t01").innerHTML = 
 `
 <tr>
 <th>label</th>
 <th>Xmin</th>
 <th>Ymin</th>
 <th>Xmax</th>
 <th>Ymax</th>
</tr>

 `



 loadRectFromCSV(event.target.textContent)
 
 currentImg=event.target.textContent

 filenames.childNodes.forEach(function(item){
  item.style = "color: black;"
 })
 event.target.style.color = "#69FF00"

}
function onCsvExport(){
 var downloadBtn = document.getElementById("downloadcsv")
 downloadBtn.addEventListener("click",function(){
   console.log(csvCleaning())
  
 
  exportToCsv("abc.csv", csvCleaning())
 
 
 })

}
function csvCleaning(){
  // this function turn array object to array array 
  // array of object  => array of array 
  var cleanedCsv = []
   csv.map(function(item){
     if(item.label){
      cleanedCsv.push([item.image, item.label,item.xmin,item.ymin,item.xmax,item.ymax])
     }
  
  })
  cleanedCsv.unshift(['image',"label","xmin","ymin","xmax","ymax"])

console.log(cleanedCsv)
  return cleanedCsv

}
function exportToCsv(filename, rows) {
  var processRow = function (row) {
      var finalVal = '';
      for (var j = 0; j < row.length; j++) {
       
       
          var innerValue = row[j] === null ? '' : row[j].toString();
          if (row[j] instanceof Date) {
              innerValue = row[j].toLocaleString();
          };
          var result = innerValue.replace(/"/g, '""');
          if (result.search(/("|,|\n)/g) >= 0)
              result = '"' + result + '"';
          if (j > 0)
              finalVal += ',';
          finalVal += result;
      }
      return finalVal + '\n';
  };

  var csvFile = '';
  for (var i = 0; i < rows.length; i++) {
      csvFile += processRow(rows[i]);
  }

  var blob = new Blob([csvFile], { type: 'text/csv;charset=utf-8;' });
  if (navigator.msSaveBlob) { // IE 10+
      navigator.msSaveBlob(blob, filename);
  } else {
      var link = document.createElement("a");
      if (link.download !== undefined) { // feature detection
          // Browsers that support HTML5 download attribute
          var url = URL.createObjectURL(blob);
          link.setAttribute("href", url);
          link.setAttribute("download", filename);
          link.style.visibility = 'hidden';
          document.body.appendChild(link);
          link.click();
          document.body.removeChild(link);
      }
  }
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

function oncsvImport(){

 
    var fileInput = document.getElementById("files").addEventListener('change', function(event){
      if(event.target.files[0].type.match("csv")){
        var reader = new FileReader();
        reader.onload = function (event) {
            // alert(reader.result)
            
          
          var importedCSV = csvToArray(reader.result)
          
            
            csv = attachId(importedCSV)
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
console.log("image",imgName)
console.log("loaded CSV",csv)
console.log(rects)
rects.forEach(function(item){

  // addLoadedRectToCanvas("red",item.label,item.xmin,item.ymin,item.xmax,item.ymax)
  // this will only return number part of value
  typeof(item.xmin) 
  var  x = Math.trunc( parseFloat(item.xmin) )
  var  y = Math.trunc( parseFloat(item.ymin))
addLoadedRectToCanvas(getRandomColor(),item.label,x,y,parseFloat(item.xmax),parseFloat(item.ymax),item.id)

  // console.log(`Xmin ${item.xmin} Ymin ${item.ymin} Xmax ${item.xmax} YMax ${item.ymax}`)
})



canvas.requestRenderAll()
canvas.renderAll()
}

function isEven(value) {
    return !(value % 2)
}

function generateID(){
  return  Date.now().toString(36) + Math.random().toString(36).substr(2);
}
function attachId(csv){
 return csv.map(function(item){
    var newId = generateID()
   return Object.assign(item, {id:newId});

  })
}
function getRandomColor() {
  var letters = '0123456789ABCDEF';
  var color = '#';
  for (var i = 0; i < 6; i++) {
    color += letters[Math.floor(Math.random() * 16)];
  }
  return color;
}

function addNewRecordToCsv(newRecord){
  var lastIndex  =  0 
 csv.forEach(function(item,index){
    if (item.image== currentImg){
      lastIndex  = index
     
    } 
})
console.log(lastIndex)
if(lastIndex === 0)   csv.push(newRecord)  
 else{
  lastIndex++ 
   csv.splice(lastIndex,0,newRecord)
 }
 
console.log("csv New Record Added" , csv)


}
function editRecordToCsv(id , newValues){
  csv.forEach(function(item,index){
    if(item.id == id){
      item.xmin = newValues.tl.x
      item.ymin = newValues.tl.y
      item.xmax = newValues.br.x
      item.ymax = newValues.br.y
      console.log("item updated"  , item , "index" ,index )

    }
  })
  
console.log("CSV Updated ",csv)

}

function onDeleteObject(){
  document.addEventListener('keydown', function(event) {
    const key = event.key; // const {key} = event; ES6+
    if (key === "Delete") {
      var object = canvas.getActiveObject()
      deleteItemfromCanvas(object)
      deleteItemFromTable(object) 
      deleteItemFromCSV(object)
    
      
    }
  });
  
}
function deleteItemfromCanvas(rectange){
canvas.remove(rectange)
}

function deleteItemFromTable(rectange){
  var table = document.getElementById("t01")
 
  var tableRows = table.rows
  
  for(var i = 0 ; i < tableRows.length; i++){
   if(tableRows[i].id == rectange.name){
    table.deleteRow(i)
   }
  }
 
}


function deleteItemFromCSV(rectange){
//rectange.name is the id 

 csv = csv.filter(function(item,index){
  return item.id !== rectange.name
})
console.log("item removed with id = " + rectange.name)
}
