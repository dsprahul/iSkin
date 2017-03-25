# iSkin
iSkin - Haptic interface for the sense of touch

 Physical objects can be perceived by their texture, shape, weight
 and their dynamics(as of a spring when compressed between fingers).
 The first version of **iSkin** is built to take advantage of an arbitary object's (rigid and non-rigid) shape and dynamics and 
 help us feel sensation of object with our fingers **with actually holding the object!**. 
 
## Interface description
 - Consists of a `exoskeleton with actuators` which grips your fingers and overhead `camera` along with `force sensor, microprocessor & IMU` to sense and correct force on your finger tips and shape your palm
 - For example, if you want to emulate `pressing a spring stuck to the surface of a table,` you'd be pressing your finger against one of the fingers of exoskeleton(stuck to table) whose surface is fitted with a flex force sensor to measure the amount of force your finger is sensing. The actuators will have in-built encoders to estimate the depth of press. This information will be used to emulate the sense of touch by programming the dynamics of a spring.
 - Another example, if you want to emulate `playing a keyboard without actually having one physically`, you'll again have 1 finger of exoskeleton (stuck to table) facing your fingers, this time we'll also use camera's position feedback to help the skeleton fingers follow yours while you move your hand playing the **virtual** keyboard
 
# Stages
|Stage #|Emulator target|Desk/Mobile|Dynamics|Shape|Status|
|------:|---------------:|---------:|--------:|---:|------:|
|Stage-1|Spring emulator|Desk|Y|N|Success|
|Stage-2|Keyboard emulator|Desk|Y|N|Success|
|Stage-3|5 fingers piano emulator|Desk|Y|N|Not implemented|
|Stage-4|5 fingers piano emulator|Mobile|Y|N|Not implemented|
|Stage-5|5 fingers generic emulator|Mobile|Y|Y|Not implemented|

# Preview
![alt tag](https://github.com/RahulDamineni/iSkin/blob/master/img/a.jpg) 
![alt tag](https://github.com/RahulDamineni/iSkin/blob/master/img/b.jpg)
![alt tag](https://github.com/RahulDamineni/iSkin/blob/master/img/c.png)


