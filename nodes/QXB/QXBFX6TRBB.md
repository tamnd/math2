---
tag: QXBFX6TRBB
kind: proof
name: Proof of the additivity of line integrals under concatenation
msc: ["26B12"]
proves: 00ZEBSMNNV
uses: [0YS8RX87F4, 0M50E4WYWJ, 0C28RT5BG7, 069P20KYQT, 0JF1XXGWB4, 0NHGY0N0JB, 0RFWW56Y22, 03HF5PMY5T, 0WS1A8E2P9]
sources:
  - url: https://en.wikipedia.org/wiki/Line_integral
    locator: Line integral of a vector field
---

## Proof

We use the sums in the definitions, restricted to partitions that contain the point $b$.

1. The curve $\gamma$ is continuous, since $\gamma_1(b) = \gamma_2(b)$. Join the break points of $\gamma_1$, the point $b$ and the break points of $\gamma_2$. This gives a [[partition|069P20KYQT]] $a = p_0 < \dots < p_m = c$ such that $\gamma$ is a [[$C^1$ curve|0JF1XXGWB4]] on each $[p_{l-1}, p_l]$.
2. By the [[extreme value theorem|0WS1A8E2P9]] there is $M \ge 0$ with $\norm{\gamma'} \le M$ on each piece, with one-sided derivatives at the $p_l$.
3. Let $s < t$ lie in one piece, and let $w = \gamma(t) - \gamma(s)$. The [[fundamental theorem of calculus|0NHGY0N0JB]] gives $w = \int_s^t \gamma'(u) \, du$ componentwise. By the [[Cauchy–Schwarz inequality|0RFWW56Y22]], $\norm{w}^2 = \int_s^t w \cdot \gamma'(u) \, du \le \norm{w} M (t - s)$, so $\norm{w} \le M (t - s)$.
4. For any $s < t$ in $[a, c]$, insert the points $p_l$ between them. The [[triangle inequality|03HF5PMY5T]] and step 3 give $\norm{\gamma(t) - \gamma(s)} \le M (t - s)$. So every inscribed polygon of $\gamma$ has length at most $M (c - a)$.
5. Hence $\gamma$ is [[rectifiable|0C28RT5BG7]], and so are its restrictions $\gamma_1$ and $\gamma_2$. So the six line integrals in the statement exist.
6. Let $I$, $I_1$ and $I_2$ be the vector line integrals of $F$ over $\gamma$, $\gamma_1$ and $\gamma_2$. Fix $\varepsilon > 0$.
7. By the definition of the [[vector line integral|0YS8RX87F4]] there is $\delta > 0$ with the following property. Every sum for $\gamma$, $\gamma_1$ or $\gamma_2$ over a partition of mesh less than $\delta$ lies within $\varepsilon$ of $I$, $I_1$ or $I_2$ respectively.
8. Choose a partition $P_1$ of $[a, b]$ and a partition $P_2$ of $[b, c]$, both of mesh less than $\delta$, with points chosen in their subintervals. Their union $P$ is a partition of $[a, c]$ of mesh less than $\delta$.
9. Each subinterval of $P$ is a subinterval of $P_1$ or of $P_2$. On $[a, b]$ we have $\gamma = \gamma_1$, and on $[b, c]$ we have $\gamma = \gamma_2$. Let $S_1$ be the sum for $\gamma_1$ and $P_1$, and $S_2$ the sum for $\gamma_2$ and $P_2$. Then the sum $S$ for $\gamma$ and $P$ is $S_1 + S_2$.
10. By step 7, $\abs{I - I_1 - I_2} \le \abs{I - S} + \abs{S_1 - I_1} + \abs{S_2 - I_2} < 3 \varepsilon$.
11. Since $\varepsilon$ is arbitrary, $\int_\gamma F \cdot d\mathbf{r} = \int_{\gamma_1} F \cdot d\mathbf{r} + \int_{\gamma_2} F \cdot d\mathbf{r}$.
12. For the [[scalar line integral|0M50E4WYWJ]], take a subinterval $[t_{i-1}, t_i]$ of $P_1$. The two curves $\gamma$ and $\gamma_1$ agree there, so they give the same length $\Delta s_i$. The same holds for $P_2$ and $\gamma_2$.
13. So steps 7 to 11, with these sums, give $\int_\gamma f \, ds = \int_{\gamma_1} f \, ds + \int_{\gamma_2} f \, ds$.

## Idea

A line integral is a limit over all fine partitions, so it can be computed with partitions that contain the joining point $b$. Each such sum splits into a sum for the first curve and a sum for the second curve, and the limits split in the same way.
