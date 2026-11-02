---
tag: H4JSMZK622
kind: definition
name: Monoid object
msc: [18M05, 18C40]
defines: 9G1XS1XZ1F
uses: [M3MSQ3NKAE, 0N6R902FG1]
sources:
  - url: https://en.wikipedia.org/wiki/Monoid_(category_theory)
---

## Definition

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ be a [[monoidal category|M3MSQ3NKAE]].
A *monoid object* in $\mathcal{C}$ is an object $M$ together with morphisms $\mu \colon M \otimes M \to M$ (multiplication) and $\eta \colon I \to M$ (unit) such that:

1. associativity: $\mu \circ (\mu \otimes \id_M) = \mu \circ (\id_M \otimes \mu) \circ \alpha_{M,M,M}$ as morphisms $(M \otimes M) \otimes M \to M$;
2. left unit: $\mu \circ (\eta \otimes \id_M) = \lambda_M$ as morphisms $I \otimes M \to M$;
3. right unit: $\mu \circ (\id_M \otimes \eta) = \rho_M$ as morphisms $M \otimes I \to M$.

A morphism of monoid objects $(M, \mu, \eta) \to (M', \mu', \eta')$ is a morphism $f \colon M \to M'$ with $f \circ \mu = \mu' \circ (f \otimes f)$ and $f \circ \eta = \eta'$.

## Remarks

Example: in $(\mathbf{Set}, \times, \set{*})$, a monoid object is a set $M$ with $\mu(a, b) = ab$ and $\eta(*) = e$; the three axioms say $(ab)c = a(bc)$, $ea = a$ and $ae = a$, so it is an ordinary [[monoid|0N6R902FG1]].
Example: in $(\mathbf{Ab}, \otimes, \Z)$, a monoid object is a ring, since a bilinear multiplication is a morphism $R \otimes R \to R$.
Non-example: in $(\mathbf{Set}, \times, \set{*})$, the set $\Z$ with $\mu(a, b) = a - b$ and $\eta(*) = 0$ fails associativity, because $(1 - 1) - 1 = -1$ while $1 - (1 - 1) = 1$.
A monoid object in a symmetric monoidal category is *commutative* if $\mu \circ \gamma_{M,M} = \mu$, where $\gamma$ is the symmetry.
