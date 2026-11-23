---
tag: CXHS8K1MB0
kind: proof
name: Proof of the filtration theorem
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
proves: T99DK51S0W
uses: [6ZZSHAKG5F, NGHWZ9Y7ZV, 12MQ2NJ29A, 0G8VEZ3WTK]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Finite model property
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on filtrations and decidability
---

## Proof

We prove the six parts of [[the filtration theorem|T99DK51S0W]]: the lemma by induction on formulas, and the other parts by checking (min) and (max) for each relation.

Members of one class $[w]$ agree on every formula of $\Sigma$.
So a condition that uses only the truth of formulas of $\Sigma$ at $w$ and $v$ is a condition on $[w]$ and $[v]$.
In particular $R^l$, $R^t$, $R^e$ and $V^f$ are well defined, and $[w] \in V^f(p)$ holds if and only if $w \in V(p)$, for $p \in \Sigma$.

### Part 1: the filtration lemma

1. We use [[structural induction|12MQ2NJ29A]] on $\varphi \in \Sigma$.
   Each subformula of $\varphi$ lies in $\Sigma$, so the induction hypothesis applies to it.
   This is where closure under subformulas is used.
2. For $\varphi = p$, the claim is that $w \in V(p)$ iff $[w] \in V^f(p)$, which holds by the remark above.
   For $\varphi = \bot$ both sides are false.
3. For $\varphi = \alpha \to \beta$, both sides are computed from the values of $\alpha$ and $\beta$, which agree by the induction hypothesis.
4. For $\varphi = \square\psi$, first let $\mathfrak{M}, w \models \square\psi$ and $[w] R^f [v]$.
   By (max), $\mathfrak{M}, v \models \psi$, so $\mathfrak{M}^f, [v] \models \psi$ by the induction hypothesis.
   So $\mathfrak{M}^f, [w] \models \square\psi$.
5. Conversely, let $\mathfrak{M}^f, [w] \models \square\psi$ and $w R v$.
   By (min), $[w] R^f [v]$, so $\mathfrak{M}^f, [v] \models \psi$, and $\mathfrak{M}, v \models \psi$ by the induction hypothesis.
   So $\mathfrak{M}, w \models \square\psi$.

### Parts 2 and 3: the range and the size

6. $R^s$ satisfies (min) by its definition.
   For (max), let $w' R v'$ with $w' \sim_\Sigma w$ and $v' \sim_\Sigma v$, and let $\square\varphi \in \Sigma$ be true at $w$.
   Then $\square\varphi$ is true at $w'$, so $\varphi$ is true at $v'$, and $\varphi$ is true at $v$ because $\varphi \in \Sigma$ and $v \sim_\Sigma v'$.
7. $R^l$ satisfies (max) by its definition.
   For (min), let $w R v$ and let $\square\varphi \in \Sigma$ be true at $w$.
   Then $\varphi$ is true at $v$ by the truth clause for $\square$, so $[w] R^l [v]$.
8. A filtration contains $R^s$ by (min), and it is contained in $R^l$ by (max).
   A relation between $R^s$ and $R^l$ satisfies (min) because $R^s$ does, and (max) because $R^l$ does.
9. The map that sends $[w]$ to the set of formulas of $\Sigma$ true at $w$ is well defined and one to one, by the definition of $\sim_\Sigma$.
   Its values are subsets of $\Sigma$, so there are at most $2^{\lvert \Sigma \rvert}$ classes.

### Part 4: the transitive filtration

10. For (min), let $R$ be transitive, $w R v$, and $\square\varphi \in \Sigma$ true at $w$.
    Then $\varphi$ is true at $v$.
    Every successor $u$ of $v$ is a successor of $w$, by transitivity, so $\varphi$ is true at $u$, and $\square\varphi$ is true at $v$.
    This is where transitivity is used.
11. (max) holds because the condition defining $R^t$ includes the truth of $\varphi$ at $v$.
12. For transitivity, let $[w] R^t [v] R^t [u]$ and let $\square\varphi \in \Sigma$ be true at $w$.
    Then $\square\varphi$ is true at $v$, so $\square\varphi$ and $\varphi$ are true at $u$, and $[w] R^t [u]$.
13. If $R$ is also reflexive, then $w R w$ gives $[w] R^t [w]$ by (min).

### Parts 5 and 6: symmetry and equivalence

14. If $[w] R^s [v]$ comes from $w' R v'$, then $v' R w'$ by symmetry of $R$, so $[v] R^s [w]$.
15. Let $R$ be an equivalence relation and $w R v$.
    Then $w$ and $v$ have the same successors, so they agree on every $\square\varphi$, and $[w] R^e [v]$.
    This is (min).
16. For (max), let $[w] R^e [v]$ and let $\square\varphi \in \Sigma$ be true at $w$.
    Then $\square\varphi$ is true at $v$, and $v R v$ gives $\varphi$ at $v$.
    This is where reflexivity of $R$ is used.
17. Agreement on every $\square\varphi \in \Sigma$ is reflexive, symmetric and transitive, so $R^e$ is an [[equivalence relation|0G8VEZ3WTK]].

## Idea

The box case of the lemma uses (max) in the direction from $\mathfrak{M}$ to $\mathfrak{M}^f$ and (min) in the other direction.
These are exactly the two conditions of a filtration, which is why they are the definition.
The remaining parts choose a relation between $R^s$ and $R^l$ that keeps a frame property.
The transitive filtration copies boxed formulas forward, which is what transitivity does in $\mathfrak{M}$.

## Variants

The same induction proves the lemma for several boxes, with one pair of conditions for each relation.

One can also take $\Sigma$ closed under subformulas and single negations.
In the canonical model the classes then match the maximal consistent subsets of $\Sigma$, and the lemma becomes a finite truth lemma.
