---
tag: 9TTJRYP841
kind: definition
name: Positive line bundle
msc: [32L05, 32Q15, 14C20]
defines: J45KWFHENP
uses: [QAC7BYK9KX, Q6X6W2N29G, 7RC9CN2Q49, JSGWAN2RJV, 0KX66CZMBB]
sources:
  - url: https://en.wikipedia.org/wiki/Ample_line_bundle
---

## Definition

Let $X$ be a [[complex manifold|JSGWAN2RJV]] and let $L \to X$ be a [[holomorphic line bundle|QAC7BYK9KX]].
For a [[Hermitian metric|Q6X6W2N29G]] $h$ on $L$, let $\Theta_h$ be the curvature of its [[Chern connection|7RC9CN2Q49]], a $(1,1)$-form on $X$.
In local coordinates $z_1, \dots, z_n$ write $i \Theta_h = i \sum_{j,k} a_{jk}\, dz_j \wedge d\bar z_k$; the matrix $(a_{jk})$ is Hermitian.
The line bundle $L$ is *positive* if some Hermitian metric $h$ on $L$ has $(a_{jk}(x))$ [[positive definite|0KX66CZMBB]] at every point $x \in X$.

## Remarks

If $e$ is a local holomorphic frame of $L$ and $\abs{e}_h^2 = e^{-\varphi}$, then $i \Theta_h = i \partial \bar\partial \varphi$.
So $L$ is positive exactly when some metric has local weights $\varphi$ that are strictly plurisubharmonic.
The form $\frac{i}{2\pi} \Theta_h$ represents the first Chern class $c_1(L)$, so positivity implies that $c_1(L)$ contains a Kähler form.

Example: $\mathcal{O}(1)$ on $\mathbb{P}^n$ with the metric dual to the standard metric on $\mathcal{O}(-1)$.
On $\set{z_0 \ne 0}$ with affine coordinates $z$, the dual frame $e^*$ has $\abs{e^*}^2 = (1 + \abs{z}^2)^{-1}$, so $\varphi = \log(1 + \abs{z}^2)$.
Then $i \partial \bar\partial \varphi$ is the Fubini–Study form, which is positive definite at each point.

Non-example: the trivial line bundle on a compact connected complex manifold $X$ of positive dimension.
Any metric is $\abs{1}_h^2 = e^{-\varphi}$ for a global smooth function $\varphi$.
At a maximum point of $\varphi$ the complex Hessian $(\partial^2 \varphi / \partial z_j \partial \bar z_k)$ is negative semidefinite, so it is not positive definite there.
