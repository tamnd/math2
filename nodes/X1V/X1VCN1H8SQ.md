---
tag: X1VCN1H8SQ
kind: statement
role: fact
name: Miner's rule
msc: [74R99, 74A45]
uses: [A8X23QRKVF]
about: [A8X23QRKVF]
sources:
  - url: https://en.wikipedia.org/wiki/Fatigue_(material)
---

## Statement

Let a part be loaded by $k$ blocks of constant-amplitude cycles, with $n_i$ cycles at stress amplitude $\sigma_i$ for $i = 1, \dots, k$.
Let $N_i$ be the [[fatigue|A8X23QRKVF]] life of the part at the amplitude $\sigma_i$ alone.
Miner's rule, also called the Palmgren–Miner linear damage rule, predicts failure when
$$D = \sum_{i=1}^{k} \frac{n_i}{N_i} = 1.$$

## Remarks

The rule assumes that each cycle at amplitude $\sigma_i$ uses up the fraction $1/N_i$ of the life, independently of the order of the cycles and of the damage already present.
It is an engineering hypothesis, not a theorem, and tests show failure at values of $D$ that can be well below or above $1$.
In particular it ignores sequence effects: a high-amplitude block followed by a low-amplitude block usually causes failure at $D < 1$.
Example: let $N_1 = 10^5$ cycles at a high amplitude and $N_2 = 10^6$ cycles at a low amplitude.
If the part has seen $5 \times 10^4$ cycles at the high amplitude, the rule allows $5 \times 10^5$ more cycles at the low amplitude, since $0.5 + 0.5 = 1$.
For random loadings, the cycles are first counted by a method such as rainflow counting and then summed by the rule.

## Explanations

### L1 human

Think of the life of a part as a budget.
Each cycle at a given load spends a fixed share of it, one over the number of cycles the part would last at that load alone.
The rule says that the part breaks when the whole budget is spent.

### L2 human

Miner's rule is the simplest damage accumulation law, used with S–N curves to estimate fatigue life under variable amplitude loading.
It corresponds to a scalar damage variable that grows linearly with cycles, which is a very special case of [[continuum damage mechanics|1272BZTN53]].
Nonlinear damage rules and crack growth laws such as [[Paris' law|YK25SZKXAX]] give more accurate predictions when the loading sequence matters.
