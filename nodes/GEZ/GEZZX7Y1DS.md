---
tag: GEZZX7Y1DS
kind: proof
name: Proof that groups of order p squared are abelian
msc: [20D15]
proves: 09JZ9P4899
uses: [08V7JHS3QZ, 051VYKA1EX, 06DAH3VS6M, 0RZCTT30H5, 0S7Y9Q990Q, 3C53TD, 04DC0SRN2K, 0YYWCNTPWR, 05MM4EK4SA, 0AH9Q6YNMT, 05N4TQKPH0]
sources:
  - url: https://en.wikipedia.org/wiki/P-group
    locator: Examples
---

## Proof

We show that the centre is the whole group. Let $e$ be the identity of $G$, with $\abs{G} = p^2$.

1. Each positive divisor of $p^2$ is $1$, $p$ or $p^2$: a prime factor of a divisor divides $p$ by [[Euclid's lemma|051VYKA1EX]], so it equals $p$.
2. Let $g \in G$. The [[order of $g$ divides $\abs{G}$|08V7JHS3QZ]], so it is $1$, $p$ or $p^2$ by step 1. So $G$ is a [[$p$-group|06DAH3VS6M]], and $G \neq \set{e}$.
3. By the [[nontrivial centre theorem|0RZCTT30H5]], the [[centre|0S7Y9Q990Q]] $Z(G)$ is not $\set{e}$.
4. The centre is a subgroup of $G$, by the [[subgroup criterion|05N4TQKPH0]]. Indeed $e \in Z(G)$. If $z, w \in Z(G)$ and $g \in G$, then $w g = g w$ gives $w^{-1} g = g w^{-1}$, so $z w^{-1} g = z g w^{-1} = g z w^{-1}$. By [[Lagrange's theorem|3C53TD]] and step 1, $\abs{Z(G)}$ is $1$, $p$ or $p^2$. By step 3, it is $p$ or $p^2$.
5. Suppose $\abs{Z(G)} = p$. For $z \in Z(G)$ and $g \in G$, $g z g^{-1} = z g g^{-1} = z$. So the centre is a normal subgroup, and the [[quotient group|0YYWCNTPWR]] $G/Z(G)$ exists. Its order is the index $[G : Z(G)]$.
6. By the [[index formula|04DC0SRN2K]], $[G : Z(G)] = p^2 / p = p$. So $G/Z(G)$ has prime order $p$, and it is [[cyclic|05MM4EK4SA]].
7. Since $G/Z(G)$ is cyclic, [[$G$ is abelian|0AH9Q6YNMT]]. Then each element commutes with all of $G$, so $Z(G) = G$ and $\abs{Z(G)} = p^2 \neq p$. This contradicts the assumption of step 5.
8. Hence $\abs{Z(G)} = p^2 = \abs{G}$, so $Z(G) = G$. Every element commutes with every other, and $G$ is abelian.

## Idea

The centre of a group of order $p^2$ is nontrivial, so it has order $p$ or $p^2$. If it had order $p$, the quotient by it would have prime order, hence be cyclic. A cyclic quotient by the centre forces the group to be abelian, which makes the centre everything. So the centre is already the whole group.
