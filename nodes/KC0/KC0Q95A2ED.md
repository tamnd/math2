---
tag: KC0Q95A2ED
kind: statement
role: proposition
name: Widom scaling hypothesis
msc: [82B27, 82B26]
uses: [SQ41AZGZ2P, 57789VKKAY]
about: [SQ41AZGZ2P]
sources:
  - url: https://en.wikipedia.org/wiki/Widom_scaling
same_as:
  wikidata: Q7998780
  wikipedia: Widom scaling
---

## Statement

Consider a system near a [[critical point|57789VKKAY]], with reduced temperature $t$ and external field $h$.
Let $f_s(t, h)$ be the singular part of its free energy density.
The *Widom scaling hypothesis* asserts that there are constants $a, b$ with $a > 0$ and $0 < b < 1$ such that
$$f_s(\lambda^a t, \lambda^b h) = \lambda f_s(t, h) \quad \text{for all } \lambda > 0.$$
Assume this hypothesis, and assume that the derivatives below have nonzero finite scaling amplitudes.
Then the [[critical exponents|SQ41AZGZ2P]] of the specific heat, the order parameter, the susceptibility and the critical isotherm are
$$\alpha = 2 - \frac{1}{a}, \qquad \beta = \frac{1 - b}{a}, \qquad \gamma = \frac{2b - 1}{a}, \qquad \delta = \frac{b}{1 - b}.$$

## Remarks

Proof idea: take $\lambda = \abs{t}^{-1/a}$ to get $f_s(t, h) = \abs{t}^{1/a} \Phi_\pm(h / \abs{t}^{b/a})$, where $\Phi_\pm(y) = f_s(\pm 1, y)$.
Two derivatives in $t$ give $C \sim \abs{t}^{1/a - 2}$, one derivative in $h$ at $h = 0$ gives $m \sim \abs{t}^{(1-b)/a}$, and two give $\chi \sim \abs{t}^{(1 - 2b)/a}$.
At $t = 0$, take $\lambda = \abs{h}^{-1/b}$ instead, so $f_s(0, h) = \abs{h}^{1/b} f_s(0, \pm 1)$ and $m \sim \abs{h}^{1/b - 1}$.
The four exponents depend on only two numbers $a$ and $b$, which gives the [[scaling relations|Z6W0AXDN9G]] $\alpha + 2\beta + \gamma = 2$ and $\gamma = \beta(\delta - 1)$.

Example: the two-dimensional Ising model has $a = 1/2$ and $b = 15/16$.
These values give $\alpha = 0$, $\beta = 1/8$, $\gamma = 7/4$ and $\delta = 15$, which are its exact exponents.

The hypothesis is not a theorem for general models.
It was proposed by Widom in 1965.
The renormalization group explains it: $a = y_t / d$ and $b = y_h / d$, where $y_t$ and $y_h$ are the scaling dimensions of $t$ and $h$ and $d$ is the dimension of space.

## Explanations

### L1 human

The scaling hypothesis says that near a critical point, zooming in on temperature and field together does not change the shape of the free energy.
Only the overall size changes, by a fixed power.
From this single symmetry all the usual power laws follow, and their powers are tied together.
So knowing two exponents is enough to know the others.

### L2 human

A function with $f(\lambda^a t, \lambda^b h) = \lambda f(t, h)$ is called generalized homogeneous.
The data collapse seen in experiments is a test of the hypothesis.
Plotting $m / \abs{t}^{\beta}$ against $h / \abs{t}^{\beta\delta}$ puts all measured curves on two universal curves, one for $t > 0$ and one for $t < 0$.
The hypothesis turns the [[Rushbrooke inequality|BJ8QPXCCF5]] into an equality.
With a matching hypothesis for the correlation length, it also gives the Fisher and Josephson relations.
