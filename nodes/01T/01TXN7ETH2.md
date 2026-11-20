---
tag: 01TXN7ETH2
kind: concept
name: Orthogonality for a bilinear form
aliases: [orthogonal-family-for-a-bilinear-form, orthogonal-complement-for-a-bilinear-form]
msc: ["15A63"]
topics: [DYAK7YMK7B]
audience: ug1
uses: [0SQZMXB6GP, 01NHFZF2SK, 0XJXTBCB2T, 0ASHNYF7AG, 0QK6K857HS]
sources:
  - url: https://en.wikipedia.org/wiki/Bilinear_form
    locator: Reflexive bilinear forms and orthogonal vectors
  - url: https://en.wikipedia.org/wiki/Orthogonal_complement
    locator: General bilinear forms
  - book: isbn:9780387728285
    locator: Chapter 11
---

## Summary

Let $B$ be a [[bilinear form|0SQZMXB6GP]] on a vector space $V$ over a field $F$.
Two vectors $u, v$ are orthogonal for $B$ when $B(u, v) = 0$, and a family of vectors is orthogonal when $B$ is zero on each pair of distinct members.
For a subspace $W$, the orthogonal complement $W^\perp$ is the subspace of all $v$ with $B(w, v) = 0$ for every $w \in W$.
The [[formal definition|05Q4JD6XEH]] states these notions.
In finite dimension, $\dim W + \dim W^\perp \geq \dim V$, with equality when $B$ is [[nondegenerate|01NHFZF2SK]], by the [[dimension statement|~fb9287d6]].
Unlike for an inner product, $W \cap W^\perp$ can be nonzero, and a vector can be orthogonal to itself.

## Motivation

For an inner product, orthogonality gives [[orthogonal complements|0XJXTBCB2T]], orthogonal bases and projections.
Many forms in algebra and physics are not inner products: the form $x_1 y_1 - x_2 y_2$ of special relativity, the determinant form on $F^2$, or any form over a finite field.
We still want to split a space into pieces that do not interact under the form.
Orthogonality for a general form gives the words for this.
In an orthogonal basis, the [[matrix of the form|0QK6K857HS]] is diagonal, which makes the form easy to compute with.

## Notation

- We write $u \perp v$ or $u \perp_B v$ for $B(u, v) = 0$.
- For a subspace $W$, the right orthogonal is $W^\perp = \{v : B(w, v) = 0 \text{ for all } w \in W\}$, and the left orthogonal is ${}^\perp W = \{u : B(u, w) = 0 \text{ for all } w \in W\}$.
- For a [[reflexive form|~b3103bb5]] the two are equal, and most books write only $W^\perp$.
- $V^\perp$ is the right radical of $B$.
- Some sources write $W^\perp$ for the left orthogonal instead. For a non-reflexive form, check which convention a source uses.
- Some books write $W^{\perp_B}$ when several forms are in use.

## Remarks

### Examples

- For the [[dot product|0S52TNNTH9]] on $\R^n$, these notions are the usual ones, and $W^\perp$ is the usual orthogonal complement.
- For [[the form $x_1 y_1 - x_2 y_2$ on $\R^2$|~68ff0c35]], the line $W$ through $(1, 1)$ has $W^\perp = W$.
- For the [[determinant form|~d5093041]] $B(x, y) = x_1 y_2 - x_2 y_1$ on $F^2$, every vector is orthogonal to itself, and $W^\perp = W$ for every line $W$.
- For $x_1 y_1 + x_2 y_2 + x_3 y_3$ on $\mathbb{F}_2^3$, the vector $(1, 1, 0)$ is orthogonal to itself.
- The standard basis of $F^n$ is an orthogonal family for every form with a diagonal matrix.

### Non-examples

- For the form $B(x, y) = x_1 y_2$ on $F^2$, $B(e_1, e_2) = 1$ but $B(e_2, e_1) = 0$. So $e_2 \perp e_1$ holds and $e_1 \perp e_2$ fails: orthogonality for a non-reflexive form is not a symmetric relation.
- The determinant form on $F^2$ has no orthogonal basis. In an orthogonal basis its matrix would be diagonal, with diagonal entries $B(v, v) = 0$, so the form would be zero.

### Basic properties

- $W^\perp$ is a subspace, and $W_1 \subseteq W_2$ implies $W_2^\perp \subseteq W_1^\perp$.
- $W^\perp$ is the kernel of the linear map $V \to W^*$, $v \mapsto B(\cdot, v)|_W$. So $\dim W + \dim W^\perp \geq \dim V$.
- If $B$ is nondegenerate, then $\dim W + \dim W^\perp = \dim V$.
- $V = W \oplus W^\perp$ exactly when $B$ restricted to $W$ is nondegenerate.
- If $B$ is reflexive and nondegenerate, then $(W^\perp)^\perp = W$.
- In an orthogonal basis $(v_1, \dots, v_n)$, the matrix of $B$ is $\operatorname{diag}(B(v_1, v_1), \dots, B(v_n, v_n))$.

### Common errors

- $V = W \oplus W^\perp$ is false in general, even for a nondegenerate form. For $x_1 y_1 - x_2 y_2$ and $W$ the line through $(1, 1)$, $W + W^\perp = W$.
- An orthogonal family of nonzero vectors need not be linearly independent. In the example above, $(1, 1)$ and $(2, 2)$ are orthogonal to each other.
- The orthogonal complement of $W$ for a form lies in $V$, while the [[annihilator|0ASHNYF7AG]] of $W$ lies in $V^*$. A nondegenerate form identifies the two.

## Explanations

### L1 human

Two vectors are orthogonal for a form when the form gives zero on them.
For the dot product this is the usual right angle.
For other forms, strange things happen.
A nonzero vector can be orthogonal to itself, and a line can be its own orthogonal complement.

### L2 human

We compute an orthogonal complement for $B(x, y) = x^T A y$ on $\Q^3$ with $A = \operatorname{diag}(1, 1, -1)$.
Let $W$ be the line through $w = (1, 0, 1)$.

1. $B(w, v) = v_1 - v_3$. So $W^\perp$ is the plane $v_1 = v_3$.
2. $\dim W + \dim W^\perp = 1 + 2 = 3$, as the dimension statement says for the nondegenerate form $B$.
3. $B(w, w) = 1 - 1 = 0$, so $w \in W^\perp$, and $W \cap W^\perp = W$.
4. So $W + W^\perp = W^\perp$ is only a plane, and $\Q^3 \neq W \oplus W^\perp$.

The typical use is to split off a subspace on which the form is nondegenerate, as in the proof of the classification of alternating forms.
A trap: always test whether the form is nondegenerate on $W$ before writing $V = W \oplus W^\perp$.

### L3 human

The orthogonal complement for a nondegenerate form is the annihilator after the identification of $V$ with $V^*$, so the theory of annihilators applies.
For a reflexive nondegenerate form, $W \mapsto W^\perp$ is an inclusion-reversing involution on the lattice of subspaces.
Subspaces with $W \subseteq W^\perp$ are totally isotropic, and those with $W = W^\perp$ are Lagrangian; they control the geometry of [[symplectic spaces|PQ7JJY0VPH]] and of split quadratic spaces.
In projective geometry, such an involution of the subspaces is called a polarity.
