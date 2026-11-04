---
tag: D6GDTJJ3SG
kind: proof
name: Proof of the parametric formula for line integrals
msc: ["26B12"]
proves: 0W3W1VYWBP
uses: [0M50E4WYWJ, 0YS8RX87F4, 0C28RT5BG7, 0JF1XXGWB4, 0D98771SM0, 0NHGY0N0JB, 080RWVVSB6, 0RFWW56Y22, 07PFYV65MB, 06B8BNJCD6, 0WS1A8E2P9]
sources:
  - url: https://en.wikipedia.org/wiki/Line_integral
    locator: Derivation
---

## Proof

We compare the sums in the definitions with Riemann sums of the right sides.

1. Let $\gamma = (\gamma_1, \dots, \gamma_n) \colon [a, b] \to \R^n$ be a [[$C^1$ curve|0JF1XXGWB4]], with [[tangent vector|0D98771SM0]] $\gamma'$. For a continuous $v \colon [c, d] \to \R^n$, let $\int_c^d v(t) \, dt$ be the vector of the integrals of its components.
2. For $a \le c < d \le b$, the [[fundamental theorem of calculus|0NHGY0N0JB]] applied to each $\gamma_k$ gives $\gamma(d) - \gamma(c) = \int_c^d \gamma'(t) \, dt$.
3. For continuous $v$, let $w = \int_c^d v(t) \, dt$. Then $\norm{w}^2 = \int_c^d w \cdot v(t) \, dt \le \norm{w} \int_c^d \norm{v(t)} \, dt$, by [[linearity of the integral|080RWVVSB6]] and the [[Cauchy–Schwarz inequality|0RFWW56Y22]]. Hence $\norm{w} \le \int_c^d \norm{v(t)} \, dt$.
4. Let $P$ be a partition $c = u_0 < \dots < u_k = d$ of $[c, d]$. By steps 2 and 3, $\sum_j \norm{\gamma(u_j) - \gamma(u_{j-1})} \le \sum_j \int_{u_{j-1}}^{u_j} \norm{\gamma'} \, dt = \int_c^d \norm{\gamma'} \, dt$.
5. So the restriction of $\gamma$ to $[c, d]$ is [[rectifiable|0C28RT5BG7]], and its length is at most $\int_c^d \norm{\gamma'(t)} \, dt$. In particular the line integrals over $\gamma$ are defined.
6. The interval $[a, b]$ is compact by the [[Heine–Borel theorem|07PFYV65MB]]. The maps $\gamma'$, $f \circ \gamma$ and $F \circ \gamma$ are continuous on $[a, b]$. By the [[Heine–Cantor theorem|06B8BNJCD6]] they are uniformly continuous.
7. By the [[extreme value theorem|0WS1A8E2P9]] there are $M, N \ge 0$ with $\norm{\gamma'(t)} \le M$ and $\abs{f(\gamma(t))} \le N$ for all $t \in [a, b]$.
8. Fix $\varepsilon > 0$. By step 6 there is $\delta > 0$ such that $\abs{s - t} < \delta$ implies $\norm{\gamma'(s) - \gamma'(t)} < \varepsilon$, $\abs{f(\gamma(s)) - f(\gamma(t))} < \varepsilon$ and $\norm{F(\gamma(s)) - F(\gamma(t))} < \varepsilon$.
9. Take a partition $a = t_0 < \dots < t_k = b$ with $\max_i (t_i - t_{i-1}) < \delta$, and points $\tau_i \in [t_{i-1}, t_i]$. Write $I_i = [t_{i-1}, t_i]$ and $\Delta t_i = t_i - t_{i-1}$.
10. Let $\Delta s_i$ be the length of $\gamma$ on $I_i$. The partition $\set{t_{i-1}, t_i}$ shows that $\Delta s_i \ge \norm{\gamma(t_i) - \gamma(t_{i-1})}$.
11. By step 2, $\gamma(t_i) - \gamma(t_{i-1}) = \Delta t_i \, \gamma'(t_i) + \int_{I_i} (\gamma'(t) - \gamma'(t_i)) \, dt$. With steps 3 and 8, its norm is at least $\Delta t_i \norm{\gamma'(t_i)} - \varepsilon \Delta t_i$.
12. Also $\int_{I_i} \norm{\gamma'(t)} \, dt \le \Delta t_i \norm{\gamma'(t_i)} + \varepsilon \Delta t_i$, by step 8. With steps 10 and 11, $\Delta s_i \ge \int_{I_i} \norm{\gamma'} \, dt - 2 \varepsilon \Delta t_i$.
13. Step 5 gives $\Delta s_i \le \int_{I_i} \norm{\gamma'} \, dt$. So $\abs{\Delta s_i - \int_{I_i} \norm{\gamma'} \, dt} \le 2 \varepsilon \Delta t_i$.
14. Let $S = \sum_i f(\gamma(\tau_i)) \, \Delta s_i$ and $I = \int_a^b f(\gamma(t)) \norm{\gamma'(t)} \, dt$. Then $S - I = \sum_i f(\gamma(\tau_i)) \big( \Delta s_i - \int_{I_i} \norm{\gamma'} \, dt \big) + \sum_i \int_{I_i} \big( f(\gamma(\tau_i)) - f(\gamma(t)) \big) \norm{\gamma'(t)} \, dt$.
15. By steps 7, 8 and 13, $\abs{S - I} \le 2 N \varepsilon (b - a) + \varepsilon M (b - a)$.
16. Since $\varepsilon$ is arbitrary, the sums of the [[scalar line integral|0M50E4WYWJ]] tend to $I$. So $\int_\gamma f \, ds = \int_a^b f(\gamma(t)) \norm{\gamma'(t)} \, dt$.
17. For the vector field, let $T = \sum_i F(\gamma(\tau_i)) \cdot (\gamma(t_i) - \gamma(t_{i-1}))$. By step 2 and linearity, $T = \sum_i \int_{I_i} F(\gamma(\tau_i)) \cdot \gamma'(t) \, dt$.
18. Hence $T - \int_a^b F(\gamma(t)) \cdot \gamma'(t) \, dt = \sum_i \int_{I_i} \big( F(\gamma(\tau_i)) - F(\gamma(t)) \big) \cdot \gamma'(t) \, dt$.
19. By the Cauchy–Schwarz inequality and steps 7 and 8, each integrand has absolute value at most $\varepsilon M$. So the difference in step 18 is at most $\varepsilon M (b - a)$ in absolute value.
20. Since $\varepsilon$ is arbitrary, the sums of the [[vector line integral|0YS8RX87F4]] tend to $\int_a^b F(\gamma(t)) \cdot \gamma'(t) \, dt$. This is the second formula.

## Idea

On a short piece of a $C^1$ curve, the chord $\gamma(t_i) - \gamma(t_{i-1})$ is the integral of $\gamma'$, and the arc length is squeezed between the chord length and $\int \norm{\gamma'}$. Uniform continuity makes all the errors small at once, so the defining sums turn into Riemann sums of ordinary integrals in $t$.
