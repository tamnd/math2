---
tag: NS1HWGTD8E
kind: concept
name: Hyperarithmetical theory
msc: [03D55, 03D60]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperarithmetical_theory
same_as:
  wikidata: Q17028365
  wikipedia: Hyperarithmetical theory
---

## Summary

Hyperarithmetical theory studies the hyperarithmetical sets of natural numbers, those computable from an iterate of the [[Turing jump|60P2XWY5QX]] along a computable ordinal.
The computable ordinals are those below the Church–Kleene ordinal $\omega_1^{CK}$, the least [[ordinal|0YSCSX5YZC]] that is not the order type of a computable well-ordering of $\N$.
By a theorem of Kleene, the hyperarithmetical sets are exactly the $\Delta^1_1$ sets of the [[analytical hierarchy|M6JGF4TPM6]].
The theory connects [[computability theory|X14Y880PN5]], descriptive set theory and the study of subsystems of second-order arithmetic.

## Explanations

### L1 human

The [[arithmetical hierarchy|7CVJCQKY41]] uses the jumps $\emptyset', \emptyset'', \ldots$, one for each natural number.
One can go further: join all of them into one set $\emptyset^{(\omega)}$, take its jump, and continue.
Doing this along every ordinal that a computer can describe gives the hyperarithmetical sets.
The set $\emptyset^{(\omega)} = \set{(n, x) : x \in \emptyset^{(n)}}$ is hyperarithmetical but not arithmetical.
These are the sets that can be defined by a single existential, and also by a single universal, quantifier over sets of numbers.
