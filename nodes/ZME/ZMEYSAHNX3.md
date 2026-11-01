---
tag: ZMEYSAHNX3
kind: statement
role: theorem
name: Banach–Zarecki theorem
msc: [26A46, 26A45]
uses: [ZT6F4C2YHK, A8251BHCMP, WMHMGJD261, 0P27W9RW0G]
about: [ZT6F4C2YHK, WMHMGJD261]
sources:
  - url: https://en.wikipedia.org/wiki/Luzin_N_property
---

## Statement

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a function.
Then $f$ is [[absolutely continuous|ZT6F4C2YHK]] on $[a, b]$ if and only if the following three conditions hold:

1. $f$ is [[continuous|0P27W9RW0G]] on $[a, b]$;
2. $f$ has [[bounded variation|A8251BHCMP]] on $[a, b]$;
3. $f$ has the [[Luzin N property|WMHMGJD261]].

## Remarks

An absolutely continuous function is continuous and of bounded variation, and covering a null set by small open intervals shows that it has the N property.
For the converse, one shows that if $f$ is differentiable at every point of a measurable set $E$, then the outer measure of $f(E)$ is at most $\int_E \abs{f'}$.
The N property handles the null set where $f'$ fails to exist, and this controls the changes of $f$ over families of short intervals.
No one condition can be dropped.
The [[Cantor function|NPBYYK63FE]] is continuous and monotone but fails the N property.
The function $x \sin(1/x)$ on $[0, 1]$ is continuous with the N property, being smooth away from $0$, but it does not have bounded variation.
A step function is monotone and maps every set to a finite set, but it is not continuous.

## Explanations

### L1 human

The theorem splits absolute continuity into three simpler conditions.
The function must not jump, must not wiggle infinitely much, and must not spread a set of length zero over a set of positive length.

### L2 human

The theorem explains exactly what goes wrong with the [[Cantor function|NPBYYK63FE]] and other [[singular functions|P5AWRD2793]]: they are continuous and monotone, so only the N property can fail.
It is often used to prove absolute continuity of compositions and inverses.
For example, a continuous strictly increasing function is absolutely continuous exactly when it maps null sets to null sets.
