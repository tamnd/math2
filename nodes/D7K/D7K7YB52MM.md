---
tag: D7K7YB52MM
kind: statement
role: theorem
name: Puppe sequence
msc: [55P05, 55Q05]
uses: [T9DG8DDE75, Q7RFNJH76Q, JB7ZBFBA9C, SMEV5BSQ5S, W5WS5EY8ZM]
about: [T9DG8DDE75, W5WS5EY8ZM]
sources:
  - url: https://en.wikipedia.org/wiki/Puppe_sequence
same_as:
  wikidata: Q7260695
  wikipedia: Puppe sequence
---

## Statement

Let $f \colon (X, x_0) \to (Y, y_0)$ be a map of [[pointed spaces|T9DG8DDE75]], and let $I = [0, 1]$.
Let $CX = (X \times I) / (X \times \set{1} \cup \set{x_0} \times I)$ be the reduced cone on $X$.
Let $\Sigma X = CX / (X \times \set{0})$ be the reduced [[suspension|Q7RFNJH76Q]] of $X$.
Let $C_f = (Y \sqcup CX) / \sim$, with $[(x, 0)] \sim f(x)$ for $x \in X$, be the reduced mapping cone of $f$.
Let $i \colon Y \to C_f$ be the inclusion, and let $q \colon C_f \to \Sigma X$ be the map that collapses $Y$ to the base point.
Then there is a sequence of pointed maps
$$X \xrightarrow{f} Y \xrightarrow{i} C_f \xrightarrow{q} \Sigma X \xrightarrow{\Sigma f} \Sigma Y \xrightarrow{\Sigma i} \Sigma C_f \xrightarrow{\Sigma q} \Sigma^2 X \xrightarrow{\Sigma^2 f} \cdots$$
with the following property.
For every pointed space $Z$, the induced sequence of sets of pointed homotopy classes
$$\cdots \to [\Sigma Y, Z]_* \to [\Sigma X, Z]_* \to [C_f, Z]_* \to [Y, Z]_* \to [X, Z]_*$$
is exact.
Exactness at a term means this: the image of the incoming map is the set of classes sent to the class of the constant map.

## Remarks

The key step is that the mapping cone of $i \colon Y \to C_f$ is homotopy equivalent to $\Sigma X$, by collapsing the cone on $Y$, which is a contractible subspace attached along a [[cofibration|W5WS5EY8ZM]].
Exactness at $[Y, Z]_*$ is direct.
A map $g \colon Y \to Z$ extends over $C_f$ exactly when $g \circ f$ is [[null-homotopic|SMEV5BSQ5S]] by a pointed homotopy, since such a null-homotopy is a map on $CX$.
Repeating the step gives the whole sequence, and up to sign the maps after $q$ are suspensions of the earlier ones.
The terms $[\Sigma^n X, Z]_*$ are groups for $n \ge 1$ and abelian groups for $n \ge 2$, and there the [[exact sequence|JB7ZBFBA9C]] is one of groups.
When $f$ is the inclusion of a subcomplex $X$ of a CW complex $Y$, the space $C_f$ is homotopy equivalent to the quotient $Y / X$.
The dual construction with loop spaces and homotopy fibres gives the fibre sequence $\cdots \to \Omega Y \to F \to X \to Y$.

## Explanations

### L1 human

The Puppe sequence turns a single map $f \colon X \to Y$ into an infinite chain of spaces and maps.
Each new space is built by coning off the previous map, and after three steps the chain repeats with suspended spaces.
Mapping this chain into any space $Z$ gives an exact sequence, so information about maps out of $X$ and $Y$ controls maps out of the cone $C_f$.

### L2 human

The Puppe sequence is the source of long exact sequences in homotopy theory.
Applied to the inclusion of a subcomplex $A \subseteq X$ and to a representing space $Z$, such as an Eilenberg–MacLane space, it yields the long exact sequence of a pair in cohomology.
Its [[Eckmann–Hilton dual|1EK3355WMC]] is the fibre sequence, which yields the long exact sequence of homotopy groups of a fibration.
It is a basic example of a triangulated structure, which in the stable homotopy category becomes the distinguished triangles $X \to Y \to C_f \to \Sigma X$.
