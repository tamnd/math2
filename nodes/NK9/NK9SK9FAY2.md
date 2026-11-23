---
tag: NK9SK9FAY2
kind: proof
name: Proof of the finite graph minor theorem and outline of its unprovability
msc: ["03F35", "05C83"]
topics: [T6FK1E7GJ1]
audience: research
proves: WXNTPQGJ38
uses: [WP3GDNWJJW, VYQ32ZBPEE, T9YXK7VPYG, C72RBH0CDR]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Robertson–Seymour_theorem
    locator: Finite form of the graph minor theorem
---

## Proof

We derive the finite form from the infinite Robertson-Seymour theorem by gluing long bad sequences into an infinite one, and we outline the unprovability with the cited lemmas marked.
We use the notation of the [[unprovability of the graph minor theorem|WXNTPQGJ38]].
A sequence of graphs is *bad* if no $i < j$ has $G_i \le G_j$.

### Parts 1 and 3: GM from the Robertson-Seymour theorem

1. Fix $n$, and suppose that no $m$ works.
   Then for every $m$ there is a bad sequence $G_1, \dots, G_m$ in which $G_i$ has size at most $n + i$.
2. There are finitely many graphs of size at most $n + i$, up to isomorphism.
   So there are finitely many candidates at each position.
3. Call a bad sequence $(G_1, \dots, G_j)$ *extendable* if it is the start of bad sequences of every length $m \ge j$.
   The empty sequence is extendable, by step 1.
4. If $(G_1, \dots, G_j)$ is extendable, then one of the finitely many choices of $G_{j+1}$ occurs in bad sequences of every length, by the pigeonhole principle.
   So some sequence of length $j + 1$ is extendable.
5. Repeating step 4 gives an infinite sequence $G_1, G_2, \dots$ whose finite starts are all bad.
6. So no $i < j$ has $G_i \le G_j$.
   This contradicts the [[Robertson-Seymour theorem|WP3GDNWJJW]], which we cite as a theorem of $\mathsf{ZFC}$.
7. So $m$ exists for every $n$, which is part 1.
   The argument is a proof in $\mathsf{ZFC}$, which gives part 3.

### Part 2: the structure of the unprovability proof

1. **Cited lemma 1** (Friedman, Robertson and Seymour 1987).
   Over a weak base system, $\mathrm{GM}$ implies a finite form of an extended Kruskal theorem for finite labeled trees.
2. **Cited lemma 2** (Friedman, Robertson and Seymour 1987).
   The trees of the extended Kruskal theorem code an ordinal notation system up to the [[proof-theoretic ordinal|C72RBH0CDR]] of $\Pi^1_1\text{-}\mathsf{CA}_0$.
   A slowly descending sequence of notations gives a bad sequence of trees with the size bound.
3. So $\mathrm{GM}$ implies a $\Pi^0_2$ statement: every slowly descending sequence of notations in this system is finite.
4. **Cited lemma 3** (ordinal analysis).
   $\Pi^1_1\text{-}\mathsf{CA}_0$ does not prove the statement of step 3 for the whole notation system.
5. Suppose that $\Pi^1_1\text{-}\mathsf{CA}_0$ proves $\mathrm{GM}$.
   Then by steps 1 to 3 it proves the statement of step 3, which contradicts lemma 3.
6. So $\Pi^1_1\text{-}\mathsf{CA}_0$ does not prove $\mathrm{GM}$.

## Idea

If every length had a bad sequence of graphs, we could choose the graphs one position at a time, always keeping a start that extends to bad sequences of all lengths.
There are only finitely many graphs of each size, so this is always possible, and the choices fit together into an infinite bad sequence, which the Robertson-Seymour theorem forbids.
For the unprovability, graph minors encode labeled trees, these encode ordinal notations, and the finite statement then proves a well-foundedness that $\Pi^1_1\text{-}\mathsf{CA}_0$ cannot prove.

## Variants

The same compactness argument derives Friedman's finite form of Kruskal's theorem from Kruskal's theorem, in the [[proof for trees|T9YXK7VPYG]].
The structure of part 2 follows the unprovability proof for the finite Kruskal theorem in $\mathsf{ATR}_0$, with a stronger theory and a larger ordinal.
