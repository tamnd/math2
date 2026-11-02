---
tag: EJNM0CV12B
kind: definition
name: Stieltjes transform
msc: [44A15, "30E20", 44A60]
defines: RG1HFAYD98
uses: [DYR1QFNGNJ, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Stieltjes_transformation
---

## Definition

Let $\mu$ be a finite positive [[Borel measure|DYR1QFNGNJ]] on $\R$.
The *Stieltjes transform* of $\mu$ is the function $S_\mu \colon \C \setminus \R \to \C$ given by
$$S_\mu(z) = \int_\R \frac{d\mu(t)}{t - z}.$$
If $\mu$ is concentrated on $[0, \infty)$, the same formula defines $S_\mu$ on $\C \setminus [0, \infty)$.

## Remarks

The integral converges absolutely, since $\abs{t - z} \ge \abs{\operatorname{Im} z} > 0$ for real $t$.
The function $S_\mu$ is [[holomorphic|0NAHXR1FRH]], satisfies $S_\mu(\bar z) = \overline{S_\mu(z)}$, and has $\operatorname{Im} S_\mu(z) > 0$ when $\operatorname{Im} z > 0$ and $\mu \ne 0$, because $\operatorname{Im} \frac{1}{t - z} = \frac{\operatorname{Im} z}{\abs{t - z}^2}$.
Many authors use the opposite sign, $\int \frac{d\mu(t)}{z - t}$, or call $S_\mu$ the Cauchy transform of $\mu$.
For $d\mu = f(t)\, dt$ on $[0, \infty)$ and $x > 0$, $S_\mu(-x) = \int_0^\infty \frac{f(t)}{x + t}\, dt$, the classical Stieltjes transform of the function $f$.

Example: for the unit point mass $\mu = \delta_0$, $S_\mu(z) = \frac{1}{0 - z} = -\frac{1}{z}$.
For the uniform probability measure on $[0, 1]$, $S_\mu(z) = \int_0^1 \frac{dt}{t - z} = \log\frac{1 - z}{-z}$ with the principal branch of the logarithm; the argument $1 - 1/z$ is a nonpositive real number only for $z \in (0, 1]$.

Non-example: Lebesgue measure on $\R$ is not finite, and $\int_\R \frac{dt}{\abs{t - z}}$ diverges for every $z$, so the formula does not define a transform.
