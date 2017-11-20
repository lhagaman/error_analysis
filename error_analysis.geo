
{
name: "GEO",
index: "world",
valid_begin: [0,0],
valid_end: [0,0],
type: "box",
mother: "",
size: [5080.0,5080.0,5080.0],
position: [0.0,0.0,0.0],
rotation: [0.0,0.0,0.0],
material: "air",
color: [0.735795615075,0.176301474581,0.896628756544,0.5],
drawstyle: "solid",
invisible: 1,
}

{
name: "GEO",
index: "sapphire_tube",
valid_begin: [0,0],
valid_end: [0,0],
type: "tube",
mother: "world",
r_max: 25.4,
r_min: 22.225,
size_z: 22.86,
phi_start: 0.0,
phi_delta: 360.0,
position: [0.0,0.0,0.0],
rotation: [0.0,0.0,0.0],
material: "sapphire",
color: [0.658954714849,0.802189023832,0.994216568893,0.2],
drawstyle: "solid",
invisible: 0,
}

{
name: "GEO",
index: "sample",
valid_begin: [0,0],
valid_end: [0,0],
type: "tube",
mother: "world",
r_max: 12.7,
r_min: 0.0,
size_z: 2.54,
phi_start: 0.0,
phi_delta: 360.0,
position: [-2.35171128542,0.959715598519,0.0],
rotation: [90.0,67.8,0.0],
material: "mirror",
color: [0.976892196027,0.408361008099,0.504698048762,0.8],
drawstyle: "solid",
invisible: 0,
}

{
name: "GEO",
index: "outer_sample_surface",
valid_begin: [0,0],
valid_end: [0,0],
type: "border",
mother: "world",
volume1: "world",
volume2: "sample",
surface: "mirror",
color: [0.464755273792,0.0147587933684,0.456396222621,0.5],
drawstyle: "solid",
invisible: 0,
}

{
name: "GEO",
index: "inner_sample_surface",
valid_begin: [0,0],
valid_end: [0,0],
type: "border",
mother: "world",
volume1: "sample",
volume2: "world",
surface: "mirror",
color: [0.932297401461,0.0779028708634,0.885306382868,0.5],
drawstyle: "solid",
invisible: 0,
}

{
name: "GEO",
index: "coherent_surface",
valid_begin: [0,0],
valid_end: [0,0],
type: "tube",
mother: "world",
r_max: 139.954,
r_min: 139.7,
size_z: 24.2586504201,
phi_start: 35.6,
phi_delta: 20.0,
position: [0.0,0.0,0.0],
rotation: [0.0,0.0,0.0],
material: "pmt_vacuum",
color: [0.0927959589341,0.393798792332,0.828444585853,0.5],
drawstyle: "solid",
invisible: 0,
}

{
name: "GEO",
index: "laser",
valid_begin: [0,0],
valid_end: [0,0],
type: "tube",
mother: "world",
r_max: 17.78,
r_min: 0.0,
size_z: 63.5,
phi_start: 0.0,
phi_delta: 360.0,
position: [0.0,-266.7,0.0],
rotation: [90.0,0.0,0.0],
material: "stainless_steel",
color: [0.5,0.5,0,0.5],
drawstyle: "solid",
invisible: 0,
}

{
name: "GEO",
index: "table",
valid_begin: [0,0],
valid_end: [0,0],
type: "box",
mother: "world",
size: [304.8,304.8,50.8],
position: [0.0,0.0,-203.2],
rotation: [0.0,0.0,0.0],
material: "stainless_steel",
color: [0.6,0.2,0.6,1],
drawstyle: "solid",
invisible: 0,
}
