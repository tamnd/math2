---
tag: FTAQH7M58N
kind: definition
name: Left-invariant measure
msc: [28C10, 43A05]
defines: JAWD14N5ES
uses: [92700QAB5Y, 0WQXY32Q8D, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Definition

Let $G$ be a [[topological group|92700QAB5Y]] and let $\mathcal{B}$ be the [[Borel sigma-algebra|0WQXY32Q8D]] of $G$.
For $g \in G$ and $A \subseteq G$, let $gA = \set{ga : a \in A}$.
A [[measure|PR11BZQQPG]] $\mu$ on $\mathcal{B}$ is *left-invariant* if
$$\mu(gA) = \mu(A) \quad \text{for every } g \in G \text{ and every } A \in \mathcal{B}.$$
A measure is *right-invariant* if $\mu(Ag) = \mu(A)$ for every $g \in G$ and every $A \in \mathcal{B}$, where $Ag = \set{ag : a \in A}$.

## Remarks

The set $gA$ is again a Borel set, since left translation by $g$ is a homeomorphism of $G$.
Equivalently, the pushforward of $\mu$ under each left translation $x \mapsto gx$ equals $\mu$.
In integral form, $\int_G f(gx) \, d\mu(x) = \int_G f(x) \, d\mu(x)$ for every $g \in G$ and every nonnegative Borel function $f$.

Example: Lebesgue measure $\lambda$ on $(\R, +)$.
Here $gA = g + A$, and $\lambda(g + A) = \lambda(A)$ for every Borel set $A$, since length does not change under shifts.

Non-example: the Dirac measure $\delta_0$ on $(\R, +)$.
One has $\delta_0(\set{0}) = 1$ but $\delta_0(1 + \set{0}) = \delta_0(\set{1}) = 0$.

The zero measure and the counting measure are left-invariant on every group, but they are not Haar measures on $\R$.
The first is zero, and the second is infinite on infinite compact sets.
A [[Haar measure|VY0HXD3GC4]] is a left-invariant measure that is a nonzero Radon measure.
