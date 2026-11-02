---
tag: S5VTE2R86M
kind: definition
name: Haar measure on a Lie group
msc: ["22E30", 28C10]
defines: JCSR7HJ7PC
uses: [7JBRGCVJRB, VY0HXD3GC4, 0E3G0GRPZ6, E7A5DHFT01, P6ZP0TE07M]
sources:
  - url: https://en.wikipedia.org/wiki/Haar_measure
---

## Definition

Let $G$ be a real [[Lie group|7JBRGCVJRB]] of dimension $n$, with identity $e$, and for $g \in G$ let $L_g(h) = gh$.
Fix a nonzero alternating $n$-linear form $\omega_e$ on the [[tangent space|E7A5DHFT01]] $T_eG$.
Let $\omega$ be the left-invariant $n$-form on $G$ given by $\omega_g = (L_{g^{-1}})^* \omega_e$, a nowhere-vanishing [[differential form|0E3G0GRPZ6]] of top degree.
The *left Haar measure* of $\omega$ is the Borel measure $\mu_\omega$ on $G$ such that
$$\int_G f \, d\mu_\omega = \int_G f \, \abs{\omega}$$
for every continuous function $f$ with compact support.
Here $\abs{\omega}$ is the density associated with $\omega$.

## Remarks

Since $L_h^* \omega = \omega$ for all $h \in G$, the measure $\mu_\omega$ is invariant under left translations, so it is a left [[Haar measure|VY0HXD3GC4]] of $G$; changing $\omega_e$ multiplies it by a positive constant.

Example: on $G = GL_n(\R)$, open in $M_n(\R) = \R^{n^2}$, the measure $\abs{\det X}^{-n} \, dX$, with $dX$ Lebesgue measure, is a left Haar measure.
Left multiplication $X \mapsto AX$ is linear with determinant $(\det A)^n$, which cancels the change of $\abs{\det X}^{-n}$.

Example and non-example: on $G = \set{(a, b) : a > 0, b \in \R}$ with $(a, b)(a', b') = (aa', ab' + b)$, the measure $a^{-2}\, da\, db$ is a left Haar measure.
The measure $a^{-1}\, da\, db$ is not left-invariant: left translation by $(c, 0)$ maps $(a, b)$ to $(ca, cb)$, with Jacobian $c^2$, and multiplies $a^{-1}\, da\, db$ by $c$.
It is a right Haar measure instead.

A right Haar measure arises in the same way from right-invariant forms.
The group is unimodular, meaning that left and right Haar measures coincide, if and only if $\abs{\det \operatorname{Ad}(g)} = 1$ for all $g \in G$, where $\operatorname{Ad}$ is the [[adjoint representation|P6ZP0TE07M]].
