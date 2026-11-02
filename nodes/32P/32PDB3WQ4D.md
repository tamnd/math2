---
tag: 32PDB3WQ4D
kind: concept
name: Interpretation of varieties
msc: [08B05]
sources:
  - url: https://en.wikipedia.org/wiki/Interpretation_(model_theory)
---

## Summary

An interpretation of a [[variety|AJNZJD8442]] $\mathcal{V}$ in a variety $\mathcal{W}$ translates each basic operation of $\mathcal{V}$ into a term of $\mathcal{W}$.
The translation must turn every algebra of $\mathcal{W}$ into an algebra of $\mathcal{V}$ on the same set.
Interpretations order varieties by strength: if $\mathcal{V}$ is interpretable in $\mathcal{W}$, then $\mathcal{W}$ is at least as rich as $\mathcal{V}$.
Suppose $\mathcal{V}$ is interpretable in $\mathcal{W}$ and $\mathcal{V}$ has terms that satisfy some identities.
Then the translated terms of $\mathcal{W}$ satisfy the same identities, so such properties pass from $\mathcal{V}$ to $\mathcal{W}$.

## Explanations

### L1 human

Every ring can be seen as an abelian group by forgetting the multiplication.
More generally, one variety can sit inside another when its operations can be written as formulas in the operations of the other.
For example, in a Boolean ring the formula $x + y + xy$ behaves like the join of a Boolean algebra.
An interpretation records such a choice of formulas, one for each operation.
