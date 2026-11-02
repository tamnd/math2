---
tag: TDA94C2JYT
kind: concept
name: Backward differentiation formula
msc: [65L06, 65L04]
specializes: [BX4D85A79P]
sources:
  - url: https://en.wikipedia.org/wiki/Backward_differentiation_formula
same_as:
  wikidata: Q795746
  wikipedia: Backward differentiation formula
---

## Summary

A backward differentiation formula, or BDF method, is an implicit [[linear multistep method|BX4D85A79P]].
It differentiates the polynomial through the latest computed values and sets its slope at the new point equal to $f$.
The $k$-step formula has order $k$, and it is zero-stable only for $k \le 6$.
Because of their large regions of stability, BDF methods are the standard methods for [[stiff equations|RR5FCG92PN]].
The one-step formula is the [[backward Euler method|M7XKVNATFA]].

## Explanations

### L1 human

Most methods use the slope at known points to guess the next point.
A BDF method works the other way.
It looks for a new point such that the curve through it and the previous points has, at the new point, the slope that the equation demands.
This has to be solved as an equation at each step, which costs work, but it makes the method very robust when parts of the solution decay very fast.
The simplest case is $y_{k+1} = y_k + h f(t_{k+1}, y_{k+1})$.
