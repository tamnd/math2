---
tag: F0YGC89S9R
kind: statement
role: theorem
name: Bernstein's inequality for polynomials
msc: [41A17, 30C10, 26D05]
uses: [0Q9EZS90GY, 0DPF6WRZW6, 09FTAET5Z4]
about: [0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_(polynomials)
same_as:
  wikidata: Q25345912
  wikipedia: Bernstein's theorem (polynomials)
---

## Statement

Let $n \ge 0$ and let $P$ be a polynomial with [[complex|09FTAET5Z4]] coefficients of [[degree|0DPF6WRZW6]] at most $n$.
Then
$$\max_{\abs{z} = 1} \abs{P'(z)} \le n \max_{\abs{z} = 1} \abs{P(z)}.$$
Equality holds if and only if $P(z) = a z^n$ for some $a \in \C$.

## Remarks

Proof idea: let $M = \max_{\abs{z} = 1} \abs{P(z)} > 0$ and let $\lambda \in \C$ with $\abs{\lambda} > 1$.
On $\abs{z} = 1$ one has $\abs{\lambda M z^n} > \abs{P(z)}$, so by Rouché's theorem all $n$ roots of $P(z) - \lambda M z^n$ lie in $\abs{z} < 1$.
By the [[Gauss–Lucas theorem|A56086N8XQ]], so do the roots of $P'(z) - \lambda n M z^{n-1}$.
If $\abs{P'(z_0)} > n M$ for some $\abs{z_0} = 1$, then $\lambda = P'(z_0) / (n M z_0^{n-1})$ has $\abs{\lambda} > 1$ and makes $z_0$ such a root, a contradiction.

The inequality has an equivalent trigonometric form: a real or complex trigonometric polynomial $T$ of degree at most $n$ satisfies $\max \abs{T'} \le n \max \abs{T}$.
With $x = \cos \theta$, the trigonometric form gives, for a real polynomial $P$ of degree at most $n$ and $-1 < x < 1$, the bound $\abs{P'(x)} \le \frac{n}{\sqrt{1 - x^2}} \max_{[-1, 1]} \abs{P}$.

Example: $P(z) = z^n$ gives $\abs{P'(z)} = n$ on the unit circle, so equality holds.

## Explanations

### L1 human

A polynomial of degree $n$ that is at most $1$ in size on the unit circle has derivative at most $n$ there.
The pure power $z^n$, which turns around the circle $n$ times as fast, is the extreme case.

### L2 human

Bernstein's inequality is the basic tool for inverse theorems in approximation theory: good approximation by polynomials of low degree forces smoothness.
Its form on $[-1, 1]$ is sharp in the interior, while near the endpoints the [[Markov brothers' inequality|EHA5MF9VKE]] gives the correct bound $n^2$.
The proof through the Gauss–Lucas theorem shows how geometric facts about roots give analytic estimates.
