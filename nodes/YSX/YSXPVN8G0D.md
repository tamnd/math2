---
tag: YSXPVN8G0D
kind: statement
role: theorem
name: Schützenberger's theorem on star-free languages
msc: [68Q70, 20M35]
uses: [K83HS1C5WG, D47RMDH8MJ, 18WVBDCS38]
about: [K83HS1C5WG, D47RMDH8MJ]
sources:
  - url: https://en.wikipedia.org/wiki/Star-free_language
---

## Statement

Let $\Sigma$ be an alphabet and let $L \subseteq \Sigma^*$ be a [[regular language|18WVBDCS38]], with [[syntactic monoid|D47RMDH8MJ]] $M(L)$.
Then $L$ is a [[star-free language|K83HS1C5WG]] if and only if $M(L)$ is aperiodic, that is, there is an integer $n \ge 0$ with $x^n = x^{n+1}$ for every $x \in M(L)$.

## Remarks

For a finite monoid, being aperiodic is equivalent to having only trivial subgroups.
The easier direction shows by induction on the star-free construction that the syntactic monoids stay aperiodic; the key case is concatenation.
The harder direction builds a star-free expression for each preimage of an element of an aperiodic monoid, by induction on the ideal structure of the monoid.
Example: $(aa)^*$ over $\set{a}$ has syntactic monoid $\Z/2\Z$, in which $x^n \ne x^{n+1}$ for the generator and every $n$, so it is not star-free.
In contrast, $(ab)^*$ over $\set{a, b}$ has an aperiodic syntactic monoid with six elements, and indeed it is star-free.
Since the syntactic monoid of a regular language is computable and finite, the theorem gives an algorithm to decide whether a regular language is star-free.

## Explanations

### L1 human

Star-free languages are those described without the repetition operator, using complement instead.
The theorem says that one can recognize them by looking at the algebra of the language: no element of the syntactic monoid may cycle with a period greater than one.
Intuitively, star-free languages cannot count modulo any number.

### L2 human

This is the first and most famous instance of the algebraic classification of regular languages, which matches varieties of finite monoids with classes of languages.
Together with the theorem of McNaughton and Papert, it shows that three classes coincide: star-free languages, languages definable in first-order logic over words, and languages with aperiodic syntactic monoid.
Kamp's theorem adds linear temporal logic to this list, which is why the result matters in program verification.
