---
tag: BBRSEM0C4H
kind: definition
name: Rank of an abelian group
msc: [20K15, 20K20]
defines: EMCTDD3HZ1
uses: [082GHNPJ53, 0EBACQFAZW, 03GSZ8RTZJ, 0DBWXQRXQJ, 0WJX8MGG37]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_of_an_abelian_group
---

## Definition

Let $A$ be an [[abelian group|082GHNPJ53]], written additively.
A subset $X \subseteq A$ is *linearly independent* if for all distinct $x_1, \ldots, x_k \in X$ and integers $n_1, \ldots, n_k$,
$$n_1 x_1 + \cdots + n_k x_k = 0 \implies n_1 = \cdots = n_k = 0.$$
The *rank* of $A$ is the [[cardinality|0EBACQFAZW]] of a maximal linearly independent subset of $A$.
It does not depend on the choice of the maximal subset.

## Remarks

Example: $A = \Z^2 \oplus \Z/3\Z$ has rank $2$.
The set $\set{(1, 0, 0), (0, 1, 0)}$ is independent, and it is maximal: for any $y \in A$, $3y$ lies in $\Z^2 \oplus 0$, so $3y = m(1,0,0) + n(0,1,0)$ gives a relation with nonzero coefficient on $y$.

Non-example of independence: in $\Z/6\Z$, the set $\set{1}$ is not independent, since $6 \cdot 1 = 0$ with coefficient $6 \neq 0$.
In fact a group in which every element has finite order, such as the [[torsion subgroup|0DBWXQRXQJ]] of any abelian group, has rank $0$.

Equivalently, the rank of $A$ is the [[dimension|03GSZ8RTZJ]] of the $\Q$-vector space $A \otimes_\Z \Q$.
Rank is additive: if $0 \to A \to B \to C \to 0$ is exact, then $\rank B = \rank A + \rank C$.
The [[free abelian group|0WJX8MGG37]] $\Z^n$ has rank $n$, and $\Q$ has rank $1$.
