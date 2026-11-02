---
tag: N42JDBT0VA
kind: statement
role: theorem
name: Hardy–Littlewood Tauberian theorem
msc: ["40E05", "40G10"]
uses: [D6XWK1NRY1, 0VP56B4EMX, 0QR92XBV6H]
about: [D6XWK1NRY1]
sources:
  - url: https://en.wikipedia.org/wiki/Hardy–Littlewood_Tauberian_theorem
same_as:
  wikidata: Q5656673
  wikipedia: Hardy–Littlewood Tauberian theorem
---

## Statement

Let $(a_n)_{n \ge 0}$ be real numbers with $a_n \ge 0$ for all $n$.
Assume that the [[power series|0VP56B4EMX]] $\sum_{n \ge 0} a_n x^n$ converges for $0 \le x < 1$ and that
$$\sum_{n \ge 0} a_n x^n \sim \frac{1}{1 - x} \quad (x \to 1^-),$$
where $\sim$ denotes [[asymptotic equivalence|0QR92XBV6H]].
Then
$$\sum_{k=0}^{n} a_k \sim n \quad (n \to \infty).$$

## Remarks

Karamata's proof shows first that $(1 - x) \sum_{n} a_n x^n P(x^n) \to \int_0^1 P(t) \, dt$ for every polynomial $P$, by checking it on monomials $P(t) = t^m$.
Then it approximates the function $g$ with $g(t) = 1/t$ on $[e^{-1}, 1]$ and $g(t) = 0$ on $[0, e^{-1})$ from above and below by polynomials with close integrals.
Positivity of $a_n$ makes these approximations compatible with the sums.
Taking $x = e^{-1/n}$, one has $x^k g(x^k) = 1$ for $k \le n$ and $0$ for $k > n$, which isolates the partial sum $\sum_{k \le n} a_k$.

Example: for $a_n = 1 + (-1)^n$, one has $\sum a_n x^n = \frac{1}{1-x} + \frac{1}{1+x} \sim \frac{1}{1-x}$, and indeed $\sum_{k \le n} a_k$ is $n + 2$ or $n + 1$.

Positivity is needed.
For $a_n = 1 + (-1)^n n$, one has $\sum a_n x^n = \frac{1}{1-x} - \frac{x}{(1+x)^2} \sim \frac{1}{1-x}$.
But $\sum_{k=0}^{n} (-1)^k k$ is $\frac{n}{2}$ for even $n$ and $-\frac{n+1}{2}$ for odd $n$, so the partial sums $\sum_{k \le n} a_k$ are close to $\frac{3n}{2}$ or to $\frac{n}{2}$ and are not $\sim n$.

## Explanations

### L1 human

Knowing how a power series with nonnegative coefficients blows up as $x \to 1$ tells you how fast its coefficients add up.
If the power series behaves like $\frac{1}{1-x}$, then the coefficients behave on average like $1$, so their first $n$ add up to about $n$.
The statement is false without the sign condition, since cancellations can hide in the power series.

### L2 human

This theorem is the prototype of Tauberian theorems with positivity conditions, where no condition on the size of single terms is needed.
In terms of $x = e^{-s}$ it says that $\sum a_n e^{-sn} \sim \frac1s$ as $s \to 0^+$ implies $\sum_{k \le n} a_k \sim n$; [[Karamata's Tauberian theorem|DBEGF38V9H]] extends it to Laplace–Stieltjes transforms with regularly varying growth.
The same method of proof gives [[Littlewood's Tauberian theorem|Z35TD4ZZRD]], and the theorem applies to counting problems in number theory where generating functions are easier to estimate than partial sums.
