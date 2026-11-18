---
tag: RRRHWH9F6Y
kind: definition
name: Common knowledge
msc: [03B42, 91A27]
topics: [CQM9SRN8PM]
audience: grad
defines: 7BCMKF2P7X
uses: [08QMKTWF9T, ERG3KAQWYF, ~8b9604fb, 05J9NWX07X, 0G8VEZ3WTK, ~2e0d432a]
sources:
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Modal logic (syntactic characterization), section Set theoretic (semantic characterization)
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 2
---

## Definition

Kripke form.
Let $\mathcal{A}$ be a finite set of agents, and let $M = (W, (R_a)_{a \in \mathcal{A}}, V)$ be a [[multimodal Kripke model|ERG3KAQWYF]] of [[epistemic logic|~8b9604fb]].
Let $G \subseteq \mathcal{A}$ be a nonempty group.
Define $E_G\varphi = \bigwedge_{a \in G} K_a\varphi$, $E_G^1\varphi = E_G\varphi$ and $E_G^{k+1}\varphi = E_G E_G^k\varphi$.
Add to the language an operator $C_G$ for each group, with the clause
$$M, w \models C_G\varphi \iff M, w \models E_G^k\varphi \text{ for every } k \ge 1.$$
We say $\varphi$ is *common knowledge* in $G$ at $w$.

Partition form.
Let $\Omega$ be a set of states and let $I$ be a finite set of agents.
For each agent $i \in I$, let $\mathcal{P}_i$ be a [[partition|08QMKTWF9T]] of $\Omega$, and for $\omega \in \Omega$ let $\mathcal{P}_i(\omega)$ be the block of $\mathcal{P}_i$ that contains $\omega$.
An *event* is a subset $E \subseteq \Omega$.
Agent $i$ *knows* $E$ at $\omega$ if $\mathcal{P}_i(\omega) \subseteq E$; write $K_i(E) = \set{\omega \in \Omega : \mathcal{P}_i(\omega) \subseteq E}$.
The event $E$ is *common knowledge* at $\omega$ if
$$\omega \in K_{i_1} K_{i_2} \cdots K_{i_m}(E)$$
for every $m \ge 1$ and all agents $i_1, \dots, i_m \in I$.

## Notation

1. $C_G\varphi$, with $C\varphi$ when $G$ is the set of all agents. Some authors write $CK_G$.
2. $E_G\varphi$ is *mutual knowledge*, "everyone in $G$ knows $\varphi$".
3. In the partition form, $\mathcal{P}_i$ is agent $i$'s *information partition*.

## Remarks

The two forms agree.
A partition $\mathcal{P}_i$ is the set of classes of an [[equivalence relation|0G8VEZ3WTK]] $R_i$, where $\omega R_i \omega'$ when $\mathcal{P}_i(\omega) = \mathcal{P}_i(\omega')$.
Read $E$ as a proposition true exactly on $E$.
Then $K_i(E)$ is the truth set of $K_i$ applied to it.
Each $E_G^m\varphi$ is equivalent to the conjunction of all $K_{i_1} \cdots K_{i_m}\varphi$ with $i_1, \dots, i_m \in G$, since each $K_i$ commutes with conjunction.
So both forms ask for every finite string of knowledge operators.

By [[the theorem on common knowledge|~2e0d432a]], $C_G\varphi$ holds at $w$ iff $\varphi$ holds at every world reachable from $w$ in one or more steps along $\bigcup_{a \in G} R_a$.
This is the [[transitive closure|05J9NWX07X]] of the union.

Let the *meet* $\mathcal{M}$ be the finest partition of $\Omega$ that is coarser than every $\mathcal{P}_i$, and let $\mathcal{M}(\omega)$ be its block containing $\omega$.
Then $E$ is common knowledge at $\omega$ if and only if $\mathcal{M}(\omega) \subseteq E$.
For finite $\Omega$, the block $\mathcal{M}(\omega)$ consists of the states reached from $\omega$ by chains of steps.
Each step stays inside one block of some $\mathcal{P}_i$.

Example: let $\Omega = \set{1, 2, 3, 4}$, $\mathcal{P}_1 = \set{\set{1, 2}, \set{3, 4}}$ and $\mathcal{P}_2 = \set{\set{1}, \set{2}, \set{3, 4}}$.
The meet is $\set{\set{1, 2}, \set{3, 4}}$, so $E = \set{1, 2}$ is common knowledge at $\omega = 1$.
Directly: $K_1(E) = E$ and $K_2(E) = E$, so every iterate of the operators $K_i$ applied to $E$ is $E$, which contains $1$.

Non-example: let $\Omega = \set{1, 2, 3}$, $\mathcal{P}_1 = \set{\set{1, 2}, \set{3}}$ and $\mathcal{P}_2 = \set{\set{1}, \set{2, 3}}$, and $E = \set{1, 2}$.
At $\omega = 1$ both agents know $E$, since $K_1(E) = \set{1, 2}$ and $K_2(E) = \set{1}$.
But $K_1 K_2(E) = K_1(\set{1}) = \emptyset$, so agent 1 does not know that agent 2 knows $E$, and $E$ is not common knowledge at $1$.

The event that everyone knows $E$ is $\bigcap_{i \in I} K_i(E)$; it is called *mutual knowledge* and is weaker than common knowledge.

## Explanations

### L1 human

A fact is common knowledge when everyone knows it, everyone knows that everyone knows it, and so on forever.
In a picture of possible worlds, each person cannot tell apart some worlds.
Common knowledge means the fact is true in every world you can reach by hopping between worlds that someone cannot tell apart.

### L2 human

We compute $K_1 K_2(E)$ in the non-example above, step by step.

1. $K_2(E)$: the blocks of $\mathcal{P}_2$ inside $E = \set{1, 2}$ are only $\set{1}$, so $K_2(E) = \set{1}$.
2. $K_1(\set{1})$: no block of $\mathcal{P}_1$ lies inside $\set{1}$, so $K_1 K_2(E) = \emptyset$.
3. So at state $1$, agent 1 cannot rule out state $2$, where agent 2 does not know $E$.

The typical use is to find the first level at which the chain of "knows that knows" breaks.
A trap: $K_i(E)$ is a union of blocks of $\mathcal{P}_i$, so it can be much smaller than $E$.

### L3 human

The partition form is Aumann's, and the Kripke form is the one used in logic and computer science.
In the Kripke form the relations need not be equivalence relations, so the definition also covers common belief.
The definition is an infinite conjunction, but the fixed point axiom and induction rule of [[the theorem|~2e0d432a]] axiomatize it with finitely many schemes.
