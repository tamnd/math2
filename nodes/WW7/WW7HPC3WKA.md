---
tag: WW7HPC3WKA
kind: definition
name: Kullback–Leibler divergence
msc: [94A17, 62B10, 60F10]
defines: PQBW43X5RE
uses: [059TJN0NZ1, 04DXAFN2ES, 0D6J4B671D]
sources:
  - url: https://en.wikipedia.org/wiki/Kullback%E2%80%93Leibler_divergence
---

## Definition

Let $(\Omega, \mathcal{F})$ be a measurable space, and let $P$ and $Q$ be [[probability measures|059TJN0NZ1]] on it.
If $P$ is absolutely continuous with respect to $Q$, let $dP/dQ$ be the Radon–Nikodym derivative, and define
$$D(P \,\|\, Q) = \int_{\Omega} \log \frac{dP}{dQ} \, dP \in [0, \infty].$$
If $P$ is not absolutely continuous with respect to $Q$, define $D(P \,\|\, Q) = \infty$.
The number $D(P \,\|\, Q)$ is the *Kullback–Leibler divergence* of $P$ from $Q$.

## Remarks

The integral is well defined: with $f = dP/dQ$, it equals $\int f \log f \, dQ$, and $f \log f \ge -1/e$, so its negative part is integrable.
By Jensen's inequality it is non-negative, with equality exactly when $P = Q$; this is Gibbs' inequality.

For distributions on a countable set with [[probability mass functions|0D6J4B671D]] $p$ and $q$,
$$D(P \,\|\, Q) = \sum_{x} p(x) \log \frac{p(x)}{q(x)},$$
with the conventions $0 \log \frac{0}{q} = 0$ and $p \log \frac{p}{0} = \infty$ for $p > 0$.
With densities $p$ and $q$ with respect to a common measure, the sum becomes an integral.
The base of the [[logarithm|04DXAFN2ES]] fixes the unit: base $e$ gives nats, base $2$ gives bits.

Example: let $P$ be the Bernoulli law with parameter $1/2$ and $Q$ the Bernoulli law with parameter $1/4$.
Then $D(P \,\|\, Q) = \frac{1}{2} \log \frac{1/2}{1/4} + \frac{1}{2} \log \frac{1/2}{3/4} = \frac{1}{2} \log \frac{4}{3}$.
In the other order, $D(Q \,\|\, P) = \frac{1}{4} \log \frac{1}{2} + \frac{3}{4} \log \frac{3}{2} = \frac{1}{4} \log \frac{27}{16}$.
These differ, so $D$ is not symmetric and is not a metric.

Example of the infinite case: let $Q$ be the Dirac measure at $0$ and $P$ the Bernoulli law with parameter $1/2$.
Then $P(\set{1}) > 0 = Q(\set{1})$, so $P$ is not absolutely continuous with respect to $Q$, and $D(P \,\|\, Q) = \infty$.

Pinsker's inequality bounds the total variation distance by $\sqrt{D(P \,\|\, Q)/2}$.
