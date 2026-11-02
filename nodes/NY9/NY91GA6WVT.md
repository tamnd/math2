---
tag: NY91GA6WVT
kind: definition
name: Periodic solution of a difference equation
msc: [39A23, 37C25]
defines: 3W358BSRN2
uses: [Q3B6K9HYRG, T75CZ5H47N]
sources:
  - url: https://en.wikipedia.org/wiki/Periodic_point
---

## Definition

Let $k \ge 1$, let $S$ be a set, and let $F \colon S^k \to S$ be a map.
Consider the autonomous difference equation of order $k$
$$x_{n+k} = F(x_n, x_{n+1}, \dots, x_{n+k-1}), \qquad n \ge 0.$$
Let $p \ge 1$ be an integer.
A solution $(x_n)_{n \ge 0}$ is *periodic with period $p$* if it is a [[periodic sequence|Q3B6K9HYRG]] with period $p$, that is, $x_{n+p} = x_n$ for all $n \ge 0$.
Its *prime period* is its least period.

## Remarks

Example: for $x_{n+2} = x_{n+1} / x_n$ on $S = (0, \infty)$ with $x_0 = a$ and $x_1 = b$, the solution is $a, b, b/a, 1/a, 1/b, a/b, a, b, \dots$, so every solution is periodic with period $6$.

Non-example: for $x_{n+1} = 2 x_n$ on $\R$ with $x_0 = 1$, the solution $x_n = 2^n$ is strictly increasing, so $x_{n+p} \ne x_n$ for all $p \ge 1$ and it is not periodic.

For $k = 1$ and $F = f$, the solution starting at $x_0$ is periodic with period $p$ if and only if $f^p(x_0) = x_0$, that is, $x_0$ is a [[periodic point|T75CZ5H47N]] of $f$.
A periodic solution of period $1$ is an equilibrium.
For a non-autonomous equation, one asks for periodic solutions when the equation itself is periodic in $n$.
