---
tag: G4CA22W2XX
kind: definition
name: Banach lattice
msc: [46B42, 46A40]
defines: HDJ1GKG0NA
uses: [06GZ956657, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Banach_lattice
---

## Definition

Let $E$ be a real [[Banach space|06GZ956657]] with norm $\norm{\cdot}$, and let $\le$ be a [[partial order|0QV2JS9RJ3]] on $E$.
The pair is a *Banach lattice* if the following hold.

1. If $x \le y$, then $x + z \le y + z$ for all $z \in E$.
2. If $x \le y$ and $t \ge 0$ is real, then $t x \le t y$.
3. Every two elements $x, y$ have a least upper bound $x \vee y$ in $E$.
4. If $\abs{x} \le \abs{y}$, then $\norm{x} \le \norm{y}$, where $\abs{x} = x \vee (-x)$.

## Remarks

Clauses 1 to 3 say that $E$ is a Riesz space, and clause 4 says that the norm is a lattice norm.

Example: $C(K)$ for a compact Hausdorff space $K$, with $f \le g$ when $f(t) \le g(t)$ for all $t \in K$.
Clauses 1 and 2 are clear, and $f \vee g$ is the pointwise maximum, which is continuous.
Then $\abs{f}$ is the pointwise absolute value, and $\abs{f} \le \abs{g}$ gives $\sup \abs{f} \le \sup \abs{g}$.

Non-example: $\R^2$ with the coordinatewise order and the norm $\norm{(a, b)} = \abs{a} + \abs{a - b}$.
Clauses 1 to 3 hold, and this is a norm.
For $x = (1, 0)$ and $y = (1, 1)$, one has $\abs{x} \le \abs{y}$, but $\norm{x} = 2 > 1 = \norm{y}$, so clause 4 fails.
