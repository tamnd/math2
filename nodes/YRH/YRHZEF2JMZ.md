---
tag: YRHZEF2JMZ
kind: concept
name: Descriptive complexity theory
msc: [68Q19, 03C13, 68Q15]
sources:
  - url: https://en.wikipedia.org/wiki/Descriptive_complexity_theory
same_as:
  wikidata: Q1200755
  wikipedia: Descriptive complexity theory
---

## Summary

Descriptive complexity theory characterizes complexity classes by the logics needed to define their problems.
It treats an input as a finite [[structure|983GZBQYT4]], such as a graph, and asks how rich a logic must be to express a property.
The founding result is [[Fagin's theorem|BG8Q0BYSQ3]]: NP is the class of properties definable in existential second-order logic.
It is a part of [[finite model theory|4XRVJE0KAN]].
Later results characterize P, NL and PSPACE on ordered structures by extensions of first-order logic with fixed points or transitive closure.

## Explanations

### L1 human

A computer problem asks whether an input has a certain property, such as "this graph can be colored with three colors".
Usually one measures how much time a machine needs to check the property.
Descriptive complexity instead asks how complicated a logical sentence must be to describe the property.
For example, three-colorability can be written as "there exist three sets of vertices such that every vertex is in one and no edge stays inside one".
Fagin's theorem says that the problems describable in this "there exist sets such that" style are exactly the problems in NP.
