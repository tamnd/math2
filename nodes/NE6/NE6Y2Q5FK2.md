---
tag: NE6Y2Q5FK2
kind: definition
name: System identification
msc: [93B30, "93E12"]
defines: EK9DDSWDS6
uses: [6J9MPVHSMF, 0BYTQ4X1HC, 0ZC9YTXZRY]
sources:
  - url: https://en.wikipedia.org/wiki/System_identification
---

## Definition

Let $\Theta \subseteq \R^d$ be a parameter set.
A *model structure* is a family of discrete-time systems $\mathcal{M}(\theta)$, $\theta \in \Theta$.
Each $\mathcal{M}(\theta)$ gives a one-step predictor $\hat{y}(t \mid \theta)$ of the output at time $t$ from the inputs and outputs before time $t$.
Let $u(1), \ldots, u(N)$ and $y(1), \ldots, y(N)$ be measured input and output data of a system.
*System identification* is the selection of a parameter $\hat{\theta} \in \Theta$, and so of a model $\mathcal{M}(\hat{\theta})$, from these data.
In the prediction error method, $\hat{\theta}$ minimises
$$V_N(\theta) = \frac{1}{N} \sum_{t=1}^{N} \norm{y(t) - \hat{y}(t \mid \theta)}^2$$
over $\Theta$.

## Remarks

The ARX structure with orders $n_a, n_b$ is $y(t) + a_1 y(t-1) + \cdots + a_{n_a} y(t - n_a) = b_1 u(t-1) + \cdots + b_{n_b} u(t - n_b) + e(t)$, where $e$ is a noise term.
Its predictor is linear in $\theta = (a_1, \ldots, a_{n_a}, b_1, \ldots, b_{n_b})$, so the prediction error estimate is a [[least squares|0BYTQ4X1HC]] solution $\hat{\theta} = (\Phi^T \Phi)^{-1} \Phi^T Y$, when the regression matrix $\Phi$ has full column [[rank|0ZC9YTXZRY]].

Example: take the structure $\hat{y}(t \mid \theta) = a\, y(t-1) + b\, u(t-1)$ with $\theta = (a, b)$.
Let the data start at time $0$, with $u(0) = 1$, $u(1) = u(2) = 0$, $y(0) = 0$, $y(1) = 1$, $y(2) = 1/2$ and $y(3) = 1/4$.
The regressors $(y(t-1), u(t-1))$ are $(0, 1)$, $(1, 0)$ and $(1/2, 0)$ for $t = 1, 2, 3$.
The matrix with these rows has rank $2$, and $a = 1/2$, $b = 1$ makes every prediction error zero, so $\hat{\theta} = (1/2, 1)$ is the unique minimiser.

Non-example: with the input $u = 0$ and $y(0) = 0$, the output is $y = 0$, every regressor is $(0, 0)$, and every $\theta$ minimises $V_N$.
The data are not informative enough to select a model; the input must be persistently exciting.

Identification also covers the choice of the model structure and the validation of the model on fresh data.
Subspace methods identify a state-space model of a [[linear time-invariant system|6J9MPVHSMF]] directly from Hankel matrices built from the data.
