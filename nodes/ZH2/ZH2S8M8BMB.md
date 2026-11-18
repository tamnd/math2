---
tag: ZH2S8M8BMB
kind: proof
name: Proof of linear-time CTL model checking
msc: ["03B44", "68Q60", "68Q25"]
topics: [CQM9SRN8PM]
audience: grad
proves: 1A990HC0FJ
uses: [1DA0Y6KDF8, RFQ8DJZNQT, 5XY87RKYJ4]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapter 6
  - url: https://en.wikipedia.org/wiki/Computation_tree_logic
    locator: section Semantics of CTL
---

## Proof

We prove [[the theorem|1A990HC0FJ]] for the basic operators of [[the definition|1DA0Y6KDF8]].
Write $n = \lvert S \rvert + \lvert R \rvert$.
We store each set of states as a Boolean array, and each state with its lists of successors and predecessors.
We cite one standard fact: [[Tarjan's algorithm|5XY87RKYJ4]] finds the strongly connected components of a graph in linear time.

1. Order. List the subformulas of $\varphi$ by increasing size. We compute $[\![\psi]\!]$ for each $\psi$ in this order, so the sets for its immediate subformulas are known.
2. It suffices to show that each step costs $O(n)$. There are $\lvert\varphi\rvert$ steps, which gives the bound.
3. Atoms, $\neg$ and $\wedge$. These are computed state by state from $L$ and the known arrays, in time $O(\lvert S \rvert)$.
4. $EX\psi$. For each edge $(s, t)$ with $t \in [\![\psi]\!]$, mark $s$. This takes $O(n)$ and marks exactly the states with a $\psi$-successor.
5. $E[\psi_1 U \psi_2]$, algorithm. Mark the states of $[\![\psi_2]\!]$ and put them in a queue. Take a state $t$ from the queue. Mark each unmarked predecessor $s$ of $t$ with $s \in [\![\psi_1]\!]$, and add it to the queue.
6. Each state enters the queue at most once, so each edge is used at most once. The time is $O(n)$.
7. $E[\psi_1 U \psi_2]$, correctness. A state is marked exactly when there is a finite path $s = s_0, \dots, s_j$ with $s_j \in [\![\psi_2]\!]$ and $s_i \in [\![\psi_1]\!]$ for $i < j$. One direction is by induction on the order of marking, the other by induction on $j$.
8. Since $R$ is total, such a finite path extends to an infinite path. So the marked states are exactly $[\![ E[\psi_1 U \psi_2] ]\!]$ by clause 4 of the definition.
9. $EG\psi$, the lemma. Let $S' = [\![\psi]\!]$ and $R' = R \cap (S' \times S')$. Call a strongly connected component of $(S', R')$ nontrivial if it has an edge, that is, two states or a loop.
10. Claim: $s \models EG\psi$ if and only if $s \in S'$ and $(S', R')$ has a path from $s$ to a nontrivial component.
11. Proof of "only if". A path from $s$ that stays in $S'$ is a path of $(S', R')$. Since $S'$ is finite, some state $u$ occurs on it twice. The part between the two occurrences is a cycle, so $u$ lies in a nontrivial component, and the part before it is a path from $s$ to $u$.
12. Proof of "if". Follow the path from $s$ to a state $u$ in a nontrivial component. From $u$ there is a cycle back to $u$ inside the component. Going around it forever gives an infinite path in $S'$, so $s \models EG\psi$.
13. $EG\psi$, algorithm. Build $(S', R')$ in time $O(n)$. Find its components with Tarjan's algorithm, in time $O(n)$, and mark the states of the nontrivial ones.
14. Then search backwards from the marked states along $R'$, as in step 5. By the claim of step 10, the result is $[\![ EG\psi ]\!]$, in time $O(n)$.
15. Derived operators. $AX$, $AF$, $AG$, $EF$ and $A[\,\cdot \, U \, \cdot\,]$ are rewritten with notation items 1 and 2 of the definition. The rewriting multiplies the number of subformulas by a constant, so the bound remains $O(\lvert\varphi\rvert \cdot n)$.

## Idea

Every CTL subformula is a set of states, so the formula can be evaluated from the inside out.
Until is backward reachability, and "always along some path" is reachability of a cycle inside the states where the formula holds.

## Variants

1. Instead of components, $[\![ EG\psi ]\!]$ is the greatest fixpoint of $Z \mapsto [\![\psi]\!] \cap \mathrm{pre}(Z)$. Iterating it is simpler but can take time $O(\lvert S \rvert \cdot n)$.
2. Symbolic model checking computes the same fixpoints on sets represented by binary decision diagrams.
