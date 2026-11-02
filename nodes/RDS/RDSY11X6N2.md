---
tag: RDSY11X6N2
kind: definition
name: Relation algebra
msc: ["03G15"]
defines: GQK4DSA11K
uses: [0XADJKM699, 0N6R902FG1, 05AVARPXA2, 0PYSR20HGF, 054K3HNN5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Relation_algebra
---

## Definition

A *relation algebra* is a structure $(A, \vee, \wedge, -, 0, 1, ;, c, 1')$, where $;$ is a binary operation, $c$ is a unary operation and $1'$ is an element of $A$.
Write $\breve{x}$ for $c(x)$.
The following hold for all $x, y, z \in A$:

1. $(A, \vee, \wedge, -, 0, 1)$ is a [[Boolean algebra|0XADJKM699]], with order $\le$.
2. $(A, ;, 1')$ is a [[monoid|0N6R902FG1]].
3. $(x \vee y) ; z = (x ; z) \vee (y ; z)$.
4. $\breve{\breve{x}} = x$ and $\breve{(x \vee y)} = \breve{x} \vee \breve{y}$.
5. $\breve{(x ; y)} = \breve{y} ; \breve{x}$.
6. $\breve{x} ; -(x ; y) \le -y$.

## Remarks

Example: let $U$ be a set and let $A$ be the set of all [[binary relations|05AVARPXA2]] on $U$, with the set operations.
Let $;$ be the [[composition|0PYSR20HGF]] $R ; S = \set{(a, c) : (a, b) \in R \text{ and } (b, c) \in S \text{ for some } b}$.
Let $\breve{R}$ be the [[converse|054K3HNN5Z]] relation and $1'$ the identity relation.
Check of clause 6: if $(a, c) \in \breve{R} ; -(R ; S)$, there is $b$ with $(b, a) \in R$ and $(b, c) \notin R ; S$.
If $(a, c)$ were in $S$, then $(b, c) \in R ; S$; so $(a, c) \notin S$.

Non-example: on the relations of a set $U$ with at least two elements, keep the Boolean operations, $;$ and $1'$, but take $\breve{R} = R$.
Clause 5 then says $R ; S = S ; R$ for all relations, which fails for $U = \set{a, b}$, $R = \set{(a, b)}$ and $S = \set{(b, b)}$, since $R ; S = \set{(a, b)}$ and $S ; R = \emptyset$.
