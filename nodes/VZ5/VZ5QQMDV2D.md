---
tag: VZ5QQMDV2D
kind: definition
name: Pseudoanalytic function
msc: [30G20]
defines: Y1MH7WPRDZ
uses: [0EWMDD6C14, 0WZTM0EFR6, 0NAHXR1FRH, WMXDVF36ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudoanalytic_function
---

## Definition

Let $\Omega \subset \C$ be a [[domain|0EWMDD6C14]].
A *generating pair* on $\Omega$ is a pair $(F, G)$ of [[Hölder continuous|0WZTM0EFR6]] functions $\Omega \to \C$ with $\operatorname{Im}\left( \overline{F(z)}\, G(z) \right) > 0$ for all $z \in \Omega$.
Then every function $w \colon \Omega \to \C$ can be written uniquely as $w = \varphi F + \psi G$ with $\varphi, \psi \colon \Omega \to \R$.
The function $w$ is *$(F, G)$-pseudoanalytic* if $\varphi$ and $\psi$ have continuous first partial derivatives and
$$\varphi_{\bar z}\, F + \psi_{\bar z}\, G = 0 \quad \text{on } \Omega,$$
where $\partial_{\bar z} = \frac{1}{2}\left( \partial_x + i \partial_y \right)$ is the [[Wirtinger derivative|WMXDVF36ZT]].

## Remarks

The condition $\operatorname{Im}(\bar F G) > 0$ says that $F(z)$ and $G(z)$ are linearly independent over $\R$, which gives the uniqueness of $\varphi$ and $\psi$.

Example: for $(F, G) = (1, i)$, the condition reads $(\varphi + i \psi)_{\bar z} = 0$.
So the $(1, i)$-pseudoanalytic functions are exactly the [[holomorphic functions|0NAHXR1FRH]] with continuous derivative.

Non-example: $w(z) = \bar z$ is not $(1, i)$-pseudoanalytic.
Here $\varphi = x$ and $\psi = -y$, so $\varphi_{\bar z} + i \psi_{\bar z} = \frac{1}{2} + i \cdot \left( -\frac{i}{2} \right) = 1 \ne 0$.

If $F$ and $G$ are continuously differentiable, then $w_{\bar z} = \varphi F_{\bar z} + \psi G_{\bar z}$ for a pseudoanalytic $w$.
Since $\varphi$ and $\psi$ are real-linear in $w$, this is an equation $w_{\bar z} = a w + b \bar w$ with coefficients $a, b$ determined by $F$ and $G$.
Some authors ask for less regularity of $\varphi$ and $\psi$ and use a weak form of the condition.
