---
tag: DH3PYQJXH0
kind: statement
role: theorem
name: Plancherel theorem for groups
msc: [22D10, 43A30, 22D20]
uses: [AHV05ZBCYW, VY0HXD3GC4, CXG6JZGMCK, 74BPYJNZTM, 95Q8WZMN0W, HM2HHE3J51]
about: [95Q8WZMN0W, 74BPYJNZTM]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_theorem_for_spherical_functions
  - url: https://en.wikipedia.org/wiki/Plancherel_measure
---

## Statement

Let $G$ be a second countable, [[unimodular|CXG6JZGMCK]] [[locally compact group|AHV05ZBCYW]] of type I, with a fixed [[Haar measure|VY0HXD3GC4]] $dg$.
Let $\widehat{G}$ be its [[unitary dual|95Q8WZMN0W]], the set of equivalence classes of irreducible [[unitary representations|74BPYJNZTM]] of $G$, with its Borel structure.
For $f \in L^1(G)$ and a unitary representation $\pi$ of $G$ on a [[Hilbert space|HM2HHE3J51]] $\mathcal{H}_\pi$, let $\pi(f) = \int_G f(g) \pi(g) \, dg$, a bounded operator on $\mathcal{H}_\pi$.
Then there is a unique positive Borel measure $\mu$ on $\widehat{G}$, the *Plancherel measure*, with the following property.
For every $f \in L^1(G) \cap L^2(G)$, the operator $\pi(f)$ is Hilbert–Schmidt for $\mu$-almost every $\pi$, and
$$\int_G \abs{f(g)}^2 \, dg = \int_{\widehat{G}} \norm{\pi(f)}_{\mathrm{HS}}^2 \, d\mu(\pi).$$

## Remarks

The idea of the proof is to decompose the two-sided regular representation of $G \times G$ on $L^2(G)$.
For a type I group, the left regular representation is a direct integral of irreducible representations over $\widehat{G}$.
The Plancherel measure is the measure in this direct integral, normalised by the choice of $dg$.
The identity then extends by continuity to a unitary isomorphism from $L^2(G)$ onto a direct integral of the spaces of Hilbert–Schmidt operators on the $\mathcal{H}_\pi$.

For $G = \R$ with Lebesgue measure, $\widehat{G}$ is the set of characters $x \mapsto e^{i \xi x}$ with $\xi \in \R$, each $\pi(f)$ is multiplication by a value of the Fourier transform, and $\mu = d\xi / 2\pi$.
This is the classical Plancherel theorem.
For a [[compact group|EVHCE5VR6Y]] with Haar measure of total mass $1$, the dual $\widehat{G}$ is discrete, $\mu(\set{\pi}) = \dim \mathcal{H}_\pi$, and the formula is the Parseval identity of the [[Peter–Weyl theorem|6VC9QE39XH]].

The type I hypothesis cannot simply be dropped.
For groups that are not of type I, the regular representation can decompose in essentially different ways, and the formula needs factor representations.
Without unimodularity, the operators $\pi(f)$ must be corrected by unbounded positive operators before the formula holds.

## Explanations

### L1 human

For functions on the line, the Plancherel theorem says that the energy of a function equals the energy of its Fourier transform.
For a general group, the role of the frequencies is played by the irreducible representations of the group.
The theorem gives a measure on these representations, the Plancherel measure, that makes the energy identity true.
It tells which representations really occur when one breaks $L^2(G)$ into pieces.

### L2 human

Many groups met in practice are of type I: abelian groups, compact groups, connected semisimple Lie groups and connected nilpotent Lie groups.
For abelian groups the Plancherel measure is the Haar measure on the Pontryagin dual, suitably normalised.
For a semisimple Lie group, Harish-Chandra computed the Plancherel measure explicitly; the discrete series representations are exactly the atoms of $\mu$.
For a [[Gelfand pair|W38ZDXDVYC]] $(G, K)$ and functions that are bi-invariant under $K$, the theorem becomes the Plancherel theorem for [[spherical functions|BKZNC76RC8]].
