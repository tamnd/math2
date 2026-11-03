---
tag: CJTEDNS651
kind: statement
role: proposition
name: Fisher's principle
msc: [92D15, 92D50, 91A22]
uses: [CCN582E2C4]
about: [CCN582E2C4]
sources:
  - url: https://en.wikipedia.org/wiki/Fisher%27s_principle
same_as:
  wikidata: Q2621361
  wikipedia: Fisher's principle
---

## Statement

Consider a large randomly mating population with two sexes, in which every offspring has exactly one mother and one father.
Assume that sons and daughters cost the parent the same.
Assume that each parent produces a fixed number of offspring, of which a fraction $s \in (0, 1)$ are sons.
Let all residents use the fraction $s^*$, and let a rare mutant parent use the fraction $s$.
Then the expected number of grandchildren of the mutant is proportional to
$$W(s, s^*) = \frac{s}{s^*} + \frac{1 - s}{1 - s^*},$$
with a constant that does not depend on $s$.
The value $s^* = 1/2$ is the only resident sex ratio at which no mutant has $W(s, s^*) > W(s^*, s^*)$.

## Remarks

In the next generation all males together and all females together have the same number of offspring, since each offspring has one parent of each sex.
So a son has expected success proportional to $1/s^*$ and a daughter to $1/(1 - s^*)$, which gives $W$.
Now $W(s^*, s^*) = 2$.
If $s^* = 1/2$, then $W(s, 1/2) = 2$ for every $s$, so no mutant does better.
If $s^* < 1/2$, then $W$ is increasing in $s$, so mutants that make more sons do better; the case $s^* > 1/2$ is symmetric.
When sons and daughters cost different amounts, the same argument gives equal total investment in the two sexes rather than equal numbers.
The argument fails under local mate competition or inbreeding, where female-biased ratios are observed.

## Explanations

### L1 human

Why are about half of all babies boys and half girls, in many species?
Every child has one father and one mother, so if males were rare, each male would on average have more children than each female.
Then parents who tend to have sons would have more grandchildren, and the tendency to have sons would spread until the balance is restored.
The only stable point is the even split.

### L2 human

This is an early example of a frequency-dependent argument, of the kind later made formal as an evolutionarily stable strategy in evolutionary game theory.
The fitness of a strategy depends on what the rest of the population does, and the stable strategy is the one that cannot be invaded.
The formula for $W$ is often called the Shaw–Mohler equation.
