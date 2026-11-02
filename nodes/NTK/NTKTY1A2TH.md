---
tag: NTKTY1A2TH
kind: definition
name: Jeffreys prior
msc: [62F15]
defines: 18MMYZ7922
uses: [Q0DXKAQXE1, 00NBBSXRQS, G1Z3WSTE8Q, 0C3CFHDN6R]
sources:
  - url: https://en.wikipedia.org/wiki/Jeffreys_prior
---

## Definition

Let $\set{f(\cdot \mid \theta) : \theta \in \Theta}$ be a [[parametric model|Q0DXKAQXE1]] with $\Theta \subseteq \R^k$ open, regular enough that its [[Fisher information|G1Z3WSTE8Q]] matrix $I(\theta)$ exists for every $\theta \in \Theta$.
The *Jeffreys prior* is the [[prior|00NBBSXRQS]] on $\Theta$ with density with respect to Lebesgue measure
$$\pi(\theta) \propto \sqrt{\det I(\theta)},$$
where $\det$ is the [[determinant|0C3CFHDN6R]].
If $\int_\Theta \sqrt{\det I(\theta)} \, d\theta = \infty$, it is an improper prior, used only when the resulting posterior is proper.

## Remarks

Example: for one Bernoulli observation with chance $p \in (0, 1)$, $I(p) = 1/(p(1 - p))$.
So the Jeffreys prior is proportional to $p^{-1/2}(1 - p)^{-1/2}$, which is the proper distribution $\mathrm{Beta}(1/2, 1/2)$.
For the mean $\mu$ of $\mathcal{N}(\mu, \sigma^2)$ with $\sigma$ known, $I(\mu) = 1/\sigma^2$ is constant, so the Jeffreys prior is the improper flat prior on $\R$.
For the scale $\sigma > 0$ of $\mathcal{N}(0, \sigma^2)$, $I(\sigma) = 2/\sigma^2$, so the Jeffreys prior is proportional to $1/\sigma$.
Invariance: let $\varphi = h(\theta)$ for a smooth bijection $h$ with smooth inverse.
Then the Jeffreys prior computed in the parameter $\varphi$ is the image of the Jeffreys prior in $\theta$.
The reason is that $\det I$ is multiplied by the square of the Jacobian determinant of the change of variables.
Non-example: the flat prior on $p \in (0, 1)$ is not the Jeffreys prior of the Bernoulli model, since its density $1$ is not proportional to $p^{-1/2}(1 - p)^{-1/2}$.
