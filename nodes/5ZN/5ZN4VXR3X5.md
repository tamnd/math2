---
tag: 5ZN4VXR3X5
kind: definition
name: Perron integral
msc: [26A39]
defines: M077AXJACA
uses: [0F1WR9C83K, 0BTMQ04556, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Henstock%E2%80%93Kurzweil_integral
---

## Definition

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a function.
For $U \colon [a, b] \to \R$ and $x \in [a, b]$, the lower and upper derivatives of $U$ at $x$ are
$$\underline{D} U(x) = \liminf_{y \to x} \frac{U(y) - U(x)}{y - x}, \qquad \overline{D} U(x) = \limsup_{y \to x} \frac{U(y) - U(x)}{y - x},$$
where $y$ ranges over $[a, b] \setminus \set{x}$.
A *major function* of $f$ is a function $U$ with $\underline{D} U(x) \ne -\infty$ and $\underline{D} U(x) \ge f(x)$ for every $x \in [a, b]$.
A *minor function* of $f$ is a function $V$ with $\overline{D} V(x) \ne +\infty$ and $\overline{D} V(x) \le f(x)$ for every $x \in [a, b]$.
Let $\mathcal{U}$ be the set of major functions and $\mathcal{V}$ the set of minor functions of $f$.
The function $f$ is *Perron integrable* on $[a, b]$ if both sets are nonempty and
$$\inf_{U \in \mathcal{U}} \bigl(U(b) - U(a)\bigr) = \sup_{V \in \mathcal{V}} \bigl(V(b) - V(a)\bigr) \in \R.$$
The *Perron integral* of $f$ is this value.

## Remarks

For any major function $U$ and minor function $V$, the difference $U - V$ is nondecreasing, so $V(b) - V(a) \le U(b) - U(a)$ always holds.

Example: if $F$ is differentiable at every point of $[a, b]$ and $f = F'$, then $F$ is both a major and a minor function of $f$.
So $f$ is Perron integrable with integral $F(b) - F(a)$, even when $f$ is not Lebesgue integrable.

Non-example: $f(x) = 1/x$ for $0 < x \le 1$ and $f(0) = 0$ is not Perron integrable on $[0, 1]$.
A nonnegative Perron integrable function is Lebesgue integrable, and $\int_0^1 dx / x = \infty$.

A function is Perron integrable if and only if it is [[Henstock–Kurzweil integrable|FCGHXDGVV9]], and the two integrals agree.
