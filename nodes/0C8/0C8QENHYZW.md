---
tag: 0C8QENHYZW
kind: definition
name: Möbius function
msc: [11A25]
defines: 0FANE7P0DY
uses: [004JW7A2N5, 0YVVXT3A0B]
sources:
  - url: https://en.wikipedia.org/wiki/M%C3%B6bius_function
    locator: Definition
---

## Definition

The Möbius function $\mu$ is the arithmetic function given, for each positive integer $n$, by
$$\mu(n) = \begin{cases} (-1)^{\omega(n)} & \text{if } n \text{ is squarefree}, \\ 0 & \text{otherwise}. \end{cases}$$
Here $\omega(n)$ is the [[number of distinct prime factors|0YVVXT3A0B]] of $n$, and squarefree has the meaning of the [[definition of a squarefree integer|004JW7A2N5]].

## Remarks

So $\mu(1) = 1$, $\mu(p) = -1$ for each prime $p$, and $\mu(n) = 0$ when $p^2 \mid n$ for some prime $p$.
For example, $\mu(6) = 1$, $\mu(30) = -1$ and $\mu(12) = 0$.
The function $\mu$ is [[multiplicative|0VB9G5B034]], and it is the [[inverse of the constant function 1|0ASC73QEQT]] for the Dirichlet convolution.

## Explanations

### L1 human

The Möbius function is $0$ on numbers with a repeated prime factor.
On the other numbers, it is $1$ for an even number of prime factors and $-1$ for an odd number.
It is the sign rule of inclusion and exclusion, written as a function of $n$.
