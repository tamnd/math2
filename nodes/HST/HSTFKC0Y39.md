---
tag: HSTFKC0Y39
kind: definition
name: Fisher information
msc: [62B10, 62F10]
defines: G1Z3WSTE8Q
uses: [MSC0MR8VMH, CP97GRVTQ0, 0WQNRCNY3M, 0477R9PYAE, 05AQE0QR0D]
sources:
  - url: https://en.wikipedia.org/wiki/Fisher_information
---

## Definition

Let $\set{f(\cdot\,; \theta) : \theta \in \Theta}$ be a [[parametric family|MSC0MR8VMH]] of densities with respect to a fixed measure, where $\Theta \subseteq \R$ is an open interval.
Assume that $\theta \mapsto \log f(x; \theta)$ is differentiable for every $x$ with $f(x; \theta) > 0$.
Let $X$ have density $f(\cdot\,; \theta)$, and let
$$s(\theta; X) = \frac{\partial}{\partial \theta} \log f(X; \theta)$$
be the [[score|CP97GRVTQ0]].
The *Fisher information* at $\theta$ is
$$I(\theta) = E_\theta\big[ s(\theta; X)^2 \big] \in [0, \infty].$$
For $\Theta \subseteq \R^d$ open, the *Fisher information matrix* is the $d \times d$ matrix with entries $I_{ij}(\theta) = E_\theta[ s_i(\theta; X) \, s_j(\theta; X) ]$, where $s_i = \partial \log f / \partial \theta_i$.

## Remarks

Under the usual regularity conditions, differentiation under the integral sign gives $E_\theta[s(\theta; X)] = 0$.
Then $I(\theta) = \operatorname{Var}_\theta(s(\theta; X))$, the [[variance|0477R9PYAE]] of the score.
If moreover $\log f$ is twice differentiable, then $I(\theta) = -E_\theta\big[\partial^2_\theta \log f(X; \theta)\big]$.
For $n$ independent observations with the same density, the information is $n I(\theta)$.

Example: let $X$ be [[normal|05AQE0QR0D]] with mean $\theta$ and known variance $\sigma^2$.
Then $\log f(x; \theta) = -(x - \theta)^2 / (2\sigma^2) + c$, so $s = (X - \theta)/\sigma^2$.
Hence $I(\theta) = E_\theta[(X - \theta)^2] / \sigma^4 = 1/\sigma^2$.

Non-example of the regular behaviour: the uniform densities $f(x; \theta) = 1/\theta$ on $(0, \theta)$.
Here $s = -1/\theta$ wherever it is defined, so $E_\theta[s^2] = 1/\theta^2$, but $E_\theta[s] = -1/\theta \ne 0$.
The support depends on $\theta$, differentiation under the integral fails, and the usual properties of $I(\theta)$ do not hold.
