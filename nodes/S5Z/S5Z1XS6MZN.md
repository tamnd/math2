---
tag: S5Z1XS6MZN
kind: definition
name: Group of Lie type
msc: [20G40, 20D06]
defines: NPEBABQ49M
uses: [0X6AB5P3G1, 0ZXZ82FTX2, 0T3WVTD675]
sources:
  - url: https://en.wikipedia.org/wiki/Group_of_Lie_type
---

## Definition

Let $p$ be a prime and let $k$ be an [[algebraic closure|0X6AB5P3G1]] of the [[finite field|0ZXZ82FTX2]] $\F_p$.
Let $\mathbf{G}$ be a connected reductive linear algebraic group over $k$.
A Steinberg endomorphism of $\mathbf{G}$ is an endomorphism $F$ of the algebraic group $\mathbf{G}$ with the following property.
Some power $F^m$ with $m \ge 1$ is the [[Frobenius endomorphism|0T3WVTD675]] of $\mathbf{G}$ for some structure of $\mathbf{G}$ over a finite subfield of $k$.
A *finite group of Lie type* is a group
$$\mathbf{G}^F = \set{g \in \mathbf{G} : F(g) = g}$$
for such $\mathbf{G}$ and $F$.

## Remarks

The group $\mathbf{G}^F$ is always finite.
Example: take $\mathbf{G} = \mathrm{GL}_n(k)$ and let $F$ raise every matrix entry to the power $q$, where $q$ is a power of $p$.
Then $F$ is the Frobenius endomorphism for the standard structure over $\F_q$, and $\mathbf{G}^F = \mathrm{GL}_n(\F_q)$, since the elements of $k$ fixed by $x \mapsto x^q$ are exactly the elements of $\F_q$.
Non-example: $\mathrm{GL}_n(\R)$ for $n \ge 1$ is not a finite group of Lie type, since it is infinite.
Many authors also call the simple groups obtained from $\mathbf{G}^F$, such as $\mathrm{PSL}_n(\F_q)$, groups of Lie type.
The [[Chevalley groups|YPCH4Q0V34]] over $\F_q$ come from the case where $\mathbf{G}$ is split over $\F_q$ and $F$ is the corresponding Frobenius endomorphism.
The twisted groups, such as the unitary groups, come from the other Steinberg endomorphisms.
For the [[Suzuki groups|36X3GET13B]] and the [[Ree groups|YB62XEQJAC]], the map $F$ is not a Frobenius endomorphism, but $F^2$ is one.

## Explanations

### L1 human

A finite group of Lie type is a matrix group over a finite field, or a twisted variant of one, described as the fixed points of a Frobenius-type map.
