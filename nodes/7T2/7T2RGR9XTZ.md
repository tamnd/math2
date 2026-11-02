---
tag: 7T2RGR9XTZ
kind: definition
name: Regularity theory
msc: [35B65, 35J15, 35D30]
defines: N383CX7WKS
uses: [SJZX81A783, M4CEZ5K9HP, GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_operator
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set and consider a [[partial differential equation|GC5BDZ6QBC]] $P(u) = f$ in $\Omega$.
Let $X$ be a space of functions on $\Omega$ in which solutions are first sought, such as a [[Sobolev space|M4CEZ5K9HP]] for [[weak solutions|SJZX81A783]].
Let $Y \subseteq X$ be a smaller space of smoother functions.
A *regularity result* for the equation is a statement of this form.
If $u \in X$ solves $P(u) = f$, and $f$ and the coefficients of $P$ have a given smoothness, then $u \in Y$.
The conclusion may hold on all of $\Omega$ or on every compact subset of $\Omega$.
*Regularity theory* is the study of such results and of the estimates of the norm of $u$ in $Y$ that go with them.

## Remarks

Example: let $u \in H^1_{\mathrm{loc}}(\Omega)$ be a weak solution of $-\Delta u = f$ with $f \in L^2_{\mathrm{loc}}(\Omega)$.
Then $u \in H^2_{\mathrm{loc}}(\Omega)$, and more generally $f \in H^k_{\mathrm{loc}}$ gives $u \in H^{k+2}_{\mathrm{loc}}$; this is [[elliptic regularity|2PVQY9PCT4]] with $X = H^1_{\mathrm{loc}}$ and $Y = H^2_{\mathrm{loc}}$.

Non-example: for the transport equation $u_t + u_x = 0$ in $\R^2$, the function $u(x, t) = g(x - t)$ is a weak solution for every $g \in L^2_{\mathrm{loc}}(\R)$.
So smooth data, here $f = 0$, do not force smooth solutions, and no regularity result of this kind holds; singularities travel along characteristics.

Interior regularity concerns compact subsets of $\Omega$; regularity up to the boundary also needs a smooth boundary and smooth boundary data.

## Explanations

### L1 human

Regularity theory asks how smooth a solution must be, once it is known to exist in a weak sense.
Elliptic equations improve smoothness, while hyperbolic equations only carry the roughness of the data along.
