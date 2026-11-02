---
tag: 5S30FAJNGM
kind: definition
name: Levi form
msc: [32T05, 32V05]
defines: 80MTNXWW80
uses: [48P4A1CX85, 0V33BNKZ9S, 02BH3MCBQB]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoconvexity
---

## Definition

Let $U \subseteq \C^n$ be an [[open set|02BH3MCBQB]] and let $\rho \colon U \to \R$ be a function of class $C^2$ (see [[smooth function|0V33BNKZ9S]]).
The *Levi form* of $\rho$ at a point $p \in U$ is the [[Hermitian form|48P4A1CX85]]
$$L_\rho(p; w) = \sum_{j,k=1}^{n} \frac{\partial^2 \rho}{\partial z_j \partial \bar z_k}(p)\, w_j \bar w_k, \qquad w \in \C^n.$$
It is also called the complex Hessian of $\rho$.

Now let $\Omega \subseteq \C^n$ be a domain with $C^2$ boundary.
A *defining function* of $\Omega$ is a $C^2$ function $\rho$ on a neighbourhood $U$ of $\partial\Omega$ with $\Omega \cap U = \set{z \in U : \rho(z) < 0}$ and $d\rho \ne 0$ on $\partial\Omega$.
For $p \in \partial\Omega$, the complex tangent space of $\partial\Omega$ at $p$ is
$$H_p = \set{w \in \C^n : \sum_{j=1}^{n} \frac{\partial \rho}{\partial z_j}(p)\, w_j = 0}.$$
The *Levi form of $\partial\Omega$ at $p$* is the restriction of $L_\rho(p; \cdot)$ to $H_p$.

## Remarks

Example: for the unit ball, $\rho(z) = \abs{z_1}^2 + \cdots + \abs{z_n}^2 - 1$ has $\partial^2 \rho / \partial z_j \partial \bar z_k = \delta_{jk}$, so $L_\rho(p; w) = \abs{w}^2 > 0$ for every $w \ne 0$.
Non-example of positivity: for the bidisc, near a boundary point $p = (1, b)$ with $\abs{b} < 1$, a defining function is $\rho(z) = \abs{z_1}^2 - 1$.
Here $H_p = \set{w : w_1 = 0}$, and $L_\rho(p; (0, w_2)) = 0$, so the Levi form vanishes on $H_p$.
If $\rho$ is replaced by another defining function $h \rho$ with $h > 0$, the Levi form of $\partial\Omega$ at $p$ is multiplied by $h(p)$.
So its signature does not depend on the choice.
The signature is also unchanged under holomorphic changes of coordinates.
