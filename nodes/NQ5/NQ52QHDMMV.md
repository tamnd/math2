---
tag: NQ52QHDMMV
kind: concept
name: Fractional programming
msc: [90C32]
sources:
  - url: https://en.wikipedia.org/wiki/Fractional_programming
same_as:
  wikidata: Q5477546
  wikipedia: Fractional programming
---

## Summary

Fractional programming is the optimization of a ratio of two functions over a feasible set.
Such ratios measure efficiency: profit per unit of cost, output per unit of input, or return per unit of risk.
Suppose the numerator is concave and nonnegative, the denominator is convex and positive, and the set is convex.
Then every local maximum is global, and the problem reduces to convex problems.
The special case of two affine functions is [[linear-fractional programming|XVBF9EJY10]].

## Explanations

### L1 human

Instead of "make the most profit", a fractional program asks "make the most profit per hour worked".
The ratio is usually not concave, even when its parts are simple, so special tools are needed.
One tool guesses a value $q$ of the best ratio and checks whether "numerator minus $q$ times denominator" can still be made positive; if yes, the guess was too low.
For example, $x / (1 + x^2)$ on $[0, 2]$ is largest at $x = 1$, where it equals $1/2$.
