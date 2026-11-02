---
tag: G5FAPAB2G2
kind: definition
name: Hodge Laplacian
msc: [58A14, 58J05, 58A10]
defines: PWG3GKZG80
uses: [7CBT4SM83Y, 0E3G0GRPZ6, 0ZHSTAG8ZY, 1Y4WX4XQWJ, F4NWZNTRMD, A127WFVYKW, BE9GTWMN0B]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_operators_in_differential_geometry
---

## Definition

Let $(M, g)$ be an oriented [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$, and let $\Omega^k(M)$ be the space of smooth [[differential $k$-forms|0E3G0GRPZ6]].
Let $d \colon \Omega^k(M) \to \Omega^{k+1}(M)$ be the [[exterior derivative|0ZHSTAG8ZY]], and let $\star$ be the [[Hodge star|1Y4WX4XQWJ]].
The *codifferential* $\delta \colon \Omega^k(M) \to \Omega^{k-1}(M)$ is
$$\delta = (-1)^{n(k+1)+1} \star d \star.$$
The *Hodge Laplacian* on $k$-forms is
$$\Delta = d \delta + \delta d \colon \Omega^k(M) \to \Omega^k(M).$$

## Remarks

The sign in $\delta$ makes it the formal adjoint of $d$: $\int_M \ip{d\alpha}{\beta} \, \mathrm{vol} = \int_M \ip{\alpha}{\delta\beta} \, \mathrm{vol}$ when one of the forms has compact support.
Changing the orientation changes $\star$ by a sign twice, so $\delta$ and $\Delta$ are defined on any Riemannian manifold.
Some authors write $\Delta_d$ or $\Delta_H$; it is also called the Laplace–de Rham operator.
It is a nonnegative, formally self-adjoint, elliptic operator of order $2$, and $\Delta = (d + \delta)^2$.

Example: on $\R^n$ with the flat metric, let $f$ be a function.
Then $df = \sum_j \partial_j f \, dx_j$ and $\delta(\sum_j a_j \, dx_j) = -\sum_j \partial_j a_j$, so $\Delta f = \delta df = -\sum_j \partial_j^2 f$.
So on functions $\Delta = -\operatorname{div} \operatorname{grad}$, the [[Laplace–Beltrami operator|F4NWZNTRMD]] with the sign that makes it nonnegative.
On $k$-forms of $\R^n$, $\Delta(\sum_I f_I \, dx_I) = \sum_I (-\sum_j \partial_j^2 f_I) \, dx_I$.

Non-example: the operator $d \delta$ alone is not the Hodge Laplacian; on functions it is zero, since $\delta f = 0$ for a $0$-form.

On a closed manifold, the [[Hodge theorem|A127WFVYKW]] identifies $\ker \Delta$ on $k$-forms with the de Rham cohomology $H^k(M; \R)$.
The [[Weitzenböck identity|BE9GTWMN0B]] writes $\Delta$ as a rough Laplacian plus a curvature term.

## Explanations

### L1 human

The Hodge Laplacian is the combination $d\delta + \delta d$ of the exterior derivative and its adjoint, acting on differential forms.
