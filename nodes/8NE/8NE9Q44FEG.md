---
tag: 8NE9Q44FEG
kind: statement
role: theorem
name: Kaplansky's theorem on PI rings
msc: [16R20, 16D60]
uses: [8F6EHDVJ62, C0EDT81EGH, 5HRKJBAY2V, MVT64B3B6H, EK0T7FRKCY, YDH60KPTWT, 0EA5BTA0CX]
about: [C0EDT81EGH, 8F6EHDVJ62]
sources:
  - url: https://en.wikipedia.org/wiki/Polynomial_identity_ring
---

## Statement

Let $R$ be a [[primitive ring|8F6EHDVJ62]] (right or left).
Assume that $R$ satisfies a monic [[polynomial identity|C0EDT81EGH]] of degree $d$.
Let $Z$ be the [[center|MVT64B3B6H]] of $R$.
Then $Z$ is a field, $R$ is a [[central simple algebra|5HRKJBAY2V]] over $Z$, and
$$\dim_Z R = m^2 \quad \text{with} \quad m \le d/2.$$

## Remarks

By the [[Jacobson density theorem|EK0T7FRKCY]], $R$ is a dense ring of linear maps of a vector space $V$ over a [[division ring|0EA5BTA0CX]] $D$.
If $\dim_D V$ were large, a subring of $R$ would map onto a ring of matrices $M_s(D)$ with $s$ large.
Such a matrix ring fails every monic identity of degree less than $2s$, so $\dim_D V$ is finite and $R \cong M_s(D)$.
Then $D$ is a PI division ring, and a maximal subfield argument shows that $D$ is finite-dimensional over its centre.
The bound $m \le d/2$ comes from comparing with matrix rings over a splitting field, using part 2 of the [[Amitsur–Levitzki theorem|YDH60KPTWT]].

Example: $R = M_n(F)$ for a field $F$ is primitive, satisfies the standard identity $s_{2n}$ of degree $d = 2n$, and has $\dim_F R = n^2$ with $n = d/2$.
So the bound is sharp.

The primitive hypothesis is needed: the polynomial ring $\Z[x]$ satisfies the identity $x_1 x_2 - x_2 x_1$ of degree $2$, but its centre $\Z[x]$ is not a field.

## Explanations

### L1 human

Primitive rings are the rings that act faithfully and irreducibly on some module, and in general they can be huge, such as rings of operators on infinite-dimensional spaces.
Kaplansky's theorem says that once such a ring satisfies a polynomial identity, it must be small.
It is a matrix ring over a division ring that is finite-dimensional over its centre.
The degree of the identity bounds the size of the matrices.

### L2 human

The theorem is the first structure theorem of PI theory.
Because every semiprimitive ring is a subdirect product of primitive rings, it lets one embed semiprimitive PI rings into products of central simple algebras of bounded degree.
It extends to prime PI rings through Posner's theorem, and it is one of the tools behind the positive answer to the Kurosh problem for PI algebras.
