---
tag: FV3GATMWZZ
kind: proof
name: Proof that holomorphic functions on a disc have primitives
msc: ["30E20"]
proves: 02AC7JR6G6
uses: [0DG0Z72CQD, 0D1C9Y1EXA, 0BRG85WXYC, 00FWNP9TXY, 05RCDKHZM6, 0D37QFPEZE, 0NC2A3HWGT, 05AXG3QRKR, 0KXSK8TEEB, 0T71SSYZ39]
sources:
  - url: https://math.iisc.ac.in/~vvdatar/courses/2020_Jan/Lecture_Notes/Lecture-7.pdf
    locator: Theorem 2.1
---

## Proof

We integrate $f$ along a horizontal and then a vertical segment, and check the Cauchy–Riemann equations.

1. Since $f$ is [[holomorphic|0DG0Z72CQD]], it is [[complex differentiable|0D1C9Y1EXA]] at each point, hence continuous: $f(z_1 + h) - f(z_1) = h \cdot \frac{f(z_1 + h) - f(z_1)}{h} \to 0$.
2. Write $c = x_c + i y_c$. For $z = x + iy \in D$, let $Q_z$ be the set of points $s + it$ with $s$ between $x_c$ and $x$ and $t$ between $y_c$ and $y$.
3. For $s + it \in Q_z$, $\abs{s - x_c} \le \abs{x - x_c}$ and $\abs{t - y_c} \le \abs{y - y_c}$. So $\abs{(s + it) - c} \le \abs{z - c} < R$, and $Q_z \subseteq D$.
4. For $z = x + iy \in D$ define two numbers, with oriented integrals $\int_\alpha^\beta = -\int_\beta^\alpha$ taken on real and imaginary parts:
   $$F(z) = \int_{x_c}^{x} f(s + i y_c) \, ds + i \int_{y_c}^{y} f(x + it) \, dt, \qquad G(z) = i \int_{y_c}^{y} f(x_c + it) \, dt + \int_{x_c}^{x} f(s + iy) \, ds.$$
   The segments used lie in $Q_z \subseteq D$ by step 3, and the integrands are continuous by step 1.
5. For real $\alpha_1, \beta_1, \alpha_2, \beta_2$ such that the rectangle with these side coordinates lies in $D$, put
   $$E(\alpha_1, \beta_1, \alpha_2, \beta_2) = \int_{\alpha_1}^{\beta_1} f(s + i \alpha_2) \, ds + i \int_{\alpha_2}^{\beta_2} f(\beta_1 + it) \, dt - i \int_{\alpha_2}^{\beta_2} f(\alpha_1 + it) \, dt - \int_{\alpha_1}^{\beta_1} f(s + i \beta_2) \, ds.$$
   Then $F(z) - G(z) = E(x_c, x, y_c, y)$. If $x = x_c$, both $s$-integrals vanish and the two $t$-integrals agree, so $E = 0$. In the same way, $E = 0$ if $y = y_c$.
6. Swapping $\alpha_1$ and $\beta_1$ changes the sign of $E$. Swapping $\alpha_2$ and $\beta_2$ also changes the sign of $E$. This follows from $\int_\alpha^\beta = -\int_\beta^\alpha$ and a regrouping of the four terms.
7. Now let $x \ne x_c$ and $y \ne y_c$. Then $Q_z$ is a closed rectangle $\set{s + it : p_1 \le s \le q_1, \ p_2 \le t \le q_2}$ in $D$, with $p_1 < q_1$ and $p_2 < q_2$.
8. Parametrize the sides of $\partial Q_z$ counterclockwise, using [[additivity over intervals|05RCDKHZM6]] and the [[substitution|0D37QFPEZE]] $s \mapsto p_1 + q_1 - s$ on the backward sides. The [[contour integral|00FWNP9TXY]] is then
   $$\oint_{\partial Q_z} f = \int_{p_1}^{q_1} f(s + i p_2) \, ds + i \int_{p_2}^{q_2} f(q_1 + it) \, dt - \int_{p_1}^{q_1} f(s + i q_2) \, ds - i \int_{p_2}^{q_2} f(p_1 + it) \, dt.$$
9. This is $E(p_1, q_1, p_2, q_2)$. By step 6, $E(x_c, x, y_c, y) = \pm \oint_{\partial Q_z} f$. By [[Goursat's theorem|0BRG85WXYC]] the integral is $0$. With step 5, $F = G$ on $D$.
10. Fix $z = x + iy \in D$. The set $J = \set{t \in \R : x + it \in D}$ is an open interval, since $D$ is open and convex. It contains $y_c$ and $y$, because $x + i y_c$ and $z$ lie in $Q_z$.
11. For $t \in J$, $F(x + it) = \int_{x_c}^{x} f(s + i y_c) \, ds + i \int_{y_c}^{t} f(x + i \tau) \, d\tau$. The first term does not depend on $t$.
12. By [[the integral of a continuous function is an antiderivative|0NC2A3HWGT]], applied to real and imaginary parts, the [[partial derivative|05AXG3QRKR]] in $y$ is $\partial F / \partial y (z) = i f(z)$.
13. In the same way, using $F = G$ and the open interval $\set{s \in \R : s + iy \in D}$, which contains $x_c$ and $x$, we get $\partial F / \partial x (z) = f(z)$.
14. Write $F = U + iV$ and $f = a + ib$ with real $U, V, a, b$. By steps 12 and 13, $U_x = a$, $V_x = b$, $U_y = -b$ and $V_y = a$. These are continuous on $D$ by step 1.
15. Since [[continuous partial derivatives imply differentiability|0KXSK8TEEB]], $U$ and $V$ are differentiable on $D$. Also $U_x = V_y$ and $U_y = -V_x$.
16. By the [[Cauchy–Riemann equations|0T71SSYZ39]], $F$ is complex differentiable at each $z \in D$, with $F'(z) = U_x + i V_x = a + ib = f(z)$. So $F$ is holomorphic on $D$ and $F' = f$.

## Idea

Goursat's theorem says that going around a rectangle gives $0$. So integrating first horizontally and then vertically gives the same value as the other order. One order makes the $y$-derivative easy to compute, the other the $x$-derivative. Together they give the Cauchy–Riemann equations for the primitive.
