---
tag: BNRX1PNN39
kind: proof
name: Proof of Stokes' theorem by pulling back to Green's theorem
msc: ["26B20"]
proves: 0AKRKVHW94
uses: [05788J51WZ, 0DQ8ERJZNS, 0YPRY7T4PK, 0GDNHS9J2X, 0SEDGXG9S3, 0YS8RX87F4, 0HR3N02317, 0EAAS2EHDR, 0A8TJ0VHC7, 0V9A43H7WV, 0NNQY8WCW6, 0W3W1VYWBP, 00ZEBSMNNV, 0BARQY52N5, 0TCBZMEYGN, 0KXSK8TEEB]
sources:
  - url: https://en.wikipedia.org/wiki/Stokes%27_theorem
    locator: Elementary proof
---

## Proof

We pull both integrals back to $D$ and apply Green's theorem there.

1. Let $r$ be $C^2$ on an open set $W \supseteq D$, and let $F = (F_1, F_2, F_3)$ be $C^1$ on an open set $V \supseteq S$. The set $W' = W \cap r^{-1}(V)$ is open, since $r$ is continuous, and it contains $D$.
2. Write $r_u, r_v$ for the partial derivatives of the [[parametrised surface|05788J51WZ]] $r$, and $a = r_u$, $b = r_v$ with components $a_j, b_j$. Write $\partial_j F_i = \partial F_i / \partial x_j$.
3. On $W'$ define $L(u, v) = F(r(u, v)) \cdot r_u(u, v)$ and $M(u, v) = F(r(u, v)) \cdot r_v(u, v)$.
4. Each $F_i$ is differentiable, by [[continuous partial derivatives imply differentiability|0KXSK8TEEB]]. By the [[chain rule|0EAAS2EHDR]], $\partial_v (F_i \circ r) = \sum_j \partial_j F_i(r) \, b_j$ and $\partial_u (F_i \circ r) = \sum_j \partial_j F_i(r) \, a_j$.
5. By the [[product rule|0V9A43H7WV]] in each variable, $\partial_v L = \sum_{i, j} \partial_j F_i(r) \, b_j a_i + F(r) \cdot r_{uv}$ and $\partial_u M = \sum_{i, j} \partial_j F_i(r) \, a_j b_i + F(r) \cdot r_{vu}$.
6. These partial derivatives are continuous on $W'$, because $F$ is $C^1$ and $r$ is [[$C^2$|0TCBZMEYGN]]. By [[Schwarz's theorem|0NNQY8WCW6]], $r_{uv} = r_{vu}$.
7. Hence $\partial_u M - \partial_v L = \sum_{i, j} \partial_j F_i(r) \, (a_j b_i - a_i b_j)$. The terms with $i = j$ are $0$. Grouping the terms $(i, j)$ and $(j, i)$, the sum is $\sum_{i < j} (\partial_j F_i - \partial_i F_j)(r) \, (a_j b_i - a_i b_j)$.
8. By the definitions of the [[curl|0GDNHS9J2X]] and the [[cross product|0SEDGXG9S3]], the pair $(1, 2)$ gives $(\partial_1 F_2 - \partial_2 F_1)(a_1 b_2 - a_2 b_1) = (\nabla \times F)_3 \, (a \times b)_3$.
9. The pair $(1, 3)$ gives $(\partial_3 F_1 - \partial_1 F_3)(a_3 b_1 - a_1 b_3) = (\nabla \times F)_2 \, (a \times b)_2$.
10. The pair $(2, 3)$ gives $(\partial_2 F_3 - \partial_3 F_2)(a_2 b_3 - a_3 b_2) = (\nabla \times F)_1 \, (a \times b)_1$.
11. By steps 7 to 10, $\partial_u M - \partial_v L = (\nabla \times F)(r) \cdot (r_u \times r_v)$ on $W'$.
12. Let $\gamma = (\gamma_1, \gamma_2) \colon [\alpha, \beta] \to \R^2$, with break points $\alpha = p_0 < \dots < p_m = \beta$ such that $\gamma$ is $C^1$ on each $[p_{l-1}, p_l]$.
13. On $(p_{l-1}, p_l)$, the [[chain rule along a curve|0A8TJ0VHC7]] gives $(r \circ \gamma)'(t) = r_u(\gamma(t)) \, \gamma_1'(t) + r_v(\gamma(t)) \, \gamma_2'(t)$. The right side is continuous on $[p_{l-1}, p_l]$.
14. Apply the [[mean value theorem|0BARQY52N5]] in each component. The one-sided derivatives of $r \circ \gamma$ at $p_{l-1}$ and $p_l$ exist and equal the limits of the right side. So $r \circ \gamma$ is $C^1$ on each piece, and $\partial S = r \circ \gamma$ is piecewise $C^1$.
15. By [[additivity|00ZEBSMNNV]] and the [[parametric formula|0W3W1VYWBP]] on each piece, $\oint_{\partial S} F \cdot d\mathbf{r} = \sum_l \int_{p_{l-1}}^{p_l} F(r(\gamma(t))) \cdot (r \circ \gamma)'(t) \, dt$.
16. By step 13 and the definition of $L$ and $M$, the integrand is $L(\gamma(t)) \, \gamma_1'(t) + M(\gamma(t)) \, \gamma_2'(t)$. With the parametric formula and additivity again, $\oint_{\partial S} F \cdot d\mathbf{r} = \oint_\gamma (L \, du + M \, dv)$, a [[line integral|0YS8RX87F4]] in the plane.
17. The functions $L$ and $M$ have continuous partial derivatives on the open set $W' \supseteq D$, by step 6. By [[Green's theorem|0HR3N02317]] and step 11, $\oint_\gamma (L \, du + M \, dv) = \iint_D (\nabla \times F)(r) \cdot (r_u \times r_v) \, du \, dv$.
18. Since $r$ is regular, $r_u \times r_v \ne 0$ on $D$, and $n = (r_u \times r_v) / \norm{r_u \times r_v}$. By the definitions of the [[flux|0YPRY7T4PK]] and the [[surface integral|0DQ8ERJZNS]], $\iint_S (\nabla \times F) \cdot n \, dS = \iint_D (\nabla \times F)(r) \cdot (r_u \times r_v) \, du \, dv$.
19. Steps 16 to 18 give $\oint_{\partial S} F \cdot d\mathbf{r} = \iint_S (\nabla \times F) \cdot n \, dS$.

## Idea

Through the parametrisation, the circulation of $F$ around $\partial S$ becomes a line integral of the plane field $(L, M) = (F \cdot r_u, F \cdot r_v)$ around $\gamma$. Green's theorem turns it into a double integral of $\partial_u M - \partial_v L$. The second derivatives of $r$ cancel, and what remains is exactly the curl of $F$ dotted with the normal vector $r_u \times r_v$.
