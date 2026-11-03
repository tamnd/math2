---
tag: MF4DYZ4YAX
kind: statement
role: fact
name: Born rule
msc: ["81P15", "81P16", "46N50"]
uses: [V1JTB52E8C, DF5RN297GE, 4NQN47A92F, ATGT25E5FF, 18KPYRRPZY, Z2CP530WDE, 059TJN0NZ1, JNK7GJ3AKE]
about: [DF5RN297GE, 4NQN47A92F]
sources:
  - url: https://en.wikipedia.org/wiki/Born_rule
same_as:
  wikidata: Q894014
  wikipedia: Born rule
---

## Statement

Let $\mathcal{H}$ be a complex Hilbert space, and let $\rho$ be a [[density operator|V1JTB52E8C]] on $\mathcal{H}$.
Let $A$ be an [[observable|DF5RN297GE]] on $\mathcal{H}$ with [[projection-valued measure|ATGT25E5FF]] $P^A$ on the Borel sets of $\R$.
Then
$$\mu(B) = \operatorname{tr}\big(\rho\, P^A(B)\big), \qquad B \subseteq \R \text{ Borel},$$
is a [[probability measure|059TJN0NZ1]] on $\R$ with $\mu(\sigma(A)) = 1$.
The Born rule is the postulate that $\mu$ is the probability distribution of the result of a measurement of $A$ in the [[state|4NQN47A92F]] $\rho$.
For a pure state with unit vector $\psi$, $\mu(B) = \norm{P^A(B)\psi}^2$.
If moreover $A$ has an orthonormal basis of eigenvectors $e_1, e_2, \dots$ with eigenvalues $\lambda_1, \lambda_2, \dots$, then the probability of the result $\lambda$ is $\sum_{k \,:\, \lambda_k = \lambda} \abs{\ip{e_k}{\psi}}^2$.

## Remarks

Each $P^A(B)$ is an orthogonal projection, so $\operatorname{tr}(\rho P^A(B)) = \operatorname{tr}(\rho^{1/2} P^A(B) \rho^{1/2}) \ge 0$, and $\mu(\R) = \operatorname{tr}\rho = 1$.
Countable additivity follows from that of $P^A$: write $\rho = \sum_k p_k \lvert e_k \rangle\langle e_k \rvert$, so $\mu(B) = \sum_k p_k \norm{P^A(B) e_k}^2$, a convex combination of probability measures.
The support statement holds because $P^A(\R \setminus \sigma(A)) = 0$.
If $\psi \in D(A)$, the mean of $\mu$ is the [[expectation value|JNK7GJ3AKE]] $\ip{\psi}{A\psi}$.

Example: on $\C^2$, let $\sigma_z = \mathrm{diag}(1, -1)$ with eigenvectors $e_1 = (1, 0)$, $e_2 = (0, 1)$, and let $\psi = (\cos\theta, e^{i\varphi}\sin\theta)$.
The result $1$ has probability $\abs{\ip{e_1}{\psi}}^2 = \cos^2\theta$ and the result $-1$ has probability $\sin^2\theta$; the phase $\varphi$ does not enter.

The rule was proposed by Max Born in 1926.
It is a postulate of the theory, not a theorem; within the theory, Gleason's theorem shows that the trace form is the only possible one in dimension at least $3$.

## Explanations

### L1 human

The Born rule turns the state of a quantum system into probabilities of measurement results.
For a state vector, the chance of a result is the squared length of the part of the vector that lies in the eigenspace of that result.
It is the bridge between the mathematics of Hilbert spaces and what one sees in a laboratory.

### L2 human

The rule combines two pieces of the formalism: the spectral measure of the observable, which splits the Hilbert space by measured value, and the state, which weighs the pieces.
The mean of the resulting distribution is the expectation value $\operatorname{tr}(\rho A)$, and its variance is the quantity in the uncertainty relations.
For a position measurement on $L^2(\R)$, the spectral projection of $B$ is multiplication by the indicator of $B$, and the rule gives $\int_B \abs{\psi(x)}^2 \, dx$, the usual reading of the wave function.
Generalised measurements replace the projection-valued measure by a positive operator-valued measure, with the same trace formula.
