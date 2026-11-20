---
tag: 0EX2HPXPJ6
kind: concept
name: Direct product of vector spaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
specializes: [000AYPA9AJ]
uses: [000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Construction for vector spaces and abelian groups
  - book: isbn:9783031410253
    locator: Section 3E
  - url: https://en.wikipedia.org/wiki/Direct_product
    locator: Direct product of modules
inventory: [889YSB2XEX]
---

## Summary

Let $(V_i)_{i \in I}$ be a family of [[vector spaces|000AYPA9AJ]] over a field $F$.
The *direct product* $\prod_{i \in I} V_i$ is the space of all families $(v_i)_{i \in I}$ with $v_i \in V_i$, with componentwise operations.
For two spaces it is the space $V \times W$ of pairs.
For finitely many spaces the product equals the [[external direct sum|0S7W6EG32V]], and for infinitely many nonzero spaces it is strictly larger.

## Motivation

Many spaces in analysis are spaces of all sequences or all functions, such as $\R^{\N}$ or the space of all functions $[0, 1] \to \R$.
These are products of copies of $\R$, one copy for each index.
The product is also the natural target of a family of maps: maps $X \to V_i$ for all $i$ combine into one map $X \to \prod_i V_i$, by the [[universal property|~252e7378]].
So the product is the place where we record several pieces of information at once.

## Notation

We write $\prod_{i \in I} V_i$, and $V_1 \times \cdots \times V_k$ for a finite family.
For copies of one space, $V^I = \prod_{i \in I} V$, which is the space of all functions $I \to V$.
The *projection* $\pi_j \colon \prod_i V_i \to V_j$ sends a family to its entry in place $j$.
For finite families, many books write $V_1 \oplus \cdots \oplus V_k$ instead of $V_1 \times \cdots \times V_k$.
Mathlib writes `(i : ι) → V i` for the product, with the vector space structure `Pi.module`.

## Remarks

### Examples

- [[R² × R³|~97da2c70]] is a product of dimension $5$, isomorphic to $\R^5$.
- The space $\R^{\N}$ of all real sequences is the product of countably many copies of $\R$.
- The space of all functions $S \to F$ on a set $S$ is the product $F^S$.
- The space of formal power series $F[[x]]$ is isomorphic to $F^{\N}$ through the coefficients.

### Non-examples

- [[The product of countably many lines is not their direct sum|~7439fe10]]: the sequence $(1, 1, 1, \dots)$ lies in $\R^{\N}$ but not in $\R^{(\N)}$.
- A real vector space and a complex vector space have no product as vector spaces, until we view the complex space as a real space. The factors must share one field.

### Basic properties

- The [[dimension of a direct product|06HN47VPTH]]: $\dim(V \times W) = \dim V + \dim W$.
- The projections $\pi_j$ are linear and surjective.
- The [[universal property|~252e7378]]: linear maps $g_i \colon X \to V_i$ come from exactly one linear map $g \colon X \to \prod_i V_i$ with $\pi_i \circ g = g_i$, namely $g(x) = (g_i(x))_i$. The product is the [[categorical product|S5744QZV4N]] of vector spaces.
- The external direct sum $\bigoplus_i V_i$ is the subspace of the product made of the families with finite support.

### History

Products of sets and of groups were standard by the early twentieth century.
The distinction between the product and the direct sum of infinitely many modules became important with homological algebra in the 1950s, where the two behave differently under duality.

### Common errors

- Identifying the product with the direct sum for infinite families. The product contains families with infinitely many nonzero entries.
- Thinking that $\dim \R^{\N}$ is countable because the index set is countable. The standard unit sequences span only the direct sum $\R^{(\N)}$, and $\R^{\N}$ has uncountable dimension.
- Writing $V \times W$ for two subspaces of one space and treating it as a subspace. It is a new space, and the related subspace is the [[sum|0JMTY8MF54]] $V + W$.

## Explanations

### L1 human

The product of spaces collects one vector from each space into a list.
For two spaces, a vector is a pair, and we add pairs part by part.
The plane $\R^2$ is the product of two lines, and $\R^3$ is the product of a plane and a line.

### L2 human

Take $V = \R^2$ and $W = \R^3$.

1. A vector of $V \times W$ is a pair such as $((1, 0), (2, 3, 4))$.
2. The pairs $(e_i, 0)$ and $(0, e_j)$ form a basis, so $\dim(V \times W) = 2 + 3 = 5$.
3. The projection $\pi_1((1, 0), (2, 3, 4)) = (1, 0)$ forgets the second part.
4. A map $g \colon \R \to V \times W$ is a pair of maps, for example $g(t) = ((t, 0), (0, 0, 2t))$.

The trap is the infinite case: the product of infinitely many lines is not spanned by the unit sequences.

### L3 human

In the category of vector spaces, the product is the limit of a discrete diagram and the direct sum is the colimit.
The canonical map $\bigoplus_i V_i \to \prod_i V_i$ is an isomorphism exactly when only finitely many $V_i$ are nonzero.
Duality exchanges them: $\left(\bigoplus_i V_i\right)^* \cong \prod_i V_i^*$, while the dual of a product is in general larger than the sum of the duals.
By the Erdős-Kaplansky theorem, $\dim F^{\N} = |F|^{\aleph_0}$ for an infinite field $F$, which is uncountable.
