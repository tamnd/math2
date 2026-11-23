---
tag: X8PAF0TD5W
kind: proof
name: Proof of the frame correspondences of the common modal axioms
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
proves: FDFQFWPM4X
uses: [6BQ71KQ6QT, YHGXV3SQDP, E87G6ZTMTN]
methods: [0NTF6DMVAP, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Proof

We prove the claims of [[common modal axiom schemata|FDFQFWPM4X]] for a frame $\mathfrak{F} = (W, R)$.
For each axiom, the direction from the property to validity is a check at an arbitrary world $w$ of an arbitrary model on $\mathfrak{F}$.
The other direction is by contraposition: if the property fails, we give a valuation that makes the axiom false.

### Axiom K

Let $w \models \square(p \to q)$ and $w \models \square p$, and let $w R v$.
Then $v \models p \to q$ and $v \models p$, so $v \models q$.
Hence $w \models \square q$, and $\mathrm{K}$ is valid on every frame.

### Axiom T and reflexivity

Let $R$ be reflexive and $w \models \square p$.
Since $w R w$, the clause for $\square$ gives $w \models p$.

Conversely, let $w$ be a world with $(w, w) \notin R$, and put $V(p) = R[w]$.
Every successor of $w$ lies in $V(p)$, so $w \models \square p$.
But $w \notin R[w]$, so $w \not\models p$, and $\mathrm{T}$ fails at $w$.

### Axiom D and seriality

Let $R$ be serial and $w \models \square p$.
Choose $v$ with $w R v$; then $v \models p$, so $w \models \lozenge p$.

Conversely, let $w$ be a world with $R[w] = \varnothing$, and take any valuation.
Then $w \models \square p$ because $w$ has no successor, and $w \not\models \lozenge p$ for the same reason.

### Axiom B and symmetry

Let $R$ be symmetric and $w \models p$, and let $w R v$.
Symmetry gives $v R w$, so $v \models \lozenge p$.
As $v$ was any successor of $w$, we get $w \models \square\lozenge p$.

Conversely, let $w R v$ with $(v, w) \notin R$, and put $V(p) = \{ w \}$.
Then $w \models p$.
The only world with $p$ is $w$, and $w \notin R[v]$, so $v \not\models \lozenge p$.
Since $w R v$, we get $w \not\models \square\lozenge p$, and $\mathrm{B}$ fails at $w$.

### Axiom 4 and transitivity

Let $R$ be transitive and $w \models \square p$, and let $w R v$ and $v R u$.
Transitivity gives $w R u$, so $u \models p$.
Hence $v \models \square p$ for every successor $v$ of $w$, and $w \models \square\square p$.

Conversely, let $w R v$ and $v R u$ with $(w, u) \notin R$, and put $V(p) = R[w]$.
Then $w \models \square p$.
Since $u \notin R[w]$, we have $u \not\models p$, so $v \not\models \square p$.
Since $w R v$, we get $w \not\models \square\square p$, and $\mathrm{4}$ fails at $w$.

### Axiom 5 and the Euclidean property

Let $R$ be Euclidean and $w \models \lozenge p$, and choose $u$ with $w R u$ and $u \models p$.
For any $v$ with $w R v$, the Euclidean property gives $v R u$, so $v \models \lozenge p$.
Hence $w \models \square\lozenge p$.

Conversely, let $w R v$ and $w R u$ with $(v, u) \notin R$, and put $V(p) = \{ u \}$.
Then $w \models \lozenge p$, since $w R u$.
Since $u \notin R[v]$, we get $v \not\models \lozenge p$, so $w \not\models \square\lozenge p$, and $\mathrm{5}$ fails at $w$.

### Conclusion

This proves that $\mathrm{K}$ is valid on every frame and proves the five equivalences.
Let $\Sigma$ be a set of these axioms, and take a frame with the matching properties.
All of $\Sigma$ is valid on the frame, so every theorem of $\mathsf{K}\Sigma$ is valid on it, by [[soundness of normal modal logics|E87G6ZTMTN]].

## Idea

Each direction from property to validity reads the axiom at one world and uses the frame property once.
Each converse picks the smallest valuation that makes the antecedent true at the bad world.
This is $V(p) = R[w]$ for $\mathrm{T}$ and $\mathrm{4}$, $V(p) = \{ w \}$ for $\mathrm{B}$, and $V(p) = \{ u \}$ for $\mathrm{5}$.
Then the missing pair of the relation is exactly what the consequent needs.

## Variants

The same proofs can be phrased with the [[standard translation|YW6YGBMVQY]].
Frame validity is a second-order sentence, and the minimal valuation is a choice for the second-order variable; see [[the second-order translation of T|KM2BKWZKW8]].
For combined systems one can argue at once.
A frame validates $\mathsf{S5}$ iff $R$ is reflexive and Euclidean, which is the same as being an equivalence relation.
