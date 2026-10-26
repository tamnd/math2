---
tag: 0XSDBCP4RZ
kind: statement
role: lemma
name: Eisenstein's lemma
msc: [11A15]
uses: [01J8AMV9RS, 037ACYXB5Z]
sources:
  - url: https://en.wikipedia.org/wiki/Proofs_of_quadratic_reciprocity
    locator: Eisenstein's proof
---

## Statement

Let $p$ be an odd prime and let $a$ be a positive integer with $p \nmid a$.
Then
$$\left(\frac{a}{p}\right) = (-1)^{\sum_{u} \lfloor a u / p \rfloor},$$
where the sum runs over the even integers $u = 2, 4, \dots, p - 1$, and $\left(\frac{a}{p}\right)$ is the [[Legendre symbol|01J8AMV9RS]].

## Remarks

For example, take $p = 7$ and $a = 3$. The sum is $\lfloor 6/7 \rfloor + \lfloor 12/7 \rfloor + \lfloor 18/7 \rfloor = 0 + 1 + 2 = 3$, so $\left(\frac{3}{7}\right) = -1$.
A common variant holds for odd $a$: then $\left(\frac{a}{p}\right) = (-1)^{\sum_{k=1}^{(p-1)/2} \lfloor k a / p \rfloor}$.
The proof is similar to the proof of [[Gauss's lemma|037ACYXB5Z]].
Eisenstein used the lemma in a proof of [[quadratic reciprocity|085MJS6907]] that counts lattice points in a triangle.

## Explanations

### L1 human

The lemma turns the question "is $a$ a square modulo $p$?" into a count of integer parts of fractions.
The parity of the count gives the answer.
