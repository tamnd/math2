---
tag: N4FACX7QSW
kind: definition
name: Holonomic function
msc: [33F10, 34M03, 12H05]
defines: 7H44JD9NQD
uses: [033WGN00BF, 0SDC934R52, 0QQRP17Z7S]
sources:
  - url: https://en.wikipedia.org/wiki/Holonomic_function
---

## Definition

Let $K$ be a field of characteristic $0$, for example $\C$.
A [[formal power series|033WGN00BF]] $f \in K[\![x]\!]$ is *holonomic* (or *D-finite*) if there are an integer $r \ge 0$ and polynomials $p_0, p_1, \ldots, p_r \in K[x]$ with $p_r \ne 0$ such that
$$p_r(x) f^{(r)}(x) + \cdots + p_1(x) f'(x) + p_0(x) f(x) = 0.$$
Here $f^{(k)}$ is the $k$-th formal derivative of $f$ and $K[x]$ is the [[polynomial ring|0SDC934R52]].
An analytic function on an open set of $\C$ is holonomic if it satisfies such an equation with $K = \C$.

## Remarks

Example: $f(x) = \frac{1}{1 - x} = \sum_{n \ge 0} x^n$ satisfies $(1 - x) f'(x) - f(x) = 0$, since $f'(x) = \frac{1}{(1-x)^2}$; here $r = 1$, $p_1 = 1 - x$ and $p_0 = -1$.
Non-example: $\tan x$ is not holonomic.
An analytic holonomic function extends along paths avoiding the finitely many zeros of $p_r$, so it has only finitely many singularities, while $\tan$ has poles at all points $\frac{\pi}{2} + k\pi$.
Equivalently, $f$ is holonomic if and only if the derivatives $f, f', f'', \ldots$ span a finite-dimensional vector space over the field of [[rational functions|0XDK9CGYKJ]] $K(x)$.
Another equivalent form: $f = \sum_n a_n x^n$ is holonomic if and only if its coefficients satisfy a [[recurrence|0FYX44GP92]] $q_d(n) a_{n+d} + \cdots + q_0(n) a_n = 0$ for all $n$, with polynomials $q_i$ not all zero; such sequences are called P-recursive.

## Explanations

### L1 human

A holonomic function is one that obeys a linear differential equation with polynomial coefficients.
The exponential $e^x$ is the simplest example: it satisfies $f' - f = 0$.
