---
tag: 8SH7WETCKY
kind: statement
role: axiom
name: Singular cardinals hypothesis
msc: ["03E04", "03E10", "03E35"]
uses: [0HE5WDQ9FJ, 0EBACQFAZW, BAWHE1W6MH, 13ZV2F8JAR, 0MN2MER9WN]
about: [0EBACQFAZW, BAWHE1W6MH]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_cardinals_hypothesis
same_as:
  wikidata: Q2289367
  wikipedia: Singular cardinals hypothesis
---

## Statement

Work in [[ZFC|0HE5WDQ9FJ]].
For an infinite [[cardinal|0EBACQFAZW]] $\kappa$, let $\operatorname{cf}(\kappa)$ be its [[cofinality|BAWHE1W6MH]], and call $\kappa$ singular when $\operatorname{cf}(\kappa) < \kappa$.
Let $\kappa^+$ be the least cardinal greater than $\kappa$.
The *singular cardinals hypothesis* (SCH) is the assertion: for every singular cardinal $\kappa$ with $2^{\operatorname{cf}(\kappa)} < \kappa$, one has $\kappa^{\operatorname{cf}(\kappa)} = \kappa^+$.

## Remarks

An infinite cardinal that is not singular is a [[regular cardinal|13ZV2F8JAR]].
SCH is equivalent to the statement that $2^\kappa = \kappa^+$ for every singular strong limit cardinal $\kappa$, where strong limit means $2^\lambda < \kappa$ for all $\lambda < \kappa$.
The generalized form of the [[continuum hypothesis|0MN2MER9WN]], $2^\lambda = \lambda^+$ for every infinite $\lambda$, implies SCH.
So SCH is consistent with ZFC whenever ZFC is consistent.
SCH is not provable in ZFC if suitable large cardinals are consistent: Magidor built models where it fails at $\aleph_\omega$ from large cardinal hypotheses.
Its failure needs large cardinals: by Jensen's covering lemma, if $0^\sharp$ does not exist, then SCH holds.
Gitik and Mitchell showed that the failure of SCH is equiconsistent with a measurable cardinal $\kappa$ of Mitchell order $\kappa^{++}$.
Solovay proved that SCH holds at all singular cardinals above a strongly compact cardinal.
Silver proved that if $\kappa$ is singular of uncountable cofinality and $2^\lambda = \lambda^+$ for all infinite $\lambda < \kappa$, then $2^\kappa = \kappa^+$.

## Explanations

### L1 human

Here $2^\kappa$ is the number of subsets of a set of size $\kappa$.
And $\kappa^\lambda$ is the number of functions from a set of size $\lambda$ to a set of size $\kappa$.
For regular cardinals, ZFC says very little about the size of $2^\kappa$: almost any reasonable value is consistent.
Singular cardinals, such as $\aleph_\omega$, behave differently, and ZFC proves real restrictions on their powers.
The singular cardinals hypothesis says that these powers take the smallest values that the restrictions allow.
It is a weak form of the generalized continuum hypothesis that concerns only singular cardinals.

### L2 human

In ZFC, cardinal exponentiation $\kappa^\lambda$ is governed by the continuum function $\lambda \mapsto 2^\lambda$ on regular cardinals together with the values $\kappa^{\operatorname{cf}(\kappa)}$ at singular cardinals.
Under SCH, the second part is determined by the first, so all of cardinal arithmetic is computed from the values of $2^\lambda$ at regular $\lambda$.
The study of how SCH can fail led to Shelah's pcf theory, which gives bounds in ZFC alone.
A famous such bound is that if $\aleph_\omega$ is a strong limit, then $2^{\aleph_\omega} < \aleph_{\omega_4}$.
