
var la,an;
var canvas, body; 
var ctx;
var padre =[{x:800, y: 200}];
var area=160000;
var rectangulos = [  {x:400,y:70},{x:100,y:70},{x:200,y:60},
{x:150,y:70},{x:100,y:20},{x:50,y:30},{x:60,y:10},{x:70,y:20}];
var areas=[];
var objArea={};
var rectOrden=[];
var newPoints=[];
var obj ={}
var areaUsada=0;
var anchoQueda=0;
var largoQueda=0;
var max=[]
var puntosUsados=[]
var objPuntos={}
function send()
{
    //get aareas
    for( i =0; i<rectangulos.length;i++)
    {
        objArea={x:rectangulos[i].x,y:rectangulos[i].y , area : rectangulos[i].x*rectangulos[i].y}
        areas.push(objArea)
    }
    console.log(areas)

    //order y
    rectOrden = areas.sort(function (a, b){
        return (b.y  - a.y)
    })
    console.log("order areas")
    console.log(rectOrden)
    //
    for(i = 0 ; i<3;i++)
    {
        if(areaUsada<area && anchoQueda +rectOrden[i].x <=padre[0].x)
        {
                obj ={x : 0 +(anchoQueda) ,
                y: 0 ,
                area:rectOrden[i].area,
                largo :rectOrden[i].x,
                ancho : rectOrden[i].y};

                newPoints.push(obj);
                objPuntos={ x:rectOrden[i].x,
                        y:rectOrden[i].y,
                        }
                puntosUsados.push(objPuntos)        
                areaUsada=areaUsada+rectOrden[i].area;
                anchoQueda=anchoQueda+rectOrden[i].x;
                
        }/*else if(areaUsada<area && largoQueda +rectOrden[i].x <=padre[0].x){
            max = newPoints.sort(function (a, b){
                return (b.ancho  - a.ancho)
            })
                anchoQueda=0;
                obj ={x : max[0].ancho,
                y: 0 +anchoQueda ,
                area:rectOrden[i].area,
                largo :rectOrden[i].x,
                ancho : rectOrden[i].y};

                newPoints.push(obj);
                areaUsada=areaUsada+rectOrden[i].area;
                anchoQueda = anchoQueda+rectOrden[i].y;
                largoQueda=largoQueda+rectOrden[i].x;

        }       */ 
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
    var color=10, color1=20;
        for(a = 0;a<newPoints.length ; a++)
        {   
            string="rgb(100,"+color1+","+color+")";
            ctx.fillStyle = "rgb(100,100,"+color+")";
            console.log(string)
            ctx.fillRect(newPoints[a].x, newPoints[a].y ,newPoints[a].largo ,newPoints[a].ancho); // x , y, largo,ancho
            color=color+50;
            color1=color1+100;
        }
}

function x(data) {
    la = document.getElementById("largo").value;
    an= document.getElementById("ancho").value;
   console.log(la)
   console.log(an)
}
