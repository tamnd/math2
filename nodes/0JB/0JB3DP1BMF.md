---
tag: 0JB3DP1BMF
kind: definition
name: Linear combination
msc: [15A03]
defines: 0V8F3E48E6
uses: [05EGHEQZAW]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_combination
    locator: Definition
inventory: [AW41B4D2VT]
---

## Definition

Let $F$ be a field and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
Let $v_1, \dots, v_k \in V$.
A *linear combination* of $v_1, \dots, v_k$ is a vector of the form
$$a_1 v_1 + a_2 v_2 + \cdots + a_k v_k,$$
where $a_1, \dots, a_k \in F$ are the *coefficients*.
For an arbitrary family $(v_i)_{i \in I}$, a linear combination is a sum $\sum_{i \in I} a_i v_i$ in which only finitely many coefficients $a_i$ are nonzero.

## Remarks

The empty linear combination, with $k = 0$, is the zero vector.
The vector $(3, 5)$ is the linear combination $3 e_1 + 5 e_2$ of the standard basis vectors of $F^2$.
The set of all linear combinations of a family is its [[linear span|0DTY8B9HMS]].
The [[matrix–vector product|0PDVQEP0ZC]] $Ax$ is a linear combination of the columns of $A$, with the entries of $x$ as coefficients.

## Explanations

### L1 human

A linear combination mixes some vectors: scale each one by a number, then add the results.
With the vectors $(1, 0)$ and $(0, 1)$ we can make every vector of the plane in this way.
Infinite sums are not allowed: only finitely many coefficients can be nonzero.
