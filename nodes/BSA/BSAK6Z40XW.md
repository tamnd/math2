---
tag: BSAK6Z40XW
kind: proof
name: Proof of the residue formula at a simple pole
msc: ["30E20"]
proves: 01991NCP7H
uses: [0DG0Z72CQD, 0YK27TJ4WF, 0JFGKKWWFK, 06WHRARZKY, 0826SGV3R0, 0YMP521ZR5, 045EWAXY9P, 0X3XD2ATB0]
sources:
  - url: https://en.wikipedia.org/wiki/Residue_(complex_analysis)
    locator: Simple poles
---

## Proof

*A lemma.* Let $\varphi$ be [[holomorphic|0DG0Z72CQD]] on a disc $D_\delta = \set{z : \abs{z - c} < \delta}$ with $\delta \le r$, and let $f(z) = \varphi(z)/(z - c)$ for $0 < \abs{z - c} < \delta$. We show $\operatorname{Res}(f, c) = \varphi(c) = \lim_{z \to c} (z - c) f(z)$.

1. By [[holomorphic functions are analytic|0826SGV3R0]], $\varphi(z) = \sum_{n \ge 0} b_n (z - c)^n$ on $D_\delta$, with $b_0 = \varphi(c)$.
2. Dividing by $z - c$ gives $f(z) = \sum_{n \ge -1} b_{n+1} (z - c)^n$ for $0 < \abs{z - c} < \delta$. This is a [[Laurent series|0X3XD2ATB0]] with coefficient $b_0$ at $(z - c)^{-1}$.
3. The Laurent expansion of $f$ on $0 < \abs{z - c} < r$ also converges to $f$ on the smaller annulus $0 < \abs{z - c} < \delta$.
4. By the uniqueness part of the [[existence of Laurent expansions|06WHRARZKY]] on $0 < \abs{z - c} < \delta$, the two expansions have the same coefficients.
5. By the definition of the [[residue|0JFGKKWWFK]], $\operatorname{Res}(f, c) = b_0 = \varphi(c)$.
6. Also $(z - c) f(z) = \varphi(z) \to \varphi(c)$ as $z \to c$, since $\varphi$ is continuous. This proves the lemma.

*The first formula.*

7. Since $c$ is a [[pole of order|0YK27TJ4WF]] $1$, there are $\delta > 0$ and $\varphi$ holomorphic on $D_\delta$ with $f(z) = \varphi(z)/(z - c)$ for $0 < \abs{z - c} < \delta$. We may take $\delta \le r$.
8. By the lemma, $\operatorname{Res}(f, c) = \lim_{z \to c} (z - c) f(z)$.

*The formula for $g/h$.*

9. Let $g$ and $h$ be holomorphic on a disc around $c$, with $g(c) \ne 0$, $h(c) = 0$ and $h'(c) \ne 0$, and let $f = g/h$.
10. By analyticity, $h(z) = \sum_{n \ge 1} d_n (z - c)^n$ on a disc around $c$, with $d_1 = h'(c)$ by [[term-by-term differentiation|0YMP521ZR5]].
11. The series $k(z) = \sum_{n \ge 1} d_n (z - c)^{n-1}$ converges on the same disc, since for $z \ne c$ its partial sums are those of $h(z)$ divided by $z - c$. Its [[radius of convergence|045EWAXY9P]] is at least the radius of the disc, because a convergent series has bounded terms.
12. By [[power series are holomorphic|0YMP521ZR5]], $k$ is holomorphic there. We have $h(z) = (z - c) k(z)$ and $k(c) = h'(c) \ne 0$.
13. By continuity, $k \ne 0$ and $g$ is defined on some disc $D_\delta$ with $\delta \le r$. On it, $\varphi = g/k$ is holomorphic, and $f(z) = \varphi(z)/(z - c)$ for $0 < \abs{z - c} < \delta$.
14. By the lemma, $\operatorname{Res}(f, c) = \varphi(c) = g(c)/h'(c)$.

## Idea

Near a simple pole, $f$ is a holomorphic function $\varphi$ divided by $z - c$. Dividing the Taylor series of $\varphi$ by $z - c$ gives the Laurent series of $f$, whose coefficient at $(z - c)^{-1}$ is $\varphi(c)$. For $f = g/h$, factor $h(z) = (z - c) k(z)$ with $k(c) = h'(c)$, and take $\varphi = g/k$.
