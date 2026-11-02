---
tag: HX2DMKTT3Y
kind: definition
name: Stability condition
msc: [18G80, 14F08]
defines: F0G92Q55DM
uses: [T2V7GJJ2EN, ADKK56VZHW, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Bridgeland_stability_condition
---

## Definition

Let $\mathcal{D}$ be an essentially small [[triangulated category|T2V7GJJ2EN]] with shift functor $[1]$, and let $K(\mathcal{D})$ be its Grothendieck group.
A *stability condition* on $\mathcal{D}$ is a pair $(Z, \mathcal{P})$ with the following data.
The central charge $Z \colon K(\mathcal{D}) \to \C$ is a [[group homomorphism|0HV9Y7WG5R]].
The slicing $\mathcal{P}$ assigns to each $\phi \in \R$ a full additive subcategory $\mathcal{P}(\phi)$ of $\mathcal{D}$.
These data must satisfy:

1. If $E$ is a nonzero object of $\mathcal{P}(\phi)$, then $Z(E) = m(E) e^{i \pi \phi}$ for some real number $m(E) > 0$.
2. $\mathcal{P}(\phi + 1) = \mathcal{P}(\phi)[1]$ for all $\phi \in \R$.
3. If $\phi_1 > \phi_2$ and $A_j$ is an object of $\mathcal{P}(\phi_j)$ for $j = 1, 2$, then $\Hom(A_1, A_2) = 0$.
4. Each nonzero object $E$ of $\mathcal{D}$ has a Harder–Narasimhan filtration. This means real numbers $\phi_1 > \phi_2 > \cdots > \phi_n$ and morphisms $0 = E_0 \to E_1 \to \cdots \to E_n = E$. Each step sits in a [[distinguished triangle|ADKK56VZHW]] $E_{j-1} \to E_j \to A_j \to E_{j-1}[1]$ with $A_j$ a nonzero object of $\mathcal{P}(\phi_j)$.

Here $Z(E)$ means $Z$ applied to the class of $E$ in $K(\mathcal{D})$.
The nonzero objects of $\mathcal{P}(\phi)$ are the semistable objects of phase $\phi$.

## Remarks

Example: let $k$ be a field and let $\mathcal{D}$ be the bounded derived category of finite-dimensional vector spaces over $k$.
Each object is a finite direct sum of shifts $k[n]$, and $\Hom(k[a], k[b]) = 0$ for $a \ne b$.
Put $Z(E) = -\chi(E)$, where $\chi(E) = \sum_i (-1)^i \dim H^i(E)$.
Let $\mathcal{P}(\phi)$ be the finite direct sums of copies of $k[\phi - 1]$ when $\phi$ is an integer, and $0$ otherwise.
Then $Z(k[n]) = (-1)^{n+1} = e^{i \pi (n+1)}$, so clause 1 holds, and clause 2 holds since $k[n][1] = k[n+1]$.
Clause 3 holds because $\Hom(k[a], k[b]) = 0$ for $a > b$.
Clause 4 holds by splitting an object into its shifted summands, taken in order of decreasing phase.

Non-example: keep the same $Z$ but move every slice down by one, so that $k$ lies in $\mathcal{P}(0)$.
Then $Z(k) = -1$ while $e^{i \pi \cdot 0} = 1$, so clause 1 fails.

Many authors add a finiteness hypothesis, such as local finiteness or the support property, so that the set of stability conditions becomes a complex manifold.
Equivalently, a stability condition is a bounded t-structure with heart $\mathcal{A}$ together with a stability function on $\mathcal{A}$ that has the Harder–Narasimhan property.
