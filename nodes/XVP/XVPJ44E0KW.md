---
tag: XVPJ44E0KW
kind: definition
name: Supporting hyperplane
msc: [52A20]
defines: K7N565NKCV
uses: [0XPR1E85W0, 0S52TNNTH9, 05D5EGMFYV, 1H92CYA4ZC]
sources:
  - url: https://en.wikipedia.org/wiki/Supporting_hyperplane
---

## Definition

Let $n \ge 1$ and let $S \subseteq \R^n$.
A hyperplane $H = \set{x \in \R^n : a \cdot x = b}$, with $a \in \R^n \setminus \set{0}$ and $b \in \R$, is a *supporting hyperplane* of $S$ if:

1. $S$ lies in one of the closed half-spaces of $H$, say $a \cdot x \le b$ for all $x \in S$;
2. $H$ contains at least one point of the [[boundary|05D5EGMFYV]] of $S$.

Here $a \cdot x$ is the [[dot product|0S52TNNTH9]].
If $x_0 \in H$ is such a boundary point, $H$ supports $S$ at $x_0$.

## Remarks

Example: for the closed unit disc $D \subseteq \R^2$ and $a = (0, 1)$, $b = 1$, the line $y = 1$ supports $D$ at $(0, 1)$.
Each $(x, y) \in D$ has $y \le 1$, and $(0, 1)$ is a boundary point of $D$ on the line.

Non-example: the line $y = 2$ satisfies clause 1 for $D$, but it misses $D$ and its boundary, so clause 2 fails.
The line $y = 0$ meets the boundary of $D$ but has points of $D$ on both sides, so clause 1 fails.

In terms of the [[support function|1H92CYA4ZC]] $h_S$, when $S$ is closed and bounded and nonempty, the hyperplane $a \cdot x = h_S(a)$ is the supporting hyperplane with outer normal $a$.
