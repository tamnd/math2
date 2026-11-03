---
tag: 1DQ5AE8D8E
kind: concept
name: Forward kinematics
msc: [70B15, 93C85]
sources:
  - url: https://en.wikipedia.org/wiki/Forward_kinematics
same_as:
  wikidata: Q1423222
  wikipedia: Forward kinematics
---

## Summary

Forward kinematics computes the position and orientation of the end of a robot arm or other serial mechanism from the values of its joint variables.
It is a map from the joint space to the [[Euclidean group|0H3YY8CPKH]] $SE(3)$ of rigid motions, obtained by multiplying one rigid motion per joint.
It is explicit and easy to evaluate, in contrast to the inverse problem of finding joint values for a desired pose.
[[Denavit–Hartenberg parameters|41426EQJHF]] are a standard way to write down the joint motions.

## Explanations

### L1 human

A robot arm is a chain of rigid pieces linked by motorised joints.
If you know the angle of each joint, you can work out where the hand is by following the chain from the shoulder to the hand.
This step-by-step calculation is forward kinematics.
Take an arm in the plane with two pieces of length $1$.
With both joints at angle $0$, the hand is at distance $2$ along the first axis; bending the elbow by $90$ degrees moves it to $(1, 1)$.
