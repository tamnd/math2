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

Let $\sigma : \mathbb{R} \to M_2(\mathbb{R})$ be the map $\sigma(c) = cI_2$, which sends each number to a [[scalar matrix|0FRM62SG7D]].

1. $\sigma(c) + \sigma(d) = \begin{pmatrix} c + d & 0 \\ 0 & c + d \end{pmatrix} = \sigma(c + d)$, by [[addition|0BVXADM10P]].
2. $\sigma(c)\sigma(d) = \begin{pmatrix} cd + 0 & 0 + 0 \\ 0 + 0 & 0 + cd \end{pmatrix} = \sigma(cd)$, by the [[product rule|076JGP6R3T]].
3. $\sigma(1) = I_2$, and $\sigma(c) = 0$ only for $c = 0$.
4. So $\sigma$ is an injective ring homomorphism, and its image $\{cI_2\}$ is a subring isomorphic to $\mathbb{R}$.
5. For $c \neq 0$, $\sigma(c)^{-1} = \sigma(1/c) = \tfrac{1}{c} I_2$, so the image is a field.

## Remarks

The polynomial $p(x) = x^2 - 3x + 2$ applied to a matrix $A$ means $A^2 - 3A + 2I$.
The constant term $2$ becomes the scalar matrix $2I = \sigma(2)$.
This is the reason the notation $A - \lambda$ for $A - \lambda I$ is safe.

## Explanations

### L1 human

Every real number $c$ has a twin matrix $cI$.
Adding and multiplying the twins gives the twin of the sum and of the product.

### L2 human

The image of $\sigma$ is the centre of $M_2(\mathbb{R})$, by the [[centre theorem|DVZ1V4A884]].
So the real numbers are, inside the matrix ring, exactly the matrices that commute with all others.
