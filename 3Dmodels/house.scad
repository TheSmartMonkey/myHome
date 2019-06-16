$fn = 50;

// Global dimensions
width = 60; //largeur
length = 85; //longueur
height = 70; //hauteur
thickness = 2; //épaisseur


// Sensor modules //

module led(w,l,h){
    difference(){
        cube([l,w,h]);
        translate([1,1,-1]) cube([l-2,w-2,h+10]);
    }
}

//led(8,6,5);

module temperatureSensor(w,l,h){
    difference(){
        cube([l,w,h]);
        translate([1,1,-1]) cube([l-2,w-2,h+10]);
    }
}

//temperatureSensor(10,15,15);


// All modules of a Block //

module partitionWallsLeft(w,l,h,t){
    cube([l,w,t]);
    //cube([l,t,h]); // middle side
    translate([0,w-t,0]) cube([l,t,h*sin(30)]);
}

module partitionWallsRight(w,l,h,t){
    translate([0,-w,0]) {
        cube([l,w,t]);
        //cube([l,t,h]); // middle side
        cube([l,t,h*sin(30)]);
    }
}
// left side wall
module blockLeft(w,l,h,t){
    difference(){
        cube([t,w,h]);
        translate([-20,w,h*sin(30)]) rotate([60,0,0]) cube([l,w,h]); // roof
        //translate([-20,0,h-14]) rotate([45,0,0]) cube([l,12,12]);
    }
}

// right side wall
module blockRight(w,l,h,t){
    difference(){
        translate([0,-w,0]) cube([t,w,h]);
        translate([-20,0,h*sin(90)]) rotate([120,0,0]) cube([l,w,h]); // roof
    }
}

module roof(w,l,h,t){
    translate([0,-w-15,0]) {
        cube([l*2,w+25,t]);
        translate([5,15,-10]) cube([10,w,t+10]);
        translate([(l*2)-15,15,-10]) cube([10,w,t+10]);
        
        // for start:increment:end
        /*for(x=[0:20:140]) { 
            translate([0,x,t]) cube([l*2,5,t]);
        }*/
    }
    
    /*difference() {
                        translate([0,-0.65,-5]) rotate([-30,0,0]) cube([l*2,5,12]);
        translate([0,-w-20,t]) cube([l*2,w+50,h]);
        }*/
}

module door(w,l,h,t){
    difference(){
        union(){
            cube([w-11,w/2-3,t]);
            translate([0,17,0]) cube([5,7,8]);
            translate([w-16,17,0]) cube([5,7,20]);
        }
        
        // Cylinder hole
        translate([-1,20.5,4.5]) rotate([0,90,0]) cylinder(  100,1.5,1.5);
        translate([-1,20.5,17]) rotate([0,90,0]) cylinder(  100,1.5,1.5);
    }
}


// union of 2 blocks
module blockEntrance(w,l,h,t){
    // Block 1
    difference(){
        blockLeft(w,l,h,t);
        translate([w-20,w-10,t*1.01]) cube([40,40,h*sin(30)/1.5]);
    }
    
    // Block 2
    translate([l-t,0,0]) difference() {
        blockLeft(w,l,h,t);
        translate([-10,w/3,t*1.01]) cube([40,20,h*sin(30)/1.5]);
    }
    
    // Walls and sensors
    translate([t,w/4-5,t]) led(8,6,15);
    translate([l/2,w/4-5,t]) led(8,6,15);
    difference(){
        partitionWallsLeft(w,l,h,t);
        translate([3,w/4-4,-1]) cube([6-2,8-2,5+10]); //led cables
        translate([l/2+1,w/4-4,-1]) cube([6-2,8-2,5+10]); //led cables
        
        // LCD sceen
        translate([5,w-t-1,10]) cube([40,t+2,13]);
        translate([l/2,w/3-2,-1]) cube([6,w/4-1,5+10]);
    }
    
    // Entrance door
    difference(){
        translate([l/2+10,w-4,0.01]) cube([20,t+4,h*sin(30)/1.4]);
        translate([l/2+12.5,50,-0.01]) cube([15,30,h*sin(30)/1.6]);
    }
    
    // Center partition wall
    difference(){
        cube([l,t,h*sin(30)]);
        translate([l/2+10,-10,t*1.01]) cube([20,40,h*sin(30)/1.5]);
        translate([l/4-10,-10,t*1.01]) cube([20,40,h*sin(30)/1.5]);
    }
    
    // Bathroom
    translate([0,w/2,t*0.01]) cube([l/2,t,h*sin(30)]);
    translate([l/2,0,0]) rotate([0,0,90]) cube([w/2,t,h*sin(30)]);
}

module blockRoom(w,l,h,t){
    // Block 1
    blockRight(w,l,h,t);
    
    // Block 2 
    difference(){
        translate([l-t,0,0]) blockRight(w,l,h,t);
        translate([l-10,-w/2,t*1.01]) cube([40,20,h*sin(30)/1.5]);
    }
    
    // Walls and sensors
    translate([2,-w/2-5,t]) led(8,6,15);
    difference(){
        partitionWallsRight(w,l,h,t);
        translate([3,-w/2-4,-1]) cube([6-2,8-2,5+10]); //led cables
    }
}

module blockKitchen(w,l,h,t){
    
    // Block 2 
    translate([l-t,0,0]) blockRight(w,l,h,t);
    
    // Walls and sensors
    translate([l/2,-w+t,t]) temperatureSensor(10,15,15);
    translate([l-t*4,-w/2-5,t]) led(8,6,15);
    difference(){
        partitionWallsRight(w,l,h,t);
        translate([l/2+1,-w+t+1,-1]) cube([15-2,10-2,15+10]);
        translate([l-t*4+1,-w/2-4,-1]) cube([6-2,8-2,5+10]); //led cables
    }
}

// union of 2 blocks
module blockGarage(w,l,h,t){
    // Block 2
    translate([l-t,0,0]){
        blockLeft(w,l,h,t);
    }
    
    // Center partition wall
    cube([l,t,h*sin(30)]);
    
    // Walls, sensor and garage door
    translate([l-t*4,2,t]) led(8,6,15);
    difference(){
        partitionWallsLeft(w,l,h,t);
        translate([l/6-t*2+5,w-10,t*1.01]) cube([w-10,w/2,w/2-2]); // Garage hole
        translate([l-t*4+1,3,-1]) cube([6-2,8-2,5+10]); // Led cables
        translate([w-5,l/2-10,-1]) cube([10,20,10]); // Garage cables
    }
    
    // Garage plot
    difference() {
        // Plot
        color("red") union(){
            translate([10.17,w-7,0]) cube([5,7-0.1,h/2-5]);
            translate([l-20+0.165,w-7,0]) cube([5,7-0.1,h/2-5]);
        }
        
        // Cylinder hole
        translate([0,w-4.5,w/2-7]) rotate([0,90,0]) cylinder(100,1.5,1.5);
    }
}



// all shapes //

fondation = false;
print = true;

if (print == true){
    // Fondation
    if (fondation == true){
        union(){
            blockEntrance(width,length,height,thickness);
            blockRoom(width,length,height,thickness);
            translate([length,0,0]) blockGarage(width,length,height,thickness);
            translate([length,0,0]) blockKitchen(width,length,height,thickness);    
        }
    }
    color("blue") union(){
        // Roof
        //rotate([180,0,0]) roof(width,length,height,thickness);
        
        // Door
        door(width,length,height,thickness);
    }
    
} else {
    // Fondation
    if (fondation == true){
        union(){
            blockEntrance(width,length,height,thickness);
            blockRoom(width,length,height,thickness);
            translate([length,0,0]) blockGarage(width,length,height,thickness);
            translate([length,0,0]) blockKitchen(width,length,height,thickness);    
        }
    }
    
    color("blue") union(){
        // Roof
        //translate([0,0,height]) rotate([30,0,0]) roof(width,length,height,thickness);
        
        // Door
        translate([length+15.5,width,2.5]) rotate([90,0,0]) door(width,length,height,thickness);
    }
}





















