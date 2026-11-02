---
tag: XNPVW5Z126
kind: statement
role: theorem
name: De la Vallée Poussin lower bound
msc: [41A50, 41A10]
uses: [YDN0T4MEX0, 1G0B73WPX8]
about: [YDN0T4MEX0]
sources:
  - url: https://en.wikipedia.org/wiki/Equioscillation_theorem
---

## Statement

Let $a < b$, let $f \colon [a, b] \to \R$ be continuous, let $n \ge 0$, and let $p$ be a real [[polynomial function|1G0B73WPX8]] of degree at most $n$.
Let $a \le x_0 < x_1 < \cdots < x_{n+1} \le b$ be points at which the values $f(x_i) - p(x_i)$ are nonzero and alternate in sign.
Then the [[error of best approximation|YDN0T4MEX0]] of $f$ by polynomials of degree at most $n$ in the supremum norm satisfies
$$E_n(f) \ge \min_{0 \le i \le n+1} \abs{f(x_i) - p(x_i)}.$$

## Remarks

The idea of the proof: let $\mu$ be the minimum on the right and suppose some polynomial $q$ of degree at most $n$ has $\norm{f - q}_\infty < \mu$.
At each $x_i$, the difference $q - p = (f - p) - (f - q)$ has the sign of $f(x_i) - p(x_i)$, because $\abs{f(x_i) - q(x_i)} < \mu \le \abs{f(x_i) - p(x_i)}$.
So $q - p$ alternates in sign at $n + 2$ points and has at least $n + 1$ zeros, hence $q = p$.
But then $\norm{f - q}_\infty \ge \mu$, a contradiction.

Example: for $f(x) = x^2$ on $[0, 1]$, $n = 1$ and $p(x) = x - 1/10$, the error $x^2 - x + 1/10$ takes the values $1/10, -3/20, 1/10$ at $0, 1/2, 1$.
So $E_1(f) \ge 1/10$, while $\norm{f - p}_\infty = 3/20$ gives $E_1(f) \le 3/20$; the true value is $1/8$.

The number of points matters: with only $n + 1$ alternation points no lower bound follows.
For $f(x) = x$, $n = 1$ and $p = 1/2$, the error $x - 1/2$ takes the values $-1/2, 1/2$ at $0, 1$, but $E_1(f) = 0$.

## Explanations

### L1 human

If an approximation's error changes sign enough times, then no approximation of the same degree can be much better.
The theorem turns this into a number: the best possible error is at least the smallest of the alternating error values.
Together with the actual error of $p$, it gives a two-sided bound on the best achievable error.

### L2 human

The bound is the easy half of the equioscillation theorem: when all the alternating values equal $\norm{f - p}_\infty$, it shows $p$ is best.
In the Remez algorithm it certifies progress, since each iteration produces a polynomial and a set of $n + 2$ alternation points, and the lower and upper bounds squeeze $E_n(f)$.
The same argument works for any Haar subspace of dimension $n + 1$.
