---
tag: 07HXA8KV6F
kind: statement
role: theorem
name: Pépin's test
msc: [11Y11]
uses: [0R03B54V4Z, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/P%C3%A9pin%27s_test
    locator: Description of the test
same_as:
  wikidata: Q1779493
  wikipedia: Pépin's test
---

## Statement

Let $n$ be a positive integer and let $F_n = 2^{2^n} + 1$ be the [[Fermat number|0R03B54V4Z]].
Then $F_n$ is prime if and only if
$$3^{(F_n - 1)/2} \equiv -1 \pmod{F_n}.$$

## Remarks

For example, $F_1 = 5$ and $3^2 = 9 \equiv -1 \pmod 5$.
The power can be computed by $2^n - 1$ squarings with [[modular exponentiation|04DR5PM25N]].
The "only if" part follows from [[Euler's criterion|0M7DEDKSYB]] and quadratic reciprocity, since $3$ is a nonresidue modulo $F_n$.

## History

The test is named after Théophile Pépin.

## Explanations

### L1 human

Pépin's test decides whether a Fermat number is prime with one large modular power.
The Fermat numbers grow so fast that the test is practical only for small $n$.
