---
tag: X0X1Q5JZFK
kind: definition
name: Maurer–Cartan form
msc: ["22E60", 53C05]
defines: P1JVA39H5E
uses: [7JBRGCVJRB, 02Z5B2HA3F, 6P9PXQDSEN, E7A5DHFT01, SNA3DVPK0C]
sources:
  - url: https://en.wikipedia.org/wiki/Maurer%E2%80%93Cartan_form
---

## Definition

Let $G$ be a [[Lie group|7JBRGCVJRB]] with identity $e$ and Lie algebra $\mathfrak{g} = T_eG$, the [[tangent space|E7A5DHFT01]] at $e$.
For $g \in G$, let $L_g \colon G \to G$, $L_g(h) = gh$, be left translation.
The *(left) Maurer–Cartan form* is the $\mathfrak{g}$-valued [[one-form|02Z5B2HA3F]] $\omega$ on $G$ with
$$\omega_g = (dL_{g^{-1}})_g \colon T_gG \to \mathfrak{g},$$
for each $g \in G$, where $(dL_{g^{-1}})_g$ is the [[differential|6P9PXQDSEN]] of $L_{g^{-1}}$ at $g$.

## Remarks

Example: for $G = GL_n(\R)$, left translation by $g^{-1}$ is the linear map $V \mapsto g^{-1}V$ of $M_n(\R)$.
So $\omega_g(V) = g^{-1} V$, written $\omega = g^{-1}\, dg$.
Then $d\omega = -g^{-1}\,dg\, g^{-1} \wedge dg = -\omega \wedge \omega$, which is the Maurer–Cartan equation for matrix groups.

Non-example: the form $\omega'_g = (dR_{g^{-1}})_g$, with $R_g(h) = hg$, also takes values in $\mathfrak{g}$, but it is not the left Maurer–Cartan form.
For $GL_n(\R)$ it is $dg\, g^{-1}$, and at $g = \begin{pmatrix} 1 & 0 \\ 0 & 2 \end{pmatrix}$, $V = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ one gets $V g^{-1} = \tfrac12 V \ne V = g^{-1}V$.
It is the right Maurer–Cartan form.

The form $\omega$ is left-invariant: $L_h^*\omega = \omega$ for all $h \in G$.
For each [[left-invariant vector field|SNA3DVPK0C]] $X$, the function $\omega(X)$ is constant, equal to $X_e$.
In general it satisfies $d\omega + \tfrac12[\omega \wedge \omega] = 0$.
