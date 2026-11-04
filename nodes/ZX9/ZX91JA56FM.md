---
tag: ZX91JA56FM
kind: proof
name: Proof of the Cauchy–Schwarz inequality for expectations
msc: ["60E15"]
proves: 03PGHKAJG3
uses: [0DCT0QZVQ1, 0P7PTC8DDE, 05PWWHYBX5, 0VGMEBVW1M, 0R46A1XY60]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy–Schwarz_inequality
    locator: Proof by analyzing a quadratic
---

## Proof

We study the quadratic polynomial $s \mapsto E[(X + sY)^2]$, which is never negative.

1. Let $X$ and $Y$ be real random variables on one probability space $(\Omega, \mathcal{F}, P)$ with $E[X^2] < \infty$ and $E[Y^2] < \infty$.
2. For real $u$ and $v$, $\abs{uv} \le (u^2 + v^2)/2$, since $(\abs{u} - \abs{v})^2 \ge 0$. So $\abs{XY} \le (X^2 + Y^2)/2$.
3. The integral of nonnegative functions is monotone. So $E[\abs{XY}] < \infty$, and $XY$ is integrable.
4. Let $A = E[X^2]$, $B = E[XY]$ and $C = E[Y^2]$. These are real numbers with $A \ge 0$ and $C \ge 0$.
5. Fix $s \in \R$. Pointwise, $(X + sY)^2 = X^2 + 2s XY + s^2 Y^2$, and all three terms are integrable.
6. By [[linearity of expectation|0P7PTC8DDE]], $q(s) := E[(X + sY)^2] = A + 2sB + s^2 C$.
7. The [[expected value|0DCT0QZVQ1]] of the nonnegative variable $(X + sY)^2$ is nonnegative. So $q(s) \ge 0$ for all real $s$.
8. Case $C = 0$. Then $q(s) = A + 2sB$. If $B \ne 0$, then $s = -(A + 1)/(2B)$ gives $q(s) = -1 < 0$, which contradicts step 7.
9. So in the case $C = 0$ we have $B = 0$, and $B^2 = 0 = AC$.
10. Case $C > 0$. Let $s_0 = -B/C$. Then $q(s_0) = A - 2B^2/C + B^2/C = A - B^2/C$.
11. By step 7, $A - B^2/C \ge 0$. Multiplying by $C > 0$ gives $B^2 \le AC$.
12. Steps 9 and 11 prove $(E[XY])^2 \le E[X^2] \, E[Y^2]$.

Now the equality case.

13. First a lemma. Let $W \ge 0$ be a random variable with $E[W] = 0$. For each integer $k \ge 1$, [[Markov's inequality|05PWWHYBX5]] gives $P(W \ge 1/k) \le k E[W] = 0$.
14. The event $\set{W > 0}$ is the union of the events $\set{W \ge 1/k}$ over $k \ge 1$. A [[probability measure|0VGMEBVW1M]] is countably subadditive, so $P(W > 0) = 0$.
15. So $W = 0$ [[almost surely|0R46A1XY60]].
16. Suppose $B^2 = AC$ and $C = 0$. Then $E[Y^2] = 0$. By step 15 for $W = Y^2$, $Y = 0$ almost surely. So $0 \cdot X + 1 \cdot Y = 0$ almost surely.
17. Suppose $B^2 = AC$ and $C > 0$. By step 10, $q(s_0) = A - B^2/C = 0$. So $E[(X + s_0 Y)^2] = 0$.
18. By step 15 for $W = (X + s_0 Y)^2$, $X + s_0 Y = 0$ almost surely. So $a = 1$ and $b = s_0$ work, and $a \ne 0$.
19. Conversely, let $aX + bY = 0$ almost surely, with reals $a$ and $b$ not both $0$. Variables that agree almost surely have the same expectation, since the integral ignores null sets.
20. If $b \ne 0$, let $c = -a/b$. Then $Y = cX$ almost surely. So $XY = cX^2$ and $Y^2 = c^2 X^2$ almost surely.
21. By steps 19 and 20, $B = cA$ and $C = c^2 A$. So $B^2 = c^2 A^2 = AC$.
22. If $b = 0$, then $a \ne 0$ and $X = 0$ almost surely. So $X^2 = 0$ and $XY = 0$ almost surely, and $A = B = 0$. Thus $B^2 = 0 = AC$.
23. So equality holds if and only if $aX + bY = 0$ almost surely for some reals $a$ and $b$, not both $0$.

## Idea

The mean of $(X + sY)^2$ is a quadratic polynomial in $s$ that is never negative. So it cannot have two distinct real roots, which is exactly the inequality. Equality means the polynomial reaches $0$, so some combination $X + sY$ vanishes almost surely.
