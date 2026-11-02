---
tag: N5ZHV4HWDC
kind: concept
name: Divided differences
msc: [65D05, 41A05, 39A70]
sources:
  - url: https://en.wikipedia.org/wiki/Divided_differences
same_as:
  wikidata: Q2993265
  wikipedia: Divided differences
---

## Summary

Divided differences are quotients built recursively from the values of a function at a list of points.
First comes the slope between two points, then the difference of two slopes divided by the spread of three points, and so on.
The divided difference $f[x_0, \dots, x_n]$ is the leading coefficient of the polynomial of degree at most $n$ that interpolates $f$ at the points.
They are the coefficients of the [[Newton form|9W77FPTM9E]] of the interpolation polynomial.
For smooth functions they behave like scaled derivatives: by the [[mean value theorem for divided differences|BQJ9C1CD5X]], $f[x_0, \dots, x_n] = f^{(n)}(\xi)/n!$ for some $\xi$.

## Explanations

### L1 human

The first divided difference $\frac{f(x_1) - f(x_0)}{x_1 - x_0}$ is the slope of the chord between two points of a graph.
The second one compares two neighbouring slopes and so measures how the graph bends.
For $f(x) = x^2$ and the points $0, 1, 3$, the slopes are $1$ and $4$, and the second divided difference is $\frac{4 - 1}{3 - 0} = 1$, the leading coefficient of $x^2$.
Higher divided differences continue the same pattern.
The [[definition|T942SHWSSF]] gives the recursion.
