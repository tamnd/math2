---
tag: 2WADQVGPD4
kind: definition
name: Natural duality
msc: ["08C20", "06D50"]
defines: W5VG6HS8KW
uses: [WRXEKT4NQS, KBXSZC6BV1, WJ73XYBNE4, 0CQHFPGJ45]
sources:
  - url: https://en.wikipedia.org/wiki/Stone_duality
---

## Definition

Let $M$ be a finite algebra and let $\mathcal{A} = \mathbf{ISP}(M)$ be the [[quasivariety|WRXEKT4NQS]] it generates.
An *alter ego* of $M$ is a structure $\underset{\sim}{M} = (M; G, H, R, \mathcal{T})$ on the same set, where $\mathcal{T}$ is the discrete [[topology|0CQHFPGJ45]] and:

1. $G$ is a set of operations $M^n \to M$ that are [[homomorphisms|KBXSZC6BV1]] from $M^n$ to $M$;
2. $H$ is a set of partial operations whose domains are subalgebras of powers $M^n$ and which are homomorphisms on them;
3. $R$ is a set of relations $r \subseteq M^n$ that are subalgebras of $M^n$.

For $A \in \mathcal{A}$, the set $D(A)$ of homomorphisms $A \to M$ is a closed substructure of the power $\underset{\sim}{M}^A$ with the product topology.
Let $X$ be a closed substructure of a nonzero power of $\underset{\sim}{M}$.
The set $E(X)$ of continuous maps $X \to M$ that preserve $G$, $H$ and $R$ is a subalgebra of $M^X$.
Each $A$ has the evaluation homomorphism $e_A \colon A \to E(D(A))$, $e_A(a)(x) = x(a)$.
The alter ego $\underset{\sim}{M}$ *yields a natural duality* on $\mathcal{A}$ if $e_A$ is an isomorphism for every $A \in \mathcal{A}$.

## Remarks

The duality is *full* if, in addition, every closed substructure $X$ of a nonzero power of $\underset{\sim}{M}$ is isomorphic to $D(E(X))$ by the evaluation map.
Then $D$ and $E$ form a dual equivalence of categories.

Example: let $M$ be the two-element Boolean algebra and let $\underset{\sim}{M}$ be the two-element set with the discrete topology and $G = H = R = \emptyset$.
It yields a natural duality on Boolean algebras: this is Stone's representation of a Boolean algebra as the clopen subsets of its Stone space.
For the two-element bounded lattice, the alter ego with the order relation $\le$ on $\set{0, 1}$ yields Priestley duality.

Non-example: for the two-element bounded lattice $M$, the alter ego with no structure besides the topology does not yield a duality.
Take for $A$ the three-element chain $0 < a < 1$.
It has two homomorphisms to $M$, sending $a$ to $0$ or to $1$, so $D(A)$ is a two-point discrete space.
That space has four continuous maps to $M$, while $A$ has three elements, so $e_A$ is not onto.
The relation $\le$ is a subalgebra of $M^2$, and adding it cuts these maps down to the three order-preserving ones.
