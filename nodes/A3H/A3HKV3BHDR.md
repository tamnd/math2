---
tag: A3HKV3BHDR
kind: statement
role: proposition
name: Kolmogorov 1941 theory
msc: [76F05]
uses: [VY307F8Z0S, YQ2KYDWRD0, NYRS1BJKRQ, NM5Q4845Z4]
about: [VY307F8Z0S, YQ2KYDWRD0]
sources:
  - url: https://en.wikipedia.org/wiki/Kolmogorov_microscales
---

## Statement

Consider [[turbulence|VY307F8Z0S]] at high Reynolds number in an incompressible fluid with kinematic [[viscosity|NM5Q4845Z4]] $\nu$.
Let $\varepsilon$ be the mean dissipation rate per unit mass, $L$ the size of the large eddies and $\eta = (\nu^3 / \varepsilon)^{1/4}$ the [[Kolmogorov length|NYRS1BJKRQ]].
Let $\delta u(r) = (\mathbf{u}(\mathbf{x} + \mathbf{r}) - \mathbf{u}(\mathbf{x})) \cdot \mathbf{r} / r$ be the longitudinal velocity increment over a separation $\mathbf{r}$ with $r = \abs{\mathbf{r}}$.
Assume Kolmogorov's hypotheses:

1. (local isotropy) for $r \ll L$, the statistics of the velocity increments are homogeneous and isotropic;
2. (first similarity hypothesis) for $r \ll L$, these statistics are determined uniquely by $\nu$ and $\varepsilon$;
3. (second similarity hypothesis) for $\eta \ll r \ll L$, they are determined uniquely by $\varepsilon$, independently of $\nu$.

Then the following hold for $\eta \ll r \ll L$ and for every integer $p \ge 1$ for which the structure function exists, with universal constants $C_p$:
$$S_p(r) = \langle \delta u(r)^p \rangle = C_p \, (\varepsilon r)^{p/3}.$$
The energy spectrum satisfies
$$E(k) = C_K \, \varepsilon^{2/3} k^{-5/3} \qquad \text{for } 1/L \ll k \ll 1/\eta,$$
with a universal constant $C_K$.

## Remarks

The proof is dimensional analysis.
By hypothesis 3, $S_p(r)$ depends only on $\varepsilon$, with units $\mathrm{m^2/s^3}$, and $r$, with units $\mathrm{m}$.
The only combination of them with units of $(\mathrm{m/s})^p$ is $(\varepsilon r)^{p/3}$.
The spectrum follows in the same way, since $E(k)$ has units $\mathrm{m^3/s^2}$.
The conclusions are only as good as the hypotheses, which are physical assumptions, not consequences of the Navier–Stokes equations.

For $p = 2$ the law $S_2(r) \propto (\varepsilon r)^{2/3}$, the two-thirds law, and the $-5/3$ spectrum agree well with measurements in many flows.
For $p = 3$ the prediction is consistent with the exact four-fifths law, which gives $C_3 = -4/5$.
For larger $p$ measured exponents fall below $p/3$, an effect of intermittency that the 1941 theory ignores; Kolmogorov and Obukhov proposed a refined theory in 1962 to account for it.

## Explanations

### L1 human

Kolmogorov asked what the small eddies of a turbulent flow could possibly depend on.
His answer: far from the largest and the smallest scales, only on the rate at which energy flows down the [[cascade|YQ2KYDWRD0]].
From that single quantity and the size of an eddy, there is only one way to make a speed, and this fixes how velocity differences grow with distance.
The famous result is that the energy in eddies of size $\ell$ grows like $\ell^{2/3}$, or equivalently that the spectrum falls off like $k^{-5/3}$.

### L2 human

The theory is the backbone of the phenomenology of turbulence.
It gives the scalings used everywhere: the Kolmogorov microscales, the $\mathrm{Re}^{9/4}$ cost of direct simulation, and the $-5/3$ spectrum against which data and models are checked.
It is not a theorem about the Navier–Stokes equations; deriving it, or even the existence of a dissipation rate independent of $\nu$, from the equations is a major open problem.
Its one exact consequence is the four-fifths law for $S_3$, which Kolmogorov derived from the Kármán–Howarth equation.
Deviations at higher order, called anomalous scaling, are the subject of the theory of intermittency.
