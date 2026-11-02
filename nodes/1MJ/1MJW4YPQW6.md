---
tag: 1MJW4YPQW6
kind: definition
name: Serre subcategory
msc: ["18E35", "18E10"]
defines: CSD6W0JV0P
uses: [Y9CZ3MTNF1, V3BFGKBJF7, KJKNJMGKZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Localizing_subcategory
---

## Definition

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]].
A *Serre subcategory* of $\mathcal{A}$ is a nonempty [[full subcategory|V3BFGKBJF7]] $\mathcal{C}$ of $\mathcal{A}$ with the following property.
For every [[short exact sequence|KJKNJMGKZZ]] $0 \to A' \to A \to A'' \to 0$ in $\mathcal{A}$, the object $A$ lies in $\mathcal{C}$ if and only if $A'$ and $A''$ lie in $\mathcal{C}$.

## Remarks

Equivalently, $\mathcal{C}$ is nonempty and closed under subobjects, quotient objects and extensions.
It then contains a zero object and is closed under isomorphisms, and it is itself an abelian category with exact inclusion.
In a Grothendieck category, a Serre subcategory closed under arbitrary direct sums is called a *localizing subcategory*.

Example: the torsion abelian groups form a Serre subcategory of the category of abelian groups.
Subgroups and quotients of torsion groups are torsion.
If $0 \to A' \to A \to A'' \to 0$ is exact with $A'$ and $A''$ torsion and $a \in A$, then $na$ maps to $0$ in $A''$ for some $n \ge 1$, so $na \in A'$ and $mna = 0$ for some $m \ge 1$.

Non-example: the free abelian groups do not form a Serre subcategory.
The sequence $0 \to \Z \xrightarrow{2} \Z \to \Z/2\Z \to 0$ is exact with $\Z$ free, but the quotient $\Z/2\Z$ is not free.
