---
tag: M630WA0XXG
kind: statement
role: theorem
name: Oja's rule
msc: [92B20, 68T05, 62H25]
uses: [VQZVSFF179, 0V7G6WMFK0, 0VR671PHE5, 0N6960W0BV, 0BQAA2BK3Q, 0NT64JV96A]
about: [VQZVSFF179, ABXD13M340]
sources:
  - url: https://en.wikipedia.org/wiki/Oja%27s_rule
same_as:
  wikidata: Q7081581
  wikipedia: Oja's rule
---

## Statement

Let $C$ be a real symmetric positive definite $n \times n$ matrix, the [[covariance matrix|0V7G6WMFK0]] of a zero-mean input $x \in \R^n$.
Assume that the largest [[eigenvalue|0BQAA2BK3Q]] $\lambda_1$ of $C$ is simple, and let $c_1$ be a unit [[eigenvector|0N6960W0BV]] for $\lambda_1$.
*Oja's rule* is the update $\Delta w = \eta\, y\, (x - y\, w)$ with $y = w^T x$, and its averaged form is the [[ordinary differential equation|0NT64JV96A]]
$$\frac{dw}{dt} = C w - (w^T C w)\, w.$$
If $w(0) \in \R^n$ satisfies $w(0)^T c_1 \ne 0$, then the solution $w(t)$ exists for all $t \ge 0$ and converges, as $t \to \infty$, to $c_1$ if $w(0)^T c_1 > 0$ and to $-c_1$ if $w(0)^T c_1 < 0$.

## Remarks

The rule is the [[Hebbian rule|VQZVSFF179]] $\eta\, y\, x$ plus a decay term $-\eta\, y^2 w$ that keeps the weight norm bounded.
Along solutions, $\frac{d}{dt} \norm{w}^2 = 2\, (w^T C w)(1 - \norm{w}^2)$, so $\norm{w}$ tends to $1$ when $w \ne 0$.
Writing $w$ in an orthonormal eigenbasis $c_1, \dots, c_n$ of $C$, the ratios $w_k / w_1$ of coordinates satisfy $\frac{d}{dt}(w_k / w_1) = (\lambda_k - \lambda_1)(w_k / w_1)$, so they decay to $0$, and the sign of $w_1$ never changes.
So a single linear neuron with this rule extracts the first principal component of its input, which links the rule to [[principal component analysis|ABXD13M340]].
If $\lambda_1$ is not simple and $w(0)$ is not orthogonal to the top eigenspace, $w(t)$ still tends to a unit vector of that eigenspace, but which one depends on $w(0)$.
For the stochastic rule, convergence with probability one holds under conditions on the learning rates such as $\sum \eta_t = \infty$ and $\sum \eta_t^2 < \infty$, by stochastic approximation.

## Explanations

### L1 human

Plain Hebbian learning makes weights grow without limit.
Oja added a forgetting term that is larger when the output is larger, so the weight vector keeps unit length.
The result is that the neuron learns the single direction in which its inputs vary the most.

### L2 human

The averaged equation is a gradient-like flow on the unit sphere for the Rayleigh quotient $w^T C w / w^T w$, whose maximum is $\lambda_1$ at $\pm c_1$.
The other unit eigenvectors are equilibria too, but they are unstable.
Generalisations such as Sanger's rule extract several principal components with several output neurons.
