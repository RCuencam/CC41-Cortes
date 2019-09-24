
var la,an;
var canvas, body; 
var ctx;
var padre =[{x:800, y: 400}];
//
var rectangulos = [  {x:100,y:50},{x:80,y:40},{x:200,y:50},
{x:150,y:50},{x:100,y:20},{x:50,y:30},{x:60,y:10},{x:70,y:20}];
var areas=[];
var objArea={};
var rectOrden=[];
var newPoints=[];
var obj ={}
function send()
{
    //get aareas
    for( i =0; i<rectangulos.length;i++)
    {
        objArea={x:rectangulos[i].x,y:rectangulos[i].y , area : rectangulos[i].x*rectangulos[i].y}
        areas.push(objArea)
    }
    console.log(areas)

    //order areas
    rectOrden = areas.sort(function (a, b){
        return (b.area  - a.area)
    })
    //
    for(i = 0 ; i<1;i++)
    {
                 obj ={x : 0 ,
                        y: 0,
                        largo :rectOrden[0].x,
                        ancho : rectOrden[0].y};
                        newPoints.push(obj);

    }
    console.log(newPoints)
    //create rectangle
    canvas = document.createElement('canvas');
    //properties
    canvas.id = "CursorLayer";
    canvas.width = padre[0].x;
    canvas.height = padre[0].y;
    canvas.style.zIndex = 8;
    canvas.style.position = "absolute";
    canvas.style.border = "1px solid";

    //inside in div
    body = document.getElementById("area");
    body.appendChild(canvas);
    cursorLayer = document.getElementById("CursorLayer");

    //get DOM
    ctx = cursorLayer.getContext("2d");
    ctx.fillStyle = "rgb(100,100,00)";
    
        for(a = 0;a<newPoints.length ; a++)
        {  
            ctx.fillRect(newPoints[a].x, newPoints[a].y ,newPoints[a].largo ,newPoints[a].ancho); // x , y, largo,ancho

        }
}

function x(data) {
    la = document.getElementById("largo").value;
    an= document.getElementById("ancho").value;
   console.log(la)
   console.log(an)
}
