---
tag: 0J0QEN1DZR
kind: definition
name: Reduced residue system
aliases: [reduced-system-of-residues]
msc: [11A07]
defines: 0HV01NH20W
uses: [0QRV8FPK5M, 0GFKP8F8AG]
sources:
  - url: https://en.wikipedia.org/wiki/Reduced_residue_system
    locator: lead section
inventory: [AWWMCWBCZE]
---

## Definition

Let $n$ be a positive integer.
A reduced residue system modulo $n$ is a set $R$ of integers with these properties.
Each element of $R$ is [[coprime|0GFKP8F8AG]] to $n$.
No two distinct elements of $R$ are congruent modulo $n$.
Each integer coprime to $n$ is congruent modulo $n$ to some element of $R$.

## Remarks

Thus $R$ contains exactly one element of each [[residue class|0QRV8FPK5M]] of integers coprime to $n$. It has $\varphi(n)$ elements, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].
For example, $\{1, 5, 7, 11\}$ is a reduced residue system modulo $12$.
If $R$ is a reduced residue system modulo $n$ and $\gcd(a, n) = 1$, then $\{ a r : r \in R \}$ is also a reduced residue system modulo $n$. This fact gives a proof of [[Euler's theorem|0VC4DVE7DQ]].

## Explanations

### L1 human

Take a [[complete residue system|0E22JKS4W4]] modulo $n$, and keep only the numbers with no common factor with $n$.
For $n = 10$, the numbers $0, 1, \dots, 9$ give the reduced residue system $\{1, 3, 7, 9\}$.
