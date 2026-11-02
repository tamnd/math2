---
tag: WAS3TN7VKD
kind: definition
name: Kohn Laplacian
msc: [32W10, 32V20]
defines: ZBQ6TVNZZ8
uses: [ZC78JKZX9S, X7GP9BECD8]
sources:
  - url: https://en.wikipedia.org/wiki/Dolbeault_cohomology
---

## Definition

Let $M$ be a [[CR manifold|ZC78JKZX9S]] with CR structure $T^{0,1}M \subseteq \C TM$.
Fix a Hermitian metric on $T^{0,1}M$ and a smooth volume form on $M$.
For each integer $q \ge 0$, let $\mathcal{E}^{0,q}_b(M)$ be the space of smooth sections of $\Lambda^q (T^{0,1}M)^*$, and let
$$\bar\partial_b \colon \mathcal{E}^{0,q}_b(M) \to \mathcal{E}^{0,q+1}_b(M)$$
be the [[tangential Cauchy–Riemann operator|X7GP9BECD8]].
The metric and the volume form give an $L^2$ inner product on compactly supported forms in $\mathcal{E}^{0,q}_b(M)$.
Let $\vartheta_b$ be the formal adjoint of $\bar\partial_b$ for these inner products, so that $\ip{\bar\partial_b u}{v} = \ip{u}{\vartheta_b v}$ for compactly supported $u$ and $v$.
The *Kohn Laplacian* on $(0,q)$-forms is
$$\square_b = \bar\partial_b \vartheta_b + \vartheta_b \bar\partial_b \colon \mathcal{E}^{0,q}_b(M) \to \mathcal{E}^{0,q}_b(M).$$

## Remarks

The adjoint $\vartheta_b$ is often written $\bar\partial_b^*$, and $\square_b$ is also called the Kohn–Rossi Laplacian or the boundary Laplacian.
On functions ($q = 0$) the first term is absent, and $\square_b u = \vartheta_b \bar\partial_b u$.
Example: on the Heisenberg group $\mathbb{H} = \C \times \R$ with coordinates $(z, t)$, take $T^{0,1}\mathbb{H}$ spanned by $\bar Z = \partial/\partial \bar z - i z\, \partial/\partial t$, declare $\bar Z$ to have length $1$, and use Lebesgue measure.
The vector field $\bar Z$ has divergence $0$, so integration by parts shows that the formal adjoint of $\bar Z$ is $-Z$, where $Z = \partial/\partial z + i \bar z\, \partial/\partial t$ is its complex conjugate.
Hence $\square_b u = -Z \bar Z u$ for functions $u$.
Non-example: the operator $-\bar Z Z$ is not the Kohn Laplacian on functions of $\mathbb{H}$.
It differs from $-Z \bar Z$ by the commutator $[Z, \bar Z] = -2i\, \partial/\partial t$, which is not zero.
The Kohn Laplacian is not elliptic, because its principal symbol vanishes on the nonzero real covectors that annihilate $T^{1,0}M \oplus T^{0,1}M$.

## Explanations

### L1 human

The Kohn Laplacian is built from the derivatives along the complex directions tangent to a real hypersurface.
Like the ordinary Laplacian, it is a sum of a first order operator followed by its adjoint, done in both orders.
It is the operator whose solutions describe the boundary values of holomorphic functions and forms.
