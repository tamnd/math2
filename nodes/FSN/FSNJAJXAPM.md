---
tag: FSNJAJXAPM
kind: proof
name: Proof of the Heine–Cantor theorem by a finite cover of balls
msc: ["54E45"]
proves: 06B8BNJCD6
uses: [0QPHW703PV, 0NVPNC12JY, 0DC3MPR7C9, 0B2305GNAZ, 0YF82GBTND, 01M6CW9VM6, 0FHSDCQACY]
sources:
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Cantor_theorem
    locator: Proof of Heine–Cantor theorem
---

## Proof

We use an open cover by small balls and take the smallest radius of a finite subcover.

1. Write $d_X$ and $d_Y$ for the metrics of $X$ and $Y$. Fix a real $\varepsilon > 0$. We must find $\delta > 0$ with $d_Y(f(x), f(y)) < \varepsilon$ whenever $d_X(x, y) < \delta$.
2. If $X$ is empty, every $\delta > 0$ works. From now on let $X$ be nonempty.
3. Let $p \in X$. The map $f$ is continuous, so preimages of open sets are open. By [[continuity via open sets|0YF82GBTND]], there is $\delta_p > 0$ with $d_Y(f(x), f(p)) < \varepsilon / 2$ for all $x$ with $d_X(x, p) < \delta_p$.
4. The [[open balls|0DC3MPR7C9]] $B(p, \delta_p / 2)$, for $p \in X$, are [[open|0B2305GNAZ]]. Each $p$ lies in its own ball, so they form an [[open cover|0NVPNC12JY]] of $X$.
5. Since $X$ is [[compact|0QPHW703PV]], finitely many of them cover $X$. Call their centres $p_1, \ldots, p_n$, with $n \ge 1$, and write $\delta_k = \delta_{p_k}$.
6. Let $\delta = \min(\delta_1 / 2, \ldots, \delta_n / 2)$. This is a minimum of finitely many positive reals, so $\delta > 0$.
7. Let $x, y \in X$ with $d_X(x, y) < \delta$. By step 5, $x \in B(p_k, \delta_k / 2)$ for some $k$. So $d_X(x, p_k) < \delta_k / 2 < \delta_k$.
8. By the [[triangle inequality|01M6CW9VM6]], $d_X(y, p_k) \le d_X(y, x) + d_X(x, p_k) < \delta + \delta_k / 2 \le \delta_k$.
9. By steps 7 and 8 and the choice of $\delta_k$ in step 3, $d_Y(f(x), f(p_k)) < \varepsilon / 2$ and $d_Y(f(y), f(p_k)) < \varepsilon / 2$.
10. By the triangle inequality in $Y$, $d_Y(f(x), f(y)) < \varepsilon / 2 + \varepsilon / 2 = \varepsilon$.
11. The number $\delta$ depends only on $\varepsilon$. So condition 1 of [[uniform continuity|0FHSDCQACY]] holds, and $f$ is uniformly continuous.

## Idea

Continuity gives a good radius $\delta_p$ at each point, but these radii may shrink from point to point. Compactness lets us keep only finitely many points, and the smallest of their radii works everywhere. Halving the radii makes room for the triangle inequality, so two close points both land near one centre.
