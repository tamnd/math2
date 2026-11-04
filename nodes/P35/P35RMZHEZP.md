---
tag: P35RMZHEZP
kind: proof
name: Proof of global existence for globally Lipschitz vector fields by steps of uniform length
msc: [34A12]
proves: 0BFD3A6CRH
uses: [075VBY4K4X, 055VVSN00V, 0FJZMBX0ZZ, 0WS1A8E2P9, 0J7HF2PF1H, 0P6KRD5B7A, 0G3DBXRRQJ]
sources:
  - url: https://en.wikipedia.org/wiki/Picard%E2%80%93Lindel%C3%B6f_theorem
    locator: Global existence of solution
---

## Proof

We show that the Picard–Lindelöf theorem gives local solutions on time steps of a length that does not depend on the starting point. Then we glue finitely many steps on each compact subinterval.

1. A solution on a subinterval $[c, d] \subseteq J$ is a curve $y : [c, d] \to \mathbb{R}^n$ with $y'(t) = f(t, y(t))$ at each $t \in [c, d]$, using one-sided derivatives at $c$ and $d$. A solution on $J$ is defined in the same way. If $J$ is a single point, the constant $x_0$ is the only solution. So let $J$ contain more than one point.
2. Uniqueness on a compact piece. Let $[c, d] \subseteq J$ with $c \le t_0 \le d$, and let $y, z$ be solutions on $[c, d]$ with $y(t_0) = z(t_0) = x_0$.
3. If $t_0 < d$, [[continuous dependence on initial data|0G3DBXRRQJ]] on $[t_0, d]$, with $U = \mathbb{R}^n$, gives $\|y(t) - z(t)\| \le 0 \cdot e^{K(t - t_0)} = 0$. So $y = z$ on $[t_0, d]$.
4. If $c < t_0$, let $g(t, x) = -f(-t, x)$ on $(-J) \times \mathbb{R}^n$, where $-J = \set{-t : t \in J}$. It is continuous and $K$-Lipschitz in $x$. The curves $\tilde y(t) = y(-t)$ and $\tilde z(t) = z(-t)$ satisfy $\tilde y'(t) = -y'(-t) = g(t, \tilde y(t))$, and the same for $\tilde z$.
5. Applying step 3 to $g$ on $[-t_0, -c]$ gives $\tilde y = \tilde z$ there. So $y = z$ on $[c, t_0]$, and hence on all of $[c, d]$.
6. A growth bound. By the [[Lipschitz condition|055VVSN00V]] and the [[triangle inequality|0FJZMBX0ZZ]], $\|f(t, x)\| \le \|f(t, 0)\| + K \|x\|$ for $t \in J$ and $x \in \mathbb{R}^n$.
7. One step. Fix $[c, d] \subseteq J$ with $c < d$. The map $t \mapsto \|f(t, 0)\|$ is continuous, so by the [[extreme value theorem|0WS1A8E2P9]] it has a maximum $m$ on $[c, d]$. Let $h = 1 / (1 + K)$.
8. Let $t_1 \in [c, d)$, $y_1 \in \mathbb{R}^n$ and $t_2 = \min(t_1 + h, d)$. Let $A = m + K \|y_1\| + 1 > 0$, let $B$ be the closed ball of radius $A$ about $y_1$, and let $L = m + K \|y_1\| + K A$.
9. For $t \in [t_1, t_2]$ and $x \in B$, step 6 gives $\|f(t, x)\| \le m + K (\|y_1\| + A) = L$. Also $L = A - 1 + KA \le (1 + K) A$, so $L (t_2 - t_1) \le L h \le A$.
10. So the restriction of $f$ to $[t_1, t_2] \times \mathbb{R}^n$ satisfies the [[Picard–Lindelöf hypotheses|0J7HF2PF1H]] at $(t_1, y_1)$ with constants $A, L, K$. Condition (1) is the global Lipschitz bound, (2) holds as $f$ is continuous, and (3) and (4) are step 9.
11. By the [[Picard–Lindelöf theorem|0P6KRD5B7A]], there is a solution $\alpha$ on $[t_1, t_2]$ with $\alpha(t_1) = y_1$. Now let $t_1 \in (c, d]$. Apply steps 7 to 10 to $g$ of step 4, and reverse time as in step 4. This gives a solution on $[\max(t_1 - h, c), t_1]$ with value $y_1$ at $t_1$.
12. Existence on a compact piece. Let $[c, d] \subseteq J$ with $c \le t_0 \le d$ and $c < d$. Let $s_k = \min(t_0 + k h, d)$ for $k \ge 0$.
13. Suppose $t_0 < d$. By step 11 at $(t_0, x_0)$ there is a solution $\beta_1$ on $[t_0, s_1]$ with $\beta_1(t_0) = x_0$.
14. Given a solution $\beta_k$ on $[t_0, s_k]$ with $s_k < d$, step 11 at $(s_k, \beta_k(s_k))$ gives a solution $\alpha$ on $[s_k, s_{k+1}]$ with $\alpha(s_k) = \beta_k(s_k)$. Let $\beta_{k+1}$ be $\beta_k$ on $[t_0, s_k]$ and $\alpha$ on $[s_k, s_{k+1}]$.
15. At $s_k$ the left derivative of $\beta_{k+1}$ is $f(s_k, \beta_k(s_k))$ and the right derivative is $f(s_k, \alpha(s_k))$. These are equal, so $\beta_{k+1}$ is differentiable at $s_k$, and $\beta_{k+1}$ is a solution on $[t_0, s_{k+1}]$.
16. Since $h > 0$ is fixed, $s_k = d$ once $k \ge (d - t_0)/h$. So after finitely many steps we get a solution on $[t_0, d]$.
17. In the same way, with the backward steps of step 11, we get a solution on $[c, t_0]$ with value $x_0$ at $t_0$. Both one-sided derivatives at $t_0$ equal $f(t_0, x_0)$. So the glued curve $x_{[c, d]}$ is a solution on $[c, d]$ with $x_{[c, d]}(t_0) = x_0$.
18. Exhausting $J$. Choose $c_m, d_m \in J$ for $m \ge 1$ with $c_m \le t_0 \le d_m$, $c_m < d_m$, $c_m$ non-increasing and $d_m$ non-decreasing. If $J$ has a least element, let each $c_m$ be it. Otherwise let $c_m \to \inf J$. Treat $d_m$ in the same way with the upper end of $J$.
19. Then every $t \in J$ lies in some $[c_m, d_m]$. If $t$ is an interior point of $J$, then $c_m < t < d_m$ for all large $m$.
20. Let $x_m = x_{[c_m, d_m]}$ from step 17. For $m' \ge m$, the restriction of $x_{m'}$ to $[c_m, d_m]$ is a solution with value $x_0$ at $t_0$. By steps 2 to 5 it equals $x_m$.
21. So $x(t) = x_m(t)$, for any $m$ with $t \in [c_m, d_m]$, defines a curve $x : J \to \mathbb{R}^n$ with $x(t_0) = x_0$.
22. If $t$ is interior to $J$, then $x = x_m$ on the open interval $(c_m, d_m)$ around $t$ for a large $m$, so $x'(t) = f(t, x(t))$. If $t$ is an end point of $J$ in $J$, then $t = c_m$ or $t = d_m$ for all $m$, and the one-sided derivative is that of $x_m$.
23. So $x$ is a solution of the [[initial value problem|075VBY4K4X]] $x' = f(t, x)$, $x(t_0) = x_0$ on all of $J$.
24. If $y$ is another such solution on $J$, its restriction to each $[c_m, d_m]$ equals $x_m$ by steps 2 to 5. By step 19 these intervals cover $J$, so $y = x$. Hence the solution on $J$ exists and is unique.

## Idea

For a general field, Picard–Lindelöf gives a time step that may shrink as the solution grows, and the steps can add up to a finite time. With a global Lipschitz bound, the field grows at most linearly, and a ball of radius about $\|y_1\|$ gives a step of length $1/(1+K)$ from every starting point. Finitely many such steps cover any compact time interval.
