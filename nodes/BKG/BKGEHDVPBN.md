---
tag: BKGEHDVPBN
kind: statement
role: theorem
name: Luce's choice axiom
msc: ["91E10", 91B08]
uses: [0DVDCMA2DK]
sources:
  - url: https://en.wikipedia.org/wiki/Luce's_choice_axiom
same_as:
  wikidata: Q6696419
  wikipedia: Luce's choice axiom
---

## Statement

Let $U$ be a finite set of alternatives.
For each nonempty $S \subseteq U$, let $P(\cdot \mid S)$ be a [[probability distribution|0DVDCMA2DK]] on $S$.
Here $P(i \mid S)$ is the probability of choosing $i$ when the offered set is $S$.
Write $P(R \mid S) = \sum_{i \in R} P(i \mid S)$ for $R \subseteq S$.
Assume $P(i \mid S) > 0$ for all $i \in S \subseteq U$.
*Luce's choice axiom* is the condition
$$P(i \mid T) = P(i \mid S) \, P(S \mid T) \quad \text{for all } i \in S \subseteq T \subseteq U.$$
The axiom holds if and only if some numbers $w_i > 0$, $i \in U$, satisfy
$$P(i \mid S) = \frac{w_i}{\sum_{j \in S} w_j} \quad \text{for all } i \in S \subseteq U.$$
These numbers are unique up to a common positive factor.

## Remarks

For the forward direction put $w_i = P(i \mid U)$; the axiom with $T = U$ gives $P(i \mid S) = w_i / P(S \mid U) = w_i / \sum_{j \in S} w_j$.
Conversely, the formula gives $P(i \mid S) P(S \mid T) = \frac{w_i}{\sum_{S} w_j} \cdot \frac{\sum_{S} w_j}{\sum_{T} w_j} = P(i \mid T)$.
Uniqueness: $w_i / w_j = P(i \mid U)/P(j \mid U)$ is determined by the choice probabilities.
Example: weights $w = (1, 2, 3)$ on $\set{a, b, c}$ give $P(a \mid U) = 1/6$ and $P(a \mid \set{a, b}) = 1/3$, and indeed $1/6 = (1/3)(3/6)$.
A consequence is independence of irrelevant alternatives: $P(i \mid S)/P(j \mid S)$ does not depend on $S$.
The red bus and blue bus example shows that real choices can violate it, when two alternatives are near copies of each other.

## Explanations

### L1 human

The axiom says that a choice can be described by giving each option a fixed strength.
The chance of picking an option is its strength divided by the total strength of the options on the table.
Adding or removing other options rescales all chances, but never changes how two options compare to each other.

### L2 human

R. Duncan Luce stated the axiom in his 1959 book on individual choice behavior.
With $w_i = e^{u_i}$ the formula is the multinomial logit model, which is also obtained from random utility models with independent Gumbel noise.
For two alternatives it is the Bradley–Terry model of paired comparisons, close to the [[law of comparative judgment|NE54WYCWBR]], which uses normal noise instead.
