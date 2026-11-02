---
tag: 7X1HGZ6FK0
kind: definition
name: Interior algebra
msc: ["06E25", "03G05", "03B45"]
defines: BDEX7HET71
uses: [06GKBTAA5E, 0CNQXVBHCX, 0C38S0KMJK, G8VGTW9P4F]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_algebra
---

## Definition

Let $B$ be a [[Boolean algebra|06GKBTAA5E]] with meet $\wedge$, greatest element $1$ and order $\le$.
An *interior operator* on $B$ is a map $I \colon B \to B$ such that for all $x, y \in B$:

1. $I(1) = 1$;
2. $I(x) \le x$;
3. $I(I(x)) = I(x)$;
4. $I(x \wedge y) = I(x) \wedge I(y)$.

An *interior algebra* is a pair $(B, I)$ of a Boolean algebra $B$ and an interior operator $I$ on $B$.

## Remarks

Example: let $X$ be a [[topological space|0CNQXVBHCX]] and let $B$ be the power set of $X$.
Let $I(A)$ be the [[interior|0C38S0KMJK]] of $A$.
The interior of $X$ is $X$, and the interior of $A$ lies in $A$.
The interior of an open set is the set itself, and $I(A \cap A') = I(A) \cap I(A')$.
So the four clauses hold.
Non-example: on a Boolean algebra with $0 \ne 1$, the map $I(x) = 0$ for all $x$ satisfies clauses 2, 3 and 4, but fails clause 1.
Clause 4 implies that $I$ is monotone: if $x \le y$, then $I(x) = I(x \wedge y) = I(x) \wedge I(y) \le I(y)$.
The map $C(x) = \neg I(\neg x)$ is the dual closure operator; a Boolean algebra with such a closure operator is a *closure algebra*.
Interior algebras are the algebraic semantics of the [[modal logic|G8VGTW9P4F]] S4, with $I$ interpreting the necessity operator $\square$.
