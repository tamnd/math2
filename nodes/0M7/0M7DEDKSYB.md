---
tag: 0M7DEDKSYB
kind: statement
role: theorem
name: Euler's criterion
msc: [11A15]
uses: [01J8AMV9RS, 0M25PRN3WQ]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_criterion
    locator: lead section
same_as:
  wikidata: Q2346904
  wikipedia: Euler's criterion
---

## Statement

Let $p$ be an odd prime and let $a$ be an integer.
Then
$$a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod p,$$
where $\left(\frac{a}{p}\right)$ is the [[Legendre symbol|01J8AMV9RS]].

## Remarks

So for $p \nmid a$, the integer $a$ is a quadratic residue modulo $p$ if and only if $a^{(p-1)/2} \equiv 1 \pmod p$.
For example, $3^3 = 27 \equiv -1 \pmod 7$, so $3$ is a quadratic nonresidue modulo $7$.
The proof uses [[Fermat's little theorem|0M25PRN3WQ]]: $x = a^{(p-1)/2}$ satisfies $x^2 \equiv 1$, so $x \equiv \pm 1 \pmod p$.
A consequence is the [[multiplicativity of the Legendre symbol|0NW1JP7TBR]].

## History

Leonhard Euler found the criterion.

## Explanations

### L1 human

To test whether $a$ is a square modulo $p$, raise $a$ to the power $(p-1)/2$.
The result is $1$ for a square and $-1$ for a non-square, modulo $p$.
With [[fast modular exponentiation|04DR5PM25N]], this test is quick even for large $p$.
