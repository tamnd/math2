---
tag: GK1Z3Q1WRZ
kind: concept
name: Bang–bang control
msc: [49J15, 93C15]
sources:
  - url: https://en.wikipedia.org/wiki/Bang–bang_control
same_as:
  wikidata: Q1432859
  wikipedia: Bang–bang control
---

## Summary

A bang–bang control only takes extreme values of the allowed range, such as full thrust forward or full thrust backward.
It switches abruptly between these values.
Such controls arise as optimal controls through [[Pontryagin's maximum principle|7RPV2T29CF]] when the dynamics and the cost are linear in the control.
They are typical for minimum-time problems, and they are easy to implement with simple on–off actuators.

## Explanations

### L1 human

To bring a car to a stop at a wall as fast as possible, you accelerate at full power and then brake at full power.
You never use half power: the control jumps from one extreme to the other.
That is a bang–bang control.
A household thermostat that switches a heater fully on or fully off works in the same way.
