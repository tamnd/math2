---
tag: RCSXGDTTET
kind: definition
name: Shape derivative
msc: [49Q10, 49Q12]
defines: 9XFEG6ANGM
uses: [1EQM0DJ4NC, 08EVNYZF42, 0XYP2KKSPC]
sources:
  - url: https://en.wikipedia.org/wiki/Shape_optimization
---

## Definition

Let $d \ge 1$ and let $W = W^{1,\infty}(\R^d; \R^d)$ be the Banach space of bounded Lipschitz vector fields $\theta \colon \R^d \to \R^d$, with norm $\norm{\theta}_W = \norm{\theta}_{L^\infty} + \norm{\nabla \theta}_{L^\infty}$.
Let $\mathcal{O}$ be a class of open subsets of $\R^d$, and let $J \colon \mathcal{O} \to \R$ be a shape [[functional|1EQM0DJ4NC]].
Let $\Omega \in \mathcal{O}$ be such that $(\mathrm{Id} + \theta)(\Omega) \in \mathcal{O}$ whenever $\norm{\theta}_W$ is small enough.
Then $J$ is *shape differentiable* at $\Omega$ if the map $\theta \mapsto J((\mathrm{Id} + \theta)(\Omega))$ is [[Fréchet differentiable|08EVNYZF42]] at $\theta = 0$.
Its Fréchet derivative, a bounded linear map $J'(\Omega) \colon W \to \R$, is the *shape derivative* of $J$ at $\Omega$.

## Remarks

For $\norm{\theta}_W < 1$ the map $\mathrm{Id} + \theta$ is a bi-Lipschitz homeomorphism of $\R^d$, so $(\mathrm{Id} + \theta)(\Omega)$ is again open.
Example: the volume $J(\Omega) = \abs{\Omega}$ of a bounded open set.
By the change of variables formula $J((\mathrm{Id} + \theta)(\Omega)) = \int_\Omega \det(I + \nabla \theta) \, dx$.
Since $\det(I + \nabla \theta) = 1 + \operatorname{div} \theta + O(\norm{\nabla\theta}^2)$, the shape derivative is $J'(\Omega)(\theta) = \int_\Omega \operatorname{div} \theta \, dx$.
If $\Omega$ has a $C^1$ boundary with outward unit [[normal vector|0XYP2KKSPC]] $n$, the divergence theorem gives $J'(\Omega)(\theta) = \int_{\partial \Omega} \theta \cdot n \, ds$.
Non-example: $J(\Omega) = \abs{\abs{\Omega} - 1}$ at a set $\Omega$ with $\abs{\Omega} = 1$ is not shape differentiable.
Take $\Omega$ bounded and a smooth function $\chi$ with compact support that equals $1$ on a neighbourhood of $\overline{\Omega}$.
Along $\theta_s(x) = s \chi(x) x$ one gets $(\mathrm{Id} + \theta_s)(\Omega) = (1 + s) \Omega$ and $J = \abs{(1 + s)^d - 1}$, which has a corner at $s = 0$.
For smooth $\Omega$ and smooth $J$, the Hadamard structure theorem gives $J'(\Omega)(\theta) = \int_{\partial \Omega} g \, (\theta \cdot n) \, ds$ for a function $g$ on $\partial \Omega$, the shape gradient.
