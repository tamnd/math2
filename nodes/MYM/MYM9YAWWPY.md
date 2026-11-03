---
tag: MYM9YAWWPY
kind: definition
name: Probabilistic seismic hazard analysis
msc: [86A15, 62P12, 60G55]
defines: 3MKM0DKVHS
uses: [9ZEBGCR93V, 0E5G5FMT2R, 0MTNR28K60]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_hazard
---

## Definition

Fix a site and a ground motion measure $Y$, such as peak ground acceleration.
Let there be finitely many seismic sources $k = 1, \dots, K$.
Source $k$ produces earthquakes with magnitude at least $m_0$ at the annual rate $\nu_k$.
Their magnitudes have density $f_{M,k}$, often a truncated [[Gutenberg–Richter|9ZEBGCR93V]] law, and their distances to the site have density $f_{R,k}$.
A ground motion model gives $P(Y > y \mid m, r)$ for an earthquake of magnitude $m$ at distance $r$.
*Probabilistic seismic hazard analysis* computes the hazard curve
$$\lambda(y) = \sum_{k=1}^{K} \nu_k \iint P(Y > y \mid m, r)\, f_{M,k}(m)\, f_{R,k}(r)\, dm\, dr,$$
the annual rate of earthquakes that produce $Y > y$ at the site.
If these exceedances form a [[Poisson process|0MTNR28K60]] in time, the probability of at least one exceedance in $t$ years is $1 - e^{-\lambda(y) t}$.

## Remarks

The integral is the [[law of total probability|0E5G5FMT2R]] applied to the magnitude and distance of a random earthquake, multiplied by the rate of earthquakes.
Example: a probability of $10\%$ in $50$ years corresponds to $\lambda = -\ln(0.9)/50 \approx 0.00211$ per year, that is, a return period $1/\lambda \approx 475$ years.
Non-example: a deterministic analysis takes one chosen scenario earthquake, such as the largest credible earthquake on the nearest fault.
It does not sum over the rates of all scenarios, so it does not give $\lambda(y)$.
The ground motion model usually takes $\ln Y$ normally distributed given $m$ and $r$, and the scatter of this distribution has a large effect on $\lambda(y)$ at long return periods.
Disaggregation splits $\lambda(y)$ into the contributions of magnitude and distance bins.

## Explanations

### L1 human

For each shaking level, the method adds over all possible earthquakes their yearly rate times the chance that they cause that shaking at the site.
The result says how many times per year, on average, the level is exceeded.
