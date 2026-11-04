---
tag: VB8MN7GKCW
kind: proof
name: Proof of the symmetry of second derivatives by a second difference
msc: [26B05]
proves: 01V9FPBBVK
uses: [0EY05Z9RPN, 02RSXVM1ZN, 0135XZZQ8M, 08EVNYZF42, 0MN882VJ4P, 02CYB184RC, 0CYYAF8AD2, 0CXZ217QDP, 0A6PMR20N4, 0ZTEH055YF, 03MC70ZRNR, 0SDMPMCN43, 0DC3MPR7C9, 01ZQQDCERP, 0FJZMBX0ZZ]
sources:
  - url: https://arxiv.org/abs/1910.11531
    locator: Theorem 5.1
---

## Proof

We compute the limit of the second difference $\Delta(t) / t^2$ in two ways, with the mean value inequality.

1. Let $U$, $f$ and $a$ be as in the statement. Let $E$ be the space of linear maps $\mathbb{R}^n \to \mathbb{R}^m$, with the [[operator norm|0ZTEH055YF]]. So $\|T w\| \le \|T\| \, \|w\|$ for $T \in E$ and $w \in \mathbb{R}^n$.
2. All norms on the finite-dimensional space $E$ are [[equivalent|03MC70ZRNR]]. A change to an equivalent norm changes the quotient in the definition of the [[Fréchet derivative|08EVNYZF42]] by bounded factors only. So the hypothesis on $Df$ holds for the operator norm.
3. Put $B = D(Df)(a)$, a linear map $\mathbb{R}^n \to E$. By the definition of the [[iterated derivative|0EY05Z9RPN]], $D^2 f(a)(u, v) = (B u)(v)$. This is linear in $u$ since $B$ is linear, and linear in $v$ since $B u \in E$. So $D^2 f(a)$ is [[bilinear|0SDMPMCN43]].
4. For $z$ with $a + z \in U$, put $R(z) = Df(a + z) - Df(a) - B z \in E$. By the [[little-o form of the derivative|0MN882VJ4P]], for each $\varepsilon > 0$ there is $\delta > 0$ with $\|R(z)\| \le \varepsilon \|z\|$ for $\|z\| < \delta$ and $a + z \in U$.
5. Since $U$ is [[open|01ZQQDCERP]], there is $\rho > 0$ such that the [[open ball|0DC3MPR7C9]] $B(a, \rho)$ lies in $U$.
6. Fix $u, v \in \mathbb{R}^n$ and put $K = \|u\| + \|v\| + 1$. For $0 < t < \rho / K$, put $\Delta(t) = f(a + t u + t v) - f(a + t u) - f(a + t v) + f(a)$. The four points lie in $B(a, \rho)$, since $\|t u + t v\| \le t K < \rho$.
7. Fix such a $t$, and put $r = \rho - t \|u\| > 0$. Let $V$ be the open ball of radius $r$ about $0$. For $y \in V$, the [[triangle inequality|0FJZMBX0ZZ]] gives $a + y \in B(a, \rho)$ and $a + t u + y \in B(a, \rho)$.
8. Define $G \colon V \to \mathbb{R}^m$ by $G(y) = f(a + t u + y) - f(a + y) - (B(t u))(y)$.
9. Let $p \in \mathbb{R}^n$ with $p + y \in U$. The map $y' \mapsto f(p + y')$ has the same error quotient at $y$ as $f$ at $p + y$. So it is differentiable at $y$ with derivative $Df(p + y)$.
10. The map $y \mapsto (B(t u))(y)$ is linear, so its [[derivative|0CYYAF8AD2]] is $B(t u)$ at each point. By step 9 and the [[linearity of the derivative|0CXZ217QDP]], $G$ is differentiable on $V$ with $DG(y) = Df(a + t u + y) - Df(a + y) - B(t u)$.
11. By step 4, $Df(a + t u + y) = Df(a) + B(t u + y) + R(t u + y)$ and $Df(a + y) = Df(a) + B y + R(y)$. As $B$ is linear, step 10 gives $DG(y) = R(t u + y) - R(y)$.
12. We have $G(0) = f(a + t u) - f(a)$ and $G(t v) = f(a + t u + t v) - f(a + t v) - t^2 (B u)(v)$. So $G(t v) - G(0) = \Delta(t) - t^2 (B u)(v)$.
13. For $0 \le s \le 1$, $\|s t v\| \le t \|v\| < r$, because $t K < \rho$. So the segment from $0$ to $t v$ lies in $V$.
14. Let $\varepsilon > 0$, take $\delta$ from step 4, and suppose also $t < \delta / K$. Let $y$ be on the segment from $0$ to $t v$. Then $\|y\| \le t \|v\| < \delta$ and $\|t u + y\| \le t (\|u\| + \|v\|) < \delta$.
15. By steps 4, 11 and 14, $\|DG(y)\| \le \varepsilon t (\|u\| + \|v\|) + \varepsilon t \|v\| \le 2 \varepsilon t K$.
16. By the [[mean value inequality|02CYB184RC]] for $G$ on $V$, with steps 13 and 15, $\|G(t v) - G(0)\| \le 2 \varepsilon t K \cdot t \|v\| \le 2 \varepsilon K^2 t^2$.
17. By steps 12 and 16, $\big\| \Delta(t) / t^2 - (B u)(v) \big\| \le 2 \varepsilon K^2$ for each $t$ with $0 < t < \min(\rho, \delta) / K$.
18. The formula for $\Delta(t)$ and the number $K$ do not change when $u$ and $v$ are swapped. So steps 6 to 17 with $u$ and $v$ swapped give $\big\| \Delta(t) / t^2 - (B v)(u) \big\| \le 2 \varepsilon K^2$ for the same $t$.
19. Fix one such $t$. By the triangle inequality and steps 17 and 18, $\|(B u)(v) - (B v)(u)\| \le 4 \varepsilon K^2$.
20. This holds for each $\varepsilon > 0$, and $K$ does not depend on $\varepsilon$. So $(B u)(v) = (B v)(u)$, that is, $D^2 f(a)(u, v) = D^2 f(a)(v, u)$.
21. Now let $i, j \in \{1, \dots, n\}$, with standard basis vectors $e_i$ and $e_j$. For $y \in U$, [[the derivative gives the directional derivatives|0A6PMR20N4]], so $\partial f / \partial x_j (y) = Df(y)(e_j)$.
22. For real $t \ne 0$ with $|t| < \rho$, step 21 and the definition of $R$ give $\dfrac{\partial_j f(a + t e_i) - \partial_j f(a)}{t} - (B e_i)(e_j) = \dfrac{R(t e_i)(e_j)}{t}$.
23. By steps 1 and 4, the norm of the right side is at most $\|R(t e_i)\| / |t| \le \varepsilon$ when $|t| < \min(\rho, \delta)$. So $\partial_i (\partial_j f)(a)$ exists and equals $(B e_i)(e_j)$.
24. By the definition of the [[second partial derivative|02RSXVM1ZN]], applied to each component, $\dfrac{\partial^2 f}{\partial x_i \, \partial x_j}(a) = D^2 f(a)(e_i, e_j)$. In the same way, $\dfrac{\partial^2 f}{\partial x_j \, \partial x_i}(a) = D^2 f(a)(e_j, e_i)$.
25. By step 20 with $u = e_i$ and $v = e_j$, the two mixed partial derivatives at $a$ are equal.

## Idea

The second difference $\Delta(t)$ is symmetric in $u$ and $v$ by its formula. We show that $\Delta(t) / t^2$ tends to $D^2 f(a)(u, v)$, by viewing $\Delta(t)$ as the change of an auxiliary map $G$ along the segment from $0$ to $t v$. The derivative of $G$ is only a difference of two error terms of $Df$, so the mean value inequality makes the remaining error small. Swapping $u$ and $v$ gives the same limit, which forces the symmetry.
