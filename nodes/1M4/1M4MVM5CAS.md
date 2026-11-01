---
tag: 1M4MVM5CAS
kind: definition
name: Proximity space
msc: ["54E05"]
defines: WY9BHD6GBA
uses: [00E0YZCERH, 05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Proximity_space
---

## Definition

Let $X$ be a set.
A *proximity* on $X$ is a relation $\delta$ between subsets of $X$, written $A \mathrel{\delta} B$ and read "$A$ is near $B$", such that for all $A, B, C \subseteq X$:

1. If $A \mathrel{\delta} B$, then $B \mathrel{\delta} A$.
2. If $A \mathrel{\delta} B$, then $A \neq \emptyset$.
3. If $A \cap B \neq \emptyset$, then $A \mathrel{\delta} B$.
4. $A \mathrel{\delta} (B \cup C)$ if and only if $A \mathrel{\delta} B$ or $A \mathrel{\delta} C$.
5. If $A \mathrel{\delta} E$ or $B \mathrel{\delta} (X \setminus E)$ holds for every $E \subseteq X$, then $A \mathrel{\delta} B$.

A *proximity space* is a pair $(X, \delta)$ of a set $X$ and a proximity $\delta$ on $X$.

## Remarks

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $A \mathrel{\delta} B$ mean $\inf \set{d(a, b) : a \in A, b \in B} = 0$, with $\inf \emptyset = \infty$.
Clauses 1 to 4 follow directly.
For clause 5, suppose that $A$ is not near $B$, so the distance $r$ between them is positive.
Let $E = \set{x : d(x, A) \ge r/2}$.
Then $A$ is not near $E$, and each point of $X \setminus E$ is at distance more than $r/2$ from $B$, so $B$ is not near $X \setminus E$.
The relation that makes all pairs of subsets near fails clause 2, since it makes $\emptyset$ near $\emptyset$.
A proximity defines a topology: the closure of $A$ is the set of points $x$ with $\set{x} \mathrel{\delta} A$.
Many authors also ask that $\set{x} \mathrel{\delta} \set{y}$ imply $x = y$; such a proximity is *separated*.

## Explanations

### L1 human

A proximity is a rule that says which pairs of sets touch or almost touch.
The clauses say that nearness is symmetric, that the empty set is near nothing, and that sets that meet are near.
A set is near a union exactly when it is near one of the parts.
The last clause says that two sets that are not near can be kept apart by a set in between.
