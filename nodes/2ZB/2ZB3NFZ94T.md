---
tag: 2ZB3NFZ94T
kind: concept
name: Hermitian kernel
msc: [45C05, 45P05]
specializes: [GSMBXT7FPK]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%E2%80%93Schmidt_integral_operator
---

## Summary

A Hermitian kernel is a complex-valued [[kernel|GSMBXT7FPK]] with $K(x, s) = \overline{K(s, x)}$ for all $x$ and $s$.
It is the continuous analogue of a [[Hermitian matrix|0P17NGQQMQ]].
A square-integrable Hermitian kernel gives a [[self-adjoint operator|0NEGN5CRSC]] on $L^2$, so its characteristic values are real and its eigenfunctions can be chosen orthonormal.
The Hilbert–Schmidt theory of integral equations is built on such kernels.

## Explanations

### L1 human

Swapping the two variables of a Hermitian kernel gives its complex conjugate.
For a real kernel this simply means that the kernel is symmetric in its two variables.
It mirrors the rule $a_{ij} = \overline{a_{ji}}$ for the entries of a Hermitian matrix.
For example, $K(x, s) = e^{i (x - s)}$ is Hermitian, while $K(x, s) = i$ is not.
