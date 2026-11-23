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

We compute the set of each subformula from the inside out, and we show that each operator costs one linear pass over the structure.
We prove [[the theorem|1A990HC0FJ]] for the basic operators of [[the definition|1DA0Y6KDF8]], and write $n = \lvert S \rvert + \lvert R \rvert$.
We store each set of states as a Boolean array, and each state with its lists of successors and predecessors.
We cite one standard fact: [[Tarjan's algorithm|5XY87RKYJ4]] finds the strongly connected components of a graph in linear time.

### Order and the easy cases

1. List the subformulas of $\varphi$ by increasing size, and compute $[\![\psi]\!]$ for each $\psi$ in this order, so that the sets of its immediate subformulas are already known.
   There are $\lvert\varphi\rvert$ steps, so it suffices to show that each step costs $O(n)$.
2. Atoms, $\neg$ and $\wedge$ are computed state by state from $L$ and the known arrays, in time $O(\lvert S \rvert)$.
3. For $EX\psi$, mark $s$ for each edge $(s, t)$ with $t \in [\![\psi]\!]$.
   This takes $O(n)$ and marks exactly the states with a $\psi$-successor.

### Until

4. For $E[\psi_1 U \psi_2]$, mark the states of $[\![\psi_2]\!]$ and put them in a queue.
   Take a state $t$ from the queue, mark each unmarked predecessor $s$ of $t$ with $s \in [\![\psi_1]\!]$, and add $s$ to the queue.
5. Each state enters the queue at most once, so each edge is used at most once, and the time is $O(n)$.
6. A state is marked exactly when there is a finite path $s = s_0, \dots, s_j$ with $s_j \in [\![\psi_2]\!]$ and $s_i \in [\![\psi_1]\!]$ for $i < j$.
   One direction holds by induction on the order of marking, and the other by induction on $j$.
7. Since $R$ is total, such a finite path extends to an infinite path.
   So the marked states are exactly $[\![ E[\psi_1 U \psi_2] ]\!]$, by clause 4 of the definition.

### Always along some path

8. Let $S' = [\![\psi]\!]$ and $R' = R \cap (S' \times S')$.
   Call a strongly connected component of $(S', R')$ nontrivial if it has an edge, that is, two states or a loop.
9. We claim that $s \models EG\psi$ if and only if $s \in S'$ and $(S', R')$ has a path from $s$ to a nontrivial component.
10. Suppose $s \models EG\psi$, so some infinite path from $s$ stays in $S'$, and so it is a path of $(S', R')$.
    Since $S'$ is finite, some state $u$ occurs on it twice, and the part between the two occurrences is a cycle.
    So $u$ lies in a nontrivial component, and the part of the path before $u$ goes from $s$ to $u$.
11. Conversely, follow a path from $s$ to a state $u$ in a nontrivial component, and then a cycle from $u$ back to $u$ inside the component.
    Going around the cycle forever gives an infinite path in $S'$, so $s \models EG\psi$.
12. To compute the set, build $(S', R')$ in time $O(n)$, find its components with Tarjan's algorithm in time $O(n)$, and mark the states of the nontrivial ones.
    Then search backwards from the marked states along $R'$, as in step 4.
    By the claim of step 9 the result is $[\![ EG\psi ]\!]$, in time $O(n)$.

### Derived operators

13. The operators $AX$, $AF$, $AG$, $EF$ and $A[\,\cdot \, U \, \cdot\,]$ are rewritten with the abbreviations of the definition.
    The rewriting multiplies the number of distinct subformulas by at most a constant, so the bound remains $O(\lvert\varphi\rvert \cdot n)$.

## Idea

Every CTL subformula is a set of states, so the formula can be evaluated from the inside out, one operator at a time.
Until is backward reachability from the goal states through the allowed states.
"Always along some path" is reachability of a cycle that stays inside the states where the formula holds, and strongly connected components find all such cycles at once.

## Variants

Instead of components, one can compute $[\![ EG\psi ]\!]$ as the greatest fixpoint of $Z \mapsto [\![\psi]\!] \cap \mathrm{pre}(Z)$, where $\mathrm{pre}(Z)$ is the set of states with a successor in $Z$.
Iterating this map is simpler, but it can take time $O(\lvert S \rvert \cdot n)$.
Symbolic model checking computes the same fixpoints on sets represented by binary decision diagrams.
