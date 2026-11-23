---
tag: T9YXK7VPYG
kind: proof
name: Proof of Friedman's finite form of Kruskal's theorem
msc: ["03F35", "05C05"]
topics: [T6FK1E7GJ1]
audience: research
proves: 12XRGBWH59
uses: [XVHKCX4F5Y, 0C9J6W2A8A, C72RBH0CDR, 6QFEVWKE25, 0ZHQMQ2C1N]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal's_tree_theorem
    locator: Weak tree function
  - url: https://en.wikipedia.org/wiki/Kruskal's_tree_theorem
    locator: Friedman's work
---

## Proof

We glue arbitrarily long bad sequences into an infinite one by a compactness argument, which Kruskal's theorem forbids, and we outline the unprovability with the cited lemmas marked.
We use the notation of [[Friedman's finite form|12XRGBWH59]].
A sequence of trees is *bad* if no $i < j$ has $T_i \le T_j$.

### Part 1: P(n) holds, from Kruskal's theorem

1. Fix $n$, and suppose that $P(n)$ fails.
   Then for every $m$ there is a bad sequence of length $m$ in which $T_i$ has $i + n$ vertices.
2. There are finitely many rooted trees with a given number of vertices, up to isomorphism.
   So for each $m$ there are finitely many such bad sequences of length $m$.
3. Call a bad sequence $(T_1, \dots, T_j)$ *extendable* if it is the start of bad sequences of every length $m \ge j$.
4. The empty sequence is extendable, by step 1.
5. Let $(T_1, \dots, T_j)$ be extendable.
   Each longer bad sequence that starts with it continues with one of finitely many trees $T_{j+1}$, by step 2.
6. So one choice of $T_{j+1}$ occurs in bad sequences of every length, by the pigeonhole principle, and $(T_1, \dots, T_{j+1})$ is extendable.
7. Steps 4 to 6 give an infinite sequence $T_1, T_2, T_3, \dots$ whose finite starts are all bad.
8. So no $i < j$ has $T_i \le T_j$.
   This contradicts [[Kruskal's tree theorem|XVHKCX4F5Y]], which gives such $i < j$ in every infinite sequence of finite rooted trees.
9. So $P(n)$ holds.

### Part 3: a proof in the stronger system

1. **Cited lemma 1** (reverse mathematics of Kruskal's theorem).
   Kruskal's tree theorem is provable in $\Pi^1_1\text{-}\mathsf{CA}_0$.
2. Steps 3 to 7 of part 1 are an instance of König's lemma for a finitely branching tree.
   This lemma is provable in $\mathsf{ACA}_0$, a subsystem of $\Pi^1_1\text{-}\mathsf{CA}_0$.
3. So part 1 is a proof of $\forall n\, P(n)$ in $\Pi^1_1\text{-}\mathsf{CA}_0$.

### Part 2: the structure of the unprovability proof in ATR0

1. **Cited lemma 2** (Friedman).
   There is a coding of the ordinal terms below the Feferman-Schütte ordinal $\Gamma_0$, built with the [[Veblen functions|6QFEVWKE25]], by finite rooted trees.
   If the tree of $\alpha$ embeds in the tree of $\beta$, then $\alpha \le \beta$.
2. So a strictly descending sequence of terms gives a bad sequence of trees.
   If the terms grow in size by at most one at each step, the trees satisfy the size bound of $P(n)$, for a suitable $n$.
3. **Cited lemma 3** (Friedman).
   In $\mathsf{ACA}_0$, the statement $\forall n\, P(n)$ implies a $\Pi^0_2$ form of the well-foundedness of the whole notation system below $\Gamma_0$.
   This form says that every slowly descending sequence of terms is finite.
4. **Cited lemma 4** (ordinal analysis).
   The [[proof-theoretic ordinal|C72RBH0CDR]] of $\mathsf{ATR}_0$ is $\Gamma_0$, and $\mathsf{ATR}_0$ does not prove the statement of lemma 3 for the whole system below $\Gamma_0$.
5. Suppose that $\mathsf{ATR}_0$ proves $\forall n\, P(n)$.
   Then by lemma 3 it proves the well-foundedness statement, because $\mathsf{ACA}_0$ is part of $\mathsf{ATR}_0$.
6. This contradicts lemma 4, so $\mathsf{ATR}_0$ does not prove $\forall n\, P(n)$.

## Idea

Suppose every length had a bad sequence.
At each position there are only finitely many trees to choose from, so we can choose them one at a time and keep, at every stage, a start that still extends to bad sequences of all lengths.
The choices fit together into one infinite bad sequence, which Kruskal's theorem forbids.
For the unprovability, trees code ordinal terms, so slowly descending ordinals give bad sequences of trees, and the finite statement then proves a well-foundedness that $\mathsf{ATR}_0$ cannot prove.

## Variants

The same tree argument proves the version with at most $i + n$ vertices, and the labeled version that defines $\mathrm{TREE}$.
A sharper analysis, by Rathjen and Weiermann, shows that the proof-theoretic ordinal of Kruskal's theorem for unlabeled trees is the small Veblen ordinal.
For each fixed $n$, $P(n)$ is a true $\Sigma_1$ sentence, so it can also be proved by a finite search, in $\mathsf{PA}$.
