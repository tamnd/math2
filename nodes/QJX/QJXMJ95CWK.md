---
tag: QJXMJ95CWK
kind: proof
name: Proof of the isolated zeros theorem by power series
msc: [30C15]
proves: 0K83KEJ43P
uses: [0DG0Z72CQD, 0826SGV3R0, 0VARVQ9ZW1, 045EWAXY9P, 0YMP521ZR5]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_theorem
    locator: Lemma
---

## Proof

1. Let $U$, $f$ and $z_0$ be as in the statement. Choose $R > 0$ with $D = \set{z : \abs{z - z_0} < R} \subseteq U$.
2. By [[holomorphic functions are analytic|0826SGV3R0]], there are $a_0, a_1, \dots \in \C$ with $f(z) = \sum_{n \ge 0} a_n (z - z_0)^n$ for each $z \in D$.
3. First, the two cases cannot both hold. If they held with radii $r_1$ and $r_2$, the point $z = z_0 + \min(r_1, r_2)/2$ would give $f(z) = 0$ and $f(z) \ne 0$.
4. If $a_n = 0$ for each $n$, then $f = 0$ on $D$, and case 1 holds with $r = R$.
5. Otherwise let $m$ be the smallest index with $a_m \ne 0$. Then $f(z) = \sum_{n \ge m} a_n (z - z_0)^n$ on $D$.
6. Consider the [[power series|0VARVQ9ZW1]] $\sum_{k \ge 0} a_{m+k} (z - z_0)^k$. For $z \in D$ with $z \ne z_0$, its partial sums are $(z - z_0)^{-m}$ times partial sums of the series in step 5. So it converges at each $z \in D$.
7. If a power series converges at a point $w$, its terms tend to $0$ and so are bounded. By the definition of the [[radius of convergence|045EWAXY9P]], the radius is at least $\abs{w - z_0}$.
8. By steps 6 and 7, the series of step 6 has radius of convergence at least $R$. Let $g(z)$ be its sum on $D$.
9. By [[power series are holomorphic|0YMP521ZR5]], $g$ is [[holomorphic|0DG0Z72CQD]] on $D$, hence continuous. Also $g(z_0) = a_m \ne 0$.
10. By step 6, $f(z) = (z - z_0)^m g(z)$ for each $z \in D$, including $z = z_0$ where both sides are $0$ if $m \ge 1$, and $a_0$ if $m = 0$.
11. By continuity of $g$ at $z_0$, there is $r \in (0, R]$ with $g(z) \ne 0$ for $\abs{z - z_0} < r$.
12. For $0 < \abs{z - z_0} < r$, both factors $(z - z_0)^m$ and $g(z)$ are nonzero. So $f(z) \ne 0$, and case 2 holds.
13. By steps 3, 4 and 12, exactly one of the two cases holds.

## Idea

Near $z_0$ the function is a power series. Either every coefficient is zero, so $f$ vanishes near $z_0$, or there is a first nonzero coefficient. In the second case $f(z) = (z - z_0)^m g(z)$ with $g(z_0) \ne 0$, and continuity keeps $g$ away from zero near $z_0$.
