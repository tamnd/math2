---
tag: 76VV1TE4JS
kind: definition
name: Modified Newtonian dynamics
msc: [83D05, 85A05]
defines: 321A9E6GM7
uses: [29WRN5J730, DWK5N5SKTK]
sources:
  - url: https://en.wikipedia.org/wiki/Modified_Newtonian_dynamics
---

## Definition

Fix a constant $a_0 > 0$ with the dimension of an acceleration.
Fix a continuous increasing function $\mu \colon [0, \infty) \to [0, 1]$, the interpolating function.
Assume $\mu(x) \to 1$ as $x \to \infty$ and $\mu(x) / x \to 1$ as $x \to 0$.
Let $\mathbf{g}_N$ be the gravitational acceleration at a point given by [[Newton's law of gravitation|29WRN5J730]] from the visible mass.
*Modified Newtonian dynamics* (MOND) is the rule that the true acceleration $\mathbf{a}$ of a test body there satisfies
$$\mu\!\left( \frac{\abs{\mathbf{a}}}{a_0} \right) \mathbf{a} = \mathbf{g}_N.$$

## Remarks

Example: when $\abs{\mathbf{a}} \gg a_0$, $\mu \approx 1$ and $\mathbf{a} \approx \mathbf{g}_N$, so Newton's law is recovered.
When $\abs{\mathbf{a}} \ll a_0$ (the deep-MOND regime), $\mu(x) \approx x$ gives $\abs{\mathbf{a}}^2 = a_0 \abs{\mathbf{g}_N}$.
For a point mass $M$ this gives $\abs{\mathbf{a}} = \sqrt{G M a_0} / r$, and a circular orbit has speed $v$ with $v^4 = G M a_0$, independent of $r$.
Non-example: the choice $\mu \equiv 1$ is not allowed, because it fails the condition $\mu(x)/x \to 1$; it gives back pure Newtonian gravity.
Common choices are $\mu(x) = x / (1 + x)$ and $\mu(x) = x / \sqrt{1 + x^2}$.
The rule above is not derived from a potential and does not conserve momentum in general; the field version of Bekenstein and Milgrom (1984) replaces [[Poisson's equation|DWK5N5SKTK]] by $\nabla \cdot \left[ \mu(\abs{\nabla \Phi}/a_0) \nabla \Phi \right] = 4 \pi G \rho$.
