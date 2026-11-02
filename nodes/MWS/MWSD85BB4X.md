---
tag: MWSD85BB4X
kind: definition
name: Computably enumerable set
msc: [03D25]
defines: TN9G24VABN
uses: [KZSB5E471K, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Computably_enumerable_set
---

## Definition

Let $A \subseteq \N$ be a [[subset|0BJR9QR08E]] of the natural numbers.
The set $A$ is *computably enumerable*, or *recursively enumerable*, if $A$ is the domain of a partial [[computable function|KZSB5E471K]] $f \colon \N \rightharpoonup \N$.
That is, $A = \set{n \in \N : f(n) \text{ is defined}}$.

## Remarks

The following conditions on $A \subseteq \N$ are equivalent.

1. $A$ is computably enumerable.
2. $A$ is empty or the range of a total computable function $\N \to \N$.
3. There is a computable set $R \subseteq \N^2$ such that $A = \set{n : \exists m \, (n, m) \in R}$.

Example: the halting set $K = \set{e : \text{program } e \text{ halts on input } e}$ is computably enumerable.
It is the domain of the partial computable function that, on input $e$, runs program $e$ on input $e$ and then outputs $0$.

Non-example: the complement $\N \setminus K$ is not computably enumerable.
Otherwise $K$ and its complement would both be computably enumerable, and then $K$ would be [[computable|PPGD5KW8JC]], which is false.
