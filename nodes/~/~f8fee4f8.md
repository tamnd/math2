---
tag: ~f8fee4f8
kind: definition
name: Fermat pseudoprime
msc: [11A51]
defines: ~9b1c44a5
uses: [~def9c278, ~e79e2431, ~1160e18b]
sources:
  - url: https://en.wikipedia.org/wiki/Fermat_pseudoprime
    locator: Definition
---

## Definition

Let $a$ be an integer with $a > 1$.
A Fermat pseudoprime to the base $a$ is a [[composite number|~def9c278]] $n$ such that $a^{n-1} \equiv 1 \pmod n$.

## Remarks

[[Fermat's little theorem|~1160e18b]] says that each prime $n$ with $n \nmid a$ satisfies $a^{n-1} \equiv 1 \pmod n$. A Fermat pseudoprime is a composite number that passes the same test.
The smallest Fermat pseudoprime to the base $2$ is $341 = 11 \cdot 31$.
The condition implies $\gcd(a, n) = 1$.
A composite number that is a Fermat pseudoprime to each base coprime to it is a [[Carmichael number|~4ea6a78e]].

## Explanations

### L1 human

The [[Fermat primality test|~f72cc8b3]] declares $n$ "probably prime" when $a^{n-1} \equiv 1 \pmod n$.
A Fermat pseudoprime is a composite number that fools this test for the base $a$.
For example, $2^{340} \equiv 1 \pmod{341}$, but $341$ is not prime.
