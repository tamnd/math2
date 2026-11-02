---
tag: 7JSQZ126BP
kind: concept
name: Finite difference
msc: [39A70, 39A12]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
same_as:
  wikidata: Q2068418
  wikipedia: Finite difference
---

## Summary

A finite difference of a function is the change of its value between two points at a fixed distance, such as $f(x + h) - f(x)$.
Divided by the step $h$, it becomes a [[difference quotient|AZBDB5F4M4]], which approximates the derivative when $h$ is small.
Finite differences are the basic operation of difference equations, of interpolation and of numerical methods for differential equations.

## Explanations

### L1 human

A derivative measures change over an infinitely small step; a finite difference measures change over a step of fixed size.
Think of reading a thermometer once every hour: the hourly changes are finite differences of the temperature.
For $f(x) = x^2$ and step $1$, the difference is $(x + 1)^2 - x^2 = 2x + 1$.
The three usual kinds look forward, backward, or symmetrically around the point.
