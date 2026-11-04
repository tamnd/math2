---
tag: DJPGNAVZN1
kind: proof
name: Proof of Cauchy's estimates
msc: [30A10]
proves: 0JJRENWMP6
uses: [0DG0Z72CQD, 0F0H5P5DED, 0DJMGPN8K9, 0T7ABX4CWE, 0HYNZE940T]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula
    locator: Consequences
---

## Proof

We apply the estimation lemma to the integral formula for $f^{(n)}(c)$.

1. Since $f$ is [[holomorphic|0DG0Z72CQD]] and the closed disc lies in $U$, the [[formula for the derivatives|0F0H5P5DED]] with $a = c$ gives $f^{(n)}(c) = \frac{n!}{2 \pi i} \oint_{\abs{z - c} = r} \frac{f(z)}{(z - c)^{n+1}} \, dz$.
2. For $z$ on the circle, $\abs{z - c} = r$. Since the [[modulus is multiplicative|0HYNZE940T]], $\abs{\frac{f(z)}{(z - c)^{n+1}}} = \frac{\abs{f(z)}}{r^{n+1}} \le \frac{M}{r^{n+1}}$.
3. The [[circle integral|0T7ABX4CWE]] uses the path $\gamma(\theta) = c + r e^{i \theta}$, $\theta \in [0, 2\pi]$. Since $\abs{\gamma'(\theta)} = \abs{i r e^{i \theta}} = r$, its length is $\int_0^{2\pi} r \, d\theta = 2 \pi r$.
4. By the [[estimation lemma|0DJMGPN8K9]], $\abs{\oint_{\abs{z - c} = r} \frac{f(z)}{(z - c)^{n+1}} \, dz} \le \frac{M}{r^{n+1}} \cdot 2 \pi r = \frac{2 \pi M}{r^n}$.
5. By steps 1 and 4, $\abs{f^{(n)}(c)} \le \frac{n!}{2 \pi} \cdot \frac{2 \pi M}{r^n} = \frac{n! \, M}{r^n}$.

## Idea

The derivative $f^{(n)}(c)$ is an average over the circle of $f(z)/(z - c)^{n+1}$, up to the factor $n!$. On the circle this quantity has size at most $M / r^{n+1}$, and the circle has length $2 \pi r$.
