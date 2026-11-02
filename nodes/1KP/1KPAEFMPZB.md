---
tag: 1KPAEFMPZB
kind: definition
name: Kuranishi structure
msc: [53D45, 58D27, 57R18]
defines: 4WY3A9YGDR
uses: [F45VQ47GPV, P4DZM975BV, WWX7H5W1RP, 0WCY42EV9V, 0QT00PB5G2, 0BR3FY5Q8M]
sources:
  - url: https://en.wikipedia.org/wiki/Kuranishi_structure
---

## Definition

Let $X$ be a compact metrizable space.
A *Kuranishi neighbourhood* of a point $p \in X$ is a tuple $(V_p, E_p, \Gamma_p, s_p, \psi_p)$ where:

1. $V_p$ is a [[smooth manifold|F45VQ47GPV]] and $\Gamma_p$ is a finite group with a smooth [[action|0WCY42EV9V]] on $V_p$.
2. $E_p \to V_p$ is a finite-dimensional real [[vector bundle|P4DZM975BV]] with a $\Gamma_p$-action that lifts the action on $V_p$.
3. $s_p$ is a $\Gamma_p$-equivariant smooth [[section|WWX7H5W1RP]] of $E_p$, the Kuranishi map.
4. $\psi_p \colon s_p^{-1}(0) / \Gamma_p \to X$ is a [[homeomorphism|0QT00PB5G2]] onto an open neighbourhood of $p$, where $s_p^{-1}(0) / \Gamma_p$ is the [[quotient space|0BR3FY5Q8M]].

A *Kuranishi structure* on $X$ is a choice of a Kuranishi neighbourhood for every $p \in X$, together with coordinate changes, such that:

5. For each $q \in \psi_p(s_p^{-1}(0) / \Gamma_p)$ there is a coordinate change from the chart at $q$ to the chart at $p$.
It consists of a $\Gamma_q$-invariant open neighbourhood $V_{pq} \subseteq V_q$ of a lift of $q$ and an injective homomorphism $h_{pq} \colon \Gamma_q \to \Gamma_p$.
It also has an $h_{pq}$-equivariant smooth embedding $\phi_{pq} \colon V_{pq} \to V_p$ and an $h_{pq}$-equivariant bundle embedding $\hat{\phi}_{pq} \colon E_q|_{V_{pq}} \to E_p$ over $\phi_{pq}$.
These satisfy $\hat{\phi}_{pq} \circ s_q = s_p \circ \phi_{pq}$, and $\psi_p \circ \phi_{pq} = \psi_q$ on $s_q^{-1}(0) \cap V_{pq}$.
6. The coordinate changes are compatible.
Let $q$ lie in the image of the chart at $p$, and $r$ in the image of the chart at $q$.
Then on the common domain $\phi_{pq} \circ \phi_{qr}$ agrees with $\phi_{pr}$ up to the action of an element of $\Gamma_p$, and likewise for $\hat{\phi}$ and $h$.
7. The number $\dim V_p - \operatorname{rank} E_p$ is the same for all $p$; it is the *virtual dimension* of $X$.
8. Let $N_{pq}$ be the normal bundle of $\phi_{pq}(V_{pq})$ in $V_p$.
For each coordinate change, the derivative of $s_p$ induces an isomorphism from $N_{pq}$ onto $E_p / \hat{\phi}_{pq}(E_q)$ at the points of $\phi_{pq}(s_q^{-1}(0))$.

## Remarks

Example: let $V$ be a smooth manifold, $E \to V$ a vector bundle and $s$ a section whose zero set $X = s^{-1}(0)$ is compact.
Take for every $p$ the same chart $(V, E, \set{1}, s, \id)$, with identity coordinate changes.
All composites of coordinate changes are identities, the virtual dimension is $\dim V - \operatorname{rank} E$ everywhere, and the normal bundles in clause 8 are zero, as are the quotients $E / E$.
So this is a Kuranishi structure on $X$.
In particular a compact manifold $X$ has the Kuranishi structure with $V = X$ and $E = 0$.

Non-example: let $X$ be a single point.
One Kuranishi neighbourhood is $V_A = \R$, $E_A = \R \times \R$, $\Gamma_A$ trivial and $s_A(x) = x^2$, whose zero set is one point; another is $V_B$ a point with $E_B = 0$.
Both have virtual dimension $0$, so clause 7 holds.
But a coordinate change from $B$ to $A$ fails clause 8.
The normal space of the point $0$ in $\R$ is $\R$, the quotient $E_A / \hat\phi(E_B)$ is $\R$, and the derivative $s_A'(0) = 0$ is not an isomorphism.

Several variants of this definition are in use, due to Fukaya, Oh, Ohta and Ono, to Joyce, and to others.
They differ mainly in clauses 6 and 8 and in how the coordinate changes are organised.

Clause 8 is sometimes called the tangent bundle condition, and it is what makes orientations and virtual fundamental classes well defined.
