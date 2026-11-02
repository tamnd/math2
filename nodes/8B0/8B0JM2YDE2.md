---
tag: 8B0JM2YDE2
kind: example
name: Metaplectic group
msc: ["22E46", "11F27", "22E15"]
instance_of: [7JBRGCVJRB]
uses: [X12FS2JAP0, S1XK3HXHFX, 3XZRRE165N, Q0GBCB9RA4]
sources:
  - url: https://en.wikipedia.org/wiki/Metaplectic_group
same_as:
  wikidata: Q17098877
  wikipedia: Metaplectic group
---

## Example

Let $n \ge 1$ and let $\mathrm{Sp}(2n, \R)$ be the real [[symplectic group|X12FS2JAP0]].
It is a connected Lie group, and $U(n)$ is a maximal compact subgroup of it, so its [[fundamental group|S1XK3HXHFX]] is isomorphic to $\pi_1(U(n)) \cong \Z$.
The group $\Z$ has exactly one subgroup of index $2$, so $\mathrm{Sp}(2n, \R)$ has exactly one connected two-sheeted [[covering|3XZRRE165N]], up to isomorphism.
That covering space carries a unique Lie group structure for which the covering map is a homomorphism.

The *metaplectic group* $\mathrm{Mp}(2n, \R)$ is this connected double cover of $\mathrm{Sp}(2n, \R)$.
So there is an exact sequence
$$1 \to \set{\pm 1} \to \mathrm{Mp}(2n, \R) \to \mathrm{Sp}(2n, \R) \to 1.$$
For $n = 1$, $\mathrm{Sp}(2, \R) =$ [[SL(2,R)|Q0GBCB9RA4]], and $\mathrm{Mp}(2, \R)$ is the connected double cover of $SL(2, \R)$.

## Remarks

$\mathrm{Mp}(2n, \R)$ is not a matrix group: it has no faithful finite-dimensional representation.
It does have a faithful unitary representation on the infinite-dimensional Hilbert space $L^2(\R^n)$, the oscillator representation, also called the Segal–Shale–Weil representation.
This representation does not come from a representation of $\mathrm{Sp}(2n, \R)$; it is defined only up to sign on $\mathrm{Sp}(2n, \R)$.
The group $\mathrm{Mp}(2, \R)$ is the setting for modular forms of half-integral weight, such as the Jacobi theta function.

## Explanations

### L1 human

The metaplectic group is a twofold cover of the real symplectic group, just as the spin group is a twofold cover of the rotation group.
Each symplectic matrix corresponds to two elements of the metaplectic group, which differ by a sign.
It appears because some natural constructions, such as the quantization of linear symplectic maps in quantum mechanics, are only defined up to a sign on the symplectic group.
Passing to the metaplectic group removes this sign ambiguity.
