---
tag: T70CCQFWM6
kind: concept
name: Nelder–Mead method
msc: [90C56, 65K05]
sources:
  - url: https://en.wikipedia.org/wiki/Nelder%E2%80%93Mead_method
same_as:
  wikidata: Q1253278
  wikipedia: Nelder–Mead method
---

## Summary

The Nelder–Mead method, also called the downhill simplex method, minimizes a function of $n$ variables using only function values.
It keeps a [[simplex|YX1DJK2QAG]] of $n + 1$ points and changes it by reflection, expansion, contraction and shrinking.
In this way the simplex moves downhill and adapts its shape.
It was published by Nelder and Mead in 1965 and is popular for small problems with noisy or non-smooth objectives.
It is a heuristic.
McKinnon gave strictly convex, continuously differentiable functions of two variables on which it converges to a non-minimizing point.

## Explanations

### L1 human

Think of a triangle lying on a hilly landscape, and look at the height under each corner.
Flip the highest corner through the opposite side, like a tumbling triangle.
If that went well, stretch further in the same direction; if it went badly, pull the corner in, or shrink the whole triangle toward its lowest corner.
The triangle crawls downhill and shrinks around the bottom of a valley.
