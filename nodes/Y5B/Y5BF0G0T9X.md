---
tag: Y5BF0G0T9X
kind: definition
name: Mal'cev term
msc: [08B05]
defines: Y203PPTS61
uses: [AJNZJD8442, N9M2N27END, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence-permutable_algebra
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
A *Mal'cev term* for $\mathcal{V}$ is a ternary term $p(x, y, z)$ such that $\mathcal{V}$ satisfies the [[identities|PKD440G2XW]]
$$p(x, y, y) = x \quad \text{and} \quad p(x, x, y) = y.$$
An algebra $A$ has a *Mal'cev operation* if some ternary [[term operation|N9M2N27END]] of $A$ satisfies these two equations for all elements of $A$.

## Remarks

Example: for groups, $p(x, y, z) = x y^{-1} z$ is a Mal'cev term, since $x y^{-1} y = x$ and $x x^{-1} z = z$.
For modules and rings, $p(x, y, z) = x - y + z$ is a Mal'cev term.
Non-example: the variety of semilattices has no Mal'cev term.
Every semilattice term in the variables $x, y, z$ equals the join of the set $S$ of variables that occur in it.
If $p(x, y, y) = x$, then neither $y$ nor $z$ is in $S$, so $p = x$, and then $p(x, x, y) = x \ne y$ in a semilattice with two elements.
By Mal'cev's theorem, a variety has a Mal'cev term if and only if it is a [[congruence-permutable variety|1B3N9T68YV]].

## Explanations

### L1 human

A Mal'cev term is a three-input formula that returns the outer input when the other two inputs agree.
