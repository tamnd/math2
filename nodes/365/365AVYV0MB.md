---
tag: 365AVYV0MB
kind: example
name: Common knowledge by reachability in a four-world model
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [7BCMKF2P7X]
uses: [RRRHWH9F6Y, 8K0CMPQXXB, 05J9NWX07X, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Modal logic (syntactic characterization)
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 2
---

## Example

We decide which facts are [[common knowledge|7BCMKF2P7X]] in a small model by a graph search.
There are two agents $a$ and $b$ and four worlds $w_1, w_2, w_3, w_4$.
Each relation is an [[equivalence relation|0G8VEZ3WTK]], and we give it by its classes.
Agent $a$ has the classes $\{w_1, w_2\}$, $\{w_3\}$ and $\{w_4\}$.
Agent $b$ has the classes $\{w_1\}$, $\{w_2, w_3\}$ and $\{w_4\}$.
The atom $p$ is true at $w_1, w_2, w_3$, and the atom $q$ is true at $w_1, w_2$.
Let $G = \{a, b\}$, and evaluate at $w_1$.

1. From $w_1$, agent $a$ reaches $w_2$, and from $w_2$, agent $b$ reaches $w_3$.
2. No class that contains $w_1$, $w_2$ or $w_3$ contains $w_4$.
   So the worlds reachable from $w_1$ in one or more steps are $w_1$, $w_2$ and $w_3$.
3. The atom $p$ is true at all three, so $C_G p$ is true at $w_1$ by [[the reachability clause|8K0CMPQXXB]].
4. The atom $q$ is false at $w_3$, which is reachable, so $C_G q$ is false at $w_1$.
5. Still $E_G q$ is true at $w_1$, because $q$ holds on $a$'s class $\{w_1, w_2\}$ and on $b$'s class $\{w_1\}$.
6. $E_G^2 q$ is false at $w_1$.
   It needs $E_G q$ at $w_2$, hence $K_b q$ at $w_2$, but $b$'s class $\{w_2, w_3\}$ contains $w_3$.
7. At $w_4$ the only reachable world is $w_4$, so $C_G \neg p$ is true at $w_4$.

So at $w_1$ both agents know $q$, but $q$ is not common knowledge, while $p$ is.

## Remarks

The reachable sets are the classes of the [[transitive closure|05J9NWX07X]] of $R_a \cup R_b$, here $\{w_1, w_2, w_3\}$ and $\{w_4\}$.
They are the blocks of the meet of the two partitions, as in [[the partition form of the definition|RRRHWH9F6Y]].
Common knowledge is constant on each block, so $C_G \varphi$ has the same value at $w_1$, $w_2$ and $w_3$.

The level at which "everyone knows" breaks is the distance from $w_1$ to the nearest world without $q$, which is two steps.
If we make $q$ true at $w_3$ as well, then $q$ holds on the whole block, and $C_G q$ becomes true at $w_1$.
If instead we merge $\{w_3\}$ and $\{w_4\}$ for agent $a$, the block grows to all four worlds, and $p$ stops being common knowledge.

## Explanations

### L1 human

Draw the four worlds, and connect two of them when some agent cannot tell them apart.
A fact is common knowledge when it holds everywhere in the connected piece that contains the actual world.
The atom $p$ holds on the whole piece, so it is common knowledge.
The atom $q$ fails at the far end of the piece, so it is not, even though both agents know it.

### L2 human

We find the first $k$ with $E_G^k q$ false at $w_1$ by distances.
By Lemma B of [[the proof|8Y7VESEXNG]], $E_G^k q$ holds at $w_1$ when $q$ holds at every world exactly $k$ steps away.
Each relation is reflexive, so a path can wait in place, and the worlds exactly $k$ steps away are the worlds within $k$ steps.
The world $w_3$ is two steps away and not one, so $E_G q$ holds and $E_G^2 q$ fails.
The typical use is to read the depth of mutual knowledge from a picture.
Watch out: without reflexivity, "within $k$ steps" and "exactly $k$ steps" differ, and the distance shortcut fails.

### L3 human

Checking $C_G$ in a finite model is a connected component computation, linear in the size of the model.
For $\mathsf{S5}$ models the components are the blocks of the meet partition, which is why Aumann's partition definition matches the modal one.
