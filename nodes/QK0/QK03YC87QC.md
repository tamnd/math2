---
tag: QK03YC87QC
kind: definition
name: Randomization
msc: [62K99]
defines: 734Q6Q51X7
uses: [2TE42ZWJ3E, 0QB913WM5E]
sources:
  - url: https://en.wikipedia.org/wiki/Randomization
---

## Definition

Let $T$ be a finite set of treatments, let $U$ be a set of $n$ experimental units, and let $r_t \ge 1$ be integers with $\sum_{t \in T} r_t = n$.
Let $\mathcal{D}$ be the set of [[experimental designs|2TE42ZWJ3E]] $d \colon U \to T$ with $\abs{d^{-1}(t)} = r_t$ for every $t \in T$.
*Complete randomization* is the choice of a design $D$ at random from $\mathcal{D}$ with the uniform [[distribution|0QB913WM5E]], that is,
$$P(D = d) = \frac{1}{\abs{\mathcal{D}}} = \frac{\prod_{t \in T} r_t!}{n!} \quad \text{for every } d \in \mathcal{D}.$$
More generally, a *randomized design* is a design chosen at random from a set of designs by a known probability distribution.
In a restricted randomization the set is smaller, for example the designs that give every treatment once in each block.

## Remarks

Example: $T = \set{A, B}$, $U = \set{1, 2, 3, 4}$ and $r_A = r_B = 2$.
Then $\abs{\mathcal{D}} = 4!/(2!\,2!) = 6$, and each of the six splits, such as $\set{1, 2}$ to $A$ and $\set{3, 4}$ to $B$, has probability $1/6$.
Each unit receives $A$ with probability $1/2$.

Non-example: giving $A$ to the first two units to arrive and $B$ to the next two is a fixed rule, not a chance mechanism.
If early arrivals differ from late ones, the comparison of $A$ and $B$ is biased.

Fix the observed responses and compute a test statistic for every design in $\mathcal{D}$.
Under the hypothesis of no treatment effect, these values give the exact null distribution of a randomization test.
