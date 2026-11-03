---
tag: N1Z9DX8XNX
kind: statement
role: theorem
name: Kirillov character formula
msc: ["22E27", "43A65", "22D10"]
uses: [DK87YN458D, H3QX1ZFC8K, 07JBSZE0V4, P6ZP0TE07M, 0YQPZB5Q1G, G9AW6R1D2F, VY0HXD3GC4, C37R11WREF]
about: [G9AW6R1D2F, RMWMYBY8TC]
sources:
  - url: https://en.wikipedia.org/wiki/Kirillov_character_formula
same_as:
  wikidata: Q6415283
  wikipedia: Kirillov character formula
---

## Statement

Let $G$ be a connected and simply connected [[nilpotent Lie group|DK87YN458D]] with Lie algebra $\mathfrak g$.
The [[exponential map|H3QX1ZFC8K]] $\exp \colon \mathfrak g \to G$ is then a diffeomorphism.
Let $\mathfrak g^*$ be the [[dual space|07JBSZE0V4]] of $\mathfrak g$ with the coadjoint action, the dual of the [[adjoint representation|P6ZP0TE07M]].
Fix a Lebesgue measure $dX$ on $\mathfrak g$, and let $dg$ be the [[Haar measure|VY0HXD3GC4]] on $G$ that is its image under $\exp$.
Let $\pi$ be an irreducible unitary representation of $G$, and let $\mathcal{O} \subseteq \mathfrak g^*$ be the coadjoint [[orbit|0YQPZB5Q1G]] attached to $\pi$ by the [[Kirillov orbit method|G9AW6R1D2F]].
Let $\beta$ be the Liouville measure of the canonical symplectic form on $\mathcal{O}$, normalized suitably in terms of $dX$.
Then for every smooth compactly supported function $f$ on $G$, the operator $\pi(f) = \int_G f(g) \pi(g) \, dg$ is [[trace class|C37R11WREF]], and
$$\tr \pi(f) = \int_{\mathcal{O}} \left( \int_{\mathfrak g} f(\exp X) \, e^{i \ell(X)} \, dX \right) d\beta(\ell).$$

## Remarks

In words, the character of $\pi$, pulled back to $\mathfrak g$ by $\exp$, is the Fourier transform of the orbital measure $\beta$.
The proof goes by induction on $\dim G$.
In the induction step, either $\pi$ is induced from a normal subgroup of codimension one, or $\pi$ factors through the quotient of $G$ by a central one-parameter subgroup.
The sign in $e^{i \ell(X)}$ matches the convention in which $\pi$ is induced from the character $\exp Y \mapsto e^{i \ell(Y)}$ of a polarizing subgroup.

Example: for $G = \R^n$ the orbits are points $\ell$, the representations are the characters $x \mapsto e^{i \ell(x)}$, and the formula reduces to $\tr \pi(f) = \int f(x) e^{i \ell(x)} \, dx$.
For the Heisenberg group and an orbit $\set{\ell : \ell(Z) = \lambda}$ with $\lambda \ne 0$, the formula shows that the character of the Schrödinger representation is a distribution supported on the centre.

For some other Lie groups and some of their representations a version of Kirillov's formula holds with a correction: near $0$ in $\mathfrak g$ one multiplies by $j(X)^{-1/2}$, where $j(X) = \det \big( \sinh(\mathrm{ad} X / 2) / (\mathrm{ad} X / 2) \big)$.
For nilpotent $\mathfrak g$, $\mathrm{ad} X$ is nilpotent and $j \equiv 1$, so no correction is needed.

## Explanations

### L1 human

The character of a representation is the trace of its operators, a function or distribution on the group.
Kirillov's formula computes it from geometry: take the orbit that corresponds to the representation and take the Fourier transform of the natural measure on that orbit.
So all the information about the representation's character is stored in the orbit.

### L2 human

The formula is the strongest form of the [[orbit method|G9AW6R1D2F]] for nilpotent groups.
It makes the bijection between orbits and representations compatible with characters.
It also identifies the [[Plancherel measure|QESEAKKABM]].
Integrating the formula over all orbits gives Fourier inversion on $\mathfrak g^*$, so the Plancherel measure is the image of Lebesgue measure on $\mathfrak g^*$ in the space of orbits.
For compact connected Lie groups an analogous formula holds with the correction factor $j^{-1/2}$.
There the representation of highest weight $\lambda$ uses the orbit through $\lambda + \rho$, and the formula is equivalent to the Weyl character formula.
