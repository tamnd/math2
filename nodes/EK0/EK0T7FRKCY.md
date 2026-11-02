---
tag: EK0T7FRKCY
kind: statement
role: theorem
name: Jacobson density theorem
msc: [16D60]
uses: [0894J980RK, G00C22AEDH, AWSBZWWMG9, TRMYSF91EV, 0WZXK05ME7]
about: [8F6EHDVJ62, G00C22AEDH]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobson_density_theorem
same_as:
  wikidata: Q17098298
  wikipedia: Jacobson density theorem
---

## Statement

Let $R$ be a [[ring|0894J980RK]] with identity and let $U$ be a [[simple|G00C22AEDH]] left $R$-module.
Let $D = \End_R(U)$ be its [[endomorphism ring|AWSBZWWMG9]], which is a [[division ring|0WZXK05ME7]], and view $U$ as a vector space over $D$.
Let $u_1, \ldots, u_n \in U$ be linearly independent over $D$, and let $v_1, \ldots, v_n \in U$ be arbitrary.
Then there is $r \in R$ with $r u_i = v_i$ for $i = 1, \ldots, n$.

## Remarks

$D$ is a division ring by [[Schur's lemma|TRMYSF91EV]].
The proof is by induction on $n$; the key step shows that if $W \subseteq U$ is a finite-dimensional $D$-subspace and $u \notin W$, then some $r \in R$ kills $W$ but not $u$.
Example: let $R = M_n(k)$ for a field $k$ and $U = k^n$, so that $D = k$.
The theorem says that any $n$ linearly independent vectors can be sent to any $n$ vectors by a matrix.
If $U$ is finite-dimensional over $D$, the map $R \to \End_D(U)$ is surjective; when $R$ is a finite-dimensional algebra over an algebraically closed field this gives Burnside's theorem.

## Explanations

### L1 human

A ring acting irreducibly on a module acts as richly as possible.
On any finite set of independent vectors, it can do whatever a linear map can do.
So a primitive ring looks like a ring of linear maps that is "dense" in the full ring of linear maps.

### L2 human

The theorem is the main tool for the structure of [[primitive rings|8F6EHDVJ62]]: a left primitive ring is isomorphic to a dense subring of $\End_D(U)$.
If in addition $R$ is left Artinian, the subring is all of $\End_D(U)$ with $U$ finite-dimensional, so $R \cong M_n(D)$.
This is the route to [[Wedderburn's theorem on simple Artinian rings|YJM07BT0KK]] and to the [[Artin–Wedderburn theorem|R1F271180N]].
