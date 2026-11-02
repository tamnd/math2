---
tag: DKV5J6N6T6
kind: definition
name: p-Laplacian
msc: [35J92, 35J70]
defines: XJMYGY0ZZF
uses: [0ABK9V9Y64, 0MWV6ZTK6S, 0E0B6RA8K0, M4CEZ5K9HP, SJZX81A783]
sources:
  - url: https://en.wikipedia.org/wiki/P-Laplacian
---

## Definition

Let $n \ge 1$, let $\Omega \subseteq \R^n$ be an open set, and let $1 < p < \infty$.
For a function $u \colon \Omega \to \R$ whose [[gradient|0ABK9V9Y64]] $\nabla u$ is regular enough, the *$p$-Laplacian* of $u$ is
$$\Delta_p u = \operatorname{div} \big( \abs{\nabla u}^{p-2} \nabla u \big),$$
where $\operatorname{div}$ is the [[divergence|0MWV6ZTK6S]].
Let $u$ be in the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}_{\mathrm{loc}}(\Omega)$.
The equation $\Delta_p u = 0$ holds in the [[weak sense|SJZX81A783]] if
$$\int_\Omega \abs{\nabla u}^{p-2} \, \nabla u \cdot \nabla \varphi \, dx = 0$$
for every smooth function $\varphi$ with compact support in $\Omega$.
Such a $u$ is called *$p$-harmonic*.

## Remarks

For $p = 2$, $\Delta_2 = \Delta$ is the [[Laplacian|0E0B6RA8K0]].
Example: on $\R^n \setminus \set{0}$ with $p \ne n$, the function $u(x) = \abs{x}^{(p-n)/(p-1)}$ is $p$-harmonic.
Indeed, for $u = r^\beta$ with $r = \abs{x}$, the field $\abs{\nabla u}^{p-2} \nabla u$ is radial with size $\abs{\beta}^{p-1} r^{(\beta - 1)(p-1)}$, and its divergence vanishes when $r^{n-1} r^{(\beta-1)(p-1)}$ is constant, that is, when $\beta = (p - n)/(p - 1)$.
Non-example: for $p = 3$, the function $u(x) = x_1^2$ is not $3$-harmonic, since $\abs{\nabla u} \nabla u = (4 x_1 \abs{x_1}, 0, \ldots, 0)$ has divergence $8 \abs{x_1} \ne 0$ for $x_1 \ne 0$.
The weak form is the Euler–Lagrange equation of $\int_\Omega \abs{\nabla u}^p \, dx$.
Some authors call $-\Delta_p$ the $p$-Laplacian.
