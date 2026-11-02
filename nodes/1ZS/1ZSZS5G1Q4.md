---
tag: 1ZSZS5G1Q4
kind: statement
role: theorem
name: Radon–Nikodym theorem
msc: [28A15, 28A10]
uses: [P15VQS5DJ9, WEBBT18D4X, P0P21KDV6E, Y98C5T956Q, YYNCJSR0PJ, DG76G5Z6XW]
about: [P0P21KDV6E, Y98C5T956Q]
sources:
  - url: https://en.wikipedia.org/wiki/Radon–Nikodym_theorem
same_as:
  wikidata: Q1191319
  wikipedia: Radon–Nikodym theorem
---

## Statement

Let $(X, \Sigma)$ be a measurable space and let $\mu$ and $\nu$ be [[σ-finite measures|WEBBT18D4X]] on $\Sigma$.
Assume that $\nu$ is [[absolutely continuous|P0P21KDV6E]] with respect to $\mu$, that is, $\mu(A) = 0$ implies $\nu(A) = 0$ for $A \in \Sigma$.
Then there is a [[measurable function|YYNCJSR0PJ]] $f \colon X \to [0, \infty)$ such that
$$\nu(A) = \int_A f \, d\mu \quad \text{for all } A \in \Sigma.$$
The function $f$ is unique up to equality $\mu$-almost everywhere.

## Remarks

A standard proof first treats finite measures.
Consider the measurable $g \ge 0$ with $\int_A g \, d\mu \le \nu(A)$ for all $A$, and take one that maximises $\int_X g \, d\mu$.
If the leftover measure $\nu - g \mu$ were not zero, a Hahn decomposition of $\nu - g\mu - \varepsilon \mu$ would allow $g$ to be increased, a contradiction.
Von Neumann gave another proof through the Riesz representation of a bounded linear functional on $L^2(\mu + \nu)$.
The σ-finite case follows by cutting $X$ into countably many pieces of finite measure.

Example: if $\nu$ is the standard normal distribution on $\R$ and $\mu$ is Lebesgue measure, then $f(x) = e^{-x^2/2} / \sqrt{2\pi}$.

The hypothesis of σ-finiteness of $\mu$ cannot be dropped.
Let $\mu$ be counting measure on the Borel sets of $[0, 1]$ and $\nu$ Lebesgue measure.
Then $\nu \ll \mu$, because only the empty set has $\mu$-measure $0$.
A density $f$ would satisfy $f(x) = \nu(\{x\}) = 0$ for every $x$, which gives $\nu = 0$, a contradiction.

The function $f$ is the [[measure with density|Y98C5T956Q]] description of $\nu$: $\nu = f \mu$.

## Explanations

### L1 human

If one measure never sees mass where another sees none, then the first is the second one weighted by a density function.
This is how a probability density arises from a distribution that has no point masses and no mass on sets of length zero.
The density plays the role of a derivative of one measure with respect to the other.

### L2 human

The theorem is the source of the Radon–Nikodym derivative $d\nu / d\mu$.
In probability it gives conditional expectation: the conditional expectation of an integrable variable given a sub-σ-algebra is a Radon–Nikodym derivative.
It also identifies the dual of $L^p(\mu)$ with $L^q(\mu)$ for $1 \le p < \infty$ and σ-finite $\mu$.
Together with the Lebesgue decomposition it describes every σ-finite measure relative to a fixed one.
