---
tag: FH0538XCZR
kind: concept
name: Trapezoidal rule
msc: [65D32, 41A55, 65D30]
specializes: [BQPQAY1FDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Trapezoidal_rule
same_as:
  wikidata: Q833293
  wikipedia: Trapezoidal rule
---

## Summary

The trapezoidal rule approximates $\int_a^b f$ by the area of the trapezoid under the chord from $(a, f(a))$ to $(b, f(b))$.
Its composite form splits $[a, b]$ into $N$ equal parts and adds the trapezoids, with error of order $h^2$ for smooth $f$, where $h = (b - a)/N$.
It is the closed [[Newton–Cotes formula|BQPQAY1FDJ]] with two nodes, and it is remarkably accurate for smooth periodic functions over a full period.

## Explanations

### L1 human

Replace the curve over each small piece by the straight line between its endpoints, and add up the areas of the resulting trapezoids.
Each trapezoid has area equal to its width times the average of its two heights.
Halving the width of the pieces roughly cuts the error by four.
For $f(x) = x^2$ on $[0, 1]$ with two pieces, the trapezoids give $3/8$, slightly more than the true value $1/3$, because the parabola bends below its chords.
