---
tag: NV54MWKT6T
kind: statement
role: theorem
name: Tauberian theorems for integral transforms
msc: ["40E05", 44A10]
uses: [05XT5AVJBK, D6XWK1NRY1, 6ZDP261K7R, DBEGF38V9H, N42JDBT0VA]
about: [0V49JEZW06, D6XWK1NRY1]
sources:
  - url: https://en.wikipedia.org/wiki/Abelian_and_Tauberian_theorems
---

## Statement

Let $f \colon [0, \infty) \to \R$ be locally integrable with $f(t) \ge 0$ for all $t$.
Assume that its [[Laplace transform|05XT5AVJBK]] $F(s) = \int_0^\infty f(t) e^{-st}\, dt$ is finite for every $s > 0$.
Let $c \ge 0$.
If $s F(s) \to c$ as $s \to 0^+$, then
$$\frac{1}{T} \int_0^T f(t)\, dt \to c \quad (T \to \infty).$$

## Remarks

This is the Hardy–Littlewood Tauberian theorem for the Laplace transform; the condition $f \ge 0$ is the [[Tauberian condition|6ZDP261K7R]].
For $c > 0$ it is the case $\rho = 1$ of [[Karamata's Tauberian theorem|DBEGF38V9H]], applied to $U(x) = \int_0^x f(t)\, dt$.
The proof follows Karamata.
One shows $s\int_0^\infty f(t) e^{-st} P(e^{-st})\, dt \to c \int_0^1 P(x)\, dx$ for polynomials $P$.
Then one approximates an indicator function by polynomials from above and below, using $f \ge 0$.
The Tauberian condition cannot be dropped.
Let $a_n = 1 + (-1)^n n$ and let $f = a_n$ on $[n, n + 1)$; then $sF(s) = (1 - x)\sum_n a_n x^n$ with $x = e^{-s}$, which tends to $1$ as $s \to 0^+$, as in the [[Hardy–Littlewood Tauberian theorem|N42JDBT0VA]] for series.
But $\frac{1}{N} \int_0^N f = \frac{1}{N} \sum_{k < N} a_k$ is close to $3/2$ for odd $N$ and to $1/2$ for even $N$, so it has no limit.
Converse direction: the Abelian theorem gives $sF(s) \to c$ from the convergence of the averages, with no sign condition (see [[Abelian theorems for integral transforms|16W9PP8ET0]]).

## Explanations

### L1 human

The Laplace transform smooths a function out, so knowing how the transform behaves does not, in general, tell how the function behaves.
A Tauberian theorem says that it does, provided the function cannot oscillate wildly.
Here the extra condition is that $f$ is never negative: then a limit of $sF(s)$ at $0$ forces the long-run average of $f$ to have the same limit.

### L2 human

Tauberian theorems are partial converses of Abelian theorems, and each needs a side condition such as positivity, monotonicity or a growth bound.
Karamata's theorem extends the statement to regularly varying growth, with a factor $\Gamma(1 + \rho)$.
Wiener's Tauberian theorem treats general convolution kernels.
The Wiener–Ikehara theorem, a Tauberian theorem for the Laplace transform with a condition on the boundary line, gives a short proof of the prime number theorem.
In probability, this theorem relates the behaviour of a Laplace transform near $0$ to the tail of a distribution.
