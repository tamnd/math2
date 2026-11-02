---
tag: EZ24HDESPB
kind: definition
name: Attractor
msc: [37C70, 37G35, 37B25]
defines: 7FWX24X5MW
uses: [0VKD1TP7F3, 0X3WGX95FE, 0TVJZYB6SH, 02BH3MCBQB, AYVTR2ES5B]
sources:
  - url: https://en.wikipedia.org/wiki/Attractor
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $f \colon X \to X$ be a [[continuous map|0X3WGX95FE]], with [[iterates|AYVTR2ES5B]] $f^n$.
For $x \in X$ and $A \subseteq X$ nonempty, let $d(x, A) = \inf_{a \in A} d(x, a)$.
A nonempty [[compact|0TVJZYB6SH]] set $A \subseteq X$ is an *attractor* of $f$ if:

1. $A$ is invariant: $f(A) = A$;
2. $A$ attracts an open neighbourhood: there is an [[open set|02BH3MCBQB]] $U \supseteq A$ such that $d(f^n(x), A) \to 0$ as $n \to \infty$ for every $x \in U$;
3. $A$ is minimal: no nonempty compact proper subset of $A$ satisfies clauses 1 and 2.

The *basin of attraction* of $A$ is the set of all $x \in X$ with $d(f^n(x), A) \to 0$.
For a flow $(\varphi_t)$ the definition is the same, with $\varphi_t(A) = A$ for all $t$ and $t \to \infty$ in place of $n \to \infty$.

## Remarks

A set that satisfies clauses 1 and 2 is often called an attracting set.
The literature uses several other versions.
Some replace clause 3 by the existence of a dense orbit in $A$.
Some ask for a neighbourhood $U$ with $f(\overline{U}) \subseteq U$ and $A = \bigcap_{n \ge 0} f^n(U)$.
Milnor's version replaces the open neighbourhood in clause 2 by a basin of positive measure.

Example: $f(x) = x/2$ on $\R$ and $A = \set{0}$.
Clause 1 holds since $f(0) = 0$; clause 2 holds with $U = \R$, since $d(f^n(x), A) = \abs{x}/2^n \to 0$; clause 3 holds since $A$ has no nonempty proper subset.

Non-example: let $f$ be the time-$1$ map of the flow of $u' = u - u^3$ on $\R$, and let $A = [-1, 1]$.
Every solution tends to $-1$, $0$ or $1$, so $A$ is invariant and attracts all of $\R$.
But the proper subset $\set{1}$ also satisfies clauses 1 and 2, with $U = (0, \infty)$, so clause 3 fails for $A$.
The attractors of this map are $\set{-1}$ and $\set{1}$.
