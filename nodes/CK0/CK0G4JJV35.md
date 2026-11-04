---
tag: CK0G4JJV35
kind: proof
name: Proof of Cauchy's integral formula by a primitive of the difference quotient
msc: ["30E20"]
proves: 0DG10TVYPN
uses: [0DG0Z72CQD, 0D1C9Y1EXA, 0T7ABX4CWE, 00FWNP9TXY, 0KDJD249DT, 07PFYV65MB, 0V4DET59NW, 0BRG85WXYC, 0DJMGPN8K9, 05RCDKHZM6, 0D37QFPEZE, 0NC2A3HWGT, 0KXSK8TEEB, 0T71SSYZ39, 0YQ458D7PF, 0SXZ68HV6F]
sources:
  - url: https://math.iisc.ac.in/~vvdatar/courses/2020_Jan/Lecture_Notes/Lecture-7.pdf
    locator: Sections 2 and 4
---

## Proof

We show that $g(z) = (f(z) - f(a))/(z - a)$ has a primitive on a disc around the circle. Then its circle integral is $0$.

1. There is $R > r$ with $D = \set{z : \abs{z - c} < R} \subseteq U$. Otherwise, for each $n$ there is $z_n \notin U$ with $\abs{z_n - c} < r + 1/n$.
2. The sequence $(z_n)$ in step 1 is bounded. Applying the [[Bolzano–Weierstrass theorem|0KDJD249DT]] to real and imaginary parts, a subsequence tends to some $z^*$ with $\abs{z^* - c} \le r$. So $z^* \in U$, and $U$ is open, so a disc around $z^*$ lies in $U$. This disc contains some $z_n$, a contradiction.
3. Since $f$ is [[holomorphic|0DG0Z72CQD]], it is [[complex differentiable|0D1C9Y1EXA]] and hence continuous on $U$. Define $g(z) = \frac{f(z) - f(a)}{z - a}$ for $z \in D$, $z \ne a$, and $g(a) = f'(a)$. Then $g$ is continuous on $D$.
4. Let $z_0 \in D$, $z_0 \ne a$. For $z \ne z_0$ near $z_0$, a direct computation gives
   $$\frac{g(z) - g(z_0)}{z - z_0} = \frac{1}{(z - a)(z_0 - a)} \left( \frac{f(z) - f(z_0)}{z - z_0} (z_0 - a) - (f(z_0) - f(a)) \right).$$
   As $z \to z_0$ this has a limit. So $g$ is holomorphic on the open set $D \setminus \set{a}$.
5. For a closed rectangle $P = \set{x + iy : p_1 \le x \le q_1, \ p_2 \le y \le q_2} \subseteq D$ with $p_1 < q_1$, $p_2 < q_2$, put $B(P) = \oint_{\partial P} g(z) \, dz$, counterclockwise. As in [[Goursat's theorem|0BRG85WXYC]], [[additivity over intervals|05RCDKHZM6]] and a [[substitution|0D37QFPEZE]] on the backward sides give
   $$B(P) = \int_{p_1}^{q_1} g(s + i p_2) \, ds + i \int_{p_2}^{q_2} g(q_1 + it) \, dt - \int_{p_1}^{q_1} g(s + i q_2) \, ds - i \int_{p_2}^{q_2} g(p_1 + it) \, dt.$$
6. If $P$ is cut by vertical and horizontal lines into smaller rectangles, $B(P)$ is the sum of their $B$ values. Indeed, in the sum of the formulas of step 5, each inner edge appears twice with opposite signs.
7. Claim: $B(P) = 0$ for each such $P \subseteq D$. If $a \notin P$, then $P$ lies in the open set $D \setminus \set{a}$, where $g$ is holomorphic by step 4. Goursat's theorem gives $B(P) = 0$.
8. Let $a = \alpha + i \beta \in P$ and $\eta > 0$. Cut $P$ by those of the lines $x = \alpha \pm \eta$ and $y = \beta \pm \eta$ that meet the inside of $P$.
9. One piece is $P_\eta = P \cap \set{x + iy : \abs{x - \alpha} \le \eta, \ \abs{y - \beta} \le \eta}$, which contains $a$. Every other piece lies in one of the half-planes $x \le \alpha - \eta$, $x \ge \alpha + \eta$, $y \le \beta - \eta$, $y \ge \beta + \eta$. So it does not contain $a$.
10. By steps 6, 7 and 9, $B(P) = B(P_\eta)$. The rectangle $P$ is closed and bounded, hence [[compact|07PFYV65MB]], so the continuous $\abs{g}$ is [[bounded on $P$|0V4DET59NW]] by some $M$.
11. The perimeter of $P_\eta$ is at most $8 \eta$. By the [[estimation lemma|0DJMGPN8K9]], $\abs{B(P)} = \abs{B(P_\eta)} \le 8 \eta M$. Since $\eta > 0$ is arbitrary, $B(P) = 0$. This proves the claim.
12. Write $c = x_c + i y_c$. For $z = x + iy \in D$, the rectangle $Q_z$ of points $s + it$ with $s$ between $x_c$ and $x$ and $t$ between $y_c$ and $y$ lies in $D$. Indeed $\abs{(s + it) - c} \le \abs{z - c}$.
13. Define, with oriented integrals,
   $$F(z) = \int_{x_c}^{x} g(s + i y_c) \, ds + i \int_{y_c}^{y} g(x + it) \, dt, \qquad G(z) = i \int_{y_c}^{y} g(x_c + it) \, dt + \int_{x_c}^{x} g(s + iy) \, ds.$$
14. The difference $F(z) - G(z)$ is the right side of step 5 with $p_1 = x_c$, $q_1 = x$, $p_2 = y_c$, $q_2 = y$. It is $0$ if $x = x_c$ or $y = y_c$. Swapping $p_1$ and $q_1$, or $p_2$ and $q_2$, changes its sign, since $\int_\alpha^\beta = -\int_\beta^\alpha$. With both pairs in increasing order, it is $B(Q_z)$.
15. So $F(z) - G(z) = \pm B(Q_z)$ or $0$. By step 11, $F = G$ on $D$.
16. By [[the integral of a continuous function is an antiderivative|0NC2A3HWGT]], applied to real and imaginary parts, $\partial F / \partial y = i g$ from the formula for $F$. In the same way $\partial F / \partial x = g$ from the formula for $G$. Each integral runs over an open interval of points in $D$.
17. Write $F = U + iV$. Then $U_x = \operatorname{Re} g$, $V_x = \operatorname{Im} g$, $U_y = -\operatorname{Im} g$, $V_y = \operatorname{Re} g$. These are continuous, so [[$U$ and $V$ are differentiable|0KXSK8TEEB]], and they satisfy the Cauchy–Riemann equations.
18. By the [[Cauchy–Riemann equations|0T71SSYZ39]], $F$ is holomorphic on $D$ with $F' = U_x + i V_x = g$.
19. The circle $\gamma(\theta) = c + r e^{i \theta}$, $\theta \in [0, 2\pi]$, is a closed continuously differentiable path in $D$. By the [[fundamental theorem of contour integration|0YQ458D7PF]], $\oint_{\abs{z - c} = r} g(z) \, dz = 0$.
20. For $z$ on the circle, $\abs{z - c} = r > \abs{a - c}$, so $z \ne a$ and $g(z) = \frac{f(z)}{z - a} - \frac{f(a)}{z - a}$.
21. By step 19 and linearity of the [[contour integral|00FWNP9TXY]], $\oint_{\abs{z - c} = r} \frac{f(z)}{z - a} \, dz = f(a) \oint_{\abs{z - c} = r} \frac{dz}{z - a}$.
22. Since $\abs{a - c} < r$, the [[integral of $1/(z - a)$ over the circle|0SXZ68HV6F]] is $2 \pi i$. So $\oint_{\abs{z - c} = r} \frac{f(z)}{z - a} \, dz = 2 \pi i f(a)$, which is the formula for the [[circle integral|0T7ABX4CWE]].

## Idea

The difference quotient $g(z) = (f(z) - f(a))/(z - a)$ is holomorphic except at $a$, where it is still continuous. A continuous bad point cannot spoil Goursat's theorem, because a tiny rectangle around it has a tiny integral. So $g$ has a primitive on a disc, its circle integral is $0$, and what is left is $f(a)$ times the integral of $1/(z - a)$.
