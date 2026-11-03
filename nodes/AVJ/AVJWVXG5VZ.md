---
tag: AVJWVXG5VZ
kind: definition
name: Infinite sites model
msc: [92D10, 92D20]
defines: 13AS2R963M
uses: [2W8Y2Y1C8J, 0XB9GQTN9G]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_sites_model
---

## Definition

Let a sample of DNA sequences have a genealogy, a rooted tree with branch lengths measured in time, as in [[coalescent theory|2W8Y2Y1C8J]].
The *infinite sites model* is the following mutation model:

1. The number of mutations on a branch of length $t$ has the [[Poisson distribution|0XB9GQTN9G]] with mean $\mu t$. Here $\mu > 0$ is the mutation rate, and distinct branches are independent.
2. Each mutation occurs at a site of the sequence where no other mutation has occurred in the history of the sample.
3. A leaf sequence carries the new state at a site exactly when the mutation there lies on its path from the root.

A site is *segregating* in the sample when the sampled sequences do not all have the same state there.

## Remarks

Example: let two sampled sequences have their common ancestor $T$ time units ago.
The number of sites at which they differ is Poisson with mean $2\mu T$, since each mutation on either branch gives one difference by clauses 2 and 3.
Non-example: the Jukes–Cantor model on a finite sequence allows two mutations at one site, which can hide each other, so clause 2 fails.
Under the model, the number $S$ of segregating sites equals the total number of mutations on the genealogy.
