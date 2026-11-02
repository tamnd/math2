---
tag: HEMXNPQBSV
kind: definition
name: Abscissa of convergence
msc: [44A10]
defines: FTHFSJ30WJ
uses: [05XT5AVJBK, 0VCTBJMEJF]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace_transform
---

## Definition

Let $f \colon [0, \infty) \to \C$ be integrable on each interval $[0, T]$ with $T > 0$.
The *abscissa of convergence* of the [[Laplace transform|05XT5AVJBK]] of $f$ is
$$\sigma_c = \inf \set{ \sigma \in \R : \int_0^\infty f(t) e^{-\sigma t}\, dt \text{ converges} } \in [-\infty, +\infty],$$
where convergence is that of the [[improper integral|0VCTBJMEJF]] $\lim_{T \to \infty} \int_0^T f(t) e^{-\sigma t}\, dt$, and $\inf \emptyset = +\infty$.

## Remarks

If the Laplace integral converges at a complex number $s_0$, it converges at every $s$ with $\operatorname{Re} s > \operatorname{Re} s_0$.
Hence the integral converges for $\operatorname{Re} s > \sigma_c$ and diverges for $\operatorname{Re} s < \sigma_c$.
Example: for $f(t) = e^{at}$ with $a \in \R$, $\int_0^T e^{(a - \sigma)t}\, dt$ has a finite limit exactly when $\sigma > a$, so $\sigma_c = a$.
Non-example of a finite value: for $f(t) = e^{t^2}$ the integral diverges for every real $\sigma$, so $\sigma_c = +\infty$; for $f(t) = e^{-t^2}$ it converges for every real $\sigma$, so $\sigma_c = -\infty$.
For $f = 1$, $\sigma_c = 0$, and on the line $\operatorname{Re} s = 0$ the integral diverges at every point.
