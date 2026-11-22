---
tag: J50X0JC5QV
kind: proof
name: Proof of the Cartesian decomposition of a complex square matrix
msc: ["15B57"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: E2MNC3W2DM
methods: [0NTF6DMVAP]
uses: [0EKZCX4K3P, 0EX045E2BP]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_matrix
    locator: Properties
---

## Proof

We check that the given $H$ and $K$ work, and then we recover $H$ and $K$ from any splitting by applying the conjugate transpose.

Let $A$ be a complex $n \times n$ matrix.
We use three rules of the [[conjugate transpose|0EX045E2BP]]: $(X^*)^* = X$, $(X + Y)^* = X^* + Y^*$ and $(cX)^* = \overline{c}\, X^*$ for a complex number $c$.

1. Existence. Put $H = \tfrac12 (A + A^*)$ and $K = \tfrac{1}{2i} (A - A^*)$.
2. The scalar $\tfrac12$ is real, so the rules give
$$H^* = \tfrac12 (A^* + A) = H.$$
So $H$ is [[Hermitian|0EKZCX4K3P]].
3. The conjugate of $\tfrac{1}{2i}$ is $\tfrac{1}{-2i} = -\tfrac{1}{2i}$, so
$$K^* = -\tfrac{1}{2i} (A^* - A) = \tfrac{1}{2i} (A - A^*) = K.$$
So $K$ is Hermitian.
4. Since $i \cdot \tfrac{1}{2i} = \tfrac12$, we get
$$H + iK = \tfrac12 (A + A^*) + \tfrac12 (A - A^*) = A.$$
5. Uniqueness. Suppose that $A = H' + iK'$ with $H'$ and $K'$ Hermitian.
6. Apply the conjugate transpose, with $\overline{i} = -i$, $H'^* = H'$ and $K'^* = K'$:
$$A^* = H' - iK'.$$
7. Add the equations of steps 5 and 6: $A + A^* = 2H'$, so $H' = \tfrac12 (A + A^*) = H$.
8. Subtract the equation of step 6 from that of step 5: $A - A^* = 2iK'$, so $K' = \tfrac{1}{2i}(A - A^*) = K$.

So $H$ and $K$ are Hermitian, $A = H + iK$, and every such splitting is this one.

## Idea

Taking the conjugate transpose of $A = H + iK$ gives $A^* = H - iK$, because $H$ and $K$ do not change and $i$ turns into $-i$.
Now we have two equations in the two unknowns $H$ and $K$.
Adding and subtracting them solves for $H$ and $K$, just as $z = x + iy$ and $\overline{z} = x - iy$ give $x$ and $y$.
The same calculation proves existence, since the solved formulas are Hermitian.

## Variants

The [[decomposition into symmetric and skew-symmetric parts|T2153B5Y7V]] has the same proof, with the transpose in place of the conjugate transpose and without the factor $i$.
A second route uses linear algebra over $\mathbb{R}$: the map $X \mapsto X^*$ is a real linear map with square equal to the identity, so $M_n(\mathbb{C})$ is the direct sum of its eigenspaces for $1$ and $-1$, the Hermitian and the skew-Hermitian matrices.
Then $iK$ is the skew-Hermitian component of $A$.
