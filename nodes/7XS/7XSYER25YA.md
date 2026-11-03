---
tag: 7XSYER25YA
kind: statement
role: fact
name: Omori's law
msc: [86A15, 62P12, 60G55]
uses: [0MTNR28K60, 04DXAFN2ES]
about: [0MTNR28K60]
sources:
  - url: https://en.wikipedia.org/wiki/Aftershock
---

## Statement

Let a large earthquake, the mainshock, occur at time $0$.
Let $n(t)$ be the rate of its aftershocks, the expected number per unit time above a fixed magnitude, at time $t > 0$.
Empirically there are constants $K > 0$, $c > 0$ and $p$ such that
$$n(t) = \frac{K}{(c + t)^p},$$
with $p$ usually close to $1$.

## Remarks

This is an observed regularity, not a theorem.
Omori proposed the form with $p = 1$ in 1894; the form with general $p$ is the modified Omori law, or Omori–Utsu law.
The aftershocks are often modelled as a non-homogeneous [[Poisson process|0MTNR28K60]] with intensity $n(t)$.
Example: integrating the rate gives the expected number of aftershocks up to time $t$.
For $p = 1$ it is $K \ln(1 + t/c)$, with $\ln$ the [[natural logarithm|04DXAFN2ES]]; for $p \ne 1$ it is $K\big((c + t)^{1-p} - c^{1-p}\big)/(1 - p)$.
For $p = 1$ the count grows without bound as $t \to \infty$; in reality the rate eventually falls to the background rate of the region.
The constant $c$ keeps the rate finite at $t = 0$; it reflects the incompleteness of catalogues just after a mainshock as well as physics.

## Explanations

### L1 human

After a big earthquake come many smaller ones, the aftershocks.
Omori's law says their rate decays roughly like one over the time since the mainshock.
So ten days after, aftershocks are about ten times rarer than one day after, but they continue for years.

### L2 human

Fitting $K$, $c$ and $p$ to the first hours of a sequence gives forecasts of the number of aftershocks in the coming days.
Combined with the Gutenberg–Richter law for the magnitudes, it gives the probability of a large aftershock.
In the ETAS model every earthquake triggers its own aftershocks with an Omori-type rate, which turns the law into a self-exciting point process.
Rate-and-state friction models of faults give a theoretical derivation of the decay with $p = 1$.
