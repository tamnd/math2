---
tag: MZXJDE7M7K
kind: example
name: A countable elementary substructure of the full model is a β-model
msc: ["03B30", "03C62"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [J0Z2GNJZ2W]
uses: [J0Z2GNJZ2W, CAA7K3VF59, 484M0TZ1S7, Y92NXGEQBD]
sources:
  - url: https://en.wikipedia.org/wiki/Löwenheim–Skolem_theorem
    locator: Downward part
  - url: https://en.wikipedia.org/wiki/Beta-model
    locator: In analysis
---

## Example

Let $\mathcal{N} = (\N, \mathcal{P}(\N))$ be the [[full model|CAA7K3VF59]].
Treat it as a one-sorted structure, with a unary predicate for numbers, a unary predicate for sets, and the symbols of [[L2|Y92NXGEQBD]].
The claim is that there is a countable family $\mathcal{S}$ such that $(\N, \mathcal{S})$ is a [[β-model|J0Z2GNJZ2W]].

1. The language is countable, so by the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] $\mathcal{N}$ has a countable elementary substructure $\mathcal{M}$.
2. Each natural number $k$ is the value of the closed term $1 + \cdots + 1$ with $k$ summands, or of $0$. A substructure contains the values of all closed terms, so the number part of $\mathcal{M}$ is all of $\N$.
3. So $\mathcal{M} = (\N, \mathcal{S})$ for a countable family $\mathcal{S} \subseteq \mathcal{P}(\N)$, and $\mathcal{M}$ is an $\omega$-model.
4. Let $\varphi$ be a $\Sigma^1_1$ formula with parameters from $\mathcal{S}$. By elementarity, $\mathcal{M} \models \varphi$ if and only if $\mathcal{N} \models \varphi$.
5. Truth in $\mathcal{N}$ is truth about all subsets of $\N$, so $\mathcal{M}$ is correct about $\varphi$. Thus $\mathcal{M}$ is a β-model.

## Remarks

Step 4 holds for all formulas of $L_2$, not only for $\Sigma^1_1$ formulas.
So $\mathcal{M}$ is a model of $\mathsf{Z}_2$, and it is correct about every formula with parameters from $\mathcal{S}$.
The proof is not effective: $\mathcal{S}$ contains sets of high complexity, since $\mathcal{S}$ must contain a witness for each true $\Sigma^1_1$ sentence with parameters in $\mathcal{S}$.

## Explanations

### L1 human

The full model has uncountably many sets, but a countable part of it can still give the right answer to every question with set quantifiers.
Such a countable part is a β-model.
