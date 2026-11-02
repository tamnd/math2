---
tag: FT2GJEHWY5
kind: concept
name: Tropical variety
msc: [14T10, 14T20]
sources:
  - url: https://en.wikipedia.org/wiki/Tropical_geometry
---

## Summary

A tropical variety is a polyhedral complex in $\R^n$ attached to an algebraic subvariety of a torus over a field with a [[valuation|B85T5VKR3M]].
It is the set where tropical polynomials are "zero", meaning that the minimum of their linear terms is attained at least twice.
Over an algebraically closed field with a nontrivial valuation, it equals the closure of the image of the variety under the coordinatewise valuation.
This is the fundamental theorem of [[tropical geometry|7YTC3BHK60]].
Tropical varieties keep dimension, degree and intersection data of the original variety in combinatorial form.

## Explanations

### L1 human

Take the line $x + y + 1 = 0$, with $x$ and $y$ in a field of power series in a small parameter $t$.
Record for each solution the orders of vanishing of $x$ and $y$ in $t$.
Two of the three terms $x$, $y$, $1$ must have the same lowest order, or they could not cancel.
So the orders lie on three rays from the origin: one where $x$ and $y$ tie below $0$, and two where one of them ties with $1$.
This tripod is the tropical line, a skeleton of the original line.
