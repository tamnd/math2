---
tag: A6GX2K5YFB
kind: example
name: Curie–Weiss model
msc: [82B20, 82B26]
instance_of: [PAEME5EQRM]
uses: [R0KGM32QN6, 1DGJYHG10E]
sources:
  - url: https://en.wikipedia.org/wiki/Curie%E2%80%93Weiss_law
---

## Example

Let $N \ge 1$, $J > 0$, $h \in \R$, and let $\beta \ge 0$ be the inverse temperature.
A configuration is $\sigma = (\sigma_1, \dots, \sigma_N) \in \set{-1, +1}^N$.
Its energy is
$$H_N(\sigma) = -\frac{J}{2N} \sum_{i, j = 1}^{N} \sigma_i \sigma_j - h \sum_{i=1}^{N} \sigma_i.$$
The *Curie–Weiss model* is the probability measure on $\set{-1, +1}^N$ proportional to $e^{-\beta H_N(\sigma)}$.
It is the [[Ising model|R0KGM32QN6]] on the complete graph, with the coupling scaled by $1/N$.

## Remarks

The energy depends on $\sigma$ only through the magnetization $m_N = \frac{1}{N} \sum_i \sigma_i$, since $H_N = -N (J m_N^2 / 2 + h m_N)$.
This makes the free energy computable exactly as $N \to \infty$.
The limit magnetization solves the equation $m = \tanh(\beta (J m + h))$.
For $h = 0$ this equation has only the solution $m = 0$ when $\beta J \le 1$, and two further solutions $\pm m^* \ne 0$ when $\beta J > 1$.
So the critical point is $\beta_c = 1/J$, and below the critical temperature the magnetization concentrates near $\pm m^*$.
It is the model behind [[mean-field theory|1DGJYHG10E]], and its critical exponents are the mean-field ones.

## Explanations

### L1 human

Imagine a magnet where every spin feels every other spin equally, no matter how far away.
Then each spin only feels the average magnetization, and the whole problem reduces to one equation for that average.
This is the simplest model with a phase transition that one can solve completely.
