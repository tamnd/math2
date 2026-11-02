---
tag: FT9JQA58KJ
kind: concept
name: Calculus of finite differences
msc: [39A12, 39A70]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_difference
---

## Summary

The calculus of finite differences studies functions and sequences through their [[finite differences|7JSQZ126BP]] and sums.
It does so in the way that ordinary calculus uses derivatives and integrals.
Its main tools are the [[forward difference operator|8E0EBA8X07]] $\Delta$, the [[shift operator|MBK6AE6734]] $E = I + \Delta$, and the [[indefinite sum|SMAQN2N739]], which inverts $\Delta$.
Many rules of calculus have exact discrete counterparts, such as [[summation by parts|9G82Z17DKA]] and the [[fundamental theorem of the calculus of finite differences|MNSSV4QHD1]].
It is the basis of the theory of difference equations, of interpolation at equally spaced points, and of closed forms for finite sums.

## Explanations

### L1 human

Ordinary calculus works with infinitely small changes; the calculus of finite differences works with steps of size one.
Differences replace derivatives and sums replace integrals.
The powers $x^k$ are replaced by the [[falling factorials|0SJNCJCCQG]] $(x)_k = x(x-1)\cdots(x-k+1)$, because $\Delta (x)_k = k\,(x)_{k-1}$, just as the derivative of $x^k$ is $k x^{k-1}$.
For example, summing this rule gives $\sum_{x=0}^{n-1} x = \frac{(n)_2}{2} = \frac{n(n-1)}{2}$, the discrete analogue of $\int_0^n x\,dx = \frac{n^2}{2}$.
