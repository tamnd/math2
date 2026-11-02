---
tag: 7P72CCAMGZ
kind: definition
name: Sturm–Liouville theory
msc: [34B24, 34B09]
defines: 7WV6B2502K
uses: [TM8VQJWGHZ, 0BQAA2BK3Q, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm–Liouville_theory
---

## Definition

Let $a < b$ be real numbers.
Let $p \in C^1([a, b])$ and $q, w \in C([a, b])$ be real functions with $p(x) > 0$ and $w(x) > 0$ for all $x \in [a, b]$.
Let $\alpha_1, \alpha_2, \beta_1, \beta_2$ be real numbers with $(\alpha_1, \alpha_2) \ne (0, 0)$ and $(\beta_1, \beta_2) \ne (0, 0)$.
The regular Sturm–Liouville problem with these data is the [[boundary value problem|TM8VQJWGHZ]]
$$-(p y')' + q y = \lambda w y \quad \text{on } [a, b],$$
$$\alpha_1 y(a) + \alpha_2 y'(a) = 0, \qquad \beta_1 y(b) + \beta_2 y'(b) = 0,$$
where $\lambda$ is a complex parameter.
A number $\lambda$ is an eigenvalue of the problem if the problem has a solution $y \in C^2([a, b])$ that is not identically zero.
Such a $y$ is an eigenfunction for $\lambda$.
Sturm–Liouville theory is the study of the eigenvalues and eigenfunctions of such problems.
It also studies singular versions, where the interval is unbounded or the coefficients are singular at an end.

## Remarks

Example: $p = w = 1$, $q = 0$ on $[0, \pi]$ with $y(0) = y(\pi) = 0$.
Then $y = \sin(nx)$ satisfies $-y'' = n^2 y$ and both boundary conditions, so $n^2$ is an eigenvalue for each $n \ge 1$.
Non-example: the problem $-y'' = \lambda y$ with $y(0) = y(2\pi)$, $y'(0) = y'(2\pi)$ is not a regular Sturm–Liouville problem in this sense.
Its [[periodic boundary conditions|3FW4J270FV]] are not separated, and the eigenvalue $1$ then has the two eigenfunctions $\cos x$ and $\sin x$.
With the inner product $\langle f, g \rangle = \int_a^b f \overline{g}\, w \, dx$, the operator $y \mapsto \frac{1}{w}(-(p y')' + q y)$ with these boundary conditions is symmetric.
This is why the eigenvalues are real and eigenfunctions for distinct eigenvalues are orthogonal.

## Explanations

### L1 human

A Sturm–Liouville problem is a second-order linear equation with a free number $\lambda$ and one condition at each end.
For most values of $\lambda$ only the zero function fits; the special values where a nonzero solution fits are the eigenvalues.
