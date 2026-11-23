---
tag: 2TQ99Y9TEJ
kind: proof
name: Proof of bisimulation invariance of modal formulas
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: grad
proves: TKFFTAX30E
uses: [7T740SFHHV, NGHWZ9Y7ZV]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Bisimulation
    locator: Bisimulation and modal logic
  - url: https://builds.openlogicproject.org/
    locator: Modal Logic
---

## Proof

We prove the main claim by induction on formulas, and then show that each of the three constructions is a bisimulation.
Fix the models $\mathfrak{M} = (W, R, V)$ and $\mathfrak{M}' = (W', R', V')$ and the [[bisimulation|7T740SFHHV]] $Z$.
Let $P(\varphi)$ be the claim: for all $w Z w'$, $\mathfrak{M}, w \models \varphi$ if and only if $\mathfrak{M}', w' \models \varphi$.
The truth clauses are those of [[Kripke semantics|NGHWZ9Y7ZV]].

### Part A: the main claim

1. Let $\varphi = p$ be a variable and $w Z w'$.
   Then $\mathfrak{M}, w \models p$ means $w \in V(p)$, and by the atom clause this holds exactly when $w' \in V'(p)$.
2. Let $\varphi = \bot$.
   It is false at every world of both models, so both sides of $P(\bot)$ are false.
3. Let $\varphi = \neg \psi$, assume $P(\psi)$, and let $w Z w'$.
   Then $w \models \neg \psi$ holds exactly when $w \not\models \psi$, which by $P(\psi)$ holds exactly when $w' \not\models \psi$, that is, $w' \models \neg \psi$.
4. Let $\varphi = \psi \wedge \chi$, assume $P(\psi)$ and $P(\chi)$, and let $w Z w'$.
   Both conjuncts transfer separately, so $w \models \psi \wedge \chi$ holds exactly when $w' \models \psi \wedge \chi$.
5. Let $\varphi = \lozenge \psi$, assume $P(\psi)$, and let $w Z w'$ with $\mathfrak{M}, w \models \lozenge \psi$.
   By the truth clause there is $v$ with $w R v$ and $\mathfrak{M}, v \models \psi$.
6. By zig there is $v'$ with $w' R' v'$ and $v Z v'$.
   By $P(\psi)$ at the pair $(v, v')$, $\mathfrak{M}', v' \models \psi$, so $\mathfrak{M}', w' \models \lozenge \psi$.
7. For the other direction, let $\mathfrak{M}', w' \models \lozenge \psi$, so $w' R' v'$ and $\mathfrak{M}', v' \models \psi$ for some $v'$.
   By zag there is $v$ with $w R v$ and $v Z v'$, and $P(\psi)$ gives $\mathfrak{M}, v \models \psi$, so $\mathfrak{M}, w \models \lozenge \psi$.
8. Steps 1 to 7 cover every formation rule, so $P(\varphi)$ holds for every formula by structural induction.

### Part B: generated submodels

9. Let $\mathfrak{N} = (U, R \cap U^2, V(\cdot) \cap U)$ be a generated submodel and $I = \{(u, u) : u \in U\}$.
   The set $I$ is nonempty because $U \neq \emptyset$.
10. The atom clause holds because $u \in V(p) \cap U$ exactly when $u \in V(p)$, for $u \in U$.
11. Zig holds because a move $u (R \cap U^2) v$ is also a move $u R v$, and $v I v$.
12. Zag holds because a move $u R v$ in $\mathfrak{M}$ has $v \in U$, since $U$ is closed under $R$, so it is a move of $\mathfrak{N}$ with $v I v$.
13. So $I$ is a bisimulation, and Part A gives item 1.

### Part C: bounded morphisms

14. Let $f$ be a bounded morphism and $G = \{(w, f(w)) : w \in W\}$, which is nonempty because $W \neq \emptyset$.
15. The atom clause is part of the definition of a bounded morphism.
16. Zig holds because $w R v$ gives $f(w) R' f(v)$ by the forth condition, and $v G f(v)$.
17. Zag holds because $f(w) R' v'$ gives, by the back condition, some $v$ with $w R v$ and $f(v) = v'$, so $v G v'$.
18. So $G$ is a bisimulation, and Part A gives item 2.

### Part D: disjoint unions

19. Let $(u, v)$ be an arrow of the union with $u \in W_i$.
   The arrow lies in some $R_j$, and $u \in W_j$ forces $j = i$ because the sets $W_j$ are pairwise disjoint, so $v \in W_i$.
20. So $\mathfrak{M}_i$ is a generated submodel of $\biguplus_j \mathfrak{M}_j$, and Part B gives item 3.

This proves the theorem.

## Idea

Each clause of a bisimulation is shaped to match one clause of the truth definition.
The atom clause handles variables, the Boolean cases need nothing, and zig and zag carry a witness for $\lozenge$ across in each direction.
Once the main claim is in place, the three constructions need only one check each: that they are bisimulations.

## Variants

A game proof runs the same way.
A formula of modal depth $n$ is decided by the first $n$ rounds of the bisimulation game, and Duplicator survives every round when the worlds are bisimilar.
The same induction works with one relation for each modality, and so for labeled transition systems.
For the frame versions, start from any valuation on the new frame and move it to the old one.
Along a surjective bounded morphism you pull the valuation back, and on a generated subframe you extend it to the whole frame in any way.
