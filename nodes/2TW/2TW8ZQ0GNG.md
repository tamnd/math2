---
tag: 2TW8ZQ0GNG
kind: statement
role: theorem
name: Additivity theorem
msc: [18F25, 19D10]
uses: [X7JG1QEB9Q, ZPNXVVZY1J, XZG6MTSWCN]
about: [ZPNXVVZY1J]
sources:
  - url: https://en.wikipedia.org/wiki/Waldhausen_category
---

## Statement

Let $\mathcal{C}$ be a [[Waldhausen category|X7JG1QEB9Q]], and let $\mathcal{E} = S_2 \mathcal{C}$ be the Waldhausen category of cofibration sequences $A \rightarrowtail B \twoheadrightarrow C$ in $\mathcal{C}$.
The category $\mathcal{E}$ carries its standard cofibrations and weak equivalences.
Let $F \colon \mathcal{E} \to \mathcal{C} \times \mathcal{C}$ be the functor $(A \rightarrowtail B \twoheadrightarrow C) \mapsto (A, C)$.
Then $F$ induces a [[homotopy equivalence|XZG6MTSWCN]]
$$\abs{wS_\bullet \mathcal{E}} \xrightarrow{\ \simeq\ } \abs{wS_\bullet \mathcal{C}} \times \abs{wS_\bullet \mathcal{C}},$$
where $wS_\bullet$ is the [[S-construction|ZPNXVVZY1J]].

## Remarks

A map back is induced by $(A, C) \mapsto (A \rightarrowtail A \vee C \twoheadrightarrow C)$, where $A \vee C = A \cup_0 C$ is the coproduct.
One composite is the identity of $\mathcal{C} \times \mathcal{C}$.
The work is to show that the other composite is homotopic to the identity on the realization, which Waldhausen did by a simplicial argument.

The main consequence: let $F' \rightarrowtail F \twoheadrightarrow F''$ be a cofibration sequence of exact functors $\mathcal{C} \to \mathcal{D}$ between Waldhausen categories.
Then the maps that $F$ and $F' \vee F''$ induce on K-theory spaces are homotopic, so $F_* = F'_* + F''_*$ on $K_n$ for all $n \ge 0$.
In degree $0$ this is the relation $[F(X)] = [F'(X)] + [F''(X)]$ in $K_0(\mathcal{D})$; the theorem says the same additivity holds in all degrees.
It is used, for instance, to compute the K-theory of filtered objects and of projective bundles.

## Explanations

### L1 human

In $K_0$, an object built from a sub $A$ and a quotient $C$ counts as $A + C$.
The additivity theorem says that this rule holds for the whole K-theory space, not only for $K_0$.
Knowing a cofibration sequence is, as far as K-theory sees, the same as knowing its two ends.

### L2 human

Additivity is the basic tool of Waldhausen K-theory.
Waldhausen derives from it his fibration theorem, and the fact that the iterated S-construction gives an $\Omega$-spectrum.
For exact categories with the isomorphisms as weak equivalences, it contains Quillen's additivity result for the Q-construction.
