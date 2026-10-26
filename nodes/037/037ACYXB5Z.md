---
tag: 037ACYXB5Z
kind: statement
role: lemma
name: Gauss's lemma on quadratic residues
aliases: [gauss-lemma]
msc: [11A15]
uses: [01J8AMV9RS]
sources:
  - url: https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)
    locator: Statement of the lemma
same_as:
  wikidata: Q2526246
  wikipedia: Gauss's lemma (number theory)
---

## Statement

Let $p$ be an odd prime and let $a$ be an integer with $p \nmid a$.
Reduce each of the integers $a, 2a, \dots, \frac{p-1}{2} a$ to its least positive residue modulo $p$.
Let $n$ be the number of these residues that are greater than $p/2$.
Then $\left(\frac{a}{p}\right) = (-1)^n$, where the left side is the [[Legendre symbol|01J8AMV9RS]].

## Remarks

For example, take $p = 7$ and $a = 3$. The residues of $3, 6, 9$ are $3, 6, 2$, and only $6$ is greater than $7/2$. So $\left(\frac{3}{7}\right) = -1$.
With $a = 2$, the lemma gives the [[second supplement to quadratic reciprocity|0ZXW95S44M]].
Gauss used the lemma in one of his proofs of the [[law of quadratic reciprocity|085MJS6907]].

## Explanations

### L1 human

Write the first half of the multiples of $a$ modulo $p$, and count how many land in the upper half of $1, \dots, p - 1$.
An even count means that $a$ is a square modulo $p$, and an odd count means that it is not.
