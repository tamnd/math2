---
tag: A2KKZAV29W
kind: concept
name: Discrete valuation
msc: [12J20, 13F30]
specializes: [B85T5VKR3M]
sources:
  - url: https://en.wikipedia.org/wiki/Valuation_(algebra)
---

## Summary

A discrete valuation is a [[valuation|B85T5VKR3M]] on a field whose values on nonzero elements are exactly the integers, see the [[definition|ZYK5F0GBK6]].
It counts the power of a fixed "prime" element in each nonzero element.
The [[p-adic valuation|03HDF50VN4]] on $\Q$ and the order of vanishing of a rational function at a point are discrete valuations.
The elements of nonnegative value form a [[discrete valuation ring|MGM3CNJW9V]], one of the basic rings of number theory and algebraic geometry.

## Explanations

### L1 human

A discrete valuation gives each nonzero element an integer, its order, much as the exponent of $p$ in a fraction.
Picture a rational function $f(x)$ near the point $0$: the valuation is the order of the zero of $f$ at $0$, or minus the order of the pole.
For example $x^3/(1 + x)$ has value $3$, and $1/x^2$ has value $-2$.
The values are whole numbers and every integer occurs, which is what "discrete" means here.
