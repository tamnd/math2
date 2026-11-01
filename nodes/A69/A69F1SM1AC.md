---
tag: A69F1SM1AC
kind: definition
name: Continuous-time Markov chain
msc: [60J27]
defines: TWQFE0FZZS
uses: [0QH5ENKZM1, 0F462493EA, 0B77KZCQ51, 0E99F51GVB, 020M04FN1H, 01APZ8GDQH, VPA41PWRR1]
sources:
  - url: https://en.wikipedia.org/wiki/Continuous-time_Markov_chain
---

## Definition

Let $S$ be a countable set.
A *time-homogeneous continuous-time Markov chain* on $S$ is a [[stochastic process|0QH5ENKZM1]] $(X_t)_{t \ge 0}$ with values in $S$ and right-continuous paths that has the following property.
There are [[transition matrices|0F462493EA]] $P(t) = (p_{ij}(t))_{i, j \in S}$, $t \ge 0$, such that, for all $n \ge 0$, all times $0 \le t_0 < t_1 < \cdots < t_{n+1}$ and all states $i_0, \ldots, i_{n+1} \in S$ with $P(X_{t_0} = i_0, \ldots, X_{t_n} = i_n) > 0$,
$$P(X_{t_{n+1}} = i_{n+1} \mid X_{t_0} = i_0, \ldots, X_{t_n} = i_n) = p_{i_n i_{n+1}}(t_{n+1} - t_n).$$

## Remarks

The condition is the [[Markov property|0B77KZCQ51]] in continuous time, and it implies the [[Chapman–Kolmogorov equation|01APZ8GDQH]] $P(s + t) = P(s) P(t)$.
For a finite $S$ there is a rate matrix $Q = P'(0)$, the [[generator|VPA41PWRR1]], with $q_{ij} \ge 0$ for $i \ne j$ and zero row sums, and $P(t) = e^{tQ}$ is a [[matrix exponential|020M04FN1H]].
The chain stays in state $i$ for an [[exponential|0E99F51GVB]] time with rate $q_i = -q_{ii}$, then jumps to $j \ne i$ with probability $q_{ij}/q_i$, when $q_i > 0$.
Example: the Poisson process of rate $\lambda > 0$ is a chain on $\N$ with $q_{i, i+1} = \lambda$ and $q_{ii} = -\lambda$, and $p_{ij}(t) = e^{-\lambda t} (\lambda t)^{j-i} / (j-i)!$ for $j \ge i$.
Non-example: a process on $\Z$ that moves up by $1$ at the times $1, 2, 3, \ldots$ is not time-homogeneous.
Indeed $P(X_{t+1/2} = X_t + 1)$ is $1$ for $t = 3/4$ and $0$ for $t = 1/4$, so no single $P(1/2)$ works.
