---
tag: SJM276KGDB
kind: example
name: The scalar matrices form a copy of the real numbers
msc: ["15A99", "16S50"]
topics: [Y1ESNQ2V52]
audience: ug1
instance_of: [067NKSBEWT]
uses: [0FRM62SG7D, 0BVXADM10P, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_ring
    locator: Properties
---

## Example

Each real number has a twin among the $2 \times 2$ matrices, and the twins add and multiply like the numbers.
Let $\sigma : \mathbb{R} \to M_2(\mathbb{R})$ be the map $\sigma(c) = cI_2$, which sends each number to a [[scalar matrix|0FRM62SG7D]].
We check that $\sigma$ is an injective ring homomorphism.

1. Sums go to sums. By entrywise [[addition|0BVXADM10P]],
$$\sigma(c) + \sigma(d) = \begin{pmatrix} c + d & 0 \\ 0 & c + d \end{pmatrix} = \sigma(c + d).$$
2. Products go to products. By the [[product rule|076JGP6R3T]],
$$\sigma(c)\sigma(d) = \begin{pmatrix} cd + 0 & 0 + 0 \\ 0 + 0 & 0 + cd \end{pmatrix} = \sigma(cd).$$
3. The identity goes to the identity, since $\sigma(1) = I_2$.
4. The kernel is zero: $\sigma(c) = 0$ forces the diagonal entry $c$ to be $0$.
5. By steps 1 to 4, $\sigma$ is an injective ring homomorphism, and its image $\{ cI_2 : c \in \mathbb{R} \}$ is a subring of $M_2(\mathbb{R})$ isomorphic to $\mathbb{R}$.
6. For $c \ne 0$, step 2 gives $\sigma(c)\sigma(1/c) = \sigma(1) = I_2$, so $\sigma(c)^{-1} = \tfrac{1}{c} I_2$. So the image is a field inside a ring that is not a field.

## Remarks

### Numbers inside polynomials of a matrix

The map $\sigma$ explains how a polynomial is applied to a matrix.
For $p(x) = x^2 - 3x + 2$, the value $p(A)$ is $A^2 - 3A + 2I$, where the constant $2$ becomes $\sigma(2) = 2I$.
Since $\sigma$ respects sums and products and each $\sigma(c)$ commutes with $A$, evaluation at $A$ respects sums and products of polynomials, so every identity between real polynomials, such as $x^2 - 3x + 2 = (x - 1)(x - 2)$, gives the matching identity $A^2 - 3A + 2I = (A - I)(A - 2I)$ for every matrix $A$.

### The image is the center

The image of $\sigma$ is exactly the set of matrices that commute with all of $M_2(\mathbb{R})$, by the [[center theorem|DVZ1V4A884]].
The [[complex numbers also sit inside|GHV77C35RT]] $M_2(\mathbb{R})$, as the matrices $\begin{pmatrix} a & -b \\ b & a \end{pmatrix}$, and the image of $\sigma$ is the part with $b = 0$.
That larger copy is commutative, but it is not central.

## Explanations

### L1 human

Every real number $c$ has a twin matrix $cI$, with $c$ on the diagonal and $0$ elsewhere.
Adding two twins gives the twin of the sum, and multiplying two twins gives the twin of the product.
So the real numbers live inside the $2 \times 2$ matrices.

### L2 human

The typical use is to read a number as a matrix when it meets a matrix, as in $A - \lambda I$ or $A^2 - 3A + 2I$.
Because $\sigma$ is a ring homomorphism, no calculation changes when we make this switch.
Watch out: the twin of $2$ is $2I$, not the matrix with every entry equal to $2$.
