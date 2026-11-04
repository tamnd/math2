---
tag: BYDNRZM97D
kind: proof
name: Proof of the residue theorem by subtracting principal parts
msc: ["30E20"]
proves: 032HKYS329
uses: [0DG0Z72CQD, 06WHRARZKY, 0JFGKKWWFK, 0X3XD2ATB0, 045EWAXY9P, 0YMP521ZR5, 0D1C9Y1EXA, 01MPZXYVYF, 00FWNP9TXY, 0V4DET59NW, 0NX5NWAFC9, 0DJMGPN8K9, 0YQ458D7PF, 0X7SBS8E0F]
sources:
  - url: https://proofwiki.org/wiki/Residue_Theorem
---

## Proof

1. Let $U$, $a_1, \dots, a_n$, $f$ and $\gamma : [a, b] \to U \setminus \set{a_1, \dots, a_n}$ be as in the statement.
2. For each $k$, choose $r_k > 0$ so that the disc $D_k = \set{z : \abs{z - a_k} < r_k}$ lies in $U$ and contains no $a_j$ with $j \ne k$.
3. By the [[existence of Laurent expansions|06WHRARZKY]] on $0 < \abs{z - a_k} < r_k$, $f(z) = \sum_{m \in \Z} c_{k,m} (z - a_k)^m$ there. By the definition of the [[residue|0JFGKKWWFK]], $\operatorname{Res}(f, a_k) = c_{k,-1}$.
4. Let $E_k(\zeta) = \sum_{m \ge 1} c_{k,-m} \zeta^m$. By the definition of a [[Laurent series|0X3XD2ATB0]], it converges at $\zeta = 1/(z - a_k)$ for $0 < \abs{z - a_k} < r_k$, that is, at each $\zeta$ with $\abs{\zeta} > 1/r_k$.
5. At such points the terms are bounded. So for each $t > 0$ there is $B_t$ with $\abs{c_{k,-m}} t^m \le B_t$ for all $m$: take $t' > \max(t, 1/r_k)$ and use $t^m \le t'^m$.
6. So the [[radius of convergence|045EWAXY9P]] of $E_k$ is $\infty$, and $E_k$ is [[holomorphic|0DG0Z72CQD]] on $\C$ by [[power series are holomorphic|0YMP521ZR5]].
7. Let $P_k(z) = E_k\bigl(1/(z - a_k)\bigr)$ for $z \ne a_k$. As a composition of [[complex differentiable|0D1C9Y1EXA]] functions, $P_k$ is holomorphic on $\C \setminus \set{a_k}$.
8. On $0 < \abs{z - a_k} < r_k$, the function $T_k = f - P_k$ is the sum of the power series $\sum_{m \ge 0} c_{k,m} (z - a_k)^m$. This series converges on the punctured disc, so its radius is at least $r_k$, and its sum is holomorphic on all of $D_k$.
9. Let $g = f - \sum_{k=1}^{n} P_k$ on $U \setminus \set{a_1, \dots, a_n}$. It is holomorphic there.
10. On $0 < \abs{z - a_k} < r_k$, $g = T_k - \sum_{j \ne k} P_j$. The right side is holomorphic on all of $D_k$, since $a_j \notin D_k$ for $j \ne k$.
11. Define $g(a_k)$ as the value of this right side at $a_k$. Then $g$ is holomorphic on a disc around each $a_k$, so $g$ is holomorphic on $U$.
12. By [[Cauchy's integral theorem|01MPZXYVYF]] on the simply connected set $U$, $\oint_\gamma g(z) \, dz = 0$. By linearity of the [[contour integral|00FWNP9TXY]], $\oint_\gamma f(z) \, dz = \sum_{k=1}^{n} \oint_\gamma P_k(z) \, dz$.
13. Fix $k$. The image of $\gamma$ is compact and does not contain $a_k$. By [[attainment of bounds|0V4DET59NW]], $d = \min_t \abs{\gamma(t) - a_k} > 0$.
14. On the image of $\gamma$, $\abs{c_{k,-m} (z - a_k)^{-m}} \le \abs{c_{k,-m}} d^{-m} \le B_{2/d} \, 2^{-m}$, with $B_{2/d}$ from step 5.
15. By the [[Weierstrass M-test|0NX5NWAFC9]], applied to real and imaginary parts, the series for $P_k$ converges uniformly on the image of $\gamma$.
16. By the [[estimation lemma|0DJMGPN8K9]] applied to the tails, $\oint_\gamma P_k(z) \, dz = \sum_{m \ge 1} c_{k,-m} \oint_\gamma (z - a_k)^{-m} \, dz$.
17. For $m \ge 2$, the function $(z - a_k)^{-m}$ has the primitive $-(z - a_k)^{1-m}/(m - 1)$ on $\C \setminus \set{a_k}$. By the [[fundamental theorem of contour integration|0YQ458D7PF]], its integral over the closed path $\gamma$ is $0$.
18. For $m = 1$, the definition of the [[winding number|0X7SBS8E0F]] gives $\oint_\gamma \frac{dz}{z - a_k} = 2\pi i \, n(\gamma, a_k)$.
19. By steps 16 to 18, $\oint_\gamma P_k(z) \, dz = 2\pi i \, n(\gamma, a_k) \, c_{k,-1} = 2\pi i \, n(\gamma, a_k) \operatorname{Res}(f, a_k)$.
20. Summing over $k$ in step 12 gives $\oint_\gamma f(z) \, dz = 2\pi i \sum_{k=1}^{n} n(\gamma, a_k) \operatorname{Res}(f, a_k)$.

## Idea

Near each $a_k$, the negative powers in the Laurent series form the principal part $P_k$, which is holomorphic everywhere except at $a_k$. Subtracting all principal parts from $f$ leaves a function with only removable singularities, whose integral over $\gamma$ is zero by Cauchy's theorem. In each principal part only the term $c_{k,-1}/(z - a_k)$ contributes, and it contributes $2\pi i$ times the winding number times the residue.
