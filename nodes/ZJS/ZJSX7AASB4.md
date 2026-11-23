---
tag: ZJSX7AASB4
kind: example
name: Full frames are general frames
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
instance_of: [GGG7BB78JB]
uses: [6W9MEGN982, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Definition
---

## Example

Let $(W, R)$ be a [[Kripke frame|NGHWZ9Y7ZV]] and let $A = \mathcal{P}(W)$, the family of all subsets of $W$.
We check that $(W, R, A)$ is a [[general frame|6W9MEGN982]], that it validates the same formulas as $(W, R)$, and that it is refined.

1. Finite unions: the union of two subsets of $W$ is a subset of $W$, so it lies in $A$.
2. Complements: $W \setminus X$ is a subset of $W$, so it lies in $A$.
3. The operator: $m_R(X) = \{ w : w R v \text{ for some } v \in X \}$ is a subset of $W$, so it lies in $A$.
4. Every valuation $V$ has $V(p) \subseteq W$, so every valuation is admissible.
   Hence "true under all admissible valuations" means "true under all valuations", and the two notions of validity agree.
5. Differentiated: for $u \neq v$, the set $\{u\}$ is admissible, contains $u$ and misses $v$.
6. Tight: if $u R v$ fails, take $a = \{v\}$.
   Then $m_R(a)$ is the set of worlds that see $v$, and $u$ is not among them.

## Remarks

The example shows that general frames extend Kripke frames, so every theorem about general frames is also a theorem about Kripke frames.
Compactness is the one condition that can fail.
The full frame is compact exactly when $W$ is finite.
If $W$ is infinite, the sets $W \setminus \{w\}$ for $w \in W$ have the finite intersection property, because finitely many of them miss only finitely many points.
Their intersection is empty, so an infinite full frame is refined but not descriptive.
Its complex algebra is the full powerset algebra with $m_R$, a complete and atomic modal algebra, and the dual of that algebra is the ultrafilter extension of $(W, R)$, which is larger than $W$.

## Explanations

### L1 human

A Kripke frame lets a statement be true on any group of points.
Allowing every group as a region gives a general frame with nothing taken away.
So the old notion of a frame is the special case of the new notion with all regions allowed.
For three points, there are $2^3 = 8$ regions, and all eight are allowed.

### L2 human

Here is the failure of compactness for an infinite full frame.
Take $W = \mathbb{N}$ with $R = \{ (n, n + 1) : n \in \mathbb{N} \}$, and all subsets admissible.
Let $C_n = \mathbb{N} \setminus \{0, \dots, n\}$.
Any finitely many of these sets, up to $C_k$, all contain $k + 1$, so the family has the finite intersection property.
Every $n$ lies outside $C_n$, so
$$\bigcap_{n} C_n = \emptyset.$$
The typical use of the example is to read results about general frames as results about Kripke frames, by admitting every subset.
Watch out: results about descriptive frames apply to full frames only when they are finite.
