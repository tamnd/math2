---
tag: ~f1b3fa0e
kind: proof
name: Proof of the disjunction property by gluing Kripke models
msc: ["03B20"]
topics: [38EQ20GR7M]
audience: grad
proves: ~59f11dc8
uses: [~11b532e9, ~ac029000]
methods: [0BB5TPGQ1N, 12MQ2NJ29A]
sources:
  - url: https://plato.stanford.edu/entries/logic-intuitionistic/
    locator: 5.1 Kripke and Beth semantics for intuitionistic logic
---

## Proof

This proof gives item 1 of the theorem.
We use [[Kripke models|~11b532e9]] and [[Kripke soundness and completeness|~ac029000]].

1. Lemma: in a Kripke model, whether $w \Vdash \chi$ depends only on the worlds $v \geq w$ and their valuation.
2. Proof of the lemma: by induction on $\chi$. The clauses for atoms, $\bot$, $\wedge$ and $\vee$ look only at $w$. The clause for $\to$ looks only at worlds $v \geq w$.
3. Suppose $\mathsf{IPC} \nvdash \varphi$ and $\mathsf{IPC} \nvdash \psi$. We show $\mathsf{IPC} \nvdash \varphi \vee \psi$.
4. By completeness, there is a rooted model $\mathfrak{M}_1$ with root $r_1$ and $r_1 \nVdash \varphi$.
5. In the same way, there is a rooted model $\mathfrak{M}_2$ with root $r_2$ and $r_2 \nVdash \psi$.
6. Take the two models with disjoint sets of worlds. Add a new world $r$ below every world of both.
7. The new order is reflexive, transitive and antisymmetric. Let $r$ force no variable. Each $V(p)$ is still an up-set.
8. Call the new model $\mathfrak{M}$. In $\mathfrak{M}$, the worlds above $r_1$ are those of $\mathfrak{M}_1$, with the same valuation.
9. By the lemma, $r_1 \nVdash \varphi$ in $\mathfrak{M}$. In the same way, $r_2 \nVdash \psi$ in $\mathfrak{M}$.
10. If $r \Vdash \varphi$, then $r_1 \Vdash \varphi$ by persistence, since $r \leq r_1$. So $r \nVdash \varphi$.
11. In the same way, $r \nVdash \psi$, by persistence to $r_2$.
12. By the clause for disjunction, $r \nVdash \varphi \vee \psi$.
13. By soundness, $\mathsf{IPC} \nvdash \varphi \vee \psi$. This is the contrapositive of item 1.

## Idea

Two countermodels, one for each disjunct, are placed side by side.
A new root below both sees both failures.
At the root neither disjunct holds, since each would persist upward into its own countermodel.
So the disjunction fails at the root.

## Variants

1. The same gluing proves the disjunction property for every logic that is complete for a class of rooted frames closed under this operation.
2. The proof fails for [[Gödel-Dummett logic|~cfc28e48]], since gluing two chains below a new root gives a fork, which is not linear.
3. The [[slash proof|~35cd3b76]] gives the same result syntactically, and extends to sets of Harrop premises.
