---
tag: 04SGPNT8R9
kind: object
name: Galois field
msc: ["12E20"]
instance_of: [08RTDHX1SK]
uses: [0T8M3YC5RG, 010PKCQPXP]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Description

For each prime power $q = p^n$, the Galois field $\mathrm{GF}(q)$, also written $\mathbb{F}_q$, is the [[finite field|08RTDHX1SK]] with $q$ elements.
It [[exists|0T8M3YC5RG]], and it is [[unique up to isomorphism|010PKCQPXP]].
One model is the splitting field of $x^q - x$ over $\mathbb{F}_p = \mathbb{Z}/p\mathbb{Z}$.
Another model is $\mathbb{F}_p[x]/(f)$ for an irreducible polynomial $f \in \mathbb{F}_p[x]$ of degree $n$.

## Remarks

The name honours Évariste Galois.
The field $\mathrm{GF}(4) = \mathbb{F}_2[x]/(x^2 + x + 1)$ has the elements $0, 1, \alpha, \alpha + 1$, with $\alpha^2 = \alpha + 1$.
The field $\mathrm{GF}(p^m)$ is isomorphic to a subfield of $\mathrm{GF}(p^n)$ if and only if $m$ divides $n$.

## Explanations

### L1 human

Since there is only one finite field of each order, up to a change of names, one gives it a fixed name: the Galois field with $q$ elements.
Computations in it are done with polynomials over the integers modulo $p$.
