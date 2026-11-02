---
tag: 4RG1RB1MXH
kind: definition
name: Biproduct
msc: ["18E05", 18A30]
defines: BZEJKTQ76T
uses: [YF9F9EG6M3, S5744QZV4N, 4FJ0S71P58, SC6FD5F4J0, 082GHNPJ53, TM7QS7P7X9]
sources:
  - url: https://en.wikipedia.org/wiki/Biproduct
---

## Definition

Let $\mathcal{C}$ be a category with [[zero morphisms|YF9F9EG6M3]], and let $X_1, X_2$ be objects of $\mathcal{C}$.
A *biproduct* of $X_1$ and $X_2$ is an object $X$ with morphisms $p_k \colon X \to X_k$ and $i_k \colon X_k \to X$ for $k = 1, 2$ such that:

1. $p_k \circ i_k = \id_{X_k}$ for $k = 1, 2$, and $p_l \circ i_k = 0$ for $k \ne l$;
2. $(X, p_1, p_2)$ is a [[product|S5744QZV4N]] of $X_1$ and $X_2$;
3. $(X, i_1, i_2)$ is a [[coproduct|4FJ0S71P58]] of $X_1$ and $X_2$.

The biproduct is written $X_1 \oplus X_2$; biproducts of finite families are defined in the same way.

## Remarks

In a [[preadditive category|SC6FD5F4J0]], an object $X$ with maps $p_k$, $i_k$ satisfying clause 1 and $i_1 \circ p_1 + i_2 \circ p_2 = \id_X$ is a biproduct, and every biproduct has this form.
In particular, in a preadditive category every binary product, and every binary coproduct, is a biproduct.

Example: for [[abelian groups|082GHNPJ53]] $A$ and $B$, the direct sum $A \oplus B$ with $p_1(a, b) = a$, $p_2(a, b) = b$, $i_1(a) = (a, 0)$, $i_2(b) = (0, b)$ is a biproduct.
Clause 1 is immediate, and $i_1 p_1 + i_2 p_2$ sends $(a, b)$ to $(a, 0) + (0, b) = (a, b)$.

Non-example: in the category of groups, with the trivial group as zero object, the product $\Z \times \Z$ with its inclusions satisfies clauses 1 and 2 but not clause 3.
If it were a coproduct, the maps $\Z \to F_2$ onto the two generators $a, b$ of the free group $F_2$ would extend to one homomorphism $\Z \times \Z \to F_2$.
Its image would be abelian and contain $a$ and $b$, but $ab \ne ba$ in $F_2$.
The coproduct in groups is the [[free product|TM7QS7P7X9]] instead.
