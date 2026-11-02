---
tag: NQVQFMXMGE
kind: definition
name: p-harmonic function
msc: [31C45, 35J92]
defines: 7BKQT71FYZ
uses: [XJMYGY0ZZF, M4CEZ5K9HP, C3EC148VZD, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/P-Laplacian
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set and let $1 < p < \infty$.
Let $u$ lie in the local [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}_{\mathrm{loc}}(\Omega)$.
It is a *weak solution* of the [[p-Laplace equation|XJMYGY0ZZF]] $\operatorname{div}(\abs{\nabla u}^{p-2} \nabla u) = 0$ in $\Omega$ if
$$\int_\Omega \abs{\nabla u}^{p-2}\, \nabla u \cdot \nabla \varphi \, dx = 0 \quad \text{for every } \varphi \in C_c^\infty(\Omega),$$
where $\nabla u$ is the [[weak gradient|C3EC148VZD]].
A *$p$-harmonic function* in $\Omega$ is a continuous weak solution of this equation.

## Remarks

Every weak solution agrees almost everywhere with a continuous one, which is even of class $C^{1,\alpha}_{\mathrm{loc}}$ for some $\alpha > 0$, so the continuity requirement only picks a representative.
For $p = 2$ the condition is $\int \nabla u \cdot \nabla \varphi = 0$, and by Weyl's lemma the $2$-harmonic functions are the classical [[harmonic functions|0DEB0JMN0W]].
Example: for $p \ne n$, the function $u(x) = \abs{x}^{(p - n)/(p - 1)}$ is $p$-harmonic in $\R^n \setminus \set{0}$.
Indeed, for a radial function $u(r)$ the equation reads $\big(r^{n-1} \abs{u'}^{p-2} u'\big)' = 0$, and here $\abs{u'}^{p-2} u'$ is a constant multiple of $r^{1-n}$.
For $p = n$ the function $\log \abs{x}$ plays the same role.
Non-example: $u(x) = x_1^2$ on $\R^n$ is not $p$-harmonic.
Here $\abs{\nabla u}^{p-2} \nabla u = 2^{p-1} \abs{x_1}^{p-2} x_1\, e_1$, whose divergence $2^{p-1}(p - 1)\abs{x_1}^{p-2}$ is positive for $x_1 \ne 0$.
Equivalently, $u$ is $p$-harmonic in $\Omega$ when it is continuous and minimizes $\int_D \abs{\nabla v}^p \, dx$ among all $v$ with $v - u \in W^{1,p}_0(D)$, for every open $D$ with compact closure in $\Omega$.
