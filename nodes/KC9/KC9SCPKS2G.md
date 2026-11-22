---
tag: KC9SCPKS2G
kind: proof
name: Proof of the associativity of matrix multiplication by composition
msc: ["15A99", "15A04"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: 073E4XC016
methods: [0NTF6DMVAP]
uses: [076JGP6R3T, 0CCQV3884B, ZE36VEAY80, 0V7ZD6P7RK]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_multiplication
    locator: Associativity
  - url: https://www.math.brown.edu/streil/papers/LADW/LADW.html
    locator: Chapter 1, Section 5
---

## Proof

We work over a field $F$, so that the [[linearity of the matrix-vector product|ZE36VEAY80]] holds.
The plan is to show first that $(AB)y = A(By)$ for every column $y$, and then to compare the two sides column by column.

1. Let $A$ be $m \times n$ and $B$ be $n \times p$, and write $b_1, \dots, b_p$ for the columns of $B$.
2. By the [[definition of the product|076JGP6R3T]], column $k$ of $AB$ is the [[matrix-vector product|0CCQV3884B]] $A b_k$.
3. Let $y = (y_1, \dots, y_p)^{\mathsf{T}} \in F^p$. A matrix times a column is the combination of its columns with the entries of the column as weights. Applied to $AB$ and to $B$, this gives
$$(AB)y = \sum_{k=1}^{p} y_k \, (A b_k), \qquad By = \sum_{k=1}^{p} y_k \, b_k.$$
4. The map $x \mapsto Ax$ is linear, so it carries the combination $By$ to the same combination of the images:
$$A(By) = A\Bigl(\sum_{k=1}^{p} y_k b_k\Bigr) = \sum_{k=1}^{p} y_k \, (A b_k).$$
5. Steps 3 and 4 have the same right side, so $(AB)y = A(By)$ for every $y \in F^p$.
6. Now let $C$ be $p \times q$, and let $e_l$ be the $l$-th [[standard basis vector|0V7ZD6P7RK]] of $F^q$. For every matrix $M$ with $q$ columns, $M e_l$ is column $l$ of $M$.
7. Column $l$ of $(AB)C$ is $(AB)(C e_l)$, by step 2 applied to the factors $AB$ and $C$. By step 5 with $y = C e_l$, this column equals $A\bigl(B(C e_l)\bigr)$.
8. Column $l$ of $A(BC)$ is $A\bigl((BC) e_l\bigr)$, by step 2 applied to $A$ and $BC$. By step 5 for the factors $B$ and $C$, $(BC) e_l = B(C e_l)$, so this column also equals $A\bigl(B(C e_l)\bigr)$.
9. By steps 7 and 8, the matrices $(AB)C$ and $A(BC)$ have the same column $l$ for each $l = 1, \dots, q$. Both are $m \times q$, so $(AB)C = A(BC)$.

## Idea

Step 5 says that the linear map of $AB$ is the composite of the maps of $A$ and $B$: first $B$, then $A$.
Composition of functions is associative for a reason that needs no computation, since both $(f \circ g) \circ h$ and $f \circ (g \circ h)$ send $x$ to $f(g(h(x)))$.
A matrix is determined by its map, because its columns are the images of the standard basis vectors.
So the two products, which have the same map, are the same matrix.

## Variants

The [[proof by sums|1QVWFSF796]] works over any ring and needs no linear maps, but it hides the reason behind index manipulations.

Over a noncommutative ring $R$, the same argument works if we let scalars act on columns from the right, so that $A(yc) = (Ay)c$, and write step 3 as $By = \sum_k b_k y_k$.

In abstract form: the map that sends a matrix $A$ to the function $x \mapsto Ax$ is injective, and it sends products to [[composites|0THBK9V825]].
An injective map that turns products into composites carries the associativity of composition back to the product.
