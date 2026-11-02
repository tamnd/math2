---
tag: BQPQAY1FDJ
kind: concept
name: Newton–Cotes formulas
msc: [65D32, 41A55]
specializes: [ADSVMCY77A]
sources:
  - url: https://en.wikipedia.org/wiki/Newton%E2%80%93Cotes_formulas
same_as:
  wikidata: Q944241
  wikipedia: Newton–Cotes formulas
---

## Summary

The Newton–Cotes formulas are the [[quadrature rules|ADSVMCY77A]] obtained by integrating the interpolating polynomial of the integrand at equally spaced nodes.
The closed formulas include the endpoints; the trapezoidal rule and Simpson's rule are the first two.
They are simple and exact for polynomials of the interpolation degree.
High order formulas have negative weights and are unstable, so in practice low order formulas are applied on many small subintervals.

## Explanations

### L1 human

Sample the function at evenly spaced points, draw the polynomial curve through the samples, and take the area under that curve as the estimate.
With two points the curve is a line and the estimate is a trapezoid.
With three points the curve is a parabola, and the result is Simpson's rule with weights proportional to $1, 4, 1$.
Using many points at once does not work well, because polynomials through many equally spaced points can swing wildly.
