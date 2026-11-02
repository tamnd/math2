---
tag: AKMASKR0ZG
kind: definition
name: Quasivariety
msc: ["08C15", "03C52"]
defines: WRXEKT4NQS
uses: [94GVY3APPQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quasivariety
---

## Definition

Let $\sigma$ be an algebraic signature.
Let $K$ be a class of $\sigma$-algebras.
Then $K$ is a *quasivariety* if there is a set $\Sigma$ of [[quasi-identities|94GVY3APPQ]] of type $\sigma$ with the following property.
An algebra of type $\sigma$ is in $K$ exactly when it satisfies every member of $\Sigma$.

## Remarks

Example: the class of cancellative semigroups is a quasivariety.
It is defined by the associative law, which is a quasi-identity with no hypotheses, and by the two quasi-identities $z x \approx z y \rightarrow x \approx y$ and $x z \approx y z \rightarrow x \approx y$.

Non-example: the class of fields, in the signature $(+, -, \cdot, 0, 1)$, is not a quasivariety.
Every quasivariety contains the one-element algebra, since all terms take the same value there, so every conclusion $s \approx t$ holds.
But a field needs $0 \ne 1$.
Also, every quasivariety is closed under direct products, and $\Q \times \Q$ is not a field.

Each [[variety|AJNZJD8442]] is a quasivariety, defined by identities, which are quasi-identities with no hypotheses.
The smallest quasivariety containing a class $K$ is denoted $Q(K)$ or $\mathbf{ISPP_U}(K)$, by [[Mal'cev's characterization|DFNM3BGMAY]].
