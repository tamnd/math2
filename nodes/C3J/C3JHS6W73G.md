---
tag: C3JHS6W73G
kind: definition
name: Natural transformation
msc: [18A23]
defines: KYCPCC57FT
uses: [28NQ0KRHD3, 859F0TFVA3, WV898P4X16, 000AYPA9AJ, 07JBSZE0V4, 0ZJM9D7NPS]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_transformation
---

## Definition

Let $F, G \colon \mathcal{C} \to \mathcal{D}$ be [[functors|28NQ0KRHD3]].
A *natural transformation* $\alpha \colon F \Rightarrow G$ is a family of [[morphisms|859F0TFVA3]] $\alpha_A \colon F(A) \to G(A)$ of $\mathcal{D}$, one for each object $A$ of $\mathcal{C}$.
The family must satisfy
$$G(f) \circ \alpha_A = \alpha_B \circ F(f)$$
for every morphism $f \colon A \to B$ of $\mathcal{C}$.
The morphism $\alpha_A$ is the *component* of $\alpha$ at $A$.
If every component is an isomorphism, $\alpha$ is a *natural isomorphism*, and $F$ and $G$ are *naturally isomorphic*, written $F \cong G$.

## Remarks

The condition says that the naturality square with sides $F(f)$, $\alpha_B$, $\alpha_A$ and $G(f)$ is a [[commutative diagram|WV898P4X16]].
Example: on [[vector spaces|000AYPA9AJ]] over a field $K$, let $\mathrm{ev}_V \colon V \to V^{**}$ send $v$ to the map $\varphi \mapsto \varphi(v)$, where $V^*$ is the [[dual space|07JBSZE0V4]].
For a linear map $f \colon V \to W$ and $\psi \in W^*$, both $f^{**}(\mathrm{ev}_V(v))$ and $\mathrm{ev}_W(f(v))$ send $\psi$ to $\psi(f(v))$.
So $\mathrm{ev}$ is a natural transformation from the identity functor to the double dual functor.
On finite-dimensional spaces it is a natural isomorphism, by the [[canonical isomorphism with the double dual|0ZJM9D7NPS]].
Non-example: on the category of nonempty sets, choose for each set $X$ a point $x_X \in X$ and let $\alpha_X \colon X \to X$ be the constant map with value $x_X$.
This family is not a natural transformation from the identity functor to itself.
For a two-element set $Y$ and the constant map $f \colon X \to Y$ whose value is not $x_Y$, the condition would require $f(x_X) = x_Y$.
