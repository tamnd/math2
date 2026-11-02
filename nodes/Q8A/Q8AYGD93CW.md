---
tag: Q8AYGD93CW
kind: statement
role: lemma
name: Snake lemma
msc: ["18G35", "18E10"]
uses: [Y9CZ3MTNF1, JB7ZBFBA9C, S417YNEJ6M, H8W38933NC, WV898P4X16, Y2NP1JFR86, RVXDSY04KG, 1WV2THA6NY]
about: [JB7ZBFBA9C]
sources:
  - url: https://en.wikipedia.org/wiki/Snake_lemma
same_as:
  wikidata: Q1064342
  wikipedia: Snake lemma
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]], such as the category of modules over a ring.
Consider a [[commutative diagram|WV898P4X16]]
$$\begin{array}{ccccccc} & A & \xrightarrow{f} & B & \xrightarrow{g} & C & \to 0 \\ & \downarrow{\scriptstyle a} & & \downarrow{\scriptstyle b} & & \downarrow{\scriptstyle c} & \\ 0 \to & A' & \xrightarrow{f'} & B' & \xrightarrow{g'} & C' & \end{array}$$
in $\mathcal{A}$ whose rows are [[exact|JB7ZBFBA9C]].
Then there is a morphism $\partial \colon \ker c \to \operatorname{coker} a$ such that the sequence
$$\ker a \to \ker b \to \ker c \xrightarrow{\partial} \operatorname{coker} a \to \operatorname{coker} b \to \operatorname{coker} c$$
is exact, where the unlabeled morphisms are induced by $f, g, f', g'$ on [[kernels|S417YNEJ6M]] and [[cokernels|H8W38933NC]].
Moreover, if $f$ is a [[monomorphism|Y2NP1JFR86]], then $\ker a \to \ker b$ is a monomorphism, and if $g'$ is an [[epimorphism|RVXDSY04KG]], then $\operatorname{coker} b \to \operatorname{coker} c$ is an epimorphism.

## Remarks

The morphism $\partial$ is called the *connecting morphism*.
For modules, $\partial$ is defined by a chase.
Given $z \in \ker c$, choose $y \in B$ with $g(y) = z$.
Then $g'(b(y)) = c(z) = 0$, so $b(y) = f'(x')$ for a unique $x' \in A'$, and $\partial(z)$ is the class of $x'$ in $\operatorname{coker} a$.
One checks that this class does not depend on the choice of $y$, and then checks exactness at each place by similar chases.
In a general abelian category one uses [[pseudo-elements|1WV2THA6NY]] or an embedding theorem.

Example: map $0 \to \Z \xrightarrow{2} \Z \to \Z/2\Z \to 0$ to itself by multiplication by $2$ in each place, which is $0$ on $\Z/2\Z$.
The kernels are $0, 0, \Z/2\Z$ and the cokernels are $\Z/2\Z, \Z/2\Z, \Z/2\Z$.
Exactness forces $\partial \colon \Z/2\Z \to \Z/2\Z$ to be an isomorphism, the map $\operatorname{coker} a \to \operatorname{coker} b$ to be $0$, and $\operatorname{coker} b \to \operatorname{coker} c$ to be an isomorphism, which one can confirm directly.

## Explanations

### L1 human

The lemma starts from two exact rows joined by three vertical maps.
It produces one long exact sequence that runs through the three kernels and then the three cokernels.
The surprising link is the connecting map from the last kernel to the first cokernel; drawn in the diagram, the whole sequence winds through it like a snake.

### L2 human

The snake lemma is the engine behind most long exact sequences.
Applied to a short exact sequence of chain complexes, it gives the long exact sequence in homology.
It also gives the long exact sequences of derived functors and the nine lemma.
In practice, it is how one computes a kernel or cokernel that is hard to see directly, from ones that are easy to see.
