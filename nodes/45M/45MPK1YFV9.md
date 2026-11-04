---
tag: 45MPK1YFV9
kind: proof
name: Proof of the completeness of the space of bounded continuous functions
msc: [54C35]
proves: 09GRCZVR5E
uses: [0CNQXVBHCX, 063W5JMY85, 08EWT7J0SC, 0SY9ECQ19Q, 0P953MG05E, 0BTMQ04556, 01M6CW9VM6, 0MCK8K2D7Z, 06JYPJ4WHH, 0A26X79RTB, 0DC3MPR7C9, 0B2305GNAZ]
sources:
  - url: https://webspace.maths.qmul.ac.uk/m.jerrum/MTH6126/note6.pdf
    locator: Theorem 6.9 and Corollary 6.10
---

## Proof

We first check that $d_\infty$ is a metric. Then we build the limit of a Cauchy sequence point by point and show it is uniform.

1. Let $X$ be a [[topological space|0CNQXVBHCX]] and let $(Y, d_Y)$ be a [[complete metric space|08EWT7J0SC]]. Write $C_b = C_b(X, Y)$.
2. If $X$ is empty, then $C_b$ has one element, the empty map. Then $d_\infty$ is a [[metric|063W5JMY85]], and each sequence is constant and converges. So we assume $X \ne \emptyset$ from now on.
3. Let $f, g \in C_b$ and fix $x_0 \in X$. Since $f(X)$ and $g(X)$ are [[bounded|0P953MG05E]], there are reals $M_f$ and $M_g$ with $d_Y(f(x), f(x')) \le M_f$ and $d_Y(g(x), g(x')) \le M_g$ for all $x, x' \in X$.
4. By the [[triangle inequality|01M6CW9VM6]], $d_Y(f(x), g(x)) \le d_Y(f(x), f(x_0)) + d_Y(f(x_0), g(x_0)) + d_Y(g(x_0), g(x)) \le M_f + d_Y(f(x_0), g(x_0)) + M_g$ for each $x \in X$.
5. So the set $\set{d_Y(f(x), g(x)) : x \in X}$ is nonempty and bounded above. Its [[supremum|0BTMQ04556]] $d_\infty(f, g)$ is a real number $\ge 0$.
6. We have $d_\infty(f, f) = 0$ and $d_\infty(f, g) = d_\infty(g, f)$, since $d_Y$ has these properties at each point.
7. If $f \ne g$, there is $x$ with $f(x) \ne g(x)$. Then $d_\infty(f, g) \ge d_Y(f(x), g(x)) > 0$.
8. Let $h \in C_b$. For each $x$, $d_Y(f(x), h(x)) \le d_Y(f(x), g(x)) + d_Y(g(x), h(x)) \le d_\infty(f, g) + d_\infty(g, h)$. Taking the supremum over $x$ gives the triangle inequality for $d_\infty$.
9. By steps 5 to 8, $d_\infty$ is a metric on $C_b$.
10. Let $(f_n)$ be a [[Cauchy sequence|0MCK8K2D7Z]] in $(C_b, d_\infty)$. Fix $x \in X$.
11. For all $m, n$, $d_Y(f_m(x), f_n(x)) \le d_\infty(f_m, f_n)$. So $(f_n(x))$ is a Cauchy sequence in $Y$.
12. Since $Y$ is complete, $(f_n(x))$ [[converges|06JYPJ4WHH]] to a point of $Y$. Call it $f(x)$. This defines a map $f \colon X \to Y$.
13. Let $\varepsilon > 0$. Choose $N$ with $d_\infty(f_m, f_n) < \varepsilon$ for all $m, n \ge N$.
14. Fix $x \in X$ and $n \ge N$. Since $f_m(x) \to f(x)$, there is $m \ge N$ with $d_Y(f_m(x), f(x)) < \varepsilon$.
15. Then $d_Y(f_n(x), f(x)) \le d_Y(f_n(x), f_m(x)) + d_Y(f_m(x), f(x)) < 2 \varepsilon$.
16. So, for each $\varepsilon > 0$, there is $N$ with $d_Y(f_n(x), f(x)) < 2 \varepsilon$ for all $n \ge N$ and all $x \in X$. Call this fact (U).
17. The image $f(X)$ is bounded. Apply (U) with $\varepsilon = 1$ and take $n = N$. For $x, x' \in X$, the triangle inequality gives $d_Y(f(x), f(x')) < 2 + M_{f_n} + 2$.
18. Next, $f$ is [[continuous|0SY9ECQ19Q]]. Let $W$ be open in $Y$ and let $x \in f^{-1}(W)$.
19. By the description of [[open sets of a metric space|0A26X79RTB]], there is $r > 0$ with $B(f(x), r) \subseteq W$. Here $B$ is the [[open ball|0DC3MPR7C9]].
20. Apply (U) with $\varepsilon = r / 6$. This gives $n$ with $d_Y(f_n(z), f(z)) < r / 3$ for all $z \in X$.
21. Let $V = f_n^{-1}(B(f_n(x), r / 3))$. [[Open balls are open|0B2305GNAZ]] and $f_n$ is continuous, so $V$ is open in $X$. Also $x \in V$.
22. Let $y \in V$. Then $d_Y(f(y), f(x)) \le d_Y(f(y), f_n(y)) + d_Y(f_n(y), f_n(x)) + d_Y(f_n(x), f(x)) < r$. So $f(y) \in W$.
23. So each point $x$ of $f^{-1}(W)$ lies in an open set $V$ with $V \subseteq f^{-1}(W)$. Thus $f^{-1}(W)$ is the union of these open sets, and it is open.
24. By steps 17 to 23, $f \in C_b$.
25. By (U), for each $\varepsilon > 0$ there is $N$ with $d_\infty(f_n, f) \le 2 \varepsilon$ for all $n \ge N$. So $f_n \to f$ in $(C_b, d_\infty)$.
26. Thus each Cauchy sequence in $C_b$ converges in $C_b$, and $(C_b, d_\infty)$ is a complete metric space.

## Idea

A Cauchy sequence for the sup metric is Cauchy at each point, so completeness of $Y$ gives a pointwise limit.
The Cauchy bound holds for all points at once, so the convergence is uniform. A uniform limit keeps boundedness and continuity, by an $\varepsilon / 3$ argument.
