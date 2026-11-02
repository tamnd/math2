---
tag: 2CKZETC3QA
kind: definition
name: Discrete series representation
msc: ["22E46", 22D10]
defines: 9AB7HYGPEK
uses: [AHV05ZBCYW, CXG6JZGMCK, VY0HXD3GC4, 74BPYJNZTM, FX3NEFYFFN, 7KGF78FGEF]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete_series_representation
---

## Definition

Let $G$ be a [[unimodular|CXG6JZGMCK]] [[locally compact group|AHV05ZBCYW]] with a [[Haar measure|VY0HXD3GC4]] $dg$.
Let $\lambda$ be the left regular representation of $G$ on $L^2(G)$, given by $(\lambda(g) f)(x) = f(g^{-1} x)$.
Let $\pi$ be an [[irreducible|FX3NEFYFFN]] [[unitary representation|74BPYJNZTM]] of $G$ on a Hilbert space $H$.
Then $\pi$ is a *discrete series representation* if it is unitarily equivalent to a subrepresentation of $\lambda$.

## Remarks

For $u, v \in H$, the matrix coefficient of $\pi$ is the function $g \mapsto \ip{\pi(g) u}{v}$.
Equivalently, $\pi$ is in the discrete series if and only if some nonzero matrix coefficient lies in $L^2(G)$.
Then every matrix coefficient lies in $L^2(G)$.

Example: let $G$ be a compact group, with Haar measure of total mass $1$.
Each matrix coefficient of a unitary representation is continuous and bounded by $\norm{u} \norm{v}$, so it lies in $L^2(G)$.
So every irreducible unitary representation of $G$ is in the discrete series.

Non-example: the irreducible unitary representations of $G = \R$ are the characters $x \mapsto e^{ixt}$ with $t \in \R$.
Each matrix coefficient has constant absolute value, so it is not square-integrable on $\R$.
So $\R$ has no discrete series, and $L^2(\R)$ decomposes as a continuous direct integral by Fourier analysis.

For groups with non-compact center, such as $\mathrm{GL}_n(\R)$, one asks instead that the matrix coefficients be square-integrable modulo the center.
For connected semisimple $G$ with finite center and maximal compact subgroup $K$, discrete series exist if and only if $\rank G = \rank K$, by a theorem of Harish-Chandra.
For example, $\mathrm{SL}_2(\R)$ has discrete series, while $\mathrm{SL}_2(\C)$ has none.
