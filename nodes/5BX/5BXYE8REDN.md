---
tag: 5BXYE8REDN
kind: definition
name: Modal mu-calculus
msc: ["03B45", "03B70", "68Q60"]
topics: [SPQVNPZDTB]
audience: research
defines: MZ0M2KR9S0
uses: [C3RZY20ETK, NGHWZ9Y7ZV, DBD64TH52D, RHXP3HA64M, 0A7KV2WB7A, D7A0ZGZT5S]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
    locator: Syntax
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
    locator: Denotational semantics
---

## Definition

Let $P$ be a set of propositional variables, $A$ a set of actions, and $\mathcal{V}$ a set of fixed-point variables.
The formulas of the modal $\mu$-calculus are given by the grammar
$$\varphi ::= p \mid X \mid \neg \varphi \mid \varphi \wedge \varphi \mid \langle a \rangle \varphi \mid \mu X . \varphi, \qquad p \in P, \ a \in A, \ X \in \mathcal{V},$$
with one condition: in $\mu X . \varphi$, every free occurrence of $X$ in $\varphi$ lies under an even number of negations.

A model is a Kripke model with one relation for each action, $\mathfrak{M} = (W, (R_a)_{a \in A}, V)$, where $W$ is a nonempty set, each $R_a \subseteq W \times W$, and $V \colon P \to \mathcal{P}(W)$.
A valuation of the fixed-point variables is a map $\rho \colon \mathcal{V} \to \mathcal{P}(W)$.
The set $\|\varphi\|_\rho \subseteq W$ of worlds where $\varphi$ is true is defined by induction on $\varphi$:

1. $\|p\|_\rho = V(p)$ and $\|X\|_\rho = \rho(X)$;
2. $\|\neg \varphi\|_\rho = W \setminus \|\varphi\|_\rho$ and $\|\varphi \wedge \psi\|_\rho = \|\varphi\|_\rho \cap \|\psi\|_\rho$;
3. $\|\langle a \rangle \varphi\|_\rho = \set{w \in W : w R_a v \text{ for some } v \in \|\varphi\|_\rho}$;
4. $\|\mu X . \varphi\|_\rho = \bigcap \set{T \subseteq W : \|\varphi\|_{\rho[X \mapsto T]} \subseteq T}$.

Here $\rho[X \mapsto T]$ agrees with $\rho$ except that it sends $X$ to $T$.
We write $\mathfrak{M}, w \models_\rho \varphi$ for $w \in \|\varphi\|_\rho$, and we drop $\rho$ when $\varphi$ has no free fixed-point variables.

## Notation

1. The other connectives are abbreviations: $\varphi \vee \psi = \neg (\neg \varphi \wedge \neg \psi)$, $[a] \varphi = \neg \langle a \rangle \neg \varphi$, and $\nu X . \varphi = \neg \mu X . \neg \varphi[\neg X / X]$, where $\varphi[\neg X / X]$ replaces each free $X$ by $\neg X$.
2. With one action we write $\square$ and $\lozenge$ for $[a]$ and $\langle a \rangle$, and $(W, R, V)$ for the model.
3. Many books use only formulas in negation normal form: negation is applied only to propositional variables, and $\vee$, $[a]$ and $\nu$ are primitive. Every formula is equivalent to one in this form.
4. Some books write $\|\varphi\|^{\mathfrak{M}}_\rho$ or $[\![\varphi]\!]_\rho$ for the set of worlds.

## Remarks

The condition on negations makes the map $T \mapsto \|\varphi\|_{\rho[X \mapsto T]}$ a [[monotone function|0A7KV2WB7A]] on the [[complete lattice|D7A0ZGZT5S]] $(\mathcal{P}(W), \subseteq)$.
The proof is by induction on $\varphi$: an even number of negations above $X$ means an even number of reversals of $\subseteq$.
By the [[Knaster-Tarski theorem|RHXP3HA64M]], clause 4 is the [[least fixed point|DBD64TH52D]] of this map, and $\|\nu X . \varphi\|_\rho$ is its greatest fixed point, the union of all $T$ with $T \subseteq \|\varphi\|_{\rho[X \mapsto T]}$.
On a finite model with $n$ worlds, the least fixed point is reached by iteration: put $T_0 = \emptyset$ and $T_{k+1} = \|\varphi\|_{\rho[X \mapsto T_k]}$; then $T_n$ is the least fixed point.
The greatest fixed point is reached in the same way from $T_0 = W$.

Without the condition on negations, clause 4 can give a set that is not a fixed point.
For $\varphi = \neg X$ the map is $T \mapsto W \setminus T$, which has no fixed point, since $T = W \setminus T$ is impossible for a nonempty $W$.
So $\mu X . \neg X$ is not a formula.

## Explanations

### L1 human

The modal $\mu$-calculus lets a formula mention itself, like a recursive definition in a program.
The formula $\mu X . (p \vee \lozenge X)$ says: "$p$ holds here, or one step leads to a world where this same formula holds".
To find where it is true, start with no worlds, and keep adding the worlds that satisfy the right side.
In a chain of worlds $1 \to 2 \to 3$ with $p$ true only at $3$, we add $3$, then $2$, then $1$.

### L2 human

We compute $\|\nu X . \square X\|$ on a model with one action.

1. Let $W = \{1, 2\}$ and $R = \{(1, 2)\}$. The map is $T \mapsto \|\square X\|_{[X \mapsto T]} = \set{w : \text{every } R\text{-successor of } w \text{ lies in } T}$.
2. Start from $T_0 = W = \{1, 2\}$. Every world has all its successors in $W$, so $T_1 = \{1, 2\}$.
3. $T_1 = T_0$, so the greatest fixed point is $\{1, 2\}$.
4. Now compute $\|\mu X . \square X\|$ from $T_0 = \emptyset$. World $2$ has no successor, so $2 \in T_1$, and $1 \notin T_1$ because its successor $2 \notin \emptyset$. So $T_1 = \{2\}$.
5. $T_2 = \{1, 2\}$, since the successor $2$ of $1$ lies in $T_1$. $T_3 = T_2$, so the least fixed point is $\{1, 2\}$.

The least fixed point $\mu X . \square X$ holds at the worlds from which every path is finite.
Here both fixed points agree, because the model has no infinite path.
A trap: on a model with a loop $3 R 3$, the world $3$ lies in the greatest fixed point and not in the least one.

### L3 human

The definition is the special case for powerset lattices of a general scheme: a language of monotone operators on a complete lattice, closed under least and greatest fixed points.
The same scheme gives fixed-point logics over first-order structures, such as least fixed-point logic in finite model theory.
The modal $\mu$-calculus is the case where the basic operators are the Boolean operations and the maps $T \mapsto \set{w : w R_a v \text{ for some } v \in T}$, which are the operators of basic modal logic.
