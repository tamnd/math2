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

The direct product of vector spaces is the space of all lists that take one vector from each space, with no limit on how many entries are nonzero.
It is the natural home of sequences and functions: the space of all real sequences is the product of countably many copies of $\R$.
For a family $(V_i)_{i \in I}$ of [[vector spaces|000AYPA9AJ]] over a field $F$, the [[direct product|0MM085RX00]] is the set
$$\prod_{i \in I} V_i = \{(v_i)_{i \in I} : v_i \in V_i \text{ for each } i \in I\},$$
with the componentwise operations $(v_i)_i + (w_i)_i = (v_i + w_i)_i$ and $a (v_i)_i = (a v_i)_i$.
For two spaces it is the space $V \times W$ of pairs.
For finitely many spaces the product equals the [[external direct sum|0S7W6EG32V]], and for infinitely many nonzero spaces it is strictly larger.

## Motivation

Many spaces in analysis are spaces of all sequences or of all functions, such as $\R^{\N}$ or the space of all functions $[0, 1] \to \R$.
Each of these is a product of copies of $\R$, with one copy for each index: a function $f$ is the list of its values $f(s)$.
Adding functions pointwise is exactly the componentwise addition of the product.

The product is also the natural target of a family of maps.
Linear maps $g_i \colon X \to V_i$ combine into one map $X \to \prod_i V_i$ that records all the values at once, by the [[universal property|YT3GZ6YCAH]].
This makes the product the categorical product of vector spaces.
It returns in the sub-area on [[duality|9K7FFF26QR]], where the dual of a direct sum turns out to be a product of duals.

## Notation

We write $\prod_{i \in I} V_i$ for a family and $V_1 \times \cdots \times V_k$ for finitely many spaces.
For copies of one space, $V^I = \prod_{i \in I} V$ is the space of all functions $I \to V$.
The *projection* $\pi_j \colon \prod_i V_i \to V_j$ sends a family to its entry in place $j$.
For finite families many books write $V_1 \oplus \cdots \oplus V_k$ instead of $V_1 \times \cdots \times V_k$, which is harmless because the two spaces are the same.
Mathlib writes `(i : ι) → V i` for the product, with the vector space structure `Pi.module`.

## Remarks

### A first product

Take $V = \R^2$ and $W = \R^3$.
A vector of $V \times W$ is a pair such as $((1, 0), (2, 3, 4))$, and pairs add part by part:
$$((1, 0), (2, 3, 4)) + ((1, 1), (0, 0, -4)) = ((2, 1), (2, 3, 0)).$$
The pairs $(e_i, 0)$ for the two standard vectors of $\R^2$ and $(0, e_j)$ for the three standard vectors of $\R^3$ form a basis.
So [[the product R² × R³ has dimension 5|QW80919JXK]], and it is isomorphic to $\R^5$.

### Dimension

The same argument works for any two finite-dimensional spaces.
A basis $(v_i)$ of $V$ and a basis $(w_j)$ of $W$ give the basis of pairs $(v_i, 0)$ and $(0, w_j)$ of $V \times W$, which gives the [[dimension of a direct product|06HN47VPTH]]:
$$\dim(V \times W) = \dim V + \dim W.$$
By induction, $\dim(V_1 \times \cdots \times V_k) = \dim V_1 + \cdots + \dim V_k$.
The formula is the reason that $F^m \times F^n \cong F^{m + n}$.

### Infinite products

The space $\R^{\N}$ of all real sequences, the space $F^S$ of all functions from a set $S$ to $F$, and the space $F[[x]]$ of formal power series, through its coefficients, are infinite products.
Inside $\R^{\N}$ lies the direct sum $\R^{(\N)}$ of sequences with finitely many nonzero terms.
The sequence $(1, 1, 1, \dots)$ lies in the product but not in the sum, so [[the product of countably many lines is not their direct sum|6DEMNQEGG8]].
In general, the external direct sum $\bigoplus_i V_i$ is the subspace of the product made of the families with finite support.

### The rules you can use

Each projection $\pi_j$ is linear, because the operations are componentwise, and it is surjective, because any $v \in V_j$ is the entry in place $j$ of the family with zeros elsewhere.
Linear maps $g_i \colon X \to V_i$ come from exactly one linear map $g \colon X \to \prod_i V_i$ with $\pi_i \circ g = g_i$, namely $g(x) = (g_i(x))_i$.
This is the [[universal property of the product|YT3GZ6YCAH]], and it says that the direct product is the [[categorical product|S5744QZV4N]] of vector spaces.
For example, $g_1(t) = (t, -t)$ and $g_2(t) = 3t$ combine into $g(t) = ((t, -t), 3t)$ from $\R$ to $\R^2 \times \R$.

### What it is not

The direct product of infinitely many nonzero spaces is not their direct sum, as the sequence of ones shows.
The product needs one field for all the factors.
A real space and a complex space have no product as vector spaces until we view the complex space as a real space by restricting the scalars.
For two subspaces $U$ and $W$ of one space, $U \times W$ is a new space and not a subspace of the old one; the subspace that they span is the [[sum|0JMTY8MF54]] $U + W$.

### Watch out

A common mistake is to think that $\R^{\N}$ has countable dimension because its index set is countable.
The unit sequences $e_n$ span only the direct sum $\R^{(\N)}$, since a span contains only finite combinations.
In fact $\R^{\N}$ has uncountable dimension, so no countable family spans it.
Writing $(1, 1, 1, \dots) = \sum_n e_n$ does not help, because a vector space without a topology has no infinite sums.

### Try it

First, find the dimension of $\R^2 \times P_3 \times \R^4$, where $P_3$ is the space of real polynomials of degree at most $3$.
The dimensions add, so the answer is $2 + 4 + 4 = 10$.

Second, decide whether the projection $\pi_1 \colon \R^2 \times \R^3 \to \R^2$ is injective.
It is not, because $\pi_1((0, 0), (1, 0, 0)) = (0, 0)$, so its kernel $0 \times \R^3$ has dimension $3$.

## Explanations

### L1 human

The product of spaces collects one vector from each space into a list.
For two spaces, a vector is a pair, and we add pairs part by part.
The plane $\R^2$ is the product of two lines, and $\R^3$ is the product of a plane and a line.
The space of all infinite lists of numbers is the product of infinitely many lines.

### L2 human

Here is a typical use: we describe the linear map $g \colon \R \to \R^2 \times \R^3$ whose two parts are $g_1(t) = (t, 0)$ and $g_2(t) = (0, 0, 2t)$.
The universal property says that the pair of parts is all the information:
$$g(t) = ((t, 0), (0, 0, 2t)).$$
Check: $\pi_1(g(t)) = (t, 0) = g_1(t)$ and $\pi_2(g(t)) = (0, 0, 2t) = g_2(t)$.
In coordinates of $\R^5$, the matrix of $g$ is the column $(1, 0, 0, 0, 2)^{\mathsf{T}}$, the block column of the matrices of $g_1$ and $g_2$.
So a map into a product is designed one factor at a time.
Watch out: in the infinite case the combined map can leave the direct sum, which is why the target must be the product.

### L3 human

In the category of vector spaces, the product is the limit of a discrete diagram, and the [[external direct sum|0S7W6EG32V]] is the colimit.
The canonical map $\bigoplus_i V_i \to \prod_i V_i$ is an isomorphism exactly when only finitely many $V_i$ are nonzero.
Duality exchanges the two constructions, $\left(\bigoplus_i V_i\right)^* \cong \prod_i V_i^*$, while the dual of an infinite product is in general larger than the direct sum of the duals.
By the Erdős-Kaplansky theorem, an infinite-dimensional space $V$ over $F$ has $\dim V^* = |F|^{\dim V}$, so $\dim F^{\N} = |F|^{\aleph_0}$, which is uncountable for every field $F$.
