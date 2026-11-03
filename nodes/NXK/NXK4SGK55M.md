---
tag: NXK4SGK55M
kind: definition
name: Quillen Q-construction
msc: [19D06, 18F25]
defines: J9XP7CS943
uses: [TFADSC9YPZ, A2DE66937D, RV0MKJ3CQ6, TG6WHHR7CF, P976WYEFMB, 5FDMY7PDYY]
sources:
  - url: https://en.wikipedia.org/wiki/Q-construction
---

## Definition

Let $\mathcal{C}$ be a small [[exact category|TFADSC9YPZ]].
Write $A \rightarrowtail B$ for an admissible monomorphism and $B \twoheadrightarrow C$ for an admissible epimorphism of $\mathcal{C}$.
The *Q-construction* $Q\mathcal{C}$ is the [[category|A2DE66937D]] defined as follows.

1. The objects of $Q\mathcal{C}$ are the objects of $\mathcal{C}$.
2. A morphism $M \to N$ in $Q\mathcal{C}$ is an isomorphism class of diagrams $M \twoheadleftarrow N' \rightarrowtail N$ in $\mathcal{C}$. Two diagrams $M \twoheadleftarrow N' \rightarrowtail N$ and $M \twoheadleftarrow N'' \rightarrowtail N$ are isomorphic when an isomorphism $N' \to N''$ makes both triangles commute.
3. The composite of $M \twoheadleftarrow N' \rightarrowtail N$ and $N \twoheadleftarrow P' \rightarrowtail P$ is $M \twoheadleftarrow N' \times_N P' \rightarrowtail P$, where $N' \times_N P'$ is the pullback of $N' \rightarrowtail N$ along $P' \twoheadrightarrow N$.

Let $BQ\mathcal{C}$ be the [[geometric realization|TG6WHHR7CF]] of the [[nerve|RV0MKJ3CQ6]] of $Q\mathcal{C}$, and let $0$ be a zero object of $\mathcal{C}$.
For $n \ge 0$, the *$n$-th K-group* of $\mathcal{C}$ is the [[homotopy group|P976WYEFMB]]
$$K_n(\mathcal{C}) = \pi_{n+1}(BQ\mathcal{C}, 0).$$

## Remarks

The pullback in clause 3 exists because admissible monomorphisms are stable under pullback along admissible epimorphisms, and the two composites $N' \times_N P' \rightarrowtail P' \rightarrowtail P$ and $N' \times_N P' \twoheadrightarrow N' \twoheadrightarrow M$ are again admissible.
Each admissible monomorphism $i \colon M \rightarrowtail N$ gives the morphism $M \twoheadleftarrow M \rightarrowtail N$ (identity on the left), and each admissible epimorphism $p \colon N \twoheadrightarrow M$ gives the morphism $M \twoheadleftarrow N \rightarrowtail N$ (identity on the right).
Quillen proved that $\pi_1(BQ\mathcal{C}, 0)$ is the [[Grothendieck group|5FDMY7PDYY]] $K_0(\mathcal{C})$, so the definition is right in degree $0$.

Example: for a ring $R$, the category $\mathcal{P}(R)$ of finitely generated projective left $R$-modules, with the split short exact sequences, is exact, and $K_n(\mathcal{P}(R))$ is the Quillen K-group $K_n(R)$.

Non-example: in $\mathcal{P}(\Z)$, the diagram $0 \twoheadleftarrow \Z \xrightarrow{\,2\,} \Z$ is not a morphism of $Q\mathcal{P}(\Z)$.
Multiplication by $2$ is a monomorphism, but it is not admissible, because its cokernel $\Z/2$ is not a projective $\Z$-module.
