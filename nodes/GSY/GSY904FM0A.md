---
tag: GSY904FM0A
kind: concept
name: Moments and orthogonal polynomials
msc: [44A60, 42C05]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_polynomials
---

## Summary

The [[orthogonal polynomials|8TXASARQN1]] of a measure on the real line depend only on its [[moments|01XAHPADBA]].
Given a moment sequence $(m_n)$ whose [[Hankel matrices|PQ1D8FQB3E]] are positive definite, the monic orthogonal polynomials are explicit quotients of determinants built from the $m_n$.
This link lets one pass between a sequence of numbers, a family of polynomials, a three-term recurrence and a measure.
It is a main tool in the solution of the [[Hamburger moment problem|TBNCFXTMMW]] and in the theory of Gaussian quadrature.

## Explanations

### L1 human

The moments $m_n = \int x^n \, d\mu$ are all one needs to compute integrals of polynomials against $\mu$.
Orthogonality of polynomials is defined by such integrals, so the moments alone determine the orthogonal polynomials.
One can write each orthogonal polynomial as a determinant whose entries are moments, with the powers $1, x, \dots, x^n$ in the last row.
For the uniform weight on $[-1, 1]$ the moments are $2, 0, \tfrac{2}{3}, 0, \tfrac{2}{5}, \dots$, and the determinant formula gives $1$, $x$, $x^2 - \tfrac13$, the monic Legendre polynomials.
