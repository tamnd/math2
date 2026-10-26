---
tag: 0BYZTFM0DJ
kind: statement
role: theorem
name: Zero derivative on a connected open set implies constant
msc: [26B05]
uses: [02CYB184RC, 0135XZZQ8M]
sources:
  - url: https://en.wikipedia.org/wiki/Mean_value_theorem
    locator: Mean value theorem in several variables
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be a connected open set and let $f \colon U \to \mathbb{R}^m$ be [[differentiable|0135XZZQ8M]] on $U$.
Suppose that $Df(x) = 0$ for each $x \in U$.
Then $f$ is constant on $U$.

## Remarks

The proof fixes $a \in U$ and shows that the set $S = \{x \in U : f(x) = f(a)\}$ is open and closed in $U$. It is open by the [[mean value inequality|02CYB184RC]] with $M = 0$ on small balls, and closed because $f$ is continuous. As $U$ is connected and $a \in S$, $S = U$.
Connectedness is needed: on $U = (0, 1) \cup (2, 3)$, the function that is $0$ on the first interval and $1$ on the second has derivative $0$ but is not constant.
For real-valued $f$, the condition $Df = 0$ means that all partial derivatives of $f$ vanish on $U$.

## Explanations

### L1 human

Suppose that $f$ does not change in any direction at any point, and that the domain is in one piece. Then $f$ cannot change at all.
On a domain in two pieces, $f$ can take a different constant value on each piece.
