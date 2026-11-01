---
tag: M077AXJACA
kind: concept
name: Perron integral
msc: [26A39]
sources:
  - url: https://en.wikipedia.org/wiki/Henstock%E2%80%93Kurzweil_integral
---

## Summary

The Perron integral squeezes the integral of a function between the increments of major and minor functions.
The lower derivatives of a major function lie above the function, and the upper derivatives of a minor function lie below it.
It integrates every derivative, and it gives the same integrable functions and the same values as the [[Henstock–Kurzweil integral|FCGHXDGVV9]].
It extends the Lebesgue integral.

## Explanations

### L1 human

The Darboux integral traps the area between step functions lying above and below the graph.
The Perron integral traps the integral instead between functions whose slopes lie above and below the function.
A function $U$ whose slope is everywhere at least $f$ should grow at least as much as the integral of $f$.
A function $V$ whose slope is at most $f$ should grow at most as much.
If these bounds meet, the common value is the Perron integral.
