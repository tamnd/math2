---
tag: 4KCECXYW81
kind: statement
role: theorem
name: Hom-set characterization of adjunctions
msc: [18A40]
uses: [TZHF6ZM92S, MYGWT305AB, KYCPCC57FT]
about: [TZHF6ZM92S, MYGWT305AB]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_functors
---

## Statement

Let $F \colon \mathcal{C} \to \mathcal{D}$ and $G \colon \mathcal{D} \to \mathcal{C}$ be functors.

1. Let $\varphi$ be an [[adjunction|TZHF6ZM92S]] between $F$ and $G$, with [[unit and counit|MYGWT305AB]] $\eta$ and $\varepsilon$.
Then $\eta$ and $\varepsilon$ are [[natural transformations|KYCPCC57FT]] and satisfy $\varepsilon_{F c} \circ F(\eta_c) = \id_{F c}$ and $G(\varepsilon_d) \circ \eta_{G d} = \id_{G d}$.
2. Conversely, let $\eta \colon \mathrm{Id}_{\mathcal{C}} \Rightarrow G F$ and $\varepsilon \colon F G \Rightarrow \mathrm{Id}_{\mathcal{D}}$ be natural transformations that satisfy these two triangle identities.
Then $\varphi(g) = G(g) \circ \eta_c$, for $g \colon F c \to d$, is an adjunction.
Its inverse is $f \mapsto \varepsilon_d \circ F(f)$ for $f \colon c \to G d$.
3. These two constructions are inverse to each other.

## Remarks

For part 1, naturality of $\varphi$ gives $\varphi(g) = G(g) \circ \eta_c$ and $\varphi^{-1}(f) = \varepsilon_d \circ F(f)$.
Applying these to identities gives the triangle identities.
For part 2, the triangle identities are exactly what is needed for the two maps to be inverse to each other, and naturality is a direct check.

Example: for sets, $F = - \times Y$ and $G = (-)^Y$, the unit sends $x \in X$ to the map $y \mapsto (x, y)$.
The counit is evaluation $Z^Y \times Y \to Z$.
The triangle identities then say that currying and evaluating undo each other.

## Explanations

### L1 human

There are two ways to describe an adjunction.
One matches maps $F c \to d$ with maps $c \to G d$.
The other gives two families of maps, the unit and the counit, which satisfy two simple equations.
The theorem says that the two descriptions carry the same information.

### L2 human

The hom-set form is useful for recognizing adjunctions, since it is often a familiar bijection such as currying or the universal property of free objects.
The unit and counit form is better for computation, because it is a finite set of equations between natural transformations.
It also makes sense in any 2-category, so it is the form used to define adjunctions in general.
A third equivalent form says that each $\eta_c$ is an initial object of the comma category $c \downarrow G$.
