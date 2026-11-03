---
tag: MT4F76XFRQ
kind: definition
name: BCJR algorithm
msc: [94B35, 94B10, 62M05]
defines: RV2VQVS2YS
uses: [HJVM390354, 0KJ7ZS8AJA, 0G48PYM96Q]
sources:
  - url: https://en.wikipedia.org/wiki/BCJR_algorithm
---

## Definition

Let a [[hidden Markov model|HJVM390354]] have a finite state set $S$, initial probabilities $\pi(s)$, transition probabilities $a(s, s')$ and emission probabilities $b(s, y)$.
Let $y_1, \dots, y_T$ be observations with $T \ge 1$.
For $t \ge 2$ put $\gamma_t(s, s') = a(s, s')\, b(s', y_t)$.
The *BCJR algorithm* computes the following.

1. Forward pass: $\alpha_1(s) = \pi(s)\, b(s, y_1)$, and $\alpha_t(s') = \sum_{s \in S} \alpha_{t-1}(s)\, \gamma_t(s, s')$ for $t = 2, \dots, T$.
2. Backward pass: $\beta_T(s) = 1$, and $\beta_{t-1}(s) = \sum_{s' \in S} \gamma_t(s, s')\, \beta_t(s')$ for $t = T, \dots, 2$.
3. Output, for each $t$ and each pair of states, $\sigma_t(s, s') = \alpha_{t-1}(s)\, \gamma_t(s, s')\, \beta_t(s')$ and $\lambda_t(s) = \alpha_t(s)\, \beta_t(s)$.

## Remarks

One has $\alpha_t(s) = P(y_1, \dots, y_t, s_t = s)$ and $\beta_t(s) = P(y_{t+1}, \dots, y_T \mid s_t = s)$.
Hence $\lambda_t(s) = P(s_t = s, y_1, \dots, y_T)$ and $\sigma_t(s, s') = P(s_{t-1} = s, s_t = s', y_1, \dots, y_T)$, and dividing by $P(y_1, \dots, y_T) = \sum_s \alpha_T(s)$ gives the [[posterior probabilities|0KJ7ZS8AJA]].
For a code trellis, each transition carries an input bit.
Summing $\sigma_t$ over the transitions with input $0$, and with input $1$, gives the posterior probability of each bit.
This yields the bitwise maximum a posteriori decision.
The cost is $O(T \abs{S}^2)$ operations.

Example: $S = \set{H, L}$, $\pi(H) = \pi(L) = 1/2$, $a(s, s) = 0.7$, $a(s, s') = 0.3$ for $s \ne s'$, $b(H, 1) = b(L, 0) = 0.8$, $b(H, 0) = b(L, 1) = 0.2$, observations $(1, 0)$.
Then $\alpha_1(H) = 0.4$, $\alpha_1(L) = 0.1$, $\alpha_2(H) = 0.4 \cdot 0.14 + 0.1 \cdot 0.06 = 0.062$ and $\alpha_2(L) = 0.4 \cdot 0.24 + 0.1 \cdot 0.56 = 0.152$.
So $P(y) = 0.214$ and $P(s_2 = L \mid y) = 0.152 / 0.214 \approx 0.71$.

Non-example: replacing the sums in the forward pass by maxima and adding back-pointers gives the [[Viterbi algorithm|356PTJ3R46]], which returns the most likely state sequence and not the posterior probabilities.
