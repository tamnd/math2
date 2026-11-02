---
tag: NVFF58NEKV
kind: definition
name: Crossed product
msc: [46L55, 46L05, 47L65]
defines: 8HG8TS46A6
uses: [0WCY42EV9V, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Crossed_product
---

## Definition

Let $A$ be a unital C*-algebra, and let $G$ be a discrete group.
Let $\alpha \colon G \to \Aut(A)$ be a [[group action|0WCY42EV9V]] of $G$ on $A$ by $*$-automorphisms.
Let $C_c(G, A)$ be the space of finitely supported functions $f \colon G \to A$, with the product and involution
$$(f * g)(s) = \sum_{t \in G} f(t) \, \alpha_t\big(g(t^{-1} s)\big), \qquad f^*(s) = \alpha_s\big(f(s^{-1})^*\big).$$
Let $H$ be a [[Hilbert space|HM2HHE3J51]].
A *covariant representation* of $(A, G, \alpha)$ on $H$ is a pair $(\pi, u)$ with two parts.
The first, $\pi$, is a unital $*$-representation of $A$ on $H$; the second, $u$, is a unitary representation of $G$ on $H$.
The pair must satisfy $u_s \pi(a) u_s^* = \pi(\alpha_s(a))$ for all $s \in G$ and $a \in A$.
It gives the $*$-representation $(\pi \rtimes u)(f) = \sum_{s \in G} \pi(f(s)) u_s$ of $C_c(G, A)$.
The *crossed product* $A \rtimes_\alpha G$ is the completion of $C_c(G, A)$ in the norm
$$\norm{f} = \sup \set{\norm{(\pi \rtimes u)(f)} : (\pi, u) \text{ a covariant representation}}.$$

## Remarks

The element $a \delta_s$ that takes the value $a$ at $s$ and $0$ elsewhere is written $a u_s$; then $u_s a u_s^* = \alpha_s(a)$ in $A \rtimes_\alpha G$.
The *reduced crossed product* $A \rtimes_{\alpha, r} G$ uses only the regular covariant representations on $\ell^2(G, H)$; it equals the full one when $G$ is amenable.
For locally compact groups, $C_c(G, A)$ is replaced by continuous compactly supported functions and sums by integrals against Haar measure.

Example: take $A = \C$ and the trivial action.
Then $C_c(G, \C)$ is the group algebra of $G$ with convolution, and the covariant representations are the unitary representations of $G$.
So $\C \rtimes G$ is the full group C*-algebra $C^*(G)$.

Non-example: let $\Z$ act on $A = C(\mathbb{T})$ by an irrational rotation.
If $\alpha$ is replaced by the identity in the formulas for the product and the involution, the result is the crossed product for the trivial action.
That algebra is $C(\mathbb{T}) \otimes C^*(\Z) \cong C(\mathbb{T}^2)$, which is commutative.
The twisted product gives instead the noncommutative irrational rotation algebra.
