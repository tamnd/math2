---
tag: 1TQ1JQXEWP
kind: concept
name: Midpoint convex function
msc: [26A51, 39B62]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_function
---

## Summary

A midpoint convex function, also called a Jensen-convex function, is a real function $f$ on an interval with $f\big(\tfrac{x + y}{2}\big) \le \tfrac{f(x) + f(y)}{2}$ for all $x, y$.
Every [[convex function|07Q7CNM5WF]] is midpoint convex, but the converse fails without some regularity.
Mild extra conditions close the gap: a midpoint convex function that is bounded above on a small interval, or that is measurable, is convex.
The notion is the starting point of the theory of convex functions as solutions of a [[functional inequality|YQB2B0EXY8]].

## Explanations

### L1 human

Convexity asks that every chord of the graph lies above the graph.
Midpoint convexity only asks this at the midpoint of each chord.
For nice functions this is the same thing, because midpoints of midpoints fill out the whole chord.
Strange functions built with the axiom of choice show that, in general, the midpoint condition alone is weaker.
