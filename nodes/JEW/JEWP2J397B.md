---
tag: JEWP2J397B
kind: definition
name: Grothendieck group
msc: [19A49, 18F30]
defines: 5FDMY7PDYY
uses: [0N6R902FG1, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Grothendieck_group
---

## Definition

Let $M$ be a commutative [[monoid|0N6R902FG1]], written additively.
A *Grothendieck group* of $M$ is an [[abelian group|082GHNPJ53]] $K(M)$ with a monoid homomorphism $i \colon M \to K(M)$ with this universal property.
For every abelian group $A$ and monoid homomorphism $f \colon M \to A$, there is exactly one group homomorphism $g \colon K(M) \to A$ with $g \circ i = f$.

## Remarks

It exists and is unique up to unique isomorphism.
One construction: on $M \times M$ put $(m, n) \sim (m', n')$ if $m + n' + p = m' + n + p$ for some $p \in M$.
The classes form an abelian group under componentwise addition, $i(m)$ is the class of $(m, 0)$, and the class of $(m, n)$ is $i(m) - i(n)$.
Example: for $M = \N$ under addition, the inclusion $\N \to \Z$ is a Grothendieck group, since a homomorphism $f$ from $\N$ extends uniquely by $g(k) = k f(1)$.
Non-example: the inclusion $\N \to \Q$ is not, because the identity map $\N \to \N \subseteq \Z$ has no extension to a group homomorphism $\Q \to \Z$.
The map $i$ is injective exactly when $M$ is cancellative; for $M = \N \cup \set{\infty}$ with $n + \infty = \infty$, one gets $K(M) = 0$.
