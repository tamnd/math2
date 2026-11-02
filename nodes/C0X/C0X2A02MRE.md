---
tag: C0X2A02MRE
kind: statement
role: theorem
name: Stieltjes inversion formula
msc: [44A15, "30E20", 44A60]
uses: [RG1HFAYD98, DYR1QFNGNJ, TCYSWCTYYM]
about: [RG1HFAYD98]
sources:
  - url: https://en.wikipedia.org/wiki/Stieltjes_transformation
---

## Statement

Let $\mu$ be a finite positive [[Borel measure|DYR1QFNGNJ]] on $\R$, and let $S_\mu(z) = \int_\R \frac{d\mu(t)}{t - z}$ be its [[Stieltjes transform|RG1HFAYD98]] for $z \in \C \setminus \R$.
Then for all real numbers $a < b$,
$$\lim_{\varepsilon \to 0^+} \frac{1}{\pi} \int_a^b \operatorname{Im} S_\mu(x + i\varepsilon)\, dx = \mu\big((a, b)\big) + \tfrac12 \mu(\set{a}) + \tfrac12 \mu(\set{b}).$$
In particular, $S_\mu$ determines $\mu$.

## Remarks

For $\varepsilon > 0$ one has $\frac{1}{\pi} \operatorname{Im} S_\mu(x + i\varepsilon) = \int_\R P_\varepsilon(x - t)\, d\mu(t)$ with the [[Poisson kernel|TCYSWCTYYM]] $P_\varepsilon(u) = \frac{1}{\pi} \frac{\varepsilon}{u^2 + \varepsilon^2}$ of the upper half-plane.
By Fubini, the left side before the limit is $\int_\R \frac{1}{\pi}\big(\arctan\frac{b - t}{\varepsilon} - \arctan\frac{a - t}{\varepsilon}\big)\, d\mu(t)$.
The integrand is bounded by $1$ and tends to $1$ for $a < t < b$, to $\frac12$ for $t = a$ or $t = b$, and to $0$ otherwise, so dominated convergence gives the formula.
If $\mu$ has a continuous density $\rho$ near $x$, then $\rho(x) = \lim_{\varepsilon \to 0^+} \frac{1}{\pi} \operatorname{Im} S_\mu(x + i\varepsilon)$.

Example: for $\mu = \delta_0$, $\frac{1}{\pi} \operatorname{Im} S_\mu(x + i\varepsilon) = \frac{1}{\pi} \frac{\varepsilon}{x^2 + \varepsilon^2}$, which concentrates at $0$ with total mass $1$.

## Explanations

### L1 human

The Stieltjes transform loses no information: the measure can be recovered from it.
Push the variable $z$ down to the real axis from above and look at the imaginary part.
In the limit it becomes the density of the measure, up to the factor $\pi$.

### L2 human

The formula is the reason why the Stieltjes transform is the standard tool to identify a measure.
In random matrix theory one computes the limit of the Stieltjes transforms of empirical eigenvalue distributions, and the inversion formula then gives the limiting law, such as the semicircle law.
In the moment problem and in the spectral theory of self-adjoint operators the same formula recovers a spectral measure from its resolvent.
