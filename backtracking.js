var canvas, desDom, bodyDes,body,ctx; 
var padre =[{x:800, y: 190}];
var area=padre[0].x*padre[0].y;
var rectangulos = [  {x:400,y:70},{x:250,y:70},{x:170,y:60},
{x:200,y:50},{x:100,y:20},{x:130,y:30},{x:150,y:15},{x:140,y:25}];
var areas=[];
var objArea={};
var rectOrden=[], newPoints=[];
var obj ={};
var areaUsada=0,anchoUsado=0,cont=0;
var largoQueda=0,maxAncho=0;
var max=[]
var puntosUsados=[]
var objPuntos={}
var areaRectangulos=0
var desperdicio=0;


function createRectangle()
{  
    n = rectangulos.length;
    //get aareas
    for( i =0; i<rectangulos.length;i++)
    {
        objArea={x:rectangulos[i].x,y:rectangulos[i].y , area : rectangulos[i].x*rectangulos[i].y}
        areas.push(objArea)
        areaRectangulos=areaRectangulos+ objArea.area;
    }
   
    //Desperdicio 
    desperdicio = (1-(areaRectangulos/(padre[0].x*padre[0].y)))*100;
    desDom = document.createElement("input");
    //properties
    desDom.id = "layer";
    desDom.value = "Desperdicio:" + desperdicio.toFixed(2) +"%, Area: "+ (((desperdicio)/100)*(padre[0].x*padre[0].y)) +" metros cuadrados";
    desDom.style.width = "250%";
    desDom.style.border = "none" ;
    
    bodyDes = document.getElementById("text");
    bodyDes.appendChild(desDom);


    //order y
    rectOrden = areas.sort(function (a, b){
        return (b.y  - a.y)
    })
    console.log("order y")
    console.log(rectOrden)
    //
    for(i = 0 ; i<n;i++)
    {
        if(areaUsada<area && largoQueda +rectOrden[i].x <=padre[0].x)
        {
                obj ={x : 0 +(largoQueda) ,
                y: 0 +maxAncho ,
                area:rectOrden[i].area,
                largo :rectOrden[i].x,
                ancho : rectOrden[i].y};

                newPoints.push(obj);
                 if(i==0){ objPuntos={
                             xi:0,
                             yi:0,
                             xf:rectOrden[i].x ,
                             yf:rectOrden[i].y
                           
                             }
                            }else{
                                objPuntos={ xi:puntosUsados[i-1].xf ,
                                yi:puntosUsados[i-1].yi,
                               xf:rectOrden[i].x +puntosUsados[i-1].xf  ,
                               yf:rectOrden[i].y +puntosUsados[i-1].yi}
                               cont=cont+puntosUsados[i-1].xf;
                            }
                        
                puntosUsados.push(objPuntos)      
                  
                areaUsada=areaUsada+rectOrden[i].area;
                largoQueda=largoQueda+rectOrden[i].x;
                
                          
        }else if(areaUsada<area){
            max=newPoints.sort(function (a, b){
                return (b.ancho  - a.ancho)
            })
            maxAncho = max[0].ancho + maxAncho;
            console.log(maxAncho)
               
                 largoQueda=0
                 obj ={x : 0 +(largoQueda) ,
                    y:maxAncho,
                    area:rectOrden[i].area,
                    largo :rectOrden[i].x,
                    ancho : rectOrden[i].y};
                    newPoints.push(obj);

                    if(i==0){ objPuntos={
                        xi:0,
                        yi:0,
                        xf:rectOrden[i].x ,
                        yf:rectOrden[i].y
                      
                        }
                       }else{
                           objPuntos={ xi:puntosUsados[i-1].xf ,
                           yi:puntosUsados[i-1].yi,
                          xf:rectOrden[i].x +puntosUsados[i-1].xf  ,
                          yf:rectOrden[i].y +puntosUsados[i-1].yi}
                          cont=cont+puntosUsados[i-1].xf;
                       }
                   
           puntosUsados.push(objPuntos) 
 
                 areaUsada=areaUsada+rectOrden[i].area;
                 anchoUsado = anchoUsado+rectOrden[i].y;
                 largoQueda=largoQueda+rectOrden[i].x;
 
         }       
    }
    console.log(newPoints)
    console.log(puntosUsados)

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

