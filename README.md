# Nomad
An autonomous robot project.

The Nomad project is an autonomous robot project initially being built for the 2016 Sparkfun Autonomous Vehicle Challenge (AVC). Nomad is built on (and named after) a heavily modified robot chassis kit from Actobotics called Nomad. 

The electronics consist of:
Primary computer: Intel Edison Arduino breakout board
Motor controller: Roboclaw 2x30
Vision: Microsoft XBox Kinect

The software for Nomad is written in Python using the Robot Operating System (ROS) framework. This framework breaks the processing into separate, independent nodes. The nodes are:
Joynode: Standard jotstick package from ROS.
roboclaw: A custom node built to interact with the Roboclaw motor controller via USB. The node leverages sample code provided by Orion Robotics to control the Roboclaw. The example code has been converted into a library for this project.
Nomad_control: A custom node built to convert commands from the joystick into direction and rotation commands for the motors. This is the node which will likely change the most throughout development.
