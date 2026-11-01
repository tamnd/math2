---
tag: D5BDZZW9D4
kind: definition
name: Puiseux series
msc: [13F25, 14H20, 12J25]
defines: SENTYNSKSF
uses: [YZWYF7DXTW, 0QA8CHH8MG]
sources:
  - url: https://en.wikipedia.org/wiki/Puiseux_series
---

## Definition

Let $k$ be a [[field|0QA8CHH8MG]] and let $X$ be a variable.
Let $m$ be a positive integer, $N$ an integer, and $a_n \in k$ for all $n \ge N$.
A *Puiseux series* in $X$ over $k$ is a formal sum of the form
$$f = \sum_{n \ge N} a_n X^{n/m}.$$
Equivalently, $f$ is an element of the [[field of formal Laurent series|YZWYF7DXTW]] $k((X^{1/m}))$ in the variable $X^{1/m}$, for some $m \ge 1$.

For $m \mid m'$, the field $k((X^{1/m}))$ is identified with a subfield of $k((X^{1/m'}))$ through $X^{1/m} = (X^{1/m'})^{m'/m}$.
The field of Puiseux series is the union $\bigcup_{m \ge 1} k((X^{1/m}))$ with these identifications.

## Remarks

Example: $f = X^{1/2}$ is a Puiseux series with $m = 2$, and it is a root of $Y^2 - X$ in the field of Puiseux series, since $(X^{1/2})^2 = X$ in $k((X^{1/2}))$.
Non-example: the formal sum $\sum_{n \ge 1} X^{1 - 1/n}$ has the exponents $0, 1/2, 2/3, 3/4, \ldots$, whose denominators are unbounded, so there is no single $m$ and it is not a Puiseux series.
The union is a field because any two Puiseux series lie in a common field $k((X^{1/m}))$.
The order $v(f)$ of the lowest exponent with nonzero coefficient is a valuation on the field of Puiseux series with value group $\Q$.
