---
tag: D4317BHRRP
kind: proof
name: Proof of Riemann's theorem on removable singularities
msc: [30D30]
proves: 0BSQDZWF34
uses: [0DG0Z72CQD, 0D1C9Y1EXA, 0826SGV3R0, 0YMP521ZR5, 045EWAXY9P, 0P18JC72RE, 0TYB3HM9KE]
sources:
  - url: https://en.wikipedia.org/wiki/Removable_singularity
    locator: Riemann's theorem
---

## Proof

1. Let $c$, $r$, $f$, $M$ and $\delta$ be as in the statement, so $c$ is an [[isolated singularity|0TYB3HM9KE]] of $f$. Let $D = \set{z : \abs{z - c} < r}$.
2. Define $h(z) = (z - c)^2 f(z)$ for $0 < \abs{z - c} < r$, and $h(c) = 0$.
3. On the punctured disc, $h$ is a product of [[holomorphic|0DG0Z72CQD]] functions, so it is complex differentiable there.
4. At $c$: for $0 < \abs{z - c} < \delta$, $\abs{\frac{h(z) - h(c)}{z - c}} = \abs{z - c} \abs{f(z)} \le M \abs{z - c}$. This tends to $0$ as $z \to c$.
5. So $h$ is [[complex differentiable|0D1C9Y1EXA]] at $c$ with $h'(c) = 0$. By steps 3 and 4, $h$ is holomorphic on $D$.
6. By [[holomorphic functions are analytic|0826SGV3R0]], $h(z) = \sum_{n \ge 0} a_n (z - c)^n$ for each $z \in D$.
7. We have $a_0 = h(c) = 0$. By [[term-by-term differentiation|0YMP521ZR5]] at the center, $a_1 = h'(c) = 0$.
8. Consider the power series $\sum_{k \ge 0} a_{k+2} (z - c)^k$. For $z \in D$ with $z \ne c$, its partial sums are $(z - c)^{-2}$ times partial sums of the series in step 6. So it converges at each point of $D$.
9. A power series that converges at a point $w$ has bounded terms there. By the definition of the [[radius of convergence|045EWAXY9P]], the series of step 8 has radius at least $r$.
10. Let $g(z) = \sum_{k \ge 0} a_{k+2} (z - c)^k$ for $z \in D$. By [[power series are holomorphic|0YMP521ZR5]], $g$ is holomorphic on $D$.
11. By steps 7 and 8, $g(z) = h(z)/(z - c)^2 = f(z)$ for $0 < \abs{z - c} < r$.
12. By step 11 and the definition, $c$ is a [[removable singularity|0P18JC72RE]] of $f$.
13. The function $g$ is continuous at $c$, since it is complex differentiable there. By step 11, $f(z) = g(z) \to g(c)$ as $z \to c$. So $\lim_{z \to c} f(z)$ exists and equals $g(c)$.
14. The extension of $f$ by the value $g(c)$ at $c$ is the function $g$, which is holomorphic on $D$ by step 10.

## Idea

Multiplying by $(z - c)^2$ turns the bounded function $f$ into a function $h$ that is complex differentiable even at $c$, with $h(c) = h'(c) = 0$. So the power series of $h$ at $c$ starts with $(z - c)^2$. Dividing by $(z - c)^2$ gives a power series that agrees with $f$ off $c$ and fills in the missing value.
