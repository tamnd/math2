---
tag: 7RAH6V0C5R
kind: definition
name: Regular prime
msc: [11R18, 11R29]
defines: B4VK33PCXZ
uses: [01826KMG2H, NN77VYSGXR, KTKK9B1X41, 0KC00K7KY4, 0Y5X3SDBCZ, 0YV2CKP2AV]
sources:
  - url: https://en.wikipedia.org/wiki/Regular_prime
---

## Definition

Let $p$ be an odd [[prime number|01826KMG2H]], and let $\zeta_p$ be a primitive $p$-th [[root of unity|0YV2CKP2AV]].
The prime $p$ is *regular* if $p$ does not divide the [[class number|KTKK9B1X41]] of the [[cyclotomic field|NN77VYSGXR]] $\Q(\zeta_p)$.
Otherwise $p$ is *irregular*.

## Remarks

Kummer's criterion gives an equivalent form: $p$ is regular if and only if $p$ does not divide the numerator of any of the [[Bernoulli numbers|0KC00K7KY4]] $B_k$ for $k = 2, 4, \ldots, p - 3$.
Kummer proved that if $p$ is regular, then $x^p + y^p = z^p$ has no solution in positive integers, the regular case of [[Fermat's Last Theorem|0Y5X3SDBCZ]].
It is known that there are infinitely many irregular primes.
Whether there are infinitely many regular primes is an open question.

Example: $p = 5$ is regular.
By the criterion, only $B_2 = \frac{1}{6}$ needs checking, and $5$ does not divide its numerator $1$; in fact $\Q(\zeta_5)$ has class number $1$.

Non-example: $p = 37$ is irregular.
The numerator of $B_{32}$ is divisible by $37$, and $32 \le 37 - 3$; equivalently, $37$ divides the class number of $\Q(\zeta_{37})$.
