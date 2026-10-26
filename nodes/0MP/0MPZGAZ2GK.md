---
tag: 0MPZGAZ2GK
kind: definition
name: Centre of mass
msc: [26B15]
defines: 0HNK6KT05K
uses: [0GTBGMZXV8, 0NKBMFC18R]
sources:
  - url: https://en.wikipedia.org/wiki/Center_of_mass
    locator: A continuous distribution of mass
  - url: https://en.wikipedia.org/wiki/Center_of_mass
    locator: A system of particles
---

## Definition

Let $E \subseteq \mathbb{R}^n$ be a bounded Jordan measurable set, and let $\delta \colon E \to [0, \infty)$ be a continuous density with total mass $M = \int_E \delta(x) \, dx > 0$.
The centre of mass of $E$ with density $\delta$ is the point $\bar{x} = (\bar{x}_1, \dots, \bar{x}_n)$ with
$$\bar{x}_i = \frac{1}{M} \int_E x_i \, \delta(x) \, dx, \qquad i = 1, \dots, n.$$
If $\delta$ is constant, $\bar{x}$ is the centroid of $E$, and it does not depend on the value of the constant.

## Remarks

For $n = 3$ the integrals are [[triple integrals|0GTBGMZXV8]], and for a plane lamina, $n = 2$, they are [[double integrals|0NKBMFC18R]].
For point masses $m_1, \dots, m_k$ at $p_1, \dots, p_k$, the centre of mass is $\sum_j m_j p_j / \sum_j m_j$. The definition above replaces the sum by an integral.
Example: the half disc $\{x^2 + y^2 \le a^2, \ y \ge 0\}$ with constant density has centroid $(0, 4a / (3\pi))$.
If $E$ and $\delta$ are symmetric under a reflection, then $\bar{x}$ lies in the mirror of that reflection.

## Explanations

### L1 human

The centre of mass is the balance point of a body.
If the body is supported at that point, gravity does not turn it in any direction.
