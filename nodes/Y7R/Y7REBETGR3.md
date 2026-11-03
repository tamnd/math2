---
tag: Y7REBETGR3
kind: conjecture
name: Vandiver's conjecture and K-theory of the integers
msc: ["11R18", "11R29", "19D50"]
uses: [NN77VYSGXR, KTKK9B1X41, B4VK33PCXZ, 4HXFKW55WJ]
about: [NN77VYSGXR, 4HXFKW55WJ]
sources:
  - url: https://en.wikipedia.org/wiki/Kummer–Vandiver_conjecture
history:
  posed_by: Ernst Kummer
  first_stated: "1849"
---

## Statement

For a prime $p$, let $\zeta_p$ be a primitive $p$-th root of unity.
Let $\Q(\zeta_p)^+ = \Q(\zeta_p + \zeta_p^{-1})$ be the maximal real subfield of the [[cyclotomic field|NN77VYSGXR]] $\Q(\zeta_p)$, and let $h_p^+$ be its [[class number|KTKK9B1X41]].
The conjecture states that $p$ does not divide $h_p^+$ for every prime $p$.
In terms of K-theory, it is equivalent to the statement that the [[K-groups|4HXFKW55WJ]] $K_{4n}(\Z)$ vanish for all $n \ge 1$.

## Remarks

The conjecture is often called the Kummer–Vandiver conjecture: Kummer raised it in letters to Kronecker, and Vandiver later studied it and promoted it.
The equivalence with the vanishing of $K_{4n}(\Z)$ for all $n \ge 1$ was shown by Kurihara.
It has been checked by computer for all primes below $2^{31}$.
The vanishing of $K_4(\Z)$ is a theorem of Rognes.

For [[regular primes|B4VK33PCXZ]], that is, primes $p$ that do not divide the class number of $\Q(\zeta_p)$, the conjecture holds for $p$, since $h_p^+$ divides that class number.

## Explanations

### L1 human

Cyclotomic fields are obtained by adding roots of unity to the rational numbers, and their class numbers measure how far unique factorization fails.
Kummer and Vandiver predicted that the real part of the $p$-th cyclotomic field never has class number divisible by $p$.
Surprisingly, the same statement can be phrased as the vanishing of the K-groups of the integers in degrees divisible by $4$.
So a classical question about cyclotomic fields is also a question about the algebraic K-theory of $\Z$.
