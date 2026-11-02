---
tag: K7H05NZEX8
kind: definition
name: Limit-point and limit-circle
msc: [34B20, 34B24, 34L05]
defines: 6J9FXT6HAV
uses: [7WV6B2502K, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Sturm–Liouville_theory
---

## Definition

Let $-\infty \le a < b \le \infty$.
Let $p, q, w \colon (a, b) \to \R$ be measurable with $p > 0$ and $w > 0$ almost everywhere, and with $1/p$, $q$ and $w$ locally integrable on $(a, b)$.
For $\lambda \in \C$ consider the [[Sturm–Liouville|7WV6B2502K]] equation
$$-(p y')' + q y = \lambda w y \quad \text{on } (a, b).$$
Its solutions are the functions $y$ such that $y$ and $p y'$ are locally absolutely continuous and the equation holds almost everywhere.
Fix $c \in (a, b)$.
The endpoint $b$ is in the limit-circle case if there is a $\lambda \in \C$ such that every solution $y$ of the equation satisfies
$$\int_c^b \abs{y(x)}^2 w(x) \, dx < \infty.$$
Otherwise $b$ is in the limit-point case.
The same definition applies to the endpoint $a$ with the interval $(a, c)$.

## Remarks

The definition does not depend on $c$.
Weyl's alternative says that if every solution is square integrable near $b$ for one $\lambda \in \C$, then this holds for every $\lambda \in \C$.
For $\lambda \in \C \setminus \R$ there is always at least one nonzero solution that is square integrable near $b$.
So $b$ is limit-point exactly when, for such $\lambda$, this solution is unique up to a constant factor.
Example: for $p = w = 1$, $q = 0$ on $(0, \infty)$ and $\lambda = 0$, the solutions are $y = c_1 + c_2 x$, and $y = 1$ is not square integrable near $\infty$.
By Weyl's alternative, $\infty$ is in the limit-point case.
Non-example of limit-point: a regular endpoint, such as $b < \infty$ with $1/p$, $q$, $w$ integrable near $b$, is always in the limit-circle case, since every solution then extends continuously to $b$.
For $p = w = 1$ and $q(x) = \kappa / x^2$ on $(0, 1]$, the endpoint $0$ is in the limit-point case exactly when $\kappa \ge 3/4$.
If $p = w = 1$ and $q$ is bounded below near $b = \infty$, then $\infty$ is in the limit-point case.

## Explanations

### L1 human

Look at all solutions near the endpoint and ask whether they are square integrable there.
If all of them are, the endpoint is limit-circle; if some are not, it is limit-point.
