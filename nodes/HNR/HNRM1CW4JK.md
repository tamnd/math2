---
tag: HNRM1CW4JK
kind: definition
name: Absolutely monotonic function
msc: [26A48]
defines: QQSPWH4NG9
uses: [0V33BNKZ9S, 04TKTF8KDK, 0Q1D85B8G6]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_on_monotone_functions
---

## Definition

Let $I \subseteq \R$ be an open [[interval|0Q1D85B8G6]] and let $f \colon I \to \R$ be [[infinitely differentiable|0V33BNKZ9S]].
The function $f$ is *absolutely monotonic* on $I$ if $f^{(k)}(x) \ge 0$ for every integer $k \ge 0$ and every $x \in I$.
Here $f^{(0)} = f$ and $f^{(k)}$ is the [[derivative of order $k$|04TKTF8KDK]].
The function $f$ is *completely monotone* on $I$ if $(-1)^k f^{(k)}(x) \ge 0$ for every $k \ge 0$ and every $x \in I$.

## Remarks

Example: $f(x) = e^{x}$ on $\R$ is absolutely monotonic, since $f^{(k)}(x) = e^x > 0$ for all $k$.
Likewise $g(x) = e^{-x}$ is completely monotone, since $(-1)^k g^{(k)}(x) = e^{-x} > 0$.
Non-example: $f(x) = x^3$ on $(-1, 1)$ fails at $k = 0$, since $f(-\tfrac{1}{2}) < 0$, although $f^{(3)} = 6 > 0$.
The function $f$ is absolutely monotonic on $I$ if and only if $x \mapsto f(-x)$ is completely monotone on $-I$.
On an interval that contains an endpoint, such as $[0, \infty)$, one asks the inequalities on the interior and continuity of $f$ at the endpoint.

## Explanations

### L1 human

Every derivative, starting with the function itself, is nonnegative.
So the function is nonnegative, increasing, convex, and its convexity keeps increasing, without end.
