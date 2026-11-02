---
tag: MNXC26G3BQ
kind: concept
name: Simpson's rule
msc: [65D32, 41A55, 65D30]
specializes: [BQPQAY1FDJ]
sources:
  - url: https://en.wikipedia.org/wiki/Simpson%27s_rule
same_as:
  wikidata: Q722507
  wikipedia: Simpson's rule
---

## Summary

Simpson's rule approximates $\int_a^b f$ by integrating the parabola through the values of $f$ at $a$, at the midpoint, and at $b$, which gives $\frac{b - a}{6}\big(f(a) + 4 f(m) + f(b)\big)$.
It is the closed [[Newton–Cotes formula|BQPQAY1FDJ]] with three nodes, and it is exact for all cubic polynomials.
Its composite form has error of order $h^4$ for smooth integrands, which makes it a standard simple method.

## Explanations

### L1 human

Instead of joining samples by straight lines, Simpson's rule fits a parabola through three equally spaced samples and takes the area under it.
The middle sample gets weight four times that of the ends, because the parabola's area depends most on the height in the middle.
For $f(x) = x^3$ on $[0, 1]$ it gives $\frac{1}{6}\big(0 + 4 \cdot \frac{1}{8} + 1\big) = \frac{1}{4}$, exactly the true value.
Halving the step size reduces the error by a factor of about sixteen.
