---
tag: AX46SNQCAA
kind: definition
name: Kuranishi family
msc: [32G05, 32G13]
defines: R0QABVGPRX
uses: [VKQSM3BCE4, EWZ1G10MAY, HXSZA44J5J, E7A5DHFT01, JSGWAN2RJV]
sources:
  - url: https://en.wikipedia.org/wiki/Kuranishi_structure
---

## Definition

Let $X$ be a compact [[complex manifold|JSGWAN2RJV]].
A deformation of $X$ over a pointed [[complex analytic space|HXSZA44J5J]] $(S, s_0)$ consists of two pieces of data.
The first is a proper flat holomorphic map $\varpi \colon \mathcal{X} \to S$ whose fibres are compact complex manifolds.
The second is a biholomorphism $X \cong \varpi^{-1}(s_0)$.
This extends the notion of [[deformation|VKQSM3BCE4]] over manifolds.
A *Kuranishi family* (semi-universal deformation) of $X$ is a deformation $\varpi \colon \mathcal{X} \to (S, s_0)$ of $X$ such that:

1. It is complete: let $\mathcal{Y} \to (T, t_0)$ be any deformation of $X$.
   Then there are a neighbourhood $T'$ of $t_0$ and a holomorphic map $f \colon (T', t_0) \to (S, s_0)$ such that $\mathcal{Y}|_{T'} \cong f^* \mathcal{X}$.
   The isomorphism is required to be compatible with the identifications of the central fibres with $X$.
2. The differential $df_{t_0} \colon T_{t_0} T \to T_{s_0} S$ of any such $f$ is uniquely determined by the deformation $\mathcal{Y}$.

## Remarks

Here $T_{s_0} S$ is the [[Zariski tangent space|E7A5DHFT01]] of $S$ at $s_0$.
Kuranishi's theorem states that every compact complex manifold has a Kuranishi family, unique up to a non-unique isomorphism of germs.
Its [[Kodaira–Spencer map|EWZ1G10MAY]] identifies $T_{s_0} S$ with $H^1(X, \Theta_X)$, and the germ $(S, s_0)$ is the zero set of a holomorphic map from a neighbourhood of $0$ in $H^1(X, \Theta_X)$ to $H^2(X, \Theta_X)$.
If $H^0(X, \Theta_X) = 0$, the map $f$ in clause 1 is itself unique, and the family is universal.

Example: $X = \mathbb{P}^n$ has $H^1(X, \Theta_X) = 0$, so its Kuranishi family lives over a single point: $\mathbb{P}^n$ is rigid.

Non-example: for an elliptic curve $E$, the trivial family $E \times \Delta \to \Delta$ over a disc is a deformation of $E$ but not complete.
Every pullback of it is again trivial, while the family $\C/(\Z + \tau\Z)$ near $\tau_0$ contains fibres not biholomorphic to $E$, so it is not such a pullback.
