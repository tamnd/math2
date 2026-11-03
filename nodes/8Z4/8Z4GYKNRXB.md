---
tag: 8Z4GYKNRXB
kind: definition
name: Blahut–Arimoto algorithm
msc: [94A40, 94A34, 94A24]
defines: PPH99S8MKV
uses: [J7MZ2XQP9M, B9C5RBFATB, PQBW43X5RE, 9DMSG5HAQX, 4JN2Z9DH4Y, A83CYGDXFG]
sources:
  - url: https://en.wikipedia.org/wiki/Blahut%E2%80%93Arimoto_algorithm
---

## Definition

Let $W$ be a discrete memoryless [[channel|B9C5RBFATB]] with finite input alphabet $\mathcal{X}$, finite output alphabet $\mathcal{Y}$ and transition probabilities $W(y \mid x)$.
For a probability vector $q$ on $\mathcal{Y}$ and $x \in \mathcal{X}$, let $D_x(q) = \sum_{y} W(y \mid x) \ln \frac{W(y \mid x)}{q(y)}$ be the [[Kullback–Leibler divergence|PQBW43X5RE]] of $W(\cdot \mid x)$ from $q$.
The *Blahut–Arimoto algorithm* for the capacity of $W$ starts from a probability vector $p_0$ on $\mathcal{X}$ with $p_0(x) > 0$ for all $x$.
For $t = 0, 1, 2, \dots$ it computes
$$q_t(y) = \sum_{x} p_t(x) W(y \mid x), \qquad p_{t+1}(x) = \frac{p_t(x)\, e^{D_x(q_t)}}{\sum_{x'} p_t(x')\, e^{D_{x'}(q_t)}}.$$

## Remarks

Let $C$ be the [[capacity|J7MZ2XQP9M]] of $W$ in nats and $I(p_t)$ the [[mutual information|A83CYGDXFG]] between input and output when the input has law $p_t$.
Then $I(p_t) \le C \le \max_x D_x(q_t)$ for every $t$, and $I(p_t) \to C$ as $t \to \infty$.
The two bounds give a stopping rule for the [[algorithm|9DMSG5HAQX]].
Example: for the binary symmetric channel with crossover probability $\varepsilon$, start with the uniform $p_0$.
Then $q_0$ is uniform, and $D_0(q_0) = D_1(q_0) = \ln 2 - h(\varepsilon)$, with $h$ the binary entropy in nats.
So $p_1 = p_0$, and the bounds meet: $C = \ln 2 - h(\varepsilon)$.
Non-example: a start $p_0$ with $p_0(x) = 0$ for some $x$ is not allowed.
The update keeps $p_t(x) = 0$ for all $t$, so the iteration cannot reach a capacity-achieving law that uses $x$.
A similar alternating iteration computes the [[rate–distortion function|4JN2Z9DH4Y]] for each slope of the curve.
