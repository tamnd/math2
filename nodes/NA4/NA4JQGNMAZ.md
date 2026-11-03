---
tag: NA4JQGNMAZ
kind: statement
role: theorem
name: Price equation
msc: [92D15]
uses: [0KBFAWYRTE, 0WQNRCNY3M]
about: [0KBFAWYRTE]
sources:
  - url: https://en.wikipedia.org/wiki/Price_equation
same_as:
  wikidata: Q2109459
  wikipedia: Price equation
---

## Statement

Let a parent population consist of $n$ individuals $i = 1, \dots, n$.
Let $z_i \in \R$ be the trait value of individual $i$ and let $w_i \ge 0$ be its number of offspring, with mean $\bar w = \frac1n \sum_i w_i > 0$.
For each $i$ with $w_i > 0$, let $z_i'$ be the mean trait value of the offspring of $i$, and put $\Delta z_i = z_i' - z_i$; put $\Delta z_i = 0$ when $w_i = 0$.
Let $\bar z = \frac1n \sum_i z_i$ be the parent mean and $\bar z' = \sum_i w_i z_i' \big/ \sum_i w_i$ the offspring mean, and $\Delta \bar z = \bar z' - \bar z$.
Then
$$\bar w \, \Delta \bar z = \operatorname{Cov}(w, z) + \operatorname{E}(w \, \Delta z),$$
where $\operatorname{Cov}(w, z) = \frac1n \sum_i w_i z_i - \bar w \bar z$ is the [[covariance|0KBFAWYRTE]] and $\operatorname{E}(w \Delta z) = \frac1n \sum_i w_i \Delta z_i$ is the [[mean|0WQNRCNY3M]], both taken over the parents with equal weights.

## Remarks

The proof is algebra.
Since $\bar w \bar z' = \frac1n \sum_i w_i z_i' = \frac1n \sum_i w_i z_i + \frac1n \sum_i w_i \Delta z_i$, subtracting $\bar w \bar z$ from both sides gives the identity.
The covariance term is the change due to selection: individuals with a larger trait leave more offspring when $\operatorname{Cov}(w, z) > 0$.
The second term is the change due to transmission, such as mutation or meiotic drive; it vanishes when offspring resemble their parents on average.
For example, take two parents with $z = (0, 1)$, $w = (1, 3)$ and faithful transmission; then $\bar z = 1/2$, $\bar z' = 3/4$, $\bar w = 2$, and $\operatorname{Cov}(w, z) = \frac12 (0 + 3) - 2 \cdot \frac12 = \frac12 = \bar w \Delta \bar z$.

## Explanations

### L1 human

The Price equation splits the change of the average of a trait from one generation to the next into two parts.
One part comes from selection: parents with some trait values have more children than others.
The other part comes from transmission: children may differ from their parents.
It holds for any population and any trait, because it is just a rearrangement of sums.

### L2 human

Because it is an identity, the Price equation makes no claim about biology by itself; its value is in organising arguments.
Applied to fitness as the trait, the covariance term gives the selective part of Fisher's fundamental theorem.
Writing fitness as a linear regression on genetic values of an individual and its social partners leads to Hamilton's rule.
The term $\operatorname{E}(w \Delta z)$ can itself be expanded by the same equation at a lower level, which gives multilevel selection formulas.
