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

Fix the models $\mathfrak{M} = (W, R, V)$, $\mathfrak{M}' = (W', R', V')$ and the [[bisimulation|7T740SFHHV]] $Z$.
We prove by structural induction on $\varphi$ the claim $P(\varphi)$: for all $w Z w'$, $\mathfrak{M}, w \models \varphi$ if and only if $\mathfrak{M}', w' \models \varphi$.
The truth clauses are those of [[Kripke semantics|NGHWZ9Y7ZV]].

Part A: the main claim.

1. Case $\varphi = p$, a variable. Let $w Z w'$. By the truth clause, $\mathfrak{M}, w \models p$ means $w \in V(p)$. By the atom clause, this holds if and only if $w' \in V'(p)$, that is, $\mathfrak{M}', w' \models p$.
2. Case $\varphi = \bot$. The formula $\bot$ is false at every world of both models, so both sides of $P(\bot)$ are false.
3. Case $\varphi = \neg \psi$. Assume $P(\psi)$, and let $w Z w'$. Then $w \models \neg \psi$ iff $w \not\models \psi$ iff $w' \not\models \psi$ iff $w' \models \neg \psi$, where the middle step is $P(\psi)$.
4. Case $\varphi = \psi \wedge \chi$. Assume $P(\psi)$ and $P(\chi)$, and let $w Z w'$. Then $w \models \psi \wedge \chi$ iff $w \models \psi$ and $w \models \chi$, iff $w' \models \psi$ and $w' \models \chi$, iff $w' \models \psi \wedge \chi$.
5. Case $\varphi = \lozenge \psi$, from left to right. Assume $P(\psi)$, $w Z w'$ and $\mathfrak{M}, w \models \lozenge \psi$. By the truth clause there is $v$ with $w R v$ and $\mathfrak{M}, v \models \psi$.
6. By the zig clause there is $v'$ with $w' R' v'$ and $v Z v'$. By $P(\psi)$ applied to $v Z v'$, $\mathfrak{M}', v' \models \psi$. So $\mathfrak{M}', w' \models \lozenge \psi$.
7. Case $\varphi = \lozenge \psi$, from right to left. Assume $\mathfrak{M}', w' \models \lozenge \psi$, so $w' R' v'$ and $\mathfrak{M}', v' \models \psi$ for some $v'$.
8. By the zag clause there is $v$ with $w R v$ and $v Z v'$. By $P(\psi)$, $\mathfrak{M}, v \models \psi$, so $\mathfrak{M}, w \models \lozenge \psi$.
9. Steps 1 to 8 cover every formation rule of the basic modal language. By structural induction, $P(\varphi)$ holds for every formula $\varphi$.

Part B: generated submodels.

10. Let $\mathfrak{N} = (U, R \cap U^2, V(\cdot) \cap U)$ be a generated submodel of $\mathfrak{M}$, and let $I = \set{(u, u) : u \in U}$. The set $I$ is nonempty, since $U \neq \emptyset$.
11. Atom clause: $u \in V(p) \cap U$ iff $u \in V(p)$, because $u \in U$.
12. Zig clause: if $u (R \cap U^2) v$, then $u R v$ and $v I v$.
13. Zag clause: if $u R v$ in $\mathfrak{M}$, then $v \in U$ because $U$ is closed under $R$. So $u (R \cap U^2) v$ and $v I v$.
14. So $I$ is a bisimulation, and Part A gives item 1.

Part C: bounded morphisms.

15. Let $f$ be a bounded morphism and $G = \set{(w, f(w)) : w \in W}$. The set $G$ is nonempty, since $W \neq \emptyset$.
16. Atom clause: $w$ and $f(w)$ satisfy the same variables, by the definition of a bounded morphism.
17. Zig clause: if $w R v$, then $f(w) R' f(v)$ by the forth condition, and $v G f(v)$.
18. Zag clause: if $f(w) R' v'$, then the back condition gives $v$ with $w R v$ and $f(v) = v'$, so $v G v'$.
19. So $G$ is a bisimulation, and Part A gives item 2.

Part D: disjoint unions.

20. Each $\mathfrak{M}_i$ is a generated submodel of $\biguplus_j \mathfrak{M}_j$. A pair $(u, v)$ of the union relation with $u \in W_i$ lies in $R_i$, because the sets $W_j$ are pairwise disjoint. So $v \in W_i$.
21. Part B gives item 3.

This proves the theorem.

## Idea

Each clause of a bisimulation matches one clause of the truth definition.
The atom clause handles variables, the Boolean cases need nothing, and zig and zag carry a witness for $\lozenge$ across in each direction.
The three constructions are bisimulations, so they inherit the invariance.

## Variants

The same induction works with one relation for each modality, and so for labelled transition systems.
A second proof uses the bisimulation game: a formula of modal depth $n$ is decided by the first $n$ rounds, and Duplicator survives every round.
For the frame versions, apply the theorem to every valuation on the smaller or larger frame, with the valuation transported along the construction.
