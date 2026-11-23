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

Let $\mathcal{N} = (\mathbb{N}, \mathcal{P}(\mathbb{N}))$ be the [[full model|CAA7K3VF59]].
Treat it as a one-sorted structure, with a unary predicate for numbers, a unary predicate for sets, and the symbols of [[L2|Y92NXGEQBD]].
We check that there is a countable family $\mathcal{S}$ such that $(\mathbb{N}, \mathcal{S})$ is a [[β-model|J0Z2GNJZ2W]].

1. The language is countable, so by the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]] $\mathcal{N}$ has a countable elementary substructure $\mathcal{M}$.
2. Each natural number $k$ is the value of a closed term: $0$, or $1 + \cdots + 1$ with $k$ summands.
   A substructure contains the values of all closed terms, so the number part of $\mathcal{M}$ is all of $\mathbb{N}$.
3. The set part of $\mathcal{M}$ is a countable family $\mathcal{S} \subseteq \mathcal{P}(\mathbb{N})$, and membership in $\mathcal{M}$ is true membership.
   So $\mathcal{M} = (\mathbb{N}, \mathcal{S})$, and $\mathcal{M}$ is an $\omega$-model.
4. Let $\varphi$ be a $\Sigma^1_1$ formula with parameters from $\mathcal{S}$.
   In the one-sorted language, its set quantifier is relativized to the predicate for sets.
   By elementarity, $\mathcal{M} \models \varphi$ if and only if $\mathcal{N} \models \varphi$.
5. Truth in $\mathcal{N}$ is truth about all subsets of $\mathbb{N}$, so $\mathcal{M}$ is correct about $\varphi$.
   Thus $\mathcal{M}$ is a β-model.

## Remarks

Step 4 holds for all formulas of $L_2$, not only for $\Sigma^1_1$ formulas.
So $\mathcal{M}$ is a model of full second-order arithmetic $\mathsf{Z}_2$, and it is correct about every formula with parameters from $\mathcal{S}$.
This is much more than a β-model needs.

The proof is not effective.
The family $\mathcal{S}$ contains sets of high complexity, since it must contain a witness for each true $\Sigma^1_1$ sentence with parameters in $\mathcal{S}$.
In particular it contains Kleene's O, which is defined in $\mathcal{N}$ by a formula without parameters.

Watch out: step 2 is what makes $\mathcal{M}$ an $\omega$-model.
A countable model of $\mathsf{Z}_2$ built in another way, for example by the compactness theorem, may have nonstandard numbers and then is not an $\omega$-model at all.

## Explanations

### L1 human

The full model has uncountably many sets, but a countable part of it can still give the right answer to every question with set quantifiers.
Such a countable part is a β-model.
The Löwenheim-Skolem theorem chooses the countable part, by adding witnesses for every true existential statement.

### L2 human

The argument gives countable β-models, but not coded ones that a weak system can see.
To prove inside $\mathsf{ACA}_0$ that every set lies in a countable coded β-model needs [[Π¹₁-CA0|T21WETAHN5]], by the equivalence for β-models.
Every β-model contains every hyperarithmetical set, so no countable β-model is close to the computable sets.
