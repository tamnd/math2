---
tag: T37KYMZZS5
kind: proof
name: Proof that holomorphic functions are analytic
msc: [30B10]
proves: 0826SGV3R0
uses: [0DG0Z72CQD, 0VARVQ9ZW1, 0DG10TVYPN, 0T7ABX4CWE, 05APWSX53S, 07PFYV65MB, 0V4DET59NW, 0DJMGPN8K9, 0Q7K4AXE53, 0FJZMBX0ZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Analyticity_of_holomorphic_functions
    locator: Proof
---

## Proof

We expand the Cauchy kernel in a geometric series and integrate term by term.

1. Fix $\rho$ with $0 < \rho < r$. The closed disc $\set{w : \abs{w - c} \le \rho}$ lies in $D \subseteq U$. For $n \ge 0$ put $a_n(\rho) = \frac{1}{2 \pi i} \oint_{\abs{w - c} = \rho} \frac{f(w)}{(w - c)^{n+1}} \, dw$, a [[circle integral|0T7ABX4CWE]] of a continuous function.
2. Fix $z$ with $\abs{z - c} < \rho$ and put $q = \abs{z - c}/\rho < 1$. By [[Cauchy's integral formula|0DG10TVYPN]], $f(z) = \frac{1}{2 \pi i} \oint_{\abs{w - c} = \rho} \frac{f(w)}{w - z} \, dw$.
3. For $w$ on the circle put $u = (z - c)/(w - c)$, so $\abs{u} = q$ and $w - z = (w - c)(1 - u)$. By the [[finite geometric sum|05APWSX53S]], $\frac{1}{1 - u} = \sum_{n=0}^{N} u^n + \frac{u^{N+1}}{1 - u}$.
4. Hence $\frac{f(w)}{w - z} = \sum_{n=0}^{N} \frac{f(w)}{(w - c)^{n+1}} (z - c)^n + T_N(w)$, with $T_N(w) = \frac{f(w) \, u^{N+1}}{(w - c)(1 - u)}$.
5. The circle is closed and bounded, hence [[compact|07PFYV65MB]], so $\abs{f} \le M$ on it for some $M$ by the [[extreme value theorem|0V4DET59NW]]. Since $\abs{1 - u} \ge 1 - q$ by the [[triangle inequality|0FJZMBX0ZZ]], $\abs{T_N(w)} \le \frac{M q^{N+1}}{\rho (1 - q)}$.
6. Integrate step 4 over the circle and divide by $2 \pi i$. We get $f(z) = \sum_{n=0}^{N} a_n(\rho) (z - c)^n + \frac{1}{2\pi i} \oint T_N(w) \, dw$.
7. The circle has length $2 \pi \rho$. By the [[estimation lemma|0DJMGPN8K9]], the last term has modulus at most $\frac{M q^{N+1}}{1 - q}$. This tends to $0$ as $N \to \infty$, since [[$q^N \to 0$|0Q7K4AXE53]].
8. So the [[power series|0VARVQ9ZW1]] $\sum_{n \ge 0} a_n(\rho) (z - c)^n$ converges to $f(z)$ whenever $\abs{z - c} < \rho$.
9. Now let $0 < \rho_1 < \rho_2 < r$ and $b_n = a_n(\rho_1) - a_n(\rho_2)$. By step 8 for both radii, $\sum_{n \ge 0} b_n w^n = 0$ for every $w$ with $\abs{w} < \rho_1$.
10. Suppose some $b_n \ne 0$, and let $m$ be the least such $n$. Put $s = \rho_1 / 2$. The series $\sum b_n s^n$ converges, so its terms tend to $0$. Hence $\abs{b_n} s^n \le K$ for all $n$, for some $K$.
11. Let $0 < \abs{w} < s$. Then $\abs{b_n w^{n-m}} \le K s^{-m} (\abs{w}/s)^{n-m}$ for $n \ge m$. So $T(w) = \sum_{n > m} b_n w^{n-m}$ converges and $\abs{T(w)} \le K s^{-m} \frac{\abs{w}/s}{1 - \abs{w}/s}$.
12. By steps 9 and 10, $0 = \sum_{n \ge m} b_n w^n = w^m (b_m + T(w))$. Since $w \ne 0$, $b_m = -T(w)$.
13. Letting $w \to 0$ in step 11 gives $\abs{b_m} \le \lim \abs{T(w)} = 0$. This contradicts $b_m \ne 0$. So $a_n(\rho_1) = a_n(\rho_2)$ for all $n$.
14. Thus $a_n = a_n(\rho)$ does not depend on $\rho \in (0, r)$, and it is given by the stated formula.
15. Let $z \in D$. Choose $\rho$ with $\abs{z - c} < \rho < r$. By steps 8 and 14, $\sum_{n \ge 0} a_n (z - c)^n$ converges to $f(z)$.
16. Finally, let $c \in U$ be any point. Since $U$ is open, some disc $\set{z : \abs{z - c} < r}$ with $r > 0$ lies in $U$. By step 15, $f$ is the sum of a convergent power series near $c$. So $f$ is analytic on $U$.

## Idea

Cauchy's formula writes $f(z)$ as an average of $f(w)/(w - z)$ over a circle. The kernel $1/(w - z)$ is a geometric series in $(z - c)/(w - c)$, which converges uniformly on the circle. Integrating term by term gives the power series, and the uniqueness of coefficients shows they do not depend on the radius.
