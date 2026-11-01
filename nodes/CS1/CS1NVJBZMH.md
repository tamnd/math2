---
tag: CS1NVJBZMH
kind: statement
role: theorem
name: Modularity theorem
msc: [11G05, 11F11, 11F80]
uses: [427N6S6QQW, GWKN5VG78A, A50Y012RBP, 1H6R856P3C, S4SV3QZ8B1, 0ZXZ82FTX2]
about: [427N6S6QQW, GWKN5VG78A]
sources:
  - url: https://en.wikipedia.org/wiki/Modularity_theorem
same_as:
  wikidata: Q649469
  wikipedia: Modularity theorem
---

## Statement

Let $E$ be an [[elliptic curve|427N6S6QQW]] over $\Q$ with conductor $N$, a positive integer whose prime factors are the primes where $E$ has bad reduction.
For each prime $p \nmid N$, let $\tilde{E}$ be the reduction modulo $p$ of a minimal Weierstrass model of $E$.
It is a curve over the [[finite field|0ZXZ82FTX2]] $\F_p$; let $a_p = p + 1 - \# \tilde{E}(\F_p)$.
Then there is a [[cusp form|A50Y012RBP]] $f(\tau) = \sum_{n \ge 1} b_n q^n$, with $q = e^{2\pi i \tau}$, of weight $2$ for the [[congruence subgroup|1H6R856P3C]] $\Gamma_0(N)$, such that:

1. $f$ is a normalised newform: $b_1 = 1$ and $f$ is an eigenform of all [[Hecke operators|S4SV3QZ8B1]] that does not come from a lower level;
2. $b_n \in \Z$ for all $n$;
3. $b_p = a_p$ for every prime $p \nmid N$.

## Remarks

Equivalently, the $L$-function of $E$ equals the $L$-function of $f$, or there is a nonconstant morphism $X_0(N) \to E$ defined over $\Q$ from the modular curve $X_0(N)$.
Wiles, with a key step completed jointly with Taylor, proved the theorem for semistable curves in 1995; Breuil, Conrad, Diamond and Taylor completed the general case in 2001.
The proof shows that the $\ell$-adic [[Galois representation|JQEYEQJY2G]] of $E$ is modular.
It lifts the modularity of the reduction modulo $3$, known by the Langlands–Tunnell theorem, with a modularity lifting theorem.
A switch to the prime $5$ handles the cases where the reduction modulo $3$ is not irreducible.
Example: $y^2 + y = x^3 - x^2$ has conductor $11$, and it corresponds to $f = q \prod_{n \ge 1} (1 - q^n)^2 (1 - q^{11n})^2$.
The semistable case, combined with the earlier work of Frey, Serre and Ribet, implies Fermat's Last Theorem.

## Explanations

### L1 human

Counting the points of an elliptic curve modulo each prime produces a list of numbers.
The theorem says that this list always appears as the coefficients of a very symmetric function, a modular form.
It was known as the Taniyama–Shimura–Weil conjecture before its proof.

### L2 human

Modularity gives the analytic continuation and functional equation of $L(E, s)$, which are needed even to state the [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]].
The parametrisation $X_0(N) \to E$ lets one construct [[Heegner points|2230ZKE4W9]] on $E$, the input of the [[Gross–Zagier theorem|BX558DTV2D]].
It is a case of the reciprocity conjectures of the [[Langlands program|J9T2M084W5]].
