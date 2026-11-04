---
tag: S15FFHA00G
kind: proof
name: Proof of the maximum modulus principle by Cauchy's integral formula
msc: [30C80]
proves: 048F2P90WR
uses: [097KNJFJ7V, 0DG0Z72CQD, 0DG10TVYPN, 0T7ABX4CWE, 0MBWQKM8QR, 0YBVKMYX0W]
sources:
  - url: https://en.wikipedia.org/wiki/Maximum_modulus_principle
    locator: Using Cauchy's Integral Formula
---

## Proof

1. Let $D$, $f$, $z_0$ and $r$ be as in the statement. Let $\alpha = f(z_0)$ and $M = \abs{\alpha}$.
2. If $M = 0$, then $\abs{f(z)} \le 0$ for $\abs{z - z_0} < r$, so $f = \alpha$ near $z_0$. Go to step 11 in this case.
3. Let $M > 0$. Since $D$ is open, choose $\rho_0 \in (0, r)$ with $\set{z : \abs{z - z_0} \le \rho_0} \subseteq D$. Fix $\rho \in (0, \rho_0]$.
4. By [[Cauchy's integral formula|0DG10TVYPN]] with $a = c = z_0$, written out as a [[circle integral|0T7ABX4CWE]], $$\alpha = \frac{1}{2\pi i} \int_0^{2\pi} \frac{f(z_0 + \rho e^{i\theta})}{\rho e^{i\theta}} \, i \rho e^{i\theta} \, d\theta = \frac{1}{2\pi} \int_0^{2\pi} f(z_0 + \rho e^{i\theta}) \, d\theta.$$
5. Multiply by $\overline{\alpha}$ and take real parts. With $q(\theta) = \operatorname{Re} \bigl( \overline{\alpha} f(z_0 + \rho e^{i\theta}) \bigr)$, this gives $M^2 = \frac{1}{2\pi} \int_0^{2\pi} q(\theta) \, d\theta$.
6. Since $\rho < r$, we have $q(\theta) \le \abs{\alpha} \abs{f(z_0 + \rho e^{i\theta})} \le M^2$. So $\varphi = M^2 - q$ is continuous, $\varphi \ge 0$, and $\int_0^{2\pi} \varphi = 0$ by step 5.
7. Then $\varphi = 0$ everywhere. Indeed, if $\varphi(\theta_0) > 0$, continuity gives an interval of length $\ell > 0$ on which $\varphi > \varphi(\theta_0)/2$.
8. By [[monotonicity of the integral|0MBWQKM8QR]], the integral of $\varphi$ would then be at least $\ell \varphi(\theta_0)/2 > 0$, a contradiction.
9. So $\operatorname{Re}(\overline{\alpha} f) = M^2$ on the circle $\abs{z - z_0} = \rho$. Also $\abs{\overline{\alpha} f} \le M^2$ there, so $\operatorname{Im}(\overline{\alpha} f) = 0$, and $\overline{\alpha} f = M^2 = \overline{\alpha} \alpha$.
10. Dividing by $\overline{\alpha} \ne 0$ gives $f = \alpha$ on each circle $\abs{z - z_0} = \rho$ with $0 < \rho \le \rho_0$. So $f = \alpha$ on the disc $\abs{z - z_0} < \rho_0$.
11. In both cases, $f$ equals the constant function $\alpha$ on an open disc with center $z_0$ contained in $D$. Each point of this disc is an accumulation point of the set where $f = \alpha$.
12. The constant function $\alpha$ is [[holomorphic|0DG0Z72CQD]]. By the [[identity theorem|0YBVKMYX0W]] on the [[domain|097KNJFJ7V]] $D$, $f = \alpha$ on $D$. So $f$ is constant on $D$.

## Idea

Cauchy's integral formula says that $f(z_0)$ is the average of $f$ over each small circle around $z_0$. An average of values of modulus at most $\abs{f(z_0)}$ can equal $f(z_0)$ only if every value equals $f(z_0)$. So $f$ is constant near $z_0$, and the identity theorem spreads this over the domain.
