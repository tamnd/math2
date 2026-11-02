---
tag: 6QB8J65RVV
kind: concept
name: Jensen's functional equation
msc: [39B22, 26A51]
specializes: [SRAN4EKWS0]
sources:
  - url: https://en.wikipedia.org/wiki/Functional_equation
---

## Summary

Jensen's functional equation is the [[functional equation|SRAN4EKWS0]] $f\left(\frac{x + y}{2}\right) = \frac{f(x) + f(y)}{2}$ for an unknown function $f \colon \R \to \R$.
It says that the value at the midpoint of two points is the average of the values.
Its solutions are the functions $f = A + b$ with $A$ an [[additive function|KF719SZD5T]] and $b$ a constant, and the continuous ones are the affine functions $f(x) = ax + b$.
It is the equality case of midpoint convexity, which links it to [[convex functions|07Q7CNM5WF]].

## Explanations

### L1 human

Take two points on the graph and their midpoint on the $x$-axis.
The equation asks the graph to pass exactly through the middle of the chord between the two points.
A straight line does this: for $f(x) = 2x + 3$, the midpoint of $0$ and $2$ is $1$, and $f(1) = 5$ is the average of $f(0) = 3$ and $f(2) = 7$.
A curved graph such as $x^2$ fails, since it sags below its chords.
