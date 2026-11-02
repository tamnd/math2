---
tag: DN5G4NAF95
kind: definition
name: Computable set
msc: [03D25, 03D20]
defines: PPGD5KW8JC
uses: [KZSB5E471K, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Computable_set
---

## Definition

Let $A \subseteq \N$ be a [[subset|0BJR9QR08E]] of the natural numbers.
The characteristic function of $A$ is $\chi_A \colon \N \to \set{0, 1}$, with $\chi_A(n) = 1$ if $n \in A$ and $\chi_A(n) = 0$ if $n \notin A$.
The set $A$ is *computable*, or *recursive*, or *decidable*, if $\chi_A$ is a total [[computable function|KZSB5E471K]].
The same definition applies to subsets of $\N^k$.

## Remarks

Example: the set of prime numbers is computable.
A machine can test $n \ge 2$ for divisors $d$ with $2 \le d < n$, which takes finitely many steps, and so computes $\chi_A$.

Non-example: the set $K = \set{e : \text{program } e \text{ halts on input } e}$ is not computable, by the undecidability of the [[halting problem|Z7TN2B35B0]].
Its characteristic function is total but not computable.

A set $A$ is computable if and only if both $A$ and $\N \setminus A$ are [[computably enumerable|TN9G24VABN]].
The computable sets are closed under union, intersection and complement.
