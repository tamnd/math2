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

The modal $\mu$-calculus is the extension of [[modal logic|C3RZY20ETK]] by a binder $\mu X$ that takes least fixed points of monotone maps on sets of worlds.

Let $P$ be a set of propositional variables, $A$ a set of actions, and $\mathcal{V}$ a set of fixed-point variables.
The formulas of the modal $\mu$-calculus are given by the grammar below.
$$\varphi ::= p \mid X \mid \neg \varphi \mid \varphi \wedge \varphi \mid \langle a \rangle \varphi \mid \mu X . \varphi, \qquad p \in P, \ a \in A, \ X \in \mathcal{V}.$$
There is one condition: in $\mu X . \varphi$, every free occurrence of $X$ in $\varphi$ lies under an even number of negations.

A model is a Kripke model with one relation for each action, $\mathfrak{M} = (W, (R_a)_{a \in A}, V)$.
Here $W$ is a nonempty set, each $R_a \subseteq W \times W$, and $V \colon P \to \mathcal{P}(W)$.
A valuation of the fixed-point variables is a map $\rho \colon \mathcal{V} \to \mathcal{P}(W)$.
The set $\|\varphi\|_\rho \subseteq W$ of worlds where $\varphi$ is true is defined by induction on $\varphi$.

1. $\|p\|_\rho = V(p)$ and $\|X\|_\rho = \rho(X)$.
2. $\|\neg \varphi\|_\rho = W \setminus \|\varphi\|_\rho$ and $\|\varphi \wedge \psi\|_\rho = \|\varphi\|_\rho \cap \|\psi\|_\rho$.
3. $\|\langle a \rangle \varphi\|_\rho = \{ w \in W : w R_a v \text{ for some } v \in \|\varphi\|_\rho \}$.
4. $\|\mu X . \varphi\|_\rho = \bigcap \{ T \subseteq W : \|\varphi\|_{\rho[X \mapsto T]} \subseteq T \}$.

Here $\rho[X \mapsto T]$ agrees with $\rho$ except that it sends $X$ to $T$.
We write $\mathfrak{M}, w \models_\rho \varphi$ for $w \in \|\varphi\|_\rho$, and we drop $\rho$ when $\varphi$ has no free fixed-point variables.

## Notation

The other connectives are abbreviations: $\varphi \vee \psi$ is $\neg (\neg \varphi \wedge \neg \psi)$, and $[a] \varphi$ is $\neg \langle a \rangle \neg \varphi$.
The greatest fixed point is $\nu X . \varphi = \neg \mu X . \neg \varphi[\neg X / X]$, where $\varphi[\neg X / X]$ replaces each free $X$ by $\neg X$.
With one action we write $\square$ and $\lozenge$, and $(W, R, V)$ for the model.
Many books work only with formulas in negation normal form, where $\neg$ stands only before propositional variables and $\vee$, $[a]$ and $\nu$ are primitive.
Every formula is equivalent to one in this form.
You will also see $\|\varphi\|^{\mathfrak{M}}_\rho$ or $[\![\varphi]\!]_\rho$ for the set of worlds.

## Remarks

### Why the condition on negations

The condition makes the map $T \mapsto \|\varphi\|_{\rho[X \mapsto T]}$ a [[monotone function|0A7KV2WB7A]] on the [[complete lattice|D7A0ZGZT5S]] $(\mathcal{P}(W), \subseteq)$.
The reason is an induction on $\varphi$: each negation above $X$ reverses inclusion, and an even number of reversals leaves it the right way round.
Without the condition clause 4 can give a set that is no fixed point at all.
For $\varphi = \neg X$ the map is $T \mapsto W \setminus T$, and $T = W \setminus T$ is impossible when $W$ is nonempty.
So $\mu X . \neg X$ is not a formula.

### Why clause 4 is a least fixed point

Clause 4 takes the intersection of all pre-fixed points, the sets $T$ with $\|\varphi\|_{\rho[X \mapsto T]} \subseteq T$.
By the [[Knaster-Tarski theorem|RHXP3HA64M]], for a monotone map this intersection is the [[least fixed point|DBD64TH52D]].
Dually, $\|\nu X . \varphi\|_\rho$ is the union of all post-fixed points, the sets $T$ with $T \subseteq \|\varphi\|_{\rho[X \mapsto T]}$, and that is the greatest fixed point.
On a finite model with $n$ worlds you can also iterate.
Put $T_0 = \emptyset$ and $T_{k+1} = \|\varphi\|_{\rho[X \mapsto T_k]}$; the sets grow, so $T_n$ is the least fixed point.
The greatest fixed point is reached in the same way from $T_0 = W$.

### A small case

Take $W = \{1, 2\}$ with $R = \{(1, 2)\}$, and the formula $\mu X . \square X$.
The map is $T \mapsto \{ w : \text{every successor of } w \text{ is in } T \}$.
Iterate from the empty set:
$$T_0 = \emptyset, \quad T_1 = \{2\}, \quad T_2 = \{1, 2\}, \quad T_3 = \{1, 2\}.$$
World $2$ enters first because it has no successor, and world $1$ enters once its successor is in.
In general this formula says "every path is finite", as the overview of the [[modal mu-calculus|MZ0M2KR9S0]] explains.

## Explanations

### L1 human

The modal $\mu$-calculus lets a formula mention itself, like a recursive definition in a program.
The formula $\mu X . (p \vee \lozenge X)$ says "$p$ holds here, or one step leads to a world where this same formula holds".
To find where it is true, start with no worlds and keep adding the worlds that satisfy the right side.
In a chain of worlds $1 \to 2 \to 3$ with $p$ true only at $3$, we add $3$, then $2$, then $1$.

### L2 human

We compare the two fixed points of $\square X$ when a loop is present.
Take $W = \{1, 2, 3\}$ with $R = \{(1, 2), (3, 3)\}$.
For $\mu X . \square X$, start from $\emptyset$.
World $2$ has no successor, so it enters at once, then world $1$ enters, and world $3$ never does, because its only successor is itself:
$$T_0 = \emptyset, \quad T_1 = \{2\}, \quad T_2 = \{1, 2\} = T_3.$$
For $\nu X . \square X$, start from $W$.
Every world has all its successors in $W$, so $T_1 = W$, and the greatest fixed point is $W$.
The two answers differ exactly at world $3$, which has the infinite path $3, 3, 3, \dots$.
This is the typical lesson: $\mu$ rules out infinite behavior and $\nu$ allows it, so pick the binder before you compute.

### L3 human

The definition is the powerset case of a general scheme: a language of monotone operators on a complete lattice, closed under least and greatest fixed points.
The same scheme gives fixed-point logics over first-order structures, such as least fixed-point logic in finite model theory.
The modal $\mu$-calculus is the case where the basic operators are the Boolean operations and the maps $T \mapsto \{ w : w R_a v \text{ for some } v \in T \}$.
