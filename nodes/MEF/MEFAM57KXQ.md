---
tag: MEFAM57KXQ
kind: definition
name: Viterbi algorithm
msc: [94B35, 94B10, 62M05]
defines: 356PTJ3R46
uses: [HJVM390354, R3FXF08WBH, JCFC831VS2]
sources:
  - url: https://en.wikipedia.org/wiki/Viterbi_algorithm
---

## Definition

Let a [[hidden Markov model|HJVM390354]] have a finite state set $S$, initial probabilities $\pi(s)$, transition probabilities $a(s, s')$ and emission probabilities $b(s, y)$.
Here $s, s' \in S$ and $y$ runs over a finite observation alphabet.
Let $y_1, \dots, y_T$ be observations with $T \ge 1$.
The *Viterbi algorithm* computes the following.

1. For every $s \in S$, set $V_1(s) = \pi(s)\, b(s, y_1)$.
2. For $t = 2, \dots, T$ and every $s' \in S$, set $V_t(s') = \max_{s \in S} V_{t-1}(s)\, a(s, s')\, b(s', y_t)$, and let $\mathrm{bp}_t(s')$ be a state $s$ attaining the maximum.
3. Let $\hat s_T$ be a state maximizing $V_T$, and for $t = T, \dots, 2$ set $\hat s_{t-1} = \mathrm{bp}_t(\hat s_t)$.

The output is the state sequence $(\hat s_1, \dots, \hat s_T)$.

## Remarks

By induction on $t$, $V_t(s)$ is the largest joint probability $P(s_1, \dots, s_{t-1}, s_t = s, y_1, \dots, y_t)$ over all state sequences ending in $s$.
So the output maximizes $P(s_1, \dots, s_T \mid y_1, \dots, y_T)$ over all state sequences.
The cost is $O(T \abs{S}^2)$ operations, against $\abs{S}^T$ sequences for a direct search.
In practice one adds logarithms instead of multiplying probabilities.
For a [[convolutional code|JCFC831VS2]] sent over a memoryless channel, the states are the contents of the shift register, and the output is a maximum likelihood codeword sequence.

Example: $S = \set{H, L}$, $\pi(H) = \pi(L) = 1/2$, $a(s, s) = 0.7$ and $a(s, s') = 0.3$ for $s \ne s'$, $b(H, 1) = b(L, 0) = 0.8$ and $b(H, 0) = b(L, 1) = 0.2$, and observations $(1, 0)$.
Then $V_1(H) = 0.4$ and $V_1(L) = 0.1$.
Next $V_2(H) = \max(0.4 \cdot 0.7, 0.1 \cdot 0.3) \cdot 0.2 = 0.056$ and $V_2(L) = \max(0.4 \cdot 0.3, 0.1 \cdot 0.7) \cdot 0.8 = 0.096$, with back-pointer $H$.
The output is $(H, L)$; the four sequences $HH, HL, LH, LL$ have joint probabilities $0.056, 0.096, 0.006, 0.056$, which confirms it.

Non-example: the [[BCJR algorithm|RV2VQVS2YS]] chooses at each time the state that is most likely given all observations.
This maximizes each marginal separately, and the resulting sequence can differ from the Viterbi output.
