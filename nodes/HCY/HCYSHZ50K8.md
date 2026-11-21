---
tag: HCYSHZ50K8
kind: example
name: A box of volume 1 from the scalar triple product
msc: ["15A72", "97G70"]
topics: [VKVAJ94SKZ]
audience: school
instance_of: [34VJYG6GVD]
illustrates: [059Q2XWJDC, 7RMCRQ9ERC]
uses: [34VJYG6GVD, 0N5N15HWZ7, 0S52TNNTH9, 0C08BQ3M05]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_product
    locator: Scalar triple product
---

## Example

Let $a = (1, 2, 3)$, $b = (0, 1, 4)$ and $c = (5, 6, 0)$.
We compute the [[scalar triple product|34VJYG6GVD]] in two ways and read off what it says.

1. [[Cross product|0N5N15HWZ7]]: $b \times c = (1 \cdot 0 - 4 \cdot 6, \; 4 \cdot 5 - 0 \cdot 0, \; 0 \cdot 6 - 1 \cdot 5) = (-24, 20, -5)$.
2. [[Dot product|0S52TNNTH9]]: $a \cdot (b \times c) = 1 \cdot (-24) + 2 \cdot 20 + 3 \cdot (-5) = -24 + 40 - 15 = 1$.
3. [[Laplace expansion|0C08BQ3M05]] of the determinant with rows $a$, $b$, $c$ along row $1$:
   $$1 \cdot \det \begin{pmatrix} 1 & 4 \\ 6 & 0 \end{pmatrix} - 2 \cdot \det \begin{pmatrix} 0 & 4 \\ 5 & 0 \end{pmatrix} + 3 \cdot \det \begin{pmatrix} 0 & 1 \\ 5 & 6 \end{pmatrix} = -24 + 40 - 15 = 1.$$
4. Both ways give $1$, as the [[determinant formula|059Q2XWJDC]] says.
5. By the [[volume theorem|7RMCRQ9ERC]], the parallelepiped on $a$, $b$, $c$ has volume $1$.
6. The value is not $0$, so $a$, $b$, $c$ are not coplanar, and they form a basis of $\mathbb{R}^3$.
7. The value is positive, so $(a, b, c)$ is a right-handed triple.

## Remarks

The box is long and thin.
Its edges have lengths $\sqrt{14}$, $\sqrt{17}$ and $\sqrt{61}$, so a box with perpendicular edges of these lengths would have volume $\sqrt{14 \cdot 17 \cdot 61} \approx 120$.
The actual volume $1$ shows how strongly the edges lean toward one another.

Two more facts come for free.
The tetrahedron with vertices $0$, $a$, $b$, $c$ has volume $\tfrac{1}{6}$.
The matrix with rows $a$, $b$, $c$ has integer entries and determinant $1$, so its inverse has integer entries too.

## Explanations

### L1 human

The three arrows $(1, 2, 3)$, $(0, 1, 4)$ and $(5, 6, 0)$ make a slanted box.
The computation gives the number $1$, so the box holds exactly one unit cube of space, though its edges are long.

### L2 human

The two computations in steps 2 and 3 use the same three $2 \times 2$ minors, and step 1 lists them as the components of $b \times c$.
The middle minor is $-20$, while the middle component of $b \times c$ is $+20$; the minus sign of the Laplace expansion accounts for the difference.
Watch out: a wrong sign on the middle term gives $-24 - 40 - 15 = -79$ instead of $1$.
