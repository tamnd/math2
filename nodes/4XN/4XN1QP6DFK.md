---
tag: 4XN1QP6DFK
kind: statement
role: theorem
name: Generating function of the central binomial coefficients
msc: [05A15]
uses: [01WHD9T0V6, 0HH6JX5WZZ]
about: [0JPH2Y4DFV, 0PHAC833JF]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_genfunction_binom-app.ptx#L52
    locator: source/s_genfunction_binom-app.ptx:52
---

## Statement

The function $f(x) = (1 - 4x)^{-1/2}$ is the [[generating function|0HH6JX5WZZ]] of the sequence of [[central binomial coefficients|01WHD9T0V6]]. That is,
$$(1 - 4x)^{-1/2} = \sum_{n \ge 0} \binom{2n}{n} x^n.$$

## Remarks

The power $(1 - 4x)^{-1/2}$ is expanded by the binomial series.
The first terms are $1 + 2x + 6x^2 + 20x^3 + 70x^4 + \cdots$.
