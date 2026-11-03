---
tag: 5ZR8VVTKF6
kind: concept
name: PID controller
msc: [93B52, 93B51]
sources:
  - url: https://en.wikipedia.org/wiki/PID_controller
same_as:
  wikidata: Q716829
  wikipedia: PID controller
---

## Summary

A PID controller acts on the error between a reference and a measured output.
Its control signal is a weighted sum of the error, the integral of the error and the derivative of the error.
The proportional term reacts to the present error, the integral term removes steady offsets, and the derivative term anticipates the trend.
It is by far the most common [[feedback|7NYES2D0Z4]] controller in industry.
It has only three parameters and works well for many processes without a detailed model.

## Explanations

### L1 human

Think of the cruise control of a car.
If the car is too slow, push the pedal in proportion to the shortfall: that is the P part.
If it stays slightly too slow for a long time, push a little more each second: that is the I part, and it removes the remaining gap.
If the speed is dropping fast, push extra now: that is the D part.
Adding the three pushes gives the PID control law.
