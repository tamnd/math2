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

Every bilinear form has its own notion of a right angle: two vectors are orthogonal when the form gives zero on them.
With it we can split a space into pieces that do not interact under the form, even when the form is not an inner product.
Let $B$ be a [[bilinear form|0SQZMXB6GP]] on a vector space $V$ over a field $F$.
Vectors $u, v$ are *orthogonal* for $B$ when $B(u, v) = 0$, and a family of vectors is *orthogonal* when $B$ is zero on each pair of distinct members.
For a subspace $W$, the *orthogonal complement* is
$$W^\perp = \{v \in V : B(w, v) = 0 \text{ for all } w \in W\}.$$
The [[formal definition|05Q4JD6XEH]] states these notions.
When $V$ is finite-dimensional, $\dim W + \dim W^\perp \ge \dim V$, with equality when $B$ is [[nondegenerate|01NHFZF2SK]], by the [[dimension statement|M2JH84VEY9]].
Unlike for an inner product, $W \cap W^\perp$ can be nonzero, and a nonzero vector can be orthogonal to itself.

## Motivation

For an inner product, orthogonality gives [[orthogonal complements|0XJXTBCB2T]], orthogonal bases and projections.
Many forms in algebra and physics are not inner products: the form $x_1 y_1 - x_2 y_2$ of special relativity in one space dimension, the determinant form on $F^2$, or any form over a finite field.
We still want to break a space into pieces on which the form can be studied one at a time.
Orthogonality for a general form gives the language for this.

The payoff is a simple matrix.
In an orthogonal basis the [[matrix of the form|0QK6K857HS]] is diagonal, so the form becomes a weighted sum of products of coordinates.
The later pages of the sub-area use orthogonal splittings again and again: the [[classification of alternating forms|V8KKHKXXB3]] splits off planes, and the [[Witt decomposition|BPMRSPB6GD]] splits off hyperbolic planes.

## Notation

We write $u \perp v$, or $u \perp_B v$ when several forms are in play, for $B(u, v) = 0$.
The set $W^\perp$ above is the right orthogonal of $W$, and the left orthogonal is ${}^\perp W = \{u \in V : B(u, w) = 0 \text{ for all } w \in W\}$.
For a [[reflexive form|M0G958M917]], such as a symmetric or an alternating form, the two are equal, and most books write only $W^\perp$.
With our convention, $V^\perp$ is the right radical of $B$.
Watch out: some books use $W^\perp$ for the left orthogonal, so for a form that is not reflexive, check the convention before you compare results.

## Remarks

### A first computation

Take $B(x, y) = x_1 y_1 + x_2 y_2 - x_3 y_3$ on $\mathbb{Q}^3$, and let $W$ be the line spanned by $w = (1, 0, 1)$.
A vector $v$ lies in $W^\perp$ exactly when
$$B(w, v) = 1 \cdot v_1 + 0 \cdot v_2 - 1 \cdot v_3 = v_1 - v_3 = 0.$$
So $W^\perp$ is the plane $v_1 = v_3$, and $\dim W + \dim W^\perp = 1 + 2 = 3$, as the dimension statement says for this nondegenerate form.
Now pair $w$ with itself:
$$B(w, w) = 1 + 0 - 1 = 0.$$
So $w$ lies in its own complement, $W \subseteq W^\perp$, and $W + W^\perp$ is only the plane $W^\perp$.
The complement has the right dimension but is not a complement in the sense of a direct sum.

### Lines that are their own complement

For the [[form x1y1 - x2y2 on the real plane|X6C1Z0W252]], the line $W$ spanned by $(1, 1)$ satisfies $W^\perp = W$.
Indeed $B((1, 1), v) = v_1 - v_2$, which vanishes exactly on $W$.
For the [[determinant form|8K74K4BF5H]] $B(x, y) = x_1 y_2 - x_2 y_1$ on $F^2$, every line is its own complement.
For a line spanned by $w \ne 0$, the value $B(w, v)$ is zero exactly when $v$ is a multiple of $w$, so $W^\perp = W$.
Over the field $\mathbb{F}_2$, the form $x_1 y_1 + x_2 y_2 + x_3 y_3$ makes $(1, 1, 0)$ orthogonal to itself, since $1 + 1 + 0 = 0$ in $\mathbb{F}_2$.

### What orthogonality need not do

For a form that is not reflexive, orthogonality is not a symmetric relation.
The form $B(x, y) = x_1 y_2$ on $F^2$ gives $B(e_2, e_1) = 0$ but $B(e_1, e_2) = 1$, so $e_2 \perp e_1$ holds and $e_1 \perp e_2$ fails.
The [[reflexive forms|M0G958M917]] are exactly the forms for which the relation is symmetric.

Some forms have no orthogonal basis at all.
The determinant form on $F^2$ has $B(v, v) = 0$ for every $v$, so in an orthogonal basis its matrix would be diagonal with zeros on the diagonal, that is, zero.
The form is not zero, so no orthogonal basis exists, in any characteristic.

### The rules you can use

The set $W^\perp$ is a subspace, because it is the intersection of the kernels of the linear forms $B(w, \cdot)$ for $w \in W$.
Complements reverse inclusions: $W_1 \subseteq W_2$ gives $W_2^\perp \subseteq W_1^\perp$, since fewer conditions leave more solutions.
In finite dimension, $W^\perp$ is the kernel of the map $V \to W^*$, $v \mapsto B(\cdot, v)|_W$, so rank-nullity gives $\dim W + \dim W^\perp \ge \dim V$.
The [[dimension statement|M2JH84VEY9]] adds three facts: equality when $B$ is nondegenerate, $V = W \oplus W^\perp$ exactly when $B$ restricted to $W$ is nondegenerate, and $(W^\perp)^\perp = W$ when $B$ is nondegenerate and reflexive.
In an orthogonal basis $(v_1, \dots, v_n)$, the matrix of $B$ is $\operatorname{diag}(B(v_1, v_1), \dots, B(v_n, v_n))$.

### Watch out

The splitting $V = W \oplus W^\perp$ is false in general, even for a nondegenerate form.
For $x_1 y_1 - x_2 y_2$ and the line $W$ through $(1, 1)$, we found $W^\perp = W$, so $W + W^\perp = W$ is only a line.
Before you write $V = W \oplus W^\perp$, check that $B$ is nondegenerate on $W$.

An orthogonal family of nonzero vectors need not be independent.
For the same form, $B((1, 1), (2, 2)) = 2 - 2 = 0$, so $(1, 1)$ and $(2, 2)$ form an orthogonal family, but they are dependent.
For an inner product this cannot happen, because $B(v, v) > 0$ for $v \ne 0$.

Finally, $W^\perp$ is a subspace of $V$, while the [[annihilator|0ASHNYF7AG]] of $W$ is a subspace of $V^*$.
A nondegenerate form identifies the two, but they are different objects.

### Try it

First, for $B(x, y) = x_1 y_2 + x_2 y_1$ on $\mathbb{Q}^2$, find $W^\perp$ for $W$ spanned by $e_1$.
You need $B(e_1, v) = v_2 = 0$, so $W^\perp$ is spanned by $e_1$, and $W = W^\perp$.

Second, for the same form, find $W^\perp$ for $W$ spanned by $(1, 1)$, and decide whether $\mathbb{Q}^2 = W \oplus W^\perp$.
You need $B((1, 1), v) = v_2 + v_1 = 0$, so $W^\perp$ is spanned by $(1, -1)$; since $B((1, 1), (1, 1)) = 2 \ne 0$, the sum is direct and equals $\mathbb{Q}^2$.

## Explanations

### L1 human

Two vectors are orthogonal for a form when the form gives zero on them.
For the dot product this is the usual right angle, as for $(1, 2)$ and $(-2, 1)$, where $-2 + 2 = 0$.
For other forms the word keeps its algebra but loses its picture.
For the form $x_1 y_1 - x_2 y_2$, the vector $(1, 1)$ gives $1 - 1 = 0$ with itself, so it is orthogonal to itself.
A line can then be its own orthogonal complement, which never happens for the dot product.

### L2 human

Here is a typical use: find an orthogonal basis for $B(x, y) = x^{\mathsf{T}} A y$ on $\mathbb{Q}^2$ with $A = \begin{pmatrix} 1 & 2 \\ 2 & 1 \end{pmatrix}$.
Start with $v_1 = e_1$, which has $B(v_1, v_1) = 1 \ne 0$, so $B$ is nondegenerate on its span $W$.
Then $\mathbb{Q}^2 = W \oplus W^\perp$, and $W^\perp$ is cut out by
$$B(e_1, v) = v_1 + 2v_2 = 0.$$
So $v_2 = (2, -1)$ spans $W^\perp$.
Since $A$ is symmetric, $B(v, v) = v_1^2 + 4 v_1 v_2 + v_2^2$, and so
$$B(v_2, v_2) = 2^2 + 4 \cdot 2 \cdot (-1) + (-1)^2 = 4 - 8 + 1 = -3.$$
Check directly: $A v_2 = (2 - 2, 4 - 1) = (0, 3)$, and $v_2^{\mathsf{T}} (0, 3) = -3$.
In the basis $(v_1, v_2)$ the matrix of $B$ is $\operatorname{diag}(1, -3)$.
The problem shows the standard move: split off a vector $v$ with $B(v, v) \ne 0$, and continue in its complement.

### L3 human

For a nondegenerate form, $W^\perp$ is the image of the annihilator of $W$ under the identification $V^* \cong V$, so the whole theory of annihilators transfers.
For a reflexive nondegenerate form on a finite-dimensional space, $W \mapsto W^\perp$ is an involution of the lattice of subspaces that reverses inclusions, which projective geometry calls a polarity.
Subspaces with $W \subseteq W^\perp$ are the totally [[isotropic subspaces|MZHFGPV1YT]], and in a [[symplectic space|PQ7JJY0VPH]] those with $W = W^\perp$ are the Lagrangian subspaces.
Orthogonal splittings also give the orthogonal sum of quadratic spaces, the operation behind the Witt group of a field.
