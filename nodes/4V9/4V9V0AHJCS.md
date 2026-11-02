---
tag: 4V9V0AHJCS
kind: definition
name: Characteristic value of a kernel
msc: [45C05, 47A75]
defines: DC7HMHVREP
uses: [WWMWX7AD4V, W6CYS54QXS, 4NSACSWRJZ]
sources:
  - url: https://en.wikipedia.org/wiki/Eigenvalues_and_eigenvectors
---

## Definition

Let $a < b$ and let $K \in L^2([a, b] \times [a, b])$ be a [[square-integrable kernel|WWMWX7AD4V]].
A number $\lambda \in \C$ is a *characteristic value* of $K$ if the [[homogeneous equation|W6CYS54QXS]]
$$\varphi(x) = \lambda \int_a^b K(x, y) \, \varphi(y) \, dy$$
has a solution $\varphi \in L^2[a, b]$ that is not $0$ almost everywhere.

## Remarks

A characteristic value is never $0$, since for $\lambda = 0$ the equation forces $\varphi = 0$.
So $\lambda$ is a characteristic value exactly when $1/\lambda$ is an eigenvalue of the integral operator $T_K$, and the nonzero solutions $\varphi$ are the [[eigenfunctions|4NSACSWRJZ]] for $1/\lambda$.

Example: for $K(x, y) = xy$ on $[0, 1]$, the number $\lambda = 3$ is a characteristic value with solution $\varphi(x) = x$, since $3 \int_0^1 x y \cdot y \, dy = 3 \cdot x/3 = x$.

Non-example: for the same kernel, $\lambda = 1$ is not a characteristic value.
Every solution has the form $\varphi(x) = c x$ with $c = \int_0^1 y \varphi(y) \, dy = c/3$, so $c = 0$ and $\varphi = 0$.

Many classical texts call $\lambda$ an eigenvalue of the kernel; the name characteristic value avoids confusion with the eigenvalue $1/\lambda$ of the operator.
A kernel may have no characteristic value at all: the Volterra kernel, equal to $1$ for $y \le x$ and $0$ otherwise, is an example.
