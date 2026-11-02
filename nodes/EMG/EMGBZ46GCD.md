---
tag: EMGBZ46GCD
kind: statement
role: theorem
name: Cohen's independence of CH
msc: ["03E35", "03E40", "03E50"]
uses: [0HE5WDQ9FJ, 0MN2MER9WN, F2DTWW9HP7, WEDP73Y7GK]
about: [0MN2MER9WN, F2DTWW9HP7]
sources:
  - url: https://en.wikipedia.org/wiki/Forcing_(mathematics)
---

## Statement

If [[ZF|0HE5WDQ9FJ]] is consistent, then ZFC together with the negation of the [[continuum hypothesis|0MN2MER9WN]] is consistent.
Together with [[Gödel's theorem|Q9176JRJ5M]], it follows that if ZFC is consistent, then the continuum hypothesis is neither provable nor refutable in ZFC.

## Remarks

One starts from a countable transitive model $M$ of ZFC and uses [[forcing|F2DTWW9HP7]] with the set $P$ of finite partial functions from $\omega_2^M \times \omega$ to $\set{0, 1}$, ordered by reverse inclusion.
A [[generic filter|WEDP73Y7GK]] $G$ gives a function from $\omega_2^M \times \omega$ to $\set{0, 1}$, and so $\aleph_2^M$ different new reals.
Every antichain of $P$ is countable, and this chain condition implies that $M$ and $M[G]$ have the same cardinals.
So $M[G] \models 2^{\aleph_0} \ge \aleph_2$.
The existence of a countable transitive model of ZFC does not follow from the consistency of ZFC.
The standard way around this uses countable transitive models of large finite fragments of ZFC, or Boolean-valued models.

## Explanations

### L1 human

The continuum hypothesis asks whether there is a size of infinity between the natural numbers and the real numbers.
Gödel showed that the usual axioms cannot disprove it, and Cohen showed that they cannot prove it either.
Cohen took a universe of sets and added many new real numbers to it, so many that the continuum became larger than the next infinite size.
So the usual axioms of set theory leave the question open.

### L2 human

The proof is the first use of forcing, and its pattern is used in almost all independence proofs.
The first key step is to choose a partial order whose generic filter adds the desired objects.
The second is to check that the forcing does not collapse cardinals, here by the countable chain condition.
Changing $\omega_2$ to other cardinals gives many possible values of $2^{\aleph_0}$; Easton's theorem describes the possible values of $2^\kappa$ for all regular $\kappa$.
Cohen also used forcing to show that the axiom of choice is independent of ZF.
