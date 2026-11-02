---
tag: 3TERJ5C8QK
kind: statement
role: theorem
name: Characterization of Shannon entropy
msc: [94A17, 39B22]
uses: [0DVDCMA2DK, 0X3WGX95FE, SRAN4EKWS0]
about: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Entropy_(information_theory)
---

## Statement

For each integer $n \ge 2$, let $\Delta_n$ be the set of probability vectors $(p_1, \dots, p_n)$ with $p_i \ge 0$ and $p_1 + \cdots + p_n = 1$.
Let $H$ be a function defined on $\bigcup_{n \ge 2} \Delta_n$ with real values.
Assume:

1. The function $p \mapsto H(p, 1 - p)$ is [[continuous|0X3WGX95FE]] on $[0, 1]$.
2. $H$ is symmetric: $H(p_1, \dots, p_n)$ does not change when the $p_i$ are permuted.
3. $H(\frac{1}{2}, \frac{1}{2}) = 1$.
4. For all $n \ge 2$, all $(p_1, \dots, p_n) \in \Delta_n$ with $p_n > 0$, and all $q_1, q_2 \ge 0$ with $q_1 + q_2 = p_n$,
$$H(p_1, \dots, p_{n-1}, q_1, q_2) = H(p_1, \dots, p_n) + p_n \, H\left(\frac{q_1}{p_n}, \frac{q_2}{p_n}\right).$$

Then for every $n \ge 2$ and every $(p_1, \dots, p_n) \in \Delta_n$,
$$H(p_1, \dots, p_n) = -\sum_{i=1}^{n} p_i \log_2 p_i,$$
with the convention $0 \log_2 0 = 0$.
Conversely, this function has properties 1 to 4.

## Remarks

The formula is the Shannon entropy of a finite [[probability distribution|0DVDCMA2DK]], measured in bits.
This set of axioms is due to Faddeev; Shannon and Khinchin gave earlier characterizations with stronger hypotheses.
The proof first studies $F(n) = H(\frac{1}{n}, \dots, \frac{1}{n})$: property 4 gives $F(mn) = F(m) + F(n)$, and the remaining properties force $F(n) = \log_2 n$.
Grouping equal masses then gives the formula for rational probabilities, and continuity extends it to all probability vectors.
The normalization 3 only fixes the unit; without it, $H$ is a constant multiple $c$ of the Shannon entropy.

## Explanations

### L1 human

Entropy measures how uncertain the outcome of a random experiment is.
This theorem says that once one asks for a few natural rules, there is only one possible formula.
The first rule says that small changes of the probabilities give small changes of the uncertainty.
The other rules say that the order of the outcomes does not matter, that a fair coin carries one bit, and that uncertainty can be computed in stages.
The last rule says that splitting one outcome into two adds the uncertainty of the split, weighted by the probability of that outcome.

### L2 human

The theorem is a solution of a [[functional equation|SRAN4EKWS0]]: setting $f(p) = H(p, 1 - p)$, the properties reduce to the fundamental equation of information $f(x) + (1 - x) f\left(\frac{y}{1 - x}\right) = f(y) + (1 - y) f\left(\frac{x}{1 - y}\right)$ for $x, y \in [0, 1)$ with $x + y \le 1$.
It explains why the logarithm, and no other function, appears in the entropy formula.
Dropping or changing the recursivity axiom leads to other entropies, such as the Rényi entropies.
Similar axiomatic characterizations exist for relative entropy and mutual information.
