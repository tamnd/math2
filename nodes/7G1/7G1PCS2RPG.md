---
tag: 7G1PCS2RPG
kind: statement
role: theorem
name: Thom–Mather isotopy lemmas
msc: [58A35, 57N80, 32S60]
uses: [P9R3777ZJF, 3F84AMVJNV, F45VQ47GPV, GTMT5ZFV00, 15XEBGNGHC, 0QT00PB5G2]
about: [P9R3777ZJF, 3F84AMVJNV]
sources:
  - url: https://en.wikipedia.org/wiki/Thom%E2%80%93Mather_stratified_space
---

## Statement

Let $M$, $N$ and $P$ be [[smooth manifolds|F45VQ47GPV]].
A map between stratified sets is *stratum-preserving* if it maps each stratum into a stratum.

1. (First isotopy lemma.) Let $X \subseteq M$ be a closed subset with a [[Whitney stratification|3F84AMVJNV]], and let $f \colon M \to P$ be a smooth map.
Assume that $f|_X \colon X \to P$ is [[proper|15XEBGNGHC]] and that $f|_S \colon S \to P$ is a [[submersion|GTMT5ZFV00]] for every stratum $S$ of $X$.
Then $f|_X$ is a locally trivial fibration with stratum-preserving trivialisations: every $p \in P$ has an open neighbourhood $U$ and a stratum-preserving [[homeomorphism|0QT00PB5G2]] $h \colon f^{-1}(U) \cap X \to (f^{-1}(p) \cap X) \times U$ with $\mathrm{pr}_U \circ h = f$.
2. (Second isotopy lemma.) Let $X \subseteq M$ and $Y \subseteq N$ be closed Whitney stratified subsets, and let $f \colon M \to N$ and $g \colon N \to P$ be smooth maps with $f(X) \subseteq Y$.
Assume that $f|_X$ and $g|_Y$ are proper, and that $f$ maps each stratum of $X$ submersively onto a stratum of $Y$.
Assume that $f|_X$ satisfies Thom's condition $a_f$, and that $g|_S$ is a submersion for every stratum $S$ of $Y$.
Then $f|_X$ is locally trivial over $P$, in this sense.
Every $p \in P$ has an open neighbourhood $U$ and stratum-preserving homeomorphisms $X \cap (g f)^{-1}(U) \to (X \cap (g f)^{-1}(p)) \times U$ and $Y \cap g^{-1}(U) \to (Y \cap g^{-1}(p)) \times U$.
These homeomorphisms commute with the projections to $U$ and with $f$.

## Remarks

The proof uses the control data of a [[Thom–Mather stratified space|P9R3777ZJF]], which Mather constructed on every Whitney stratified set.
One lifts the coordinate vector fields of $U$ to controlled vector fields on $X$, smooth on each stratum and compatible with the tubular projections and distance functions.
Controlled vector fields have continuous flows that preserve each stratum, and properness makes the flows defined for the needed times.
Integrating them gives the trivialisation.
The flows are only continuous across strata, so the trivialisations are homeomorphisms, not diffeomorphisms.

Example: in $M = \R^3$ let $X$ be the union of the cylinder $\set{x^2 + y^2 = 1}$ and the $t$-axis $\set{x = y = 0}$, with these two strata, and let $f(x, y, t) = t$.
Each stratum is mapped submersively onto $\R$, and $f|_X$ is proper since $X \cap \set{\abs{t} \le c}$ is compact.
The first lemma gives a homeomorphism of $X$ with $(\text{circle} \sqcup \text{point}) \times \R$ that keeps the two strata apart.

Properness is needed: the inclusion of $M = X = \R \setminus \set{0}$ into $P = \R$, with one stratum, is a submersion.
But its fibres are points over $t \ne 0$ and empty over $0$, so it is not locally trivial near $0$.

## Explanations

### L1 human

A stratified space is a space made of smooth pieces of different dimensions, such as a cone made of its tip and its smooth part.
The first lemma is a version of Ehresmann's theorem for such spaces.
If a proper map has no critical points on any piece, then its fibres all look the same, up to a homeomorphism that respects the pieces.
The second lemma does the same for a map between two stratified spaces that moves in a family.

### L2 human

For smooth manifolds, Ehresmann's fibration theorem says that a proper submersion is a locally trivial fibration.
The first isotopy lemma extends this to Whitney stratified sets, at the price of getting only homeomorphisms.
It shows, for instance, that a Whitney stratified set is locally topologically trivial along each stratum.
So the local topology near a point stays the same as the point moves within a connected stratum.
The second lemma is a key tool in Mather's proof that topologically stable maps are dense.
Thom's condition $a_f$ is the hypothesis that makes the two families of trivialisations compatible.

