---
tag: 7A67N3PVQG
kind: definition
name: Kohn–Rossi cohomology
msc: [32V05, 32W10, 32V20]
defines: VC48WDWPV1
uses: [ZC78JKZX9S, 68FGQEBD6J, 0E3G0GRPZ6]
sources:
  - url: https://en.wikipedia.org/wiki/CR_manifold
---

## Definition

Let $M$ be a smooth [[CR manifold|ZC78JKZX9S]] with CR bundle $T^{1,0}M \subset \C TM$, and let $T^{0,1}M = \overline{T^{1,0}M}$.
For $q \ge 0$, a $(0,q)$-form on $M$ is a smooth section $\varphi$ of the bundle $\Lambda^q (T^{0,1}M)^*$.
Equivalently, $\varphi$ assigns a smooth function to $q$ smooth sections of $T^{0,1}M$, and it is $C^\infty(M)$-linear and alternating.
Write $\mathcal{E}^{0,q}(M)$ for the space of $(0,q)$-forms.
Let $\bar Z_0, \dots, \bar Z_q$ be sections of $T^{0,1}M$.
A hat marks an omitted argument, and $[\cdot, \cdot]$ is the [[Lie bracket of vector fields|68FGQEBD6J]].
The tangential Cauchy–Riemann operator $\bar\partial_b \colon \mathcal{E}^{0,q}(M) \to \mathcal{E}^{0,q+1}(M)$ is given by
$$
\begin{aligned}
(\bar\partial_b \varphi)(\bar Z_0, \dots, \bar Z_q) ={} & \sum_{j=0}^{q} (-1)^j\, \bar Z_j \bigl(\varphi(\bar Z_0, \dots, \widehat{\bar Z_j}, \dots, \bar Z_q)\bigr) \\
& + \sum_{0 \le j < k \le q} (-1)^{j+k}\, \varphi\bigl([\bar Z_j, \bar Z_k], \bar Z_0, \dots, \widehat{\bar Z_j}, \dots, \widehat{\bar Z_k}, \dots, \bar Z_q\bigr)
\end{aligned}
$$
It satisfies $\bar\partial_b \circ \bar\partial_b = 0$.
The *Kohn–Rossi cohomology* groups of $M$ are
$$H^{0,q}_b(M) = \frac{\ker\bigl(\bar\partial_b \colon \mathcal{E}^{0,q}(M) \to \mathcal{E}^{0,q+1}(M)\bigr)}{\operatorname{im}\bigl(\bar\partial_b \colon \mathcal{E}^{0,q-1}(M) \to \mathcal{E}^{0,q}(M)\bigr)}, \qquad q \ge 0,$$
with $\mathcal{E}^{0,-1}(M) = 0$.

## Remarks

The formula makes sense because $T^{0,1}M$ is closed under the Lie bracket, which is the integrability condition in the definition of a CR manifold; this also gives $\bar\partial_b^2 = 0$.
It is the formula for the exterior derivative of a [[differential form|0E3G0GRPZ6]], applied only to vectors in $T^{0,1}M$.
For $q = 0$, $\bar\partial_b u$ is the restriction of $du$ to $T^{0,1}M$, so $H^{0,0}_b(M)$ is the space of smooth CR functions on $M$.
Example: on $M = \C^n$ with $T^{1,0}M$ the usual holomorphic tangent bundle, $\bar\partial_b = \bar\partial$, and $H^{0,q}_b(\C^n)$ is the Dolbeault cohomology $H^{0,q}(\C^n)$, which is $0$ for $q \ge 1$.
Non-example: on the unit sphere $S^3 \subset \C^2$, with $\bar L = z_2 \partial / \partial \bar z_1 - z_1 \partial / \partial \bar z_2$, the function $u = \bar z_1$ satisfies $\bar\partial_b u (\bar L) = \bar L \bar z_1 = z_2 \ne 0$, so it is not a cocycle and gives no element of $H^{0,0}_b(S^3)$.
More generally one defines groups $H^{p,q}_b(M)$ using forms of type $(p,q)$.
For a compact strongly pseudoconvex CR manifold of hypersurface type and real dimension $2n + 1$, Kohn proved that $H^{0,q}_b(M)$ is finite-dimensional for $1 \le q \le n - 1$.
