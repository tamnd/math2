---
tag: X7417ZQWZY
kind: statement
role: proposition
name: Dual of a compact group is discrete
msc: [43A40, 22B05, 22C05]
uses: [ZR09S9R3AW, EVHCE5VR6Y, FMW57WNPDB, H1WNVN5V7F, RG15F0TWPW, 04EAFVFTF7]
about: [FMW57WNPDB]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] that is [[compact|EVHCE5VR6Y]].
Let $\widehat{G}$ be its [[Pontryagin dual|FMW57WNPDB]], the group of continuous [[characters|H1WNVN5V7F]] $\chi \colon G \to \mathbb{T}$ with the [[compact-open topology|RG15F0TWPW]].
Then $\widehat{G}$ is discrete.

## Remarks

The idea of the proof: since $G$ is compact, the compact-open topology on $\widehat{G}$ is the topology of uniform convergence on $G$.
So $V = \set{\chi \in \widehat{G} : \abs{\chi(x) - 1} < 1 \text{ for all } x \in G}$ is an open neighbourhood of the trivial character.
For $\chi \in V$, the image $\chi(G)$ is a subgroup of the [[circle group|04EAFVFTF7]] $\mathbb{T}$ contained in the arc $\set{z : \abs{z - 1} < 1}$.
If $z = e^{i\theta}$ with $0 < \abs{\theta} \le \pi$ were in this subgroup, some power $z^n$ would have argument in $[\pi/3, 5\pi/3]$ and so $\abs{z^n - 1} \ge 1$; hence $\chi(G) = \set{1}$.
Thus $V = \set{1}$ is open, and by translation every point of $\widehat{G}$ is open.

Example: $\widehat{\mathbb{T}} \cong \Z$, where $n \in \Z$ gives the character $z \mapsto z^n$, and $\Z$ is discrete.
For a finite abelian group $G$, the dual $\widehat{G}$ is finite and discrete, and isomorphic to $G$.

The converse also holds: $G$ is discrete if and only if $\widehat{G}$ is compact.
Without compactness the conclusion fails: $\widehat{\R} \cong \R$ is not discrete.

## Explanations

### L1 human

A compact abelian group, such as the circle, has only "separated" frequencies.
On the circle the frequencies are the whole numbers, and one cannot move continuously from one to the next.
This is why a periodic function has a Fourier series indexed by integers rather than a Fourier integral.

### L2 human

The result is one half of the duality between compact and discrete groups under Pontryagin duality.
A second proof uses the normalized Haar measure: distinct characters are orthogonal in $L^2(G)$, so $\norm{\chi - \psi}_2 = \sqrt{2}$ for $\chi \ne \psi$, and characters cannot accumulate.
It explains why harmonic analysis on a compact abelian group uses sums over $\widehat{G}$, as in the Fourier series of a function in $L^2(G)$.
For compact non-abelian groups, the analogous fact is that the set of irreducible unitary representations, up to equivalence, is a discrete space in the Fell topology.
