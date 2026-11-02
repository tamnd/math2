---
tag: VNMBSYX9PY
kind: statement
role: lemma
name: Horseshoe lemma
msc: [18G10, 18G05]
uses: [Y9CZ3MTNF1, KJKNJMGKZZ, HK2AA1YSQ2, YXMXAGVC1Q, WQ82C0M3QB]
about: [HK2AA1YSQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Horseshoe_lemma
same_as:
  wikidata: Q5906080
  wikipedia: Horseshoe lemma
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]].
Let $0 \to A' \xrightarrow{i} A \xrightarrow{\pi} A'' \to 0$ be a [[short exact sequence|KJKNJMGKZZ]] in $\mathcal{A}$.
Let $P'_\bullet \to A'$ and $P''_\bullet \to A''$ be [[projective resolutions|HK2AA1YSQ2]].
Then there is a projective resolution $P_\bullet \to A$ with $P_n = P'_n \oplus P''_n$ for every $n \ge 0$ with the following property.
The inclusions $P'_n \to P_n$ and the projections $P_n \to P''_n$ form a short exact sequence of [[chain complexes|WQ82C0M3QB]]
$$0 \to P'_\bullet \to P_\bullet \to P''_\bullet \to 0$$
that lifts the sequence $0 \to A' \to A \to A'' \to 0$.

## Remarks

The proof builds $P_\bullet$ one degree at a time.
Since $P''_0$ is [[projective|YXMXAGVC1Q]], the map $P''_0 \to A''$ lifts through $\pi$ to a map $P''_0 \to A$.
Together with $P'_0 \to A' \to A$ this gives $P'_0 \oplus P''_0 \to A$, which is an epimorphism by the snake lemma.
The kernels again form a short exact sequence, and the same step is repeated with them.
The differential of $P_\bullet$ is in general not the direct sum of the differentials: it has an extra component $P''_n \to P'_{n-1}$.
For example, over $\Z$ take $0 \to \Z \xrightarrow{\cdot 2} \Z \to \Z/2\Z \to 0$ with $P'_\bullet = \Z$ and $P''_\bullet = (\Z \xrightarrow{\cdot 2} \Z)$; the lemma gives a resolution of $\Z$ by $\Z^2$ in degree $0$ and $\Z$ in degree $1$.
The dual statement holds for injective resolutions.

## Explanations

### L1 human

If the two outer terms of a short exact sequence have projective resolutions, the middle term gets one too.
The new resolution is built from the two old ones, placed side by side.
The picture of the two resolutions on the left and right, with the new one in the middle, looks like a horseshoe.

### L2 human

The lemma is the key step to show that a short exact sequence gives a long exact sequence of left [[derived functors|NPMC3K6J2F]].
Applying an additive functor to the split sequences $0 \to P'_n \to P_n \to P''_n \to 0$ keeps them exact, and the long exact sequence in homology does the rest.
The same construction, applied degree by degree, is used to build [[Cartan–Eilenberg resolutions|SX8V8GR5ZG]].
