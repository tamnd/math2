---
tag: KMAEWSVGRS
kind: statement
role: theorem
name: Riemann–Hilbert correspondence
msc: [32C38, 32S60, 14F10]
uses: [JSGWAN2RJV, GBWQF3HZG0, 5ST7NVJFSM, 5WHXRZDZFK]
about: [5WHXRZDZFK, GBWQF3HZG0]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Hilbert_correspondence
same_as:
  wikidata: Q5986522
  wikipedia: Riemann–Hilbert correspondence
---

## Statement

Let $X$ be a [[complex manifold|JSGWAN2RJV]] of dimension $d$ and let $\mathcal{D}_X$ be its sheaf of holomorphic linear [[differential operators|GBWQF3HZG0]].
Let $D^b_{rh}(\mathcal{D}_X)$ be the bounded [[derived category|5ST7NVJFSM]] of left $\mathcal{D}_X$-modules whose cohomology modules are regular holonomic.
Let $D^b_c(X)$ be the bounded derived category of sheaves of $\C$-vector spaces on $X$ with constructible cohomology sheaves.
For $\mathcal{M}$ in $D^b_{rh}(\mathcal{D}_X)$, let $\operatorname{DR}(\mathcal{M}) = \omega_X \otimes^{L}_{\mathcal{D}_X} \mathcal{M}$ be its de Rham complex, where $\omega_X = \Omega^d_X$ is the canonical sheaf, the complex
$$\mathcal{M} \to \Omega^1_X \otimes \mathcal{M} \to \cdots \to \Omega^d_X \otimes \mathcal{M}$$
placed in degrees $-d, \dots, 0$.
Then:

1. $\operatorname{DR}$ is an equivalence of triangulated categories $D^b_{rh}(\mathcal{D}_X) \to D^b_c(X)$;
2. it restricts to an equivalence between the abelian category of regular holonomic $\mathcal{D}_X$-modules and the category of [[perverse sheaves|5WHXRZDZFK]] on $X$.

## Remarks

Masaki Kashiwara and Zoghman Mebkhout proved the theorem independently around 1980.
Holonomic means that the characteristic variety of the module, a subvariety of the cotangent bundle, has dimension $d$.
Regular is a growth condition on solutions near singularities.
It extends the notion of a [[regular singular point|H96HXG6CA0]] of an ordinary differential equation.

The simplest case: a holomorphic vector bundle $E$ with a flat connection $\nabla$ is a regular holonomic $\mathcal{D}_X$-module.
Its de Rham complex is quasi-isomorphic to the local system of flat sections $\ker \nabla$, shifted by $d$.
On this part, the correspondence is the classical equivalence between flat bundles and local systems, that is, representations of the fundamental group when $X$ is connected.

There is also an algebraic version, for a smooth complex algebraic variety $X$ and algebraic regular holonomic modules, where regularity includes a condition at infinity.
There regularity is needed.
On the affine line, the algebraic connections $d$ and $d - dz$ on the trivial bundle are not isomorphic, because an isomorphism would be multiplication by $e^{z}$, which is not a polynomial.
Yet their analytic flat sections, the constants and the functions $c \, e^{z}$, form isomorphic local systems.
The connection $d - dz$ has an irregular singular point at infinity.

## Explanations

### L1 human

Systems of linear differential equations and topological data about loops are two descriptions of the same thing.
Given equations, follow their solutions around loops and record how they change; this is the monodromy.
Following Riemann, Hilbert asked whether every monodromy comes from equations with mild singularities.
The modern theorem says that, for equations with regular singularities, the dictionary between equations and topology is perfect, even in many variables and with complicated singularities.

### L2 human

The theorem gives an answer to a modern form of [[Hilbert's twenty-first problem|7RHW0KA5RY]].
Its classical forerunner, due to Deligne, treats algebraic vector bundles with regular singular connections on smooth varieties, and matches them with local systems.
In the Kashiwara–Mebkhout form, the category of perverse sheaves belongs to topology and the category of D-modules to analysis.
Many results move across.
For example, the intersection cohomology complex corresponds to a minimal extension of a D-module.
It is a basic tool of geometric representation theory, for example in the proof of the Kazhdan–Lusztig conjecture.
