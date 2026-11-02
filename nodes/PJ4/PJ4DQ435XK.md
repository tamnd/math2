---
tag: PJ4DQ435XK
kind: statement
role: theorem
name: Parametric transversality theorem
msc: [57R35, 58A05, 57R45]
uses: [F45VQ47GPV, VKFW27WXEZ, A2PDZ8GA9C, VQQM4Y550T, Z7R8J71SJN]
about: [A2PDZ8GA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Transversality_theorem
---

## Statement

Let $X$, $S$ and $Y$ be [[smooth manifolds|F45VQ47GPV]] without boundary, and let $Z \subseteq Y$ be an embedded [[submanifold|VKFW27WXEZ]].
Let $F \colon X \times S \to Y$ be a smooth map that is [[transverse|A2PDZ8GA9C]] to $Z$.
For $s \in S$, let $f_s \colon X \to Y$ be the map $f_s(x) = F(x, s)$.
Then $f_s$ is transverse to $Z$ for all $s$ outside a [[set of measure zero|VQQM4Y550T]] in $S$.

## Remarks

Since $F$ is transverse to $Z$, the preimage $W = F^{-1}(Z)$ is a submanifold of $X \times S$.
Let $\pi \colon W \to S$ be the restriction of the projection.
A short linear algebra argument shows that $f_s$ is transverse to $Z$ exactly when $s$ is a regular value of $\pi$.
By [[Sard's theorem|Z7R8J71SJN]], the critical values of $\pi$ form a set of measure zero, which gives the theorem.

Example: let $X$ be a submanifold of $Y = \R^n$, let $S = \R^n$ and let $F(x, s) = x + s$.
For each $x$, the map $s \mapsto x + s$ is a submersion, so $F$ is transverse to every submanifold $Z$.
The theorem says that for almost every translation vector $s$, the translate $X + s$ meets $Z$ transversally.

The transversality of $F$ is needed: if $F(x, s) = f(x)$ does not depend on $s$ and $f$ is not transverse to $Z$, then no $f_s$ is transverse to $Z$.

## Explanations

### L1 human

Two curves in the plane may touch tangentially, but a tiny shift separates them or makes them cross cleanly.
The theorem makes this precise: if a family of maps moves in enough directions, then almost every member of the family meets a given submanifold cleanly, that is, transversally.

### L2 human

The theorem is the main step in proving that transversality is generic.
In the Thom transversality theorem one builds, locally, a family of perturbations of a given map by adding polynomials, checks that the family is transverse, and applies the parametric theorem.
It also gives the transversality homotopy theorem: every smooth map into a manifold can be perturbed by an arbitrarily small homotopy to a map transverse to a given submanifold.
In infinite dimension the same argument works with the Sard–Smale theorem in place of Sard's theorem.
This is how moduli spaces in gauge theory and symplectic topology are made smooth for generic data.

