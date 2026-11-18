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

We prove the six parts of [[the filtration theorem|T99DK51S0W]].
Members of one class $[w]$ agree on every formula of $\Sigma$.
So a condition that uses only the truth of formulas of $\Sigma$ at $w$ and $v$ is a condition on $[w]$ and $[v]$.
In particular $R^l$, $R^t$, $R^e$ and $V^f$ are well defined, and $[w] \in V^f(p)$ if and only if $w \in V(p)$, for $p \in \Sigma$.

1. Part 1, the induction. We use [[structural induction|12MQ2NJ29A]] on $\varphi \in \Sigma$. Each subformula of $\varphi$ is in $\Sigma$, so the induction hypothesis applies to it. Here closure under subformulas is used.
2. For $\varphi = p$, the claim is $w \in V(p)$ iff $[w] \in V^f(p)$, which holds by the remark above. For $\varphi = \bot$ both sides are false.
3. For $\varphi = \alpha \to \beta$, both sides are computed from the values of $\alpha$ and $\beta$, which agree by the induction hypothesis.
4. For $\varphi = \square\psi$, first let $\mathfrak{M}, w \models \square\psi$ and $[w] R^f [v]$. By (max), $\mathfrak{M}, v \models \psi$, so $\mathfrak{M}^f, [v] \models \psi$ by the induction hypothesis. So $\mathfrak{M}^f, [w] \models \square\psi$.
5. Conversely, let $\mathfrak{M}^f, [w] \models \square\psi$ and $w R v$. By (min), $[w] R^f [v]$, so $\mathfrak{M}^f, [v] \models \psi$, and $\mathfrak{M}, v \models \psi$ by the induction hypothesis. So $\mathfrak{M}, w \models \square\psi$.
6. Part 2, $R^s$. (min) holds by the definition of $R^s$. For (max), let $w' R v'$ with $w' \sim_\Sigma w$, $v' \sim_\Sigma v$, and let $\mathfrak{M}, w \models \square\varphi$ with $\square\varphi \in \Sigma$.
7. Then $w' \models \square\varphi$, so $v' \models \varphi$, and $v \models \varphi$ since $\varphi \in \Sigma$ and $v \sim_\Sigma v'$.
8. Part 2, $R^l$. (max) holds by the definition of $R^l$. For (min), let $w R v$ and $w \models \square\varphi$; then $v \models \varphi$ by the truth clause of $\square$, so $[w] R^l [v]$.
9. Part 2, the range. A filtration contains $R^s$ by (min), and it is contained in $R^l$ by (max). A relation $R'$ with $R^s \subseteq R' \subseteq R^l$ has (min) because $R^s$ has it, and (max) because $R^l$ has it.
10. Part 3. The map $[w] \mapsto \set{\varphi \in \Sigma : \mathfrak{M}, w \models \varphi}$ is well defined and one to one, by the definition of $\sim_\Sigma$. Its values are subsets of $\Sigma$, so there are at most $2^{|\Sigma|}$ classes.
11. Part 4, (min). Let $R$ be transitive, $w R v$, and $w \models \square\varphi$ with $\square\varphi \in \Sigma$. Then $v \models \varphi$. Every successor $u$ of $v$ is a successor of $w$, by transitivity, so $u \models \varphi$ and $v \models \square\varphi$. Here transitivity is used.
12. Part 4, (max) and transitivity. (max) holds since the condition of $R^t$ contains $v \models \varphi$. If $[w] R^t [v] R^t [u]$ and $w \models \square\varphi$, then $v \models \square\varphi$, so $u \models \square\varphi \wedge \varphi$. So $[w] R^t [u]$.
13. Part 4, reflexivity. If $R$ is reflexive, then $w R w$ gives $[w] R^t [w]$ by (min).
14. Part 5. If $[w] R^s [v]$ by $w' R v'$, then $v' R w'$ by symmetry of $R$, so $[v] R^s [w]$.
15. Part 6, (min). Let $R$ be an equivalence relation and $w R v$. Then $R[w] = R[v]$, so $w$ and $v$ agree on every $\square\varphi$. So $[w] R^e [v]$.
16. Part 6, (max). Let $[w] R^e [v]$ and $w \models \square\varphi$ with $\square\varphi \in \Sigma$. Then $v \models \square\varphi$, and $v R v$ gives $v \models \varphi$. Here reflexivity of $R$ is used.
17. Part 6, equivalence. "Agreeing on every $\square\varphi \in \Sigma$" is reflexive, symmetric and transitive, so $R^e$ is an [[equivalence relation|0G8VEZ3WTK]].

## Idea

The direction from $\mathfrak{M}$ to $\mathfrak{M}^f$ of the box case uses (max), and the other direction uses (min).
These are exactly the two conditions of a filtration.
The extra parts choose a relation between $R^s$ and $R^l$ that keeps a frame property.
The transitive filtration copies boxed formulas forward, which is what transitivity does in $\mathfrak{M}$.

## Variants

1. The same induction proves the lemma for several boxes, one pair of conditions for each relation.
2. One can take $\Sigma$ closed under subformulas and single negations. In the canonical model the classes then match the maximal consistent subsets of $\Sigma$, and the lemma becomes a finite truth lemma.
