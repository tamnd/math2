---
tag: J7GYAF4FGT
kind: definition
name: Multivariate division algorithm
msc: [13P10, 68W30]
defines: T8EN3CAEQF
uses: [04C5ZBG1WT, 0SDC934R52, E874NARWPV, 0MES3KS0ZC, C83KPT47R0]
sources:
  - url: https://en.wikipedia.org/wiki/Gröbner_basis
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]], let $S = k[x_1, \ldots, x_n]$ be the [[polynomial ring|0SDC934R52]], and fix a [[monomial order|E874NARWPV]] on $S$.
For nonzero $h \in S$, let $\operatorname{LT}(h)$ be its leading term.
Let $f \in S$ and let $(g_1, \ldots, g_s)$ be an ordered list of nonzero elements of $S$.
The *multivariate division algorithm* computes $q_1, \ldots, q_s, r \in S$ as follows.

1. Start with $q_1 = \cdots = q_s = 0$, $r = 0$ and $p = f$.
2. While $p \ne 0$: if some $\operatorname{LT}(g_i)$ divides $\operatorname{LT}(p)$, take the least such $i$, and replace $q_i$ by $q_i + \operatorname{LT}(p)/\operatorname{LT}(g_i)$ and $p$ by $p - (\operatorname{LT}(p)/\operatorname{LT}(g_i)) \, g_i$.
3. Otherwise, replace $r$ by $r + \operatorname{LT}(p)$ and $p$ by $p - \operatorname{LT}(p)$.
4. When $p = 0$, return $q_1, \ldots, q_s$ and the *remainder* $r$.

## Remarks

The algorithm stops, because each step makes the leading monomial of $p$ strictly smaller, or makes $p$ zero, and a monomial order is a well-order.
The output satisfies $f = q_1 g_1 + \cdots + q_s g_s + r$.
No monomial of $r$ is divisible by any $\operatorname{LT}(g_i)$, and the leading monomial of $q_i g_i$ is at most that of $f$ whenever $q_i g_i \ne 0$.

Example: in $k[x, y]$ with the lexicographic order $x > y$, divide $f = x^2 y + x y^2 + y^2$ by $(g_1, g_2) = (xy - 1, \; y^2 - 1)$.
The steps give $q_1 = x + y$, $q_2 = 1$ and $r = x + y + 1$; check: $(x + y)(xy - 1) + (y^2 - 1) + x + y + 1 = x^2 y + x y^2 + y^2$.
With the list in the order $(y^2 - 1, \; xy - 1)$, the algorithm gives the quotients $x + 1$ for $y^2 - 1$ and $x$ for $xy - 1$, and the remainder $2x + 1$.
So in general the remainder depends on the order of the list.
For a [[Gröbner basis|C83KPT47R0]], the remainder does not depend on the order, and it is zero exactly when $f$ lies in the ideal $(g_1, \ldots, g_s)$.
