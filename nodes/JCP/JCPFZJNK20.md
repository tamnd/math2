---
tag: JCPFZJNK20
kind: definition
name: Dimension group
msc: [19K14, 06F20, 46L35]
defines: WSH8TY6MK9
uses: [KRDR04RQ7N]
sources:
  - url: https://en.wikipedia.org/wiki/Approximately_finite-dimensional_C*-algebra
---

## Definition

Let $G$ be an abelian group with a subset $G^+$ such that $G^+ + G^+ \subseteq G^+$, $G^+ \cap (-G^+) = \set{0}$, and $0 \in G^+$.
Write $x \le y$ when $y - x \in G^+$; this makes $G$ a partially [[ordered group|KRDR04RQ7N]].
The pair $(G, G^+)$ is a *dimension group* if:

1. $G$ is directed: $G = G^+ - G^+$.
2. $G$ is unperforated: if $x \in G$, $n \ge 1$ is an integer and $n x \in G^+$, then $x \in G^+$.
3. $G$ has the Riesz interpolation property: if $x_1, x_2, y_1, y_2 \in G$ and $x_i \le y_j$ for all $i, j \in \set{1, 2}$, then there is $z \in G$ with $x_i \le z \le y_j$ for all $i, j$.

## Remarks

Example: $\Z^n$ with $G^+ = \N^n$; it is directed and unperforated, and for interpolation take $z$ coordinatewise as $\max(x_1, x_2)$.
Example: any subgroup $G$ of $\R$ with $G^+ = G \cap [0, \infty)$, such as $\Z + \theta \Z$, is a dimension group, since the order is total.
Non-example: $\Z$ with $G^+ = \set{0, 2, 3, 4, \ldots}$ is a directed partially ordered group, but it is perforated: $2 \cdot 1 = 2 \in G^+$ while $1 \notin G^+$.
Non-example: $\Z^2$ with $G^+ = \set{(a, b) : a > 0, b > 0} \cup \set{(0, 0)}$ is directed and unperforated but fails interpolation: $x_1 = (0, 0)$, $x_2 = (1, -1)$, $y_1 = (2, 2)$, $y_2 = (3, 1)$ satisfy $x_i \le y_j$, but no $z$ lies between them.
Effros–Handelman–Shen theorem: a countable partially ordered abelian group is a dimension group if and only if it is an inductive limit of a sequence of ordered groups $\Z^{n_k}$.
Here each $\Z^{n_k}$ has the coordinatewise order, and the maps are positive homomorphisms.
