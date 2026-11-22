---
tag: MMSPCWKJQY
kind: example
name: Complex conjugation on Cⁿ is antilinear
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: grad
instance_of: [BNPDDM95KF]
uses: [BNPDDM95KF, 0FTH2E9TAS, 0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Semilinear_map
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Antilinear_map
    locator: Examples
---

## Example

Conjugating every coordinate respects sums, but it turns each scalar into its conjugate.
Let $C \colon \C^n \to \C^n$ apply [[complex conjugation|0FTH2E9TAS]] to each coordinate,
$$C(z_1, \dots, z_n) = (\bar z_1, \dots, \bar z_n).$$

1. Since $\overline{z_k + w_k} = \bar z_k + \bar w_k$ for each $k$, we get $C(z + w) = C(z) + C(w)$.
2. Since $\overline{\lambda z_k} = \bar\lambda\, \bar z_k$ for each $k$, we get $C(\lambda z) = \bar\lambda\, C(z)$.
3. By steps 1 and 2, $C$ is [[antilinear|BNPDDM95KF]], with $\sigma$ the conjugation of $\C$.
4. The map $C$ is not $\C$-[[linear|0RJF668P1T]], since with $e_1 = (1, 0, \dots, 0)$ we get $C(i e_1) = -i e_1$, while $i\,C(e_1) = i e_1$.
5. Since $\bar{\bar z} = z$, we get $C \circ C = \id$, so $C$ is bijective, and this composite of two antilinear maps is linear.

Check: in $\C^2$, $C((1 + i)(2, i)) = C(2 + 2i, \; -1 + i) = (2 - 2i, \; -1 - i)$, and $(1 - i)\,C(2, i) = (1 - i)(2, -i) = (2 - 2i, \; -1 - i)$.

## Remarks

The map $C$ is linear over $\R$, since $C(rz) = r\,C(z)$ for $r \in \R$, because $\bar r = r$.
Every antilinear map $T \colon \C^n \to \C^m$ has the form $z \mapsto A \bar z$ for a unique complex $m \times n$ matrix $A$, since $T \circ C$ is linear, and here $A = I$.
The fixed points of $C$ form $\R^n$, a real subspace that is not a complex subspace.
If we change the field to $\R$, conjugation becomes the identity of $\R^n$, which is linear.

## Explanations

### L1 human

Conjugation flips the sign of each imaginary part.
It respects sums, but it turns the scalar $i$ into $-i$.
So it is linear over the real numbers but antilinear over the complex numbers.

### L2 human

To recognize an antilinear map, test it on $i v$, where an antilinear map gives $-i\,T(v)$.
Conjugation passes this test, and applying it twice gives the identity.
Watch out: conjugation is an isomorphism of real vector spaces, but it is not a linear isomorphism of the complex space $\C^n$.
