---
tag: RJMSHNBBSF
kind: proof
name: Proof of the Poincaré lemma for one-forms on convex sets
msc: [58A12]
proves: 05MC3HND79
uses: [01ZQQDCERP, 0K06X9QXDX, 0MTENFBW3Q, 0F1AVGX26N, 004FRCXH6M, 0S166D363M, 05AXG3QRKR, 0135XZZQ8M, 0KXSK8TEEB, 0A8TJ0VHC7, 0V9A43H7WV, 0AR06W1E1B, 06SESV7GQY, 0XYAFCN0PT, 06SKCHDQT5]
sources:
  - url: https://arxiv.org/abs/1905.13347
    locator: Theorem 1, Proof 1 a)
---

## Proof

We compute the partial derivatives of $g$ by differentiating under the integral sign.

1. Let $U \subseteq \R^n$ be [[open|01ZQQDCERP]] and [[convex|0K06X9QXDX]], and let $\omega = \sum_{i=1}^n f_i \, dx_i$ be a [[one-form|0MTENFBW3Q]] on $U$. Each $f_i \colon U \to \R$ has continuous [[partial derivatives|05AXG3QRKR]] $\partial_k f_i = \partial f_i / \partial x_k$. Assume that $\omega$ is [[closed|0F1AVGX26N]].
2. By [[continuous partial derivatives imply differentiability|0KXSK8TEEB]], each $f_i$ is [[differentiable|0135XZZQ8M]] at every point of $U$.
3. For $a \in U$ and $v \in \R^n$, we have $Df_i(a)(v) = \sum_{k=1}^n \partial_k f_i(a) \, v_k$. Indeed, taking $h = s e_k$ in the definition of $Df_i(a)$ gives $Df_i(a)(e_k) = \partial_k f_i(a)$, where $e_k$ is the $k$-th standard basis vector. Linearity of $Df_i(a)$ then gives the formula.
4. We show that $\partial_j f_i = \partial_i f_j$ on $U$ for all $i, j$. By the definition of the [[exterior derivative|004FRCXH6M]], $d\omega = \sum_{i=1}^n \sum_{k=1}^n \partial_k f_i \, dx_k \wedge dx_i$.
5. By the rules of the [[wedge product|0S166D363M]], $dx_i \wedge dx_i = 0$ and $dx_i \wedge dx_k = -dx_k \wedge dx_i$. Grouping the terms with indices $\set{k, i}$ gives $d\omega = \sum_{k < i} (\partial_k f_i - \partial_i f_k) \, dx_k \wedge dx_i$.
6. The two-forms $dx_k \wedge dx_i$ with $k < i$ are linearly independent. Since $d\omega = 0$, every coefficient vanishes, so $\partial_k f_i = \partial_i f_k$ for $k < i$. The case $k = i$ is trivial, and the case $k > i$ follows by swapping the names of the indices.
7. Fix $p \in U$. For $x \in U$ and $t \in [0, 1]$, the point $p + t(x - p) = (1 - t) p + t x$ lies in $U$, because $U$ is convex. So the integrand in the definition of $g(x)$ is defined. It is continuous in $t$, as a composition and product of continuous functions. By [[continuous functions are Riemann integrable|06SESV7GQY]], $g(x)$ is well defined.
8. Fix $x \in U$ and an index $j$. Since $U$ is open, choose $r > 0$ such that the closed ball of radius $2r$ about $x$ lies in $U$.
9. For $t \in [0, 1]$ and $\abs{s} < 2r$, put $q(t, s) = p + t(x + s e_j - p)$. The point $x + s e_j$ lies in $U$, so $q(t, s) \in U$ by convexity.
10. Define $H(t, s) = \sum_{i=1}^n f_i(q(t, s)) \, (x_i + s \delta_{ij} - p_i)$, where $\delta_{ij}$ is $1$ if $i = j$ and $0$ otherwise. Then $g(x + s e_j) = \int_0^1 H(t, s) \, dt$. The function $H$ is continuous on $[0, 1] \times [-r, r]$.
11. Fix $t \in [0, 1]$. The curve $s \mapsto q(t, s)$ on $(-2r, 2r)$ has derivative $t e_j$. By the [[chain rule for a curve|0A8TJ0VHC7]] and Step 3, $\frac{\partial}{\partial s} f_i(q(t, s)) = Df_i(q(t, s))(t e_j) = t \, \partial_j f_i(q(t, s))$.
12. The factor $x_i + s \delta_{ij} - p_i$ has derivative $\delta_{ij}$ in $s$. By the [[product rule|0V9A43H7WV]] and Step 11,
$$\frac{\partial H}{\partial s}(t, s) = \sum_{i=1}^n t \, \partial_j f_i(q(t, s)) \, (x_i + s \delta_{ij} - p_i) + f_j(q(t, s)).$$
13. The right side of Step 12 is continuous on $[0, 1] \times [-r, r]$, because each $\partial_j f_i$ and each $f_j$ is continuous and $q$ is continuous.
14. By [[differentiation under the integral sign|0AR06W1E1B]], applied to $H$ on $[0, 1] \times [-r, r]$, the function $s \mapsto g(x + s e_j)$ is differentiable at $s = 0$. Its derivative there is $\partial_j g(x)$. So, with $\gamma(t) = p + t(x - p) = q(t, 0)$,
$$\partial_j g(x) = \int_0^1 \Big( t \sum_{i=1}^n \partial_j f_i(\gamma(t)) \, (x_i - p_i) + f_j(\gamma(t)) \Big) \, dt.$$
15. By Step 6, $\partial_j f_i = \partial_i f_j$. So the integrand in Step 14 equals $\psi(t) = t \sum_{i=1}^n \partial_i f_j(\gamma(t)) \, (x_i - p_i) + f_j(\gamma(t))$. This function $\psi$ is continuous on $[0, 1]$.
16. Put $\varphi(t) = t \, f_j(\gamma(t))$ for $t \in [0, 1]$. It is continuous on $[0, 1]$. The curve $\gamma$ has derivative $x - p$.
17. For $t \in (0, 1)$, apply the chain rule for a curve to $\gamma$ restricted to $(0, 1)$. With Step 3, it gives $\frac{d}{dt} f_j(\gamma(t)) = \sum_{i=1}^n \partial_i f_j(\gamma(t)) \, (x_i - p_i)$. By the product rule, $\varphi'(t) = f_j(\gamma(t)) + t \sum_{i=1}^n \partial_i f_j(\gamma(t)) \, (x_i - p_i) = \psi(t)$.
18. So $\varphi'$ extends to the continuous function $\psi$ on $[0, 1]$, which is Riemann integrable. By the [[second fundamental theorem of calculus|0XYAFCN0PT]], $\int_0^1 \psi(t) \, dt = \varphi(1) - \varphi(0) = f_j(x) - 0 = f_j(x)$.
19. By Steps 14, 15 and 18, $\partial_j g(x) = f_j(x)$ for every $x \in U$ and every $j$.
20. The partial derivatives $\partial_j g = f_j$ are continuous, so $g$ is [[continuously differentiable|06SKCHDQT5]]. By the definition of the exterior derivative of a function, $dg = \sum_{j=1}^n \partial_j g \, dx_j = \sum_{j=1}^n f_j \, dx_j = \omega$.
21. Hence $\omega$ is exact, and the given function $g$ satisfies $dg = \omega$ on $U$.

## Idea

The function $g(x)$ is the integral of $\omega$ along the straight segment from $p$ to $x$, which lies in $U$ by convexity. Differentiating under the integral sign gives an integrand with the terms $\partial_j f_i$. The closedness condition $\partial_j f_i = \partial_i f_j$ turns this integrand into the exact derivative $\frac{d}{dt}\big(t f_j(p + t(x - p))\big)$. The fundamental theorem of calculus then gives $f_j(x)$.
