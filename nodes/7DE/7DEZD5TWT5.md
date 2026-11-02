---
tag: 7DEZD5TWT5
kind: statement
role: theorem
name: Kunen's inconsistency theorem
msc: ["03E55"]
uses: [CGH8C8EA9N, 3SZADQXVZJ, 0HTGB13FE2]
about: [CGH8C8EA9N]
sources:
  - url: https://en.wikipedia.org/wiki/Kunen's_inconsistency_theorem
same_as:
  wikidata: Q6444407
  wikipedia: Kunen's inconsistency theorem
---

## Statement

Assume the [[axiom of choice|0HTGB13FE2]].
For an ordinal $\gamma$, let $V_\gamma$ be the set of sets of rank less than $\gamma$, as in the [[von Neumann universe|3SZADQXVZJ]].

1. For every ordinal $\delta$, there is no [[elementary embedding|CGH8C8EA9N]] $j \colon V_{\delta + 2} \to V_{\delta + 2}$ other than the identity.
2. There is no elementary embedding $j \colon V \to V$ other than the identity, where $j$ is a class in the sense of von Neumann–Bernays–Gödel set theory.

## Remarks

Let $j$ be a nontrivial embedding with critical point $\kappa_0$, let $\kappa_{n+1} = j(\kappa_n)$, and let $\lambda = \sup_n \kappa_n$, so that $j(\lambda) = \lambda$.
The proof uses the axiom of choice to find a function on the countable subsets of $\lambda$ that $j$ cannot respect.
One such tool is an $\omega$-Jónsson function, from a theorem of Erdős and Hajnal.
Part 2 follows from part 1 applied to $\delta = \lambda$, after restricting $j$ to $V_{\lambda + 2}$.
The theorem sets an upper limit to large cardinal axioms built from embeddings: the axioms just below it ask for elementary embeddings of $V_\lambda$ or $V_{\lambda + 1}$ into itself.
It is an open problem whether part 2 holds without the axiom of choice.

## Explanations

### L1 human

Many large cardinals are defined by maps from the universe of sets into a smaller copy of itself that keep all truths.
One might hope for the strongest possible version, a map from the universe into itself that is not the identity.
Kunen proved that, with the axiom of choice, such a map cannot exist.
So there is a ceiling for this way of building large cardinals.

### L2 human

The embeddings $j \colon V \to M$ of measurable and supercompact cardinals become stronger as $M$ gets closer to $V$.
Kunen's theorem says that $M$ cannot be all of $V$, and more precisely that $M$ cannot contain the set $j[\lambda]$ for the $\lambda$ above.
The strongest large cardinal axioms in use, such as elementary embeddings $j \colon V_{\lambda + 1} \to V_{\lambda + 1}$, sit just below the limit given by part 1.
