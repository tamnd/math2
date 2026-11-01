---
tag: 2FQVQCTV88
kind: concept
name: Integral quadratic form
msc: ["11E12", "11E20"]
specializes: [0RBQS1JJCR]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
---

## Summary

An integral quadratic form is a [[quadratic form|0RBQS1JJCR]] $\sum_{i \le j} a_{ij} x_i x_j$ whose coefficients $a_{ij}$ are integers.
The main questions are arithmetic: which integers the form represents, in how many ways, and when two forms are equivalent under integral changes of variables.
Classical examples are sums of squares, such as $x_1^2 + x_2^2 + x_3^2 + x_4^2$.
Integral quadratic forms correspond to [[lattices|WN9V7WSJKF]] with an integer-valued quadratic function on them.

## Explanations

### L1 human

Take a quadratic polynomial such as $x^2 + xy + y^2$ or $x^2 + y^2 + z^2$ with whole number coefficients.
Plugging in whole numbers gives whole numbers, and one asks which numbers come out.
Lagrange proved that every nonnegative integer is a sum of four squares, so the form $x_1^2 + x_2^2 + x_3^2 + x_4^2$ takes every such value.
The form $x^2 + y^2 + z^2$ misses $7$, since $7$ is not a sum of three squares.
