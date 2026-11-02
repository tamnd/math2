---
tag: MP8X04H1ZD
kind: definition
name: Function approximation
msc: [41A65, 41A30]
defines: VNWH2KADN7
uses: [03J5RAKB30, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Function_approximation
---

## Definition

Let $S$ be a set and let $X$ be a [[normed vector space|03J5RAKB30]] of [[functions|0EPAT51DXQ]] on $S$.
Let $A \subseteq X$ be a nonempty subset, the approximating class.
Let $f \in X$ and $\varepsilon > 0$.
An *approximation of $f$ from $A$ within $\varepsilon$* is a function $g \in A$ with $\norm{f - g} \le \varepsilon$.
The function $f$ *can be approximated arbitrarily well from $A$* if such a $g$ exists for every $\varepsilon > 0$.
Equivalently, $f$ lies in the closure of $A$.

## Remarks

Example: take $X = C[0, 1]$ with the supremum norm, $A$ the polynomials of degree at most $2$, and $f(x) = e^x$.
The function $g(x) = 1 + x + x^2/2$ is an approximation within $0.22$.
Indeed $e^x - g(x)$ is increasing on $[0, 1]$, since its derivative $e^x - 1 - x$ is nonnegative, so its maximum is $e - 2.5 < 0.22$.

Non-example: on $[-1, 1]$ with the supremum norm, the sign function cannot be approximated within any $\varepsilon < 1$ by continuous functions.
Let $g$ be continuous with $g(0) = c$.
Near $0$ the gaps $\abs{1 - g(x)}$ for $x > 0$ and $\abs{-1 - g(x)}$ for $x < 0$ come close to $\abs{1 - c}$ and $\abs{1 + c}$.
One of these two numbers is at least $1$.

The choice of norm matters: the sign function can be approximated arbitrarily well by continuous functions in the $L^2$ norm.
