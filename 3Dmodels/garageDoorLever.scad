$fn=64;

difference() {
    union() {
        cube([9,15,5]);
        translate([0,10,5]) cube([9,5,5]);
    }
    translate([1.9,1.9,-1]) cube([5.2,5.2,7]);
    translate([2,9,5]) cube([5,7,6]);
    translate([-1,4.5,2.5]) rotate([0,90,0]) cylinder(12,1,1);
    translate([-1,12.5,7.5]) rotate([0,90,0]) cylinder(12,1,1);
}

translate([10,0,0]) 
difference() {
    union() {
        cube([8,20,5]);
        translate([0,15,5]) cube([8,5,15]);
    }
    translate([3,-1.8,-1]) cube([2.2,9,10]);
    translate([3,6,-1]) cube([2.2,7,10]);
    translate([2.5,15,15]) cube([3,8,6]);
    translate([-1,2,2.5]) rotate([0,90,0]) cylinder(12,1,1);
    translate([-1,8,2.5]) rotate([0,90,0]) cylinder(12,1,1);
    translate([-1,17.5,17.5]) rotate([0,90,0]) cylinder(12,1,1);
}