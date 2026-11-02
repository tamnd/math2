---
tag: HRCQ3JHYY0
kind: concept
name: Rayleigh quotient for symmetric kernels
msc: [45C05, 47A75]
specializes: [06WHP8SE98]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient
---

## Summary

Let $K$ be a Hermitian kernel with integral operator $T_K$.
The Rayleigh quotient of $K$ at a nonzero function $\varphi$ is the real number $\ip{T_K \varphi}{\varphi} / \ip{\varphi}{\varphi}$.
It is the integral analogue of the [[Rayleigh quotient|06WHP8SE98]] of a Hermitian matrix.
Its extreme values and critical points give the eigenvalues and eigenfunctions of $T_K$, which turns eigenvalue problems for integral equations into problems of optimization.

## Explanations

### L1 human

The Rayleigh quotient measures how much the integral operator stretches a function in its own direction.
The function that is stretched the most is an eigenfunction, and the amount of stretching is the largest eigenvalue.
For $K(x, y) = xy$ on $[0, 1]$ and $\varphi = 1$, the quotient is $1/4$, while for the eigenfunction $\varphi(x) = x$ it reaches the maximum $1/3$.
