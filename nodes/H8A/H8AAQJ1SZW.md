---
tag: H8AAQJ1SZW
kind: definition
name: Deformation theory
msc: [14D15, 13D10]
defines: SWFR1GD6QT
uses: [5A35TYZD02, 5M6KS8F47R, ZV04WWYE2Y, 1DZMT4S9FB, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/Deformation_(mathematics)
---

## Definition

Let $k$ be a field and let $X$ be a [[scheme|5A35TYZD02]] over $k$.
Let $\mathrm{Art}_k$ be the category of local [[Artinian|ZV04WWYE2Y]] $k$-algebras $A$ with residue field $k$.
For $A \in \mathrm{Art}_k$, a *deformation of $X$ over $A$* is a pair $(\mathcal{X}, \phi)$ where:

1. $\mathcal{X}$ is a scheme with a [[flat|5M6KS8F47R]] morphism $\mathcal{X} \to \operatorname{Spec} A$;
2. $\phi \colon \mathcal{X} \times_{\operatorname{Spec} A} \operatorname{Spec} k \to X$ is an isomorphism of $k$-schemes, where the left side is a [[fiber product|1DZMT4S9FB]].

Two deformations $(\mathcal{X}, \phi)$ and $(\mathcal{X}', \phi')$ are isomorphic if there is an isomorphism $\mathcal{X} \to \mathcal{X}'$ over $A$ compatible with $\phi$ and $\phi'$.
The *deformation functor* of $X$ is $\operatorname{Def}_X \colon \mathrm{Art}_k \to \mathrm{Set}$, sending $A$ to the set of isomorphism classes of deformations of $X$ over $A$.
A *first-order deformation* is a deformation over the dual numbers $k[\varepsilon] = k[\varepsilon]/(\varepsilon^2)$.
Deformation theory is the study of $\operatorname{Def}_X$ and of the analogous functors for other objects, such as sheaves, morphisms and subschemes.

## Remarks

Let $X$ be smooth over $k$ with tangent sheaf $T_X$.
Then $\operatorname{Def}_X(k[\varepsilon]) \cong H^1(X, T_X)$, in [[sheaf cohomology|PQ6Q143ARJ]].
The obstructions to lifting a deformation over $A$ to a small extension of $A$ lie in $H^2(X, T_X)$.
Example: the trivial deformation $X \times_k \operatorname{Spec} A$ with the identity $\phi$ satisfies both clauses, since a base change of $\operatorname{Spec} A \to \operatorname{Spec} k$ is flat.
For $X = \mathbb{P}^1$, $H^1(\mathbb{P}^1, T) = H^1(\mathbb{P}^1, \mathcal{O}(2)) = 0$, so every first-order deformation of $\mathbb{P}^1$ is trivial.
Non-example: let $A = k[\varepsilon]$ and $\mathcal{X} = \operatorname{Spec} k[\varepsilon, x]/(\varepsilon x)$.
Its special fiber is $\operatorname{Spec} k[x] = \mathbb{A}^1_k$, so clause 2 holds.
But $\mathcal{X}$ is not flat over $A$, since $x$ is killed by $\varepsilon$ without being a multiple of $\varepsilon$, so clause 1 fails.
