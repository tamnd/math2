---
tag: CFCNGMEFEG
kind: example
name: The inconsistent logic is superintuitionistic but not intermediate
msc: ["03B55"]
topics: [38EQ20GR7M]
audience: research
not_instance_of:
  - target: H5NSKEP3P2
    note: the set of all formulas is closed under modus ponens and substitution and contains IPC, but it is not contained in classical logic
uses: [H5NSKEP3P2, DP4WNWHXXA]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_logic
    locator: Definition
---

## Example

Let $\mathsf{For}$ be the set of all propositional formulas.
We check that it is superintuitionistic and not an [[intermediate logic|H5NSKEP3P2]].

1. $\mathsf{For}$ contains every theorem of $\mathsf{IPC}$.
2. It is closed under modus ponens and substitution, since every formula is in it.
3. So $\mathsf{For}$ is a superintuitionistic logic.
4. It contains $\bot$, which is not a classical tautology. So $\mathsf{For} \not\subseteq \mathsf{CPC}$, and $\mathsf{For}$ is not intermediate.
5. It is the only superintuitionistic logic that is not intermediate, by [[the maximality of classical logic|DP4WNWHXXA]].

## Remarks

In the Russian literature, "superintuitionistic logic" includes $\mathsf{For}$, while "intermediate logic" excludes it.
Counts and lattices of logics differ by one element depending on the convention.
For example, the lattice of superintuitionistic logics has top $\mathsf{For}$ and unique coatom $\mathsf{CPC}$, while the lattice of intermediate logics has top $\mathsf{CPC}$.
In algebraic terms, $\mathsf{For}$ corresponds to the trivial variety of one-element Heyting algebras.

## Explanations

### L1 human

The set of all formulas satisfies every closure condition of a logic.
But it proves everything, including contradictions.
So it is not between intuitionistic and classical logic: it lies above classical logic.

### L2 human

1. Check the closure conditions: $\mathsf{IPC}$, modus ponens, substitution.
2. Check the upper bound: is every formula a classical tautology?
3. For $\mathsf{For}$, step 1 passes, and step 2 fails at $\bot$.

The typical use is to keep track of the two conventions in results that count logics.
A trap: a theorem stated for all superintuitionistic logics may need a separate check for $\mathsf{For}$, and counts may differ by one.
