---
tag: G2SA2YNA33
kind: statement
role: theorem
name: Weyl character formula
msc: [17B10, 17B20]
uses: [EY9DN7QAX1, BB098JPWGA, YT1ZJ2S4EE, C5W8BE1DRY, KFVNC2W720, J1EFY61K87]
about: [J1EFY61K87, KFVNC2W720]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl_character_formula
same_as:
  wikidata: Q7990328
  wikipedia: Weyl character formula
---

## Statement

Let $\mathfrak{g}$ be a complex [[semisimple Lie algebra|EY9DN7QAX1]] with [[Cartan subalgebra|BB098JPWGA]] $\mathfrak{h}$, positive roots $\Phi^+$ and [[Weyl group|YT1ZJ2S4EE]] $W$.
Let $\rho = \frac{1}{2} \sum_{\alpha \in \Phi^+} \alpha$, and let $\varepsilon(w) = \det(w) \in \set{1, -1}$ for $w \in W$.
Let $\Z[\mathfrak{h}^*]$ be the group ring of $\mathfrak{h}^*$, with basis elements $e^\mu$ for $\mu \in \mathfrak{h}^*$ and product $e^\mu e^\nu = e^{\mu + \nu}$.
Let $\lambda$ be a dominant integral weight, and let $L(\lambda)$ be the finite-dimensional irreducible module of [[highest weight|C5W8BE1DRY]] $\lambda$.
Its character is $\operatorname{ch} L(\lambda) = \sum_{\mu} \dim L(\lambda)_\mu \, e^\mu$, a sum over the [[weights|KFVNC2W720]] $\mu$ of $L(\lambda)$.
Then
$$\Big( \sum_{w \in W} \varepsilon(w) e^{w\rho} \Big) \operatorname{ch} L(\lambda) = \sum_{w \in W} \varepsilon(w) e^{w(\lambda + \rho)}.$$

## Remarks

The Weyl denominator formula says $\sum_{w \in W} \varepsilon(w) e^{w\rho} = \prod_{\alpha \in \Phi^+} (e^{\alpha/2} - e^{-\alpha/2})$, the case $\lambda = 0$.
One algebraic proof writes $\operatorname{ch} L(\lambda)$ as an alternating sum of characters of [[Verma modules|809XR5G0DG]] $M(w(\lambda + \rho) - \rho)$.
The [[Harish-Chandra isomorphism|YNBQS0X9ZB]] shows that only these Verma modules can occur, because they share the central character of $L(\lambda)$.
Each Verma character equals $e^{\mu} \prod_{\alpha \in \Phi^+} (1 - e^{-\alpha})^{-1}$, which gives the formula.
Example: for $\mathfrak{sl}_2(\C)$, write $e^k$ for the weight with $\lambda(h) = k$; then $\rho$ is $1$ and $W = \set{\pm 1}$.
The formula reads $(e^{1} - e^{-1}) \operatorname{ch} L(n) = e^{n+1} - e^{-n-1}$, so $\operatorname{ch} L(n) = e^n + e^{n-2} + \dots + e^{-n}$.
For compact Lie groups the same formula, evaluated on a maximal torus, is the [[Weyl character formula for compact groups|230F5FXPMQ]].

## Explanations

### L1 human

The character of a representation lists its weights with their multiplicities.
Weyl's formula gives this list in closed form, as a quotient of two alternating sums over the Weyl group.
Only the highest weight of the representation and the root data of the Lie algebra enter.

### L2 human

The formula has many consequences: the [[Weyl dimension formula|6VBN872BK1]], Kostant's multiplicity formula, and the decomposition of tensor products.
The [[Freudenthal multiplicity formula|4NGV71RMYP]] computes the same multiplicities by a recursion that is easier to run by hand.
The [[Bernstein–Gelfand–Gelfand resolution|41KGWXZ0VM]] lifts the alternating sum to an exact sequence of Verma modules.
For affine Lie algebras the analogue is the [[Kac–Weyl character formula|RJKHTWHME1]].
