---
tag: 17FVAN6HXX
kind: definition
name: Closure operator
msc: [06A15]
defines: 2HJGRABSPZ
uses: [011C29Q1S1]
sources:
  - url: https://en.wikipedia.org/wiki/Closure_operator
---

## Definition

Let $(P, \le)$ be a [[partially ordered set|011C29Q1S1]].
A *closure operator* on $P$ is a map $c \colon P \to P$ such that, for all $x, y \in P$:

1. $x \le c(x)$ (extensive);
2. if $x \le y$, then $c(x) \le c(y)$ (monotone);
3. $c(c(x)) = c(x)$ (idempotent).

An element $x$ with $c(x) = x$ is *closed*.

## Remarks

Let $X$ be a topological space and $P$ the set of subsets of $X$ ordered by inclusion.
The map sending $A$ to its [[closure|0DRKT1QJR7]] $\overline{A}$ is a closure operator: $A \subseteq \overline{A}$, $A \subseteq B$ gives $\overline{A} \subseteq \overline{B}$, and $\overline{\overline{A}} = \overline{A}$.
On $\R$, the map $c(x) = x + 1$ is extensive and monotone but not idempotent, since $c(c(0)) = 2 \ne 1 = c(0)$.
The three clauses together are equivalent to one condition: $x \le c(y)$ if and only if $c(x) \le c(y)$, for all $x, y \in P$.
The closed elements determine $c$: $c(x)$ is the least closed element above $x$.
If $(f, g)$ is a [[Galois connection|MBVJ4JQXC5]] with lower adjoint $f$, then $g \circ f$ is a closure operator.
The dual notion is an [[interior operator|BPXY5A22BB]].

## Explanations

### L1 human

A closure operator moves each element up to the nearest closed element.
Closed elements stay where they are.
