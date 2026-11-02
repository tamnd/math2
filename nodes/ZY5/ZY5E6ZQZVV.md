---
tag: ZY5E6ZQZVV
kind: definition
name: Euler–Lagrange equation
msc: [49K10, 35A15, 49K05]
defines: PS0VV149ET
uses: [PQ25NHV0KS, 05AXG3QRKR, 02NSMQVQWK]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%E2%80%93Lagrange_equation
---

## Definition

Let $\Omega \subseteq \R^n$ be an open set and let $L \colon \Omega \times \R \times \R^n \to \R$, written $L(x, z, p)$, be a function of class $C^2$.
Write $L_z = \partial L / \partial z$ and $L_{p_i} = \partial L / \partial p_i$ for its [[partial derivatives|05AXG3QRKR]].
The *Euler–Lagrange equation* of the functional $J(u) = \int_\Omega L(x, u, \nabla u) \, dx$ of the [[calculus of variations|PQ25NHV0KS]] is the second-order equation
$$-\sum_{i=1}^n \frac{\partial}{\partial x_i} \Big( L_{p_i}\big(x, u(x), \nabla u(x)\big) \Big) + L_z\big(x, u(x), \nabla u(x)\big) = 0 \quad \text{in } \Omega$$
for an unknown $u \in C^2(\Omega)$.
In short form it reads $-\operatorname{div} L_p(x, u, \nabla u) + L_z(x, u, \nabla u) = 0$, with the [[divergence|02NSMQVQWK]] taken in $x$.

## Remarks

If $\Omega$ is bounded and $u \in C^2(\overline{\Omega})$ minimises $J$ among $C^2(\overline{\Omega})$ functions with the same boundary values, then $u$ solves the Euler–Lagrange equation.
Indeed $\frac{d}{dt} J(u + t\varphi)\big|_{t=0} = 0$ for every $\varphi \in C^\infty_c(\Omega)$; integrating by parts gives $\int_\Omega (-\operatorname{div} L_p + L_z) \varphi \, dx = 0$ for all such $\varphi$, so the integrand vanishes.
The *weak* form $\int_\Omega \big( L_p(x, u, \nabla u) \cdot \nabla \varphi + L_z(x, u, \nabla u) \varphi \big) \, dx = 0$ for all $\varphi \in C^\infty_c(\Omega)$ makes sense for less regular $u$.

Example: for $L(x, z, p) = \frac{1}{2}\abs{p}^2 - f(x) z$ one has $L_p = p$ and $L_z = -f$, so the Euler–Lagrange equation is Poisson's equation $-\Delta u = f$.

Example: for $n = 1$ and $L(x, z, p) = \sqrt{1 + p^2}$, one gets $\frac{d}{dx}\big(u' / \sqrt{1 + u'^2}\big) = 0$, so $u'$ is constant and the graph is a straight line.

Non-example: a solution of the Euler–Lagrange equation need not be a minimiser.
For $n = 1$, $\Omega = (0, 2\pi)$ and $L = \frac{1}{2}(p^2 - z^2)$, the equation is $u'' + u = 0$, solved by $u = 0$; but $J(t \sin(x/2)) = \frac{t^2}{2} \int_0^{2\pi} \big(\frac{1}{4}\cos^2(x/2) - \sin^2(x/2)\big) \, dx = -\frac{3\pi t^2}{8} < 0 = J(0)$ for $t \ne 0$, and $t\sin(x/2)$ has the same boundary values $0$.

## Explanations

### L1 human

The Euler–Lagrange equation is what one gets by setting the first variation of an integral functional to zero.
Minimisers that are smooth enough must solve it, but solutions need not be minimisers.
