---
tag: RRRHWH9F6Y
kind: definition
name: Common knowledge
msc: [03B42, 91A27]
topics: [CQM9SRN8PM]
audience: grad
defines: 7BCMKF2P7X
uses: [08QMKTWF9T, ERG3KAQWYF, EA34W4ERRE, 05J9NWX07X, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Modal logic (syntactic characterization), section Set theoretic (semantic characterization)
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 2
---

## Definition

Common knowledge of a fact in a group is the conjunction of all finite levels of "everyone knows that everyone knows", and it has a Kripke form and a partition form.

Kripke form.
Let $\mathcal{A}$ be a finite set of agents, and let $M = (W, (R_a)_{a \in \mathcal{A}}, V)$ be a [[multimodal Kripke model|ERG3KAQWYF]] of [[epistemic logic|EA34W4ERRE]].
Let $G \subseteq \mathcal{A}$ be a nonempty group.
Define $E_G \varphi = \bigwedge_{a \in G} K_a \varphi$, $E_G^1 \varphi = E_G \varphi$ and $E_G^{k+1} \varphi = E_G E_G^k \varphi$.
We add to the language an operator $C_G$ for each group, with the following clause.
$$M, w \models C_G \varphi \iff M, w \models E_G^k \varphi \text{ for every } k \ge 1.$$
Then $\varphi$ is *common knowledge* in $G$ at $w$.

Partition form.
Let $\Omega$ be a set of states and $I$ a finite set of agents.
For each $i \in I$ let $\mathcal{P}_i$ be a [[partition|08QMKTWF9T]] of $\Omega$, and let $\mathcal{P}_i(\omega)$ be the block of $\mathcal{P}_i$ that contains $\omega$.
An *event* is a subset $E \subseteq \Omega$, and agent $i$ *knows* $E$ at $\omega$ when $\mathcal{P}_i(\omega) \subseteq E$.
We write $K_i(E) = \{\omega \in \Omega : \mathcal{P}_i(\omega) \subseteq E\}$.
The event $E$ is *common knowledge* at $\omega$ when $\omega \in K_{i_1} K_{i_2} \cdots K_{i_m}(E)$ for every $m \ge 1$ and all agents $i_1, \dots, i_m \in I$.

## Notation

We write $C_G \varphi$, or $C \varphi$ when $G$ is the set of all agents, and some authors write $CK_G$.
The formula $E_G \varphi$ is *mutual knowledge*.
In the partition form, $\mathcal{P}_i$ is the *information partition* of agent $i$.

## Remarks

### Why the two forms agree

A partition $\mathcal{P}_i$ is the set of classes of an [[equivalence relation|0G8VEZ3WTK]] $R_i$, with $\omega R_i \omega'$ when $\mathcal{P}_i(\omega) = \mathcal{P}_i(\omega')$.
If we read $E$ as a proposition true exactly on $E$, then $K_i(E)$ is the truth set of $K_i$ applied to it.
Each $E_G^m \varphi$ is equivalent to the conjunction of all $K_{i_1} \cdots K_{i_m} \varphi$ with $i_1, \dots, i_m \in G$, because each $K_i$ commutes with conjunction.
So both forms ask for every finite string of knowledge operators.
By [[the theorem on common knowledge|8K0CMPQXXB]], this is the same as truth at every world reachable in one or more steps along $\bigcup_{a \in G} R_a$, the [[transitive closure|05J9NWX07X]] of the union.
The Kripke form does not ask the relations to be equivalence relations, so it also covers common belief.

### The meet of the partitions

Let the meet $\mathcal{M}$ be the finest partition that is coarser than every $\mathcal{P}_i$.
Then $E$ is common knowledge at $\omega$ exactly when $\mathcal{M}(\omega) \subseteq E$.
For finite $\Omega$, the block $\mathcal{M}(\omega)$ is the set of states reached from $\omega$ by chains of steps, each inside one block of some $\mathcal{P}_i$.

For example, let $\Omega = \{1, 2, 3, 4\}$, $\mathcal{P}_1 = \{\{1, 2\}, \{3, 4\}\}$ and $\mathcal{P}_2 = \{\{1\}, \{2\}, \{3, 4\}\}$.
The meet is $\{\{1, 2\}, \{3, 4\}\}$, so $E = \{1, 2\}$ is common knowledge at $1$.
Check: $K_1(E) = E$ and $K_2(E) = E$, so every iterate of the $K_i$ applied to $E$ is $E$, which contains $1$.

### A case that fails

Let $\Omega = \{1, 2, 3\}$, $\mathcal{P}_1 = \{\{1, 2\}, \{3\}\}$, $\mathcal{P}_2 = \{\{1\}, \{2, 3\}\}$ and $E = \{1, 2\}$.
Agent 1 knows $E$ on $K_1(E) = \{1, 2\}$, and agent 2 knows it on $K_2(E) = \{1\}$, so both know $E$ at $1$.
One more level gives the following.
$$K_1 K_2(E) = K_1(\{1\}) = \emptyset.$$
At $1$, agent 1 cannot rule out state $2$, where agent 2 does not know $E$, so $E$ is mutual knowledge at $1$ but not common knowledge.
The meet has the single block $\{1, 2, 3\}$, which is not inside $E$, and that agrees.
The [[concept|7BCMKF2P7X]] gives the same model in Kripke form.

## Explanations

### L1 human

A fact is common knowledge when everyone knows it, everyone knows that everyone knows it, and so on forever.
In a picture of possible worlds, each person cannot tell some worlds apart.
Common knowledge means the fact is true in every world you can reach by hopping between worlds that someone cannot tell apart.

### L2 human

In the failing case above, the chain breaks at the second level, and we can see why by following the hops.
From state $1$, agent 1 hops to $2$, and from $2$, agent 2 hops to $3$, where $E$ is false.
That path has two hops, so the level "1 knows that 2 knows" is the first to fail.
The typical use is to find that first broken level.
Watch out: $K_i(E)$ is a union of blocks of $\mathcal{P}_i$, so it can be much smaller than $E$, and here $K_2(E)$ loses the state $2$.

### L3 human

The partition form is Aumann's, and the Kripke form is the one used in logic and computer science.
The definition is an infinite conjunction, but the fixed point axiom and the induction rule of [[the theorem|8K0CMPQXXB]] axiomatize it with finitely many schemes.
