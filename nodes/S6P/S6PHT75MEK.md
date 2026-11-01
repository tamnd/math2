---
tag: S6PHT75MEK
kind: statement
role: theorem
name: Unique factorization of ideals in a Dedekind domain
msc: [13F05, 11R04, 13A15]
uses: [7NPY2CN5KB, 096Z9MP2ME, 00MHHZ9SNE, 0670T59HGE, H20P600HQS, 0PV74TR5FP, E190TAV2S6]
about: [7NPY2CN5KB, 096Z9MP2ME]
sources:
  - url: https://en.wikipedia.org/wiki/Dedekind_domain
---

## Statement

Let $R$ be a [[Dedekind domain|7NPY2CN5KB]], that is, a [[Noetherian|0670T59HGE]] [[integrally closed domain|H20P600HQS]] in which every nonzero [[prime ideal|00MHHZ9SNE]] is [[maximal|0PV74TR5FP]].
Let $I$ be a nonzero [[ideal|096Z9MP2ME]] of $R$ with $I \ne R$.
Then there are distinct nonzero prime ideals $P_1, \ldots, P_r$ and integers $e_1, \ldots, e_r \ge 1$ with
$$I = P_1^{e_1} P_2^{e_2} \cdots P_r^{e_r}.$$
The primes $P_i$ and exponents $e_i$ are unique up to the order of the factors.

## Remarks

One proof shows first that every nonzero ideal contains a product of nonzero primes, using the Noetherian condition.
Then it shows that every nonzero prime $P$ is [[invertible|E190TAV2S6]]: there is a fractional ideal $P^{-1}$ with $P P^{-1} = R$; here integral closedness and dimension $1$ are used.
Dividing $I$ by a prime that contains it gives a strictly larger ideal, and the Noetherian condition ends the process.
Uniqueness follows by cancelling invertible primes, since $P \supseteq P_1 \cdots P_r$ forces $P = P_i$ for some $i$.

Example: in $R = \Z[\sqrt{-5}]$, the element $6$ factors in two ways as $2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5})$, so $R$ is not a [[UFD|0W4X9G6263]].
With $P = (2, 1 + \sqrt{-5})$, $Q = (3, 1 + \sqrt{-5})$ and $Q' = (3, 1 - \sqrt{-5})$, one has $P^2 = (2)$ and $Q Q' = (3)$, so $(6) = P^2 Q Q'$, and the two factorizations of $6$ come from regrouping these prime ideals.

Conversely, an integral domain in which every nonzero proper ideal is a product of prime ideals is a Dedekind domain.
The dimension hypothesis is needed: $k[x, y]$ over a field $k$ is Noetherian and integrally closed, but it has dimension $2$.
In it, the only prime ideal that contains $(x, y^2)$ is $(x, y)$, and no power of $(x, y)$ equals $(x, y^2)$, so $(x, y^2)$ is not a product of prime ideals.

## Explanations

### L1 human

In many rings of algebraic numbers, numbers do not factor uniquely into primes.
Dedekind's idea was to factor ideals instead of numbers.
In a Dedekind domain, every ideal splits into prime ideals in exactly one way, just as every integer splits into prime numbers.
This rescues unique factorization for all rings of integers of number fields.

### L2 human

The theorem shows that the nonzero fractional ideals of a Dedekind domain form a free abelian group with the nonzero prime ideals as a basis.
The quotient by the principal fractional ideals is the [[ideal class group|WQ46BD3ARY]], which measures how far $R$ is from being a [[principal ideal domain|0CMD0BCH8T]].
Locally, the exponent $e_i$ is the valuation of $I$ in the [[discrete valuation ring|MGM3CNJW9V]] $R_{P_i}$.
In number theory, the factorization of $pR$ for a prime number $p$ describes how $p$ splits in the number field.
