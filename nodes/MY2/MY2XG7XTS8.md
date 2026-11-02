---
tag: MY2XG7XTS8
kind: definition
name: Octahedral axiom
msc: [18G80]
defines: P8PFMNCB8Y
uses: [B2VP96NJSK, KAN07YC9T2]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulated_category
---

## Definition

Let $\mathcal{T}$ be an [[additive category|B2VP96NJSK]] with an [[additive|KAN07YC9T2]] automorphism $\Sigma$.
Let a class of distinguished triangles $X \to Y \to Z \to \Sigma X$ be given that satisfies the axioms TR1, TR2 and TR3 of a triangulated category.
The class satisfies the *octahedral axiom* (TR4) if the following holds.
Let $f \colon X \to Y$ and $g \colon Y \to Z$ be morphisms, and let
$$X \xrightarrow{f} Y \xrightarrow{i} Z' \xrightarrow{i'} \Sigma X, \qquad Y \xrightarrow{g} Z \xrightarrow{j} X' \xrightarrow{j'} \Sigma Y, \qquad X \xrightarrow{g f} Z \xrightarrow{k} Y' \xrightarrow{k'} \Sigma X$$
be distinguished triangles.
Then there are morphisms $a \colon Z' \to Y'$ and $b \colon Y' \to X'$ such that

1. $Z' \xrightarrow{a} Y' \xrightarrow{b} X' \xrightarrow{(\Sigma i) j'} \Sigma Z'$ is a distinguished triangle;
2. $a i = k g$ and $k' a = i'$;
3. $b k = j$ and $j' b = (\Sigma f) k'$.

## Remarks

Here $Z'$, $X'$ and $Y'$ are cones of $f$, $g$ and $g f$.
Example: take $f = \id_X$, so that $Z' = 0$ with the triangle $X \xrightarrow{\id} X \to 0 \to \Sigma X$, and take the second and third triangles equal.
Then $a = 0$ and $b = \id_{X'}$ work: $0 \to X' \xrightarrow{\id} X' \to 0$ is distinguished, being a rotation of $X' \xrightarrow{\id} X' \to 0 \to \Sigma X'$; $a i = 0 = k g$ because $k g$ is a composite of consecutive maps of a distinguished triangle; and $k' a = 0 = i'$, $b k = k = j$, $j' b = j' = k' = (\Sigma f) k'$.
In the homotopy category of chain complexes the axiom holds, with $Y'$ and the maps $a$ and $b$ built from mapping cones.
The axiom is a form of the isomorphism $(Z/X)/(Y/X) \cong Z/Y$ for $X \subseteq Y \subseteq Z$: read $Z'$ as $Y/X$, $Y'$ as $Z/X$ and $X'$ as $Z/Y$.
