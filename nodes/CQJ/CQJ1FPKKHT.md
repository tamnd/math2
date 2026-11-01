---
tag: CQJ1FPKKHT
kind: statement
role: theorem
name: Direct summand conjecture
msc: [13D22, 13H05, 13B21]
uses: [63XXTF6B5M, 0670T59HGE, 05QY1VEBYD]
about: [63XXTF6B5M]
sources:
  - url: https://en.wikipedia.org/wiki/Homological_conjectures_in_commutative_algebra
---

## Statement

Let $R$ be a [[regular local ring|63XXTF6B5M]] and let $R \subseteq S$ be an extension of commutative rings such that $S$ is a [[finitely generated|05QY1VEBYD]] $R$-module.
Then the inclusion $R \to S$ splits as a map of $R$-modules: there is an $R$-linear map $\rho \colon S \to R$ with $\rho(1) = 1$.

## Remarks

Suppose that $R$ contains the rational numbers and $S$ is a domain, and let $F$ and $L$ be the fraction fields of $R$ and $S$.
Then $\rho = \frac{1}{[L : F]} \operatorname{Tr}_{L/F}$ is a splitting.
It maps $S$ into $R$ because $R$ is regular, hence integrally closed.
Hochster proved the statement when $R$ contains a field, and André proved it in mixed characteristic, using perfectoid methods.
It is one of [[Hochster's homological conjectures|1TNS604ZST]], and it kept the name "conjecture" after its proof.
Regularity cannot be dropped: for $R = K[\![t^2, t^3]\!] \subseteq S = K[\![t]\!]$, a splitting $\rho$ would give $t^3 = \rho(t^3) = t^2 \rho(t)$, so $\rho(t) = t \notin R$, a contradiction.

## Explanations

### L1 human

If a nice ring sits inside a finite extension ring, one can project the big ring back onto the small one in a linear way.
For rings containing the rationals this is easy, by averaging with a trace.
For rings like the $p$-adic integers it was a famous open problem for decades.

### L2 human

The statement is equivalent to the monomial conjecture, and it implies several other homological conjectures.
A ring that is a direct summand of a ring is often forced to inherit good properties; for example, a direct summand of a normal domain is normal.
