---
tag: QFF87AXWN2
kind: statement
role: theorem
name: Bohr–Mollerup theorem
msc: [33B15, 26A51]
uses: [0V3FZMVB4K, 8FRWATNNMX, 0VV0HSW1ZS, 0044CPHJBV]
about: [0V3FZMVB4K]
sources:
  - url: https://en.wikipedia.org/wiki/Bohr%E2%80%93Mollerup_theorem
same_as:
  wikidata: Q2734084
  wikipedia: Bohr–Mollerup theorem
---

## Statement

Let $f \colon (0, \infty) \to (0, \infty)$ be a function such that:

1. $f(1) = 1$;
2. $f(x + 1) = x f(x)$ for every $x > 0$;
3. $\ln f$ is [[convex|0VV0HSW1ZS]] on $(0, \infty)$.

Then $f(x) = \Gamma(x)$ for every $x > 0$, where $\Gamma$ is the [[gamma function|0V3FZMVB4K]].

## Remarks

The gamma function satisfies the three conditions; its [[log-convexity|8FRWATNNMX]] follows from Hölder's inequality applied to $\Gamma(x) = \int_0^\infty t^{x-1} e^{-t}\, dt$.
For uniqueness, conditions 1 and 2 give $f(n + 1) = n!$, so the values at integers are fixed.
Fix $0 < x \le 1$ and an integer $n \ge 2$.
Convexity of $\ln f$ compares its slope on $[n, n + x]$ with its slopes on $[n - 1, n]$ and $[n, n + 1]$.
This squeezes $f(n + x)$ between two explicit bounds, and condition 2 turns them into bounds for $f(x)$.
Letting $n \to \infty$ yields $f(x) = \lim_{n \to \infty} \frac{n!\, n^x}{x (x + 1) \cdots (x + n)}$, the same limit for every such $f$.
Without condition 3 uniqueness fails: $f(x) = \Gamma(x)\,(1 + \frac12 \sin(2\pi x))$ satisfies conditions 1 and 2, takes positive values, and differs from $\Gamma$ at $x = \frac14$.

## Explanations

### L1 human

Many functions interpolate the factorials, taking the value $(n-1)!$ at each positive integer $n$.
The theorem says that the gamma function is the only one that obeys the rule $f(x + 1) = x f(x)$ and whose logarithm bends upward everywhere.
So the gamma function is not an arbitrary choice: it is the natural extension of the factorial.

### L2 human

The theorem is a convenient way to prove identities for $\Gamma$: show that the other side satisfies the three conditions.
For example, it gives the formula $B(x, y) = \Gamma(x)\Gamma(y)/\Gamma(x + y)$ for the [[beta function|QHNWVSC6AQ]], by applying the theorem to $x \mapsto B(x, y)\,\Gamma(x + y)/\Gamma(y)$ for fixed $y$.
It also gives the Gauss product formula for $\Gamma$ and the Legendre duplication formula.
It links the theory of [[convex functions|0VV0HSW1ZS]] with special functions.
