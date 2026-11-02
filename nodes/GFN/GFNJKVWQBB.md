---
tag: GFNJKVWQBB
kind: definition
name: Amenable group action
msc: [43A07, 37A15]
defines: ZCG4DJ7GH3
uses: [0WCY42EV9V, ZYNY2VFECQ, CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Definition

Let $G$ be a group acting on a set $X$ by a [[group action|0WCY42EV9V]] $(g, x) \mapsto g \cdot x$.
Let $\ell^\infty(X)$ be the space of bounded functions $X \to \R$, and for $g \in G$ and $f \in \ell^\infty(X)$ let $(g \cdot f)(x) = f(g^{-1} \cdot x)$.
A [[mean|ZYNY2VFECQ]] on $X$ is a linear map $m \colon \ell^\infty(X) \to \R$ such that:

1. $m(f) \ge 0$ whenever $f \ge 0$.
2. $m(1) = 1$ for the constant function $1$.

The action is *amenable* if there is a mean $m$ on $X$ with $m(g \cdot f) = m(f)$ for all $g \in G$ and $f \in \ell^\infty(X)$.

## Remarks

Example: suppose the action has a finite orbit $O = G \cdot x_0$.
Then $m(f) = \frac{1}{\abs{O}} \sum_{x \in O} f(x)$ is a mean, and it is invariant because each $g \in G$ permutes $O$.
So every action with a finite orbit is amenable, whatever the group.

Non-example: the free group $F_2$ acting on itself by left multiplication is not amenable.
Indeed, an invariant mean for this action is exactly what makes a group [[amenable|CEAT9BESKK]], and $F_2$ is not amenable.

A group $G$ is amenable if and only if its action on itself by left multiplication is amenable.
If $G$ is amenable, every action of $G$ is amenable: for a fixed $x_0 \in X$, an invariant mean $m$ on $G$ gives the invariant mean $f \mapsto m(g \mapsto f(g \cdot x_0))$ on $X$.

The name is also used in other senses.
In ergodic theory, an amenable group action often just means an action of an amenable group.
Zimmer's amenability of a measure-class-preserving action is a different notion: for example, the action of $F_2$ on its boundary is amenable in Zimmer's sense.
