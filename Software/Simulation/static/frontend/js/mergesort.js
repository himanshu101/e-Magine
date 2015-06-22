
            $(document).ready(function(){
                $('#startbtn').hide();
                $('#stepbtn').hide();
                $('#prevbtn').hide();
                $('#nextbtn').hide();
                $('#inputstr2').hide();
                $('#speedlabel').hide();
                $('#optradiomidl').hide();
                $('#optradiolow').hide();
                $('#optradiohigh').hide();
                // $('[data-toggle="popover"]').popover({
                //     placement : 'bottom',
                //     //trigger:'hover'
                // });
            });

//create a wrapper around native canvas element (with id="c")
var canvas = new fabric.StaticCanvas('c');
var anim =[];
var names; //=[16,4,12,5,1,6,10,2,8,3,11,7,14,9,13,10];//,13,12,11,16,15,12,13,14,15,16,80,78,56,45,34]; 

function checkInput(){
                var fail = 0;
                var inp = document.getElementById('inputstr').value;
                arrtemp = inp.split(' ');
                names = arrtemp.slice();
                if(names.length > 16){
                    alert("Maximum Entries : 16 ");
                }
                else{
                    for(var a=0;a<names.length;a++){
                        if(names[a] != parseInt(names[a])){
                         alert("Only Integers allowed");
                         fail = 1;
                         break;
                        }
                    }
                    
                    if(fail == 0){
                        $('#rendbtn').hide();
                    $('#refresh').hide();
                    $('#startbtn').show();
                    $('#stepbtn').show();
                    $('#prevbtn').show();
                    $('#nextbtn').show();
                    $('#inputstr2').show();
                    $('#speedlabel').show();
                    $('#optradiomidl').show();
                    $('#optradiolow').show();
                    $('#optradiohigh').show();
                        var group = new fabric.Group([], {
                        left: 350,
                        top: 100,
                        originX: 'center',
                        originY: 'center'
                    });



                    for (var i = 0; i < names.length; i++){    //create the first set of circles
                       var ci = new LabeledCircle({
                            fill : '#faa',
                            left : 48*i,
                            top : 0,
                            label: names[i]+"",
                            originX: 'center',
                            originY: 'center'
                        });
                        group.add(ci);
                    }

                    canvas.add(group);

                    draw(group , 2,group.top,group.left);

                    }
                }
}



/**
 * The Complete Mergesort Algorithm
 *
 * All the code for mergesort & merge algorithm is in this function
 *
 * There are 2 parts 
 *             mergesort -> the recursive call where we call the draw function 
 *             merge     -> the merging of the two sorted subarrays / subgroups
 *
 *
 * @param { fabric.Group } parentGroup  - The Parent Group
 * @param { int }          n            - The level of the parentGroup
 * @param { int }          parentHeight - The height of the parentGroup
 * @param { int }          parentLeft   - The left property of the parentGroup
 *
 * @returns { int[] } retArr - The complete sorted array of parentGroup 
 *
 */
function draw(parentGroup,n,parentHeight,l1)
{
    /**
     * This routine 'draw' returns a sorted subarray in a variable
     * retArr ( short for return array ).
     */
    var retArr=[];
    if(parentGroup.size()<2){                   //If parent.size < 2, go back => thus ensuring children created will be atleast of length 1
         retArr.push(parseInt(parentGroup.item(0).label));
         return retArr;
    }


    var leftChildGroup = new fabric.Group([],{      //construct left child
         left: l1,                          //because we will animate it later - this is just the starting left parameter
         top: parentHeight ,                //because we will animate it later - this is just the starting height
         originx: 'center',
         originy: 'center'
     });
    var rightChildGroup = new fabric.Group([],{      //construct right child
         left:  l1+(parentGroup.size()/2 ) * 48, //because we will animate it later - this is just the starting right parameter
         top: parentHeight  ,               //because we will animate it later - this is just the starting height
         originx: 'center',
         originy: 'center'
     });
    
    for (var i = 0; i <= parentGroup.size()/2 - 1 ; i++) {       //fill values in left child
         leftChildGroup.add(fabric.util.object.clone(parentGroup.item(i)));
        }
    for (var j = i ; j <= parentGroup.size() - 1; j++) {         //fill values in right child
         rightChildGroup.add(fabric.util.object.clone(parentGroup.item(j)));   
         rightChildGroup.item(j-i).set({
                 left:(j-i)*48                               // subtract because it is already shifted (!! important )
         });
        }
    
    /**
     * Next we make the animation objects of type add - we want to render the
     * child groups and animate them to their correct position.
     */

    var a1 = {  type : 'add',
                element: leftChildGroup,
                parent : parentGroup,
                lc : 1,
                level: n,
                left: l1 - (parentGroup.size()*48)/Math.pow(2,n+1) ,
                top: (parentHeight +80),
                };
    var a2 = {  type : 'add',
                element: rightChildGroup,
                parent : parentGroup,
                lc : 0,
                level: n,
                left: l1 + (parentGroup.size()*48)/Math.pow(2,n+1)+ parentGroup.size()/2 * 48,
                top: (parentHeight +80),
                };
     anim.push(a1);
     anim.push(a2);
    
    /**
     * Now we call this subroutine draw recurcsively and expect a group that
     * contains the elements in already sorted order.
     * After that the merge procedure will begin.
     */
    var g2arr = draw(leftChildGroup,n+1,parentHeight+80,a1.left);
    var g3arr = draw(rightChildGroup,n+1,parentHeight+80,a2.left);

    /**
    * And there, we now have two sorted groups - Remember this is based on
    * recursion, so the assumption is that this will return us a sorted group.
    * So, leftChildGroup & rightChildGroup are sorted now.
    *
    * Next we expect the merge routine - I put the code of merge routine in this
    * routine itself.
    */

    var g1h = parentGroup.height;
    var g1l = parentGroup.left;

    var g2l = g2arr.length;
    var g3l = g3arr.length;

    /**
     * Next we clear the parentGroup of its objects 
     * We create another animation object of type 'remove'.
     */

    a1 = { type : 'remove',
           element: parentGroup
           };

    anim.push(a1);
    
    /**
     * Here merge starts.
     * var count => holds the no. of elements pushed in the parentGroup
     * var g2c   => holds the no. of elements pushed in the parentGroup from leftsubgroup
     * var g3c   => holds the no. of elements pushed in the parentGroup from rightsubgroup
     * 
     * var col (short for color) => Animation object for the highlighting of elements when they are compared.
     *
     * var a2 => Animation object for the moving of elements from current to parentGroup.
     */

    var count=0,g2c=0,g3c=0;
    var col;
    

    while( g2l>0 && g3l>0 ) {
        if( g2arr[0] <= g3arr[0] ){
            col={   type : 'color',
                    lessGroup : leftChildGroup,
                    moreGroup : rightChildGroup
                };
            a2 = {  type : 'merge',
                    size : leftChildGroup.size(),
                    current : leftChildGroup,
                    parent : parentGroup,
                    pno : count,
                    index : g2c,
                    };
            anim.push(col);
            anim.push(a2);
            retArr.push(g2arr.shift());
            count++;
            g2c++;
            g2l--;
        }
        else{
            col={   type : 'color',
                    lessGroup : rightChildGroup,
                    moreGroup : leftChildGroup
                };
            a2 = {  type : 'merge',
                    size : rightChildGroup.size(),
                    current : rightChildGroup,
                    parent : parentGroup,
                    pno : count,
                    index : g3c,
                    };
            anim.push(col);
            anim.push(a2);
            retArr.push(g3arr.shift());
            count++;
            g3c++;
            g3l--;
        }
    }

    while(g2l>0){
        a2 = {  type : 'merge',
                    size : leftChildGroup.size(),
                    current : leftChildGroup,
                    parent : parentGroup,
                    pno : count,
                    index : g2c,
                    };
            anim.push(a2);
            retArr.push(g2arr.shift());
            count++;
            g2c++;
            g2l--;
        }

    while(g3l>0){
        a2 = {  type : 'merge',
                    size : rightChildGroup.size(),
                    current : rightChildGroup,
                    parent : parentGroup,
                    pno : count,
                    index : g3c,
                    };
        anim.push(a2);
        retArr.push(g3arr.shift());
        count++;
        g3c++;
        g3l--;
    }
    
    
    return retArr ;   //Return the now sorted retArr 
}

canvas.renderAll();

var i=-1,speed=1000;

/**
 * This function traverses through the anim array and does the corresponding
 * animations.
 *
 * @param NULL
 *
 * @return NULL
 */
function ani(){

    i++;

        if (i>=anim.length){
            return;
        }

        if(anim[i].type=='add'){
            $("code span").eq(3).css("background-color", "black");
            $("code span").eq(4).css("background-color", "black");
            $("code span").eq(5).css("background-color", "#33b5e5");
            var parentgrp = anim[i].parent;
                changeColor(parentgrp,'rgb(209,73,89)');
            canvas.add(anim[i].element);
            anim[i].element.animate({top:anim[i].top,left:anim[i].left},{
                    onChange: canvas.renderAll.bind(canvas),
                    duration:speed*0.8,
                    onComplete: function(){
                        if(anim[i].lc===0){  
                            changeColor(parent,'#faa');
                            }  
                        // var blobadd = new Blob([canvas.toSVG()], {type: "text/plain;charset=utf-8"});
                        // saveAs(blobadd, i+".svg");
                    }
             });
        }

        else  if(anim[i].type=='remove'){
            while ( anim[i].element.size() > 0 ) {
                anim[i].element.remove(anim[i].element.item(0));
            }
            canvas.renderAll();
             // var blobremove = new Blob([canvas.toSVG()], {type: "text/plain;charset=utf-8"});
             //            saveAs(blobremove, i+".svg");
        }
        
        else if(anim[i].type=='merge'){
            $("code span").eq(3).css("background-color", "#33b5e5");
            $("code span").eq(4).css("background-color", "#33b5e5");
            $("code span").eq(5).css("background-color", "black");
            //$("code span").eq(4).css("background-color", "#33b5e5");
            var curgrp=anim[i].current;
            var parent=anim[i].parent;
            var elem = curgrp.item(0);
            var index=anim[i].index;
            var pno=anim[i].pno;
            
            curgrp.remove(curgrp.item(0));
            canvas.renderAll();
            
            elem.set({
                    left : index*48 + curgrp.left,
                    top : anim[i].current.top ,//- 80*(anim[i].level - 1),
                    fill : 'rgb(190,247,9)' 
                });
            canvas.add(elem);
            canvas.renderAll();
            elem.animate({ top:parent.top ,left : parent.left + pno*48},{
                   onChange: canvas.renderAll.bind(canvas),
                   duration: speed*0.8,
                   onComplete:function(){
                       var ne=canvas.remove(elem);
                       canvas.renderAll();
                       elem.set({
                            left : pno*48,
                            top : 0,
                            fill : '#faa'
                        });
                        parent.add(elem);
                        canvas.renderAll();
                        
                        //var blobmerge =new Blob([canvas.toSVG()], {type: "text/plain;charset=utf-8"});
                        //saveAs(blobmerge, i+".svg");
                   }

                });
        }
    
        else if(anim[i].type=='color'){
            var lessGroup = anim[i].lessGroup;
            var moreGroup = anim[i].moreGroup;
            var smallElement = lessGroup.item(0);
            var largeElement = moreGroup.item(0);
            smallElement.set('fill','blue');
            largeElement.set('fill','blue');
            canvas.renderAll();
            smallElement.animate({top :smallElement.top },{
                    onChange: canvas.renderAll.bind(canvas),
                    duration: speed*0.5,
                    onComplete:function(){

                        smallElement.set('fill','rgb(190,247,9)');
                        smallElement.animate({top :smallElement.top},{
                                  onChange: canvas.renderAll.bind(canvas),
                                  duration: speed*0.5,
                                  onComplete:function(){
                                      largeElement.set('fill','#faa');
                        //                var blobcolor = new Blob([canvas.toSVG()], {type: "text/plain;charset=utf-8"});
                        // saveAs(blobcolor, i+".svg");
                                  }
                              });
                    }
                });
        }
}

/**
 * This function changes the color for the entire group.
 *
 * @params { fabric.Group } grop => The group object
 * @params { string }       colo => The desired color
 *
 * @returns NULL
 *
 * */
function changeColor(grop,colo){
    var jk=0;
    while ( jk < grop.size() ) {
         grop.item(jk).set('fill',colo);
         jk++;
            }

}

var t,startState=0,speed=1000;

function start()
{   //console.log("Yo");
    if(startState==1){
        clearInterval(t);
        startState=0;
        $("#startbtn").removeClass("glyphicon glyphicon-pause");
        $("#startbtn").addClass("glyphicon glyphicon-play");
        
        return;
    } else {
        var radspeed = getRadioValue();
         
         if(radspeed===0){
             speed = 1550;
         }
         else if(radspeed==1){
             speed = 1000;
         }
         else{
             speed = 600;
         }
         
         //speed = 1000;
        startState=1;
        $("#startbtn").removeClass("glyphicon glyphicon-play");
        $("#startbtn").addClass("glyphicon glyphicon-pause");
        
        t = setInterval(ani,speed);
    }
}

