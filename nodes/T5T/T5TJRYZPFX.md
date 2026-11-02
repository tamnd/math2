---
tag: T5TJRYZPFX
kind: definition
name: Baum–Welch algorithm
msc: [62M05, 62F10]
defines: W7P6CCSMX7
uses: [HJVM390354, 11N1AXSXYK, 0VW9E4QXR6, 0990W5PN13]
sources:
  - url: https://en.wikipedia.org/wiki/Baum–Welch_algorithm
---

## Definition

Consider a [[hidden Markov model|HJVM390354]] with hidden states $\set{1, \dots, N}$ and observation symbols $\set{1, \dots, M}$.
Its parameter $\theta = (\pi, A, B)$ consists of an initial distribution $\pi_i$, a transition matrix $a_{ij}$ and emission probabilities $b_i(k)$.
Let $y_1, \dots, y_T$ with $T \ge 2$ be an observed sequence.

For the current $\theta$, the forward and backward variables are
$$\alpha_t(i) = P_\theta(Y_1 = y_1, \dots, Y_t = y_t, X_t = i), \qquad \beta_t(i) = P_\theta(Y_{t+1} = y_{t+1}, \dots, Y_T = y_T \mid X_t = i),$$
computed by $\alpha_1(i) = \pi_i b_i(y_1)$, $\alpha_{t+1}(j) = \sum_i \alpha_t(i) a_{ij} b_j(y_{t+1})$, $\beta_T(i) = 1$ and $\beta_t(i) = \sum_j a_{ij} b_j(y_{t+1}) \beta_{t+1}(j)$.
With $L = \sum_i \alpha_T(i)$, set
$$\gamma_t(i) = \frac{\alpha_t(i) \beta_t(i)}{L}, \qquad \xi_t(i, j) = \frac{\alpha_t(i) a_{ij} b_j(y_{t+1}) \beta_{t+1}(j)}{L}.$$
The *Baum–Welch algorithm* repeats the following update until the [[likelihood|0VW9E4QXR6]] $L$ stops changing:
$$\pi_i \leftarrow \gamma_1(i), \qquad a_{ij} \leftarrow \frac{\sum_{t=1}^{T-1} \xi_t(i, j)}{\sum_{t=1}^{T-1} \gamma_t(i)}, \qquad b_i(k) \leftarrow \frac{\sum_{t \,:\, y_t = k} \gamma_t(i)}{\sum_{t=1}^{T} \gamma_t(i)}.$$

## Remarks

Here $\gamma_t(i)$ is the [[conditional probability|0990W5PN13]] that $X_t = i$ given the observations, and $\xi_t(i, j)$ is the conditional probability that $X_t = i$ and $X_{t+1} = j$.
The update is one step of the [[expectation–maximization algorithm|11N1AXSXYK]], so the likelihood never decreases from one iteration to the next.
It may converge to a local maximum rather than to the global maximum, so several starting points are often used.

Example: with $N = 1$ every $\gamma_t(1)$ equals $1$, and the update gives $b_1(k) = \#\set{t : y_t = k} / T$.
This is the observed frequency of symbol $k$, which is the maximum likelihood estimate in that case.

Non-example: the Viterbi algorithm uses the same model but returns the single most likely hidden path for fixed parameters.
It does not update $\theta$, so it is not the Baum–Welch algorithm.
