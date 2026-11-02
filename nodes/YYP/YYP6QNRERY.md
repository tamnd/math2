---
tag: YYP6QNRERY
kind: problem
name: Connes embedding problem
msc: [46L10, 46L36]
uses: [NZ4NY8SK1C, PSFWQVZ0FS, J64Y3JC0RE]
about: [NZ4NY8SK1C]
sources:
  - url: https://en.wikipedia.org/wiki/Connes_embedding_problem
same_as:
  wikidata: Q5161788
  wikipedia: Connes embedding problem
history:
  posed_by: "Alain Connes"
  first_stated: "1976"
---

## Problem

Let $R$ be the [[hyperfinite type II1 factor|NZ4NY8SK1C]] with its faithful normal tracial state $\tau$, and let $\omega$ be a free [[ultrafilter|J64Y3JC0RE]] on $\N$.
Let $\ell^\infty(R)$ be the algebra of norm-bounded sequences in $R$, and let $I_\omega$ be the ideal of sequences $(x_n)$ with $\lim_{n \to \omega} \tau(x_n^* x_n) = 0$.
The ultrapower $R^\omega = \ell^\infty(R) / I_\omega$ is a type $\mathrm{II}_1$ factor with trace $\tau_\omega((x_n)) = \lim_{n \to \omega} \tau(x_n)$.
The problem asks: does every type $\mathrm{II}_1$ factor $M$ with separable predual, with trace $\tau_M$, admit an injective unital $*$-homomorphism $\pi \colon M \to R^\omega$ with $\tau_\omega \circ \pi = \tau_M$?

## Remarks

Connes raised the question in his 1976 paper on the classification of injective factors.
Over the following decades it was shown to be equivalent to several problems in other areas.
Among them are Kirchberg's QWEP conjecture on C*-algebras and Tsirelson's problem in quantum information theory.
In 2020, Ji, Natarajan, Vidick, Wright and Yuen announced a proof of the complexity result $\mathrm{MIP}^* = \mathrm{RE}$.
It implies a negative answer to Tsirelson's problem and hence to the Connes embedding problem.
So there exist $\mathrm{II}_1$ factors with separable predual that do not embed into $R^\omega$, but no explicit example is known.
Many classes of factors are known to embed, for example the group von Neumann algebras of amenable and of free groups.

## Explanations

### L1 human

The hyperfinite factor $R$ is built from finite matrices, and its ultrapower collects all limits of sequences of such approximations.
Connes asked whether every reasonable $\mathrm{II}_1$ factor can be approximated by finite matrices in this way, at the level of traces of products.
For many years most experts expected the answer to be yes.
The problem was then linked to questions about quantum correlations, and a result in computational complexity theory showed that the answer is no.
