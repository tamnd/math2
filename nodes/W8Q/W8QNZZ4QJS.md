---
tag: W8QNZZ4QJS
kind: statement
role: proposition
name: Prime ideals of a localization
msc: [13B30, 13A15]
uses: [4C1AE84N5N, AN9SKEZ3VY, 00MHHZ9SNE, 5AFH94P4S3]
about: [4C1AE84N5N, 00MHHZ9SNE]
sources:
  - url: https://en.wikipedia.org/wiki/Localization_(commutative_algebra)
---

## Statement

Let $R$ be a [[commutative ring|0310REJJY8]], let $S \subseteq R$ be a [[multiplicative set|AN9SKEZ3VY]], and let $\lambda \colon R \to S^{-1}R$, $a \mapsto a/1$, be the canonical map to the [[localization|4C1AE84N5N]].
Then the maps
$$\mathfrak q \mapsto \lambda^{-1}(\mathfrak q), \qquad \mathfrak p \mapsto S^{-1}\mathfrak p = \set{a/s : a \in \mathfrak p, \ s \in S}$$
are mutually inverse bijections between the [[prime ideals|00MHHZ9SNE]] $\mathfrak q$ of $S^{-1}R$ and the prime ideals $\mathfrak p$ of $R$ with $\mathfrak p \cap S = \emptyset$.
Both maps preserve inclusion.

## Remarks

The preimage of a prime ideal under a ring homomorphism is prime, and $\lambda^{-1}(\mathfrak q)$ misses $S$ because elements of $S$ become units.
Conversely, if $\mathfrak p \cap S = \emptyset$, then $a/s \in S^{-1}\mathfrak p$ forces $ua \in \mathfrak p$ for some $u \in S$, hence $a \in \mathfrak p$ since $u \notin \mathfrak p$.
This shows $\lambda^{-1}(S^{-1}\mathfrak p) = \mathfrak p$ and that $S^{-1}\mathfrak p$ is a proper prime ideal.
Finally every ideal $J$ of $S^{-1}R$ is the [[extension|5AFH94P4S3]] of its contraction, which gives $S^{-1}\lambda^{-1}(\mathfrak q) = \mathfrak q$.

Example: for $R = \Z$ and $S = \set{1, 2, 4, \ldots}$, the prime ideals of $\Z[1/2]$ are $(0)$ and $p\Z[1/2]$ for the odd primes $p$; the prime $2\Z$ meets $S$ and disappears.

For $S = R \setminus \mathfrak p$ with $\mathfrak p$ prime, the primes of $R_{\mathfrak p}$ correspond to the primes of $R$ contained in $\mathfrak p$.
So $R_{\mathfrak p}$ has the unique maximal ideal $\mathfrak p R_{\mathfrak p}$, that is, it is a [[local ring|MZ02BKPHJA]].

The hypothesis that $\mathfrak p$ be prime matters: for a non-prime ideal $I$ with $I \cap S = \emptyset$ one can have $\lambda^{-1}(S^{-1}I) \ne I$.
For instance, with $R = \Z$, $I = 6\Z$ and $S = \set{1, 2, 4, \ldots}$, one gets $\lambda^{-1}(S^{-1}I) = 3\Z$.

## Explanations

### L1 human

When you localize, some prime ideals vanish and the others survive unchanged.
The ones that vanish are exactly those that contain an allowed denominator, since such an ideal would contain a unit.
In the language of geometry, localizing keeps an open part of the space of prime ideals, or the primes near a chosen point.

### L2 human

This result is the reason why localization is a "local" operation on the [[spectrum|FB45BHHA2J]].
For $S = \set{1, f, f^2, \ldots}$ it identifies $\operatorname{Spec} R_f$ with the [[basic open set|N6JX9BCKQP]] $D(f)$.
For $S = R \setminus \mathfrak p$ it identifies $\operatorname{Spec} R_{\mathfrak p}$ with the primes inside $\mathfrak p$, so the [[height|87WH65FJB8]] of $\mathfrak p$ equals the [[Krull dimension|MVGBS3J1P7]] of $R_{\mathfrak p}$.
Combined with the description of the primes of a quotient $R/I$, it describes the primes of rings such as $R_{\mathfrak p}/I R_{\mathfrak p}$ for an ideal $I$ of $R$.
