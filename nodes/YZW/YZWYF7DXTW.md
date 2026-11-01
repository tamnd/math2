---
tag: YZWYF7DXTW
kind: concept
name: Field of formal Laurent series
msc: [13F25, 12J10]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_power_series
---

## Summary

The field of formal Laurent series $k((X))$ over a field $k$ consists of formal sums $\sum_{n \ge N} a_n X^n$, see the [[definition|2S4K8FA8QY]].
Only finitely many negative powers of $X$ occur.
It is the [[field of fractions|0F2PTGX1A2]] of the ring $k[\![X]\!]$ of [[formal power series|033WGN00BF]].
With the order of the lowest term it is a complete field for a [[discrete valuation|A2KKZAV29W]], the equal-characteristic analogue of the [[p-adic numbers|BT6T702C28]].
It is the formal counterpart of the [[Laurent series|0GXMPDNYX3]] of complex analysis, without any condition of convergence.

## Explanations

### L1 human

A formal Laurent series is like a power series that may start with a few negative powers, such as $X^{-2} + 3X^{-1} + 1 + X + X^2 + \cdots$.
One adds them term by term and multiplies them like polynomials; each coefficient of a product is a finite sum because there are only finitely many negative powers.
Every nonzero series has an inverse: $1/(X - X^2) = X^{-1}(1 + X + X^2 + \cdots)$.
So these series form a field.
No question of convergence arises: the series are only lists of coefficients.
