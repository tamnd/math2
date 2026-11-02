---
tag: PFT115EGPE
kind: definition
name: Modular function
msc: ["22D05", "28C10", "43A05"]
defines: 63TX60RTRQ
uses: [AHV05ZBCYW, VY0HXD3GC4, KB792QTG4F]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Definition

Let $G$ be a [[locally compact group|AHV05ZBCYW]] and let $\mu$ be a left [[Haar measure|VY0HXD3GC4]] on $G$.
For $g \in G$, the measure $\mu_g(A) = \mu(Ag)$ on Borel sets $A$ is again a left Haar measure.
By the uniqueness part of the [[existence and uniqueness of Haar measure|KB792QTG4F]], there is a unique real number $\Delta(g) > 0$ such that
$$\mu(Ag) = \Delta(g) \, \mu(A) \quad \text{for every Borel set } A \subseteq G.$$
The map $\Delta \colon G \to (0, \infty)$ is the *modular function* of $G$.

## Remarks

The number $\Delta(g)$ does not depend on the choice of $\mu$, since any other left Haar measure is $c\mu$ with $c > 0$.
The map $\Delta$ is a continuous homomorphism into the multiplicative group $(0, \infty)$.
In integral form, $\int_G f(xg^{-1}) \, d\mu(x) = \Delta(g) \int_G f(x) \, d\mu(x)$ for compactly supported continuous $f$.

Example: let $G$ be the group of pairs $(a, b)$ with $a > 0$ and $b \in \R$, with product $(a, b)(c, d) = (ac, ad + b)$, the group of maps $x \mapsto ax + b$.
The measure $d\mu = da \, db / a^2$ is a left Haar measure.
Right multiplication by $(c, d)$ sends $(a, b)$ to $(ac, ad + b)$, a map with Jacobian determinant $c$.
So $\mu(A(c, d)) = \int_A c \, (ac)^{-2} a^2 \, d\mu = c^{-1} \mu(A)$, and $\Delta(c, d) = 1/c$.

For this group the measure $da \, db / a$ is a right Haar measure but not a left one, so the left and right Haar measures differ.

Some authors use the reciprocal convention, defining the modular function by $\mu(Ag) = \Delta(g)^{-1} \mu(A)$ or through right Haar measure, so formulas must be checked against the source.
