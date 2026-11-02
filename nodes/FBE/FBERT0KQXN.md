---
tag: FBERT0KQXN
kind: statement
role: lemma
name: Whitney decomposition
msc: [42B25, 28A75]
uses: [2Z2QVWZ262]
about: [2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Whitney_covering_lemma
same_as:
  wikidata: Q7996763
  wikipedia: Whitney covering lemma
---

## Statement

Let $n \ge 1$ and let $\Omega \subseteq \R^n$ be an open set whose complement $F = \R^n \setminus \Omega$ is nonempty.
For a set $E$ write $\operatorname{diam}(E)$ for its diameter and $\operatorname{dist}(E, F)$ for its distance to $F$.
Then there is a countable family $(Q_k)$ of closed cubes with sides parallel to the axes such that:

1. $\Omega = \bigcup_k Q_k$;
2. the interiors of the cubes $Q_k$ are pairwise disjoint;
3. for every $k$,
$$\operatorname{diam}(Q_k) \le \operatorname{dist}(Q_k, F) \le 4 \operatorname{diam}(Q_k).$$

## Remarks

The cubes can be chosen dyadic, that is, of the form $2^{-j}([0, 1]^n + m)$ with $j \in \Z$ and $m \in \Z^n$.
Proof idea: for each $j$, take the dyadic cubes of side $2^{-j}$ that meet the layer $\set{x \in \Omega : 2^{-j+1}\sqrt{n} < \operatorname{dist}(x, F) \le 2^{-j+2}\sqrt{n}}$.
These cubes satisfy clause 3 by the triangle inequality, and they cover $\Omega$.
Two dyadic cubes are either nested or have disjoint interiors, so keeping only the maximal cubes in the collection gives clause 2.

Clause 3 implies that neighbouring cubes have comparable sizes: if $Q_k$ and $Q_l$ touch, then $\operatorname{diam}(Q_l) \le \operatorname{dist}(Q_l, F) \le \operatorname{dist}(Q_k, F) + \operatorname{diam}(Q_k) \le 5 \operatorname{diam}(Q_k)$.
It follows that, for a fixed small enlargement factor such as $1 + \frac{1}{4}$, each point of $\Omega$ lies in at most $C(n)$ of the enlarged cubes.

Example: for $\Omega = (0, \infty) \subseteq \R$ and $F = (-\infty, 0]$, the intervals $[2^{j}, 2^{j+1}]$ for $j \in \Z$ cover $\Omega$ with disjoint interiors.
Their distance to $F$ equals their length, so clause 3 holds.

## Explanations

### L1 human

An open set can be tiled by cubes whose size is proportional to their distance from the boundary.
Near the boundary the cubes are tiny, far from it they are large, like a mosaic that gets finer and finer as it approaches the edge.
The proportionality makes the tiling well adapted to the shape of the set.

### L2 human

Whitney introduced this decomposition to extend smooth functions from a closed set $F$ to all of $\R^n$, in the Whitney extension theorem.
In harmonic analysis it is applied to the open set $\set{Mf > \lambda}$ in the Calderón–Zygmund decomposition, in the atomic decomposition of Hardy spaces, and in proofs of good-$\lambda$ inequalities.
A partition of unity subordinate to the slightly enlarged cubes has derivatives bounded by $C \operatorname{dist}(x, F)^{-k}$, which is what such arguments need.
