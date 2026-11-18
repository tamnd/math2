---
tag: K22FBJCTFC
kind: proof
name: Proof of the translation of LTL into Büchi automata
msc: ["03B44", "68Q45", "68Q60"]
topics: [CQM9SRN8PM]
audience: grad
proves: BYMYN6GN8E
uses: [8S64VZ6A1S, 92DM43HQZT, 6144NCYTW0]
methods: [12MQ2NJ29A, 0NTF6DMVAP]
sources:
  - book: isbn:9780262026499
    locator: Baier and Katoen, Principles of Model Checking, chapters 4 and 5
  - url: https://en.wikipedia.org/wiki/Linear_temporal_logic_to_B%C3%BCchi_automaton
    locator: section Transformation from LTL to GBA
---

## Proof

We prove [[the translation theorem|BYMYN6GN8E]] for formulas in the grammar of [[the definition|8S64VZ6A1S]].
We first build a generalized Büchi automaton, which accepts a run when the run meets each of several sets infinitely often.
At the end we cite the standard reduction to an ordinary [[Büchi automaton|92DM43HQZT]].

1. Closure. Let $\mathrm{cl}(\varphi)$ be the set of subformulas of $\varphi$ and their negations, where $\neg\neg\psi$ is identified with $\psi$. Then $\lvert \mathrm{cl}(\varphi) \rvert \le 2\lvert\varphi\rvert$.
2. States. A state is a set $B \subseteq \mathrm{cl}(\varphi)$ that contains exactly one of $\psi$ and $\neg\psi$ for each $\psi \in \mathrm{cl}(\varphi)$.
3. Further, $\psi_1 \wedge \psi_2 \in B$ must hold exactly when $\psi_1 \in B$ and $\psi_2 \in B$. There are at most $2^{\lvert\varphi\rvert}$ such sets.
4. Initial states. These are the states $B$ with $\varphi \in B$.
5. Transitions. There is a transition from $B$ to $B'$ on the letter $a \subseteq AP$ when $a \cap \mathrm{cl}(\varphi) = B \cap AP$ and two conditions hold.
6. First condition: for each $X\psi \in \mathrm{cl}(\varphi)$, $X\psi \in B$ if and only if $\psi \in B'$.
7. Second condition: for each $\psi_1 U \psi_2 \in \mathrm{cl}(\varphi)$, $\psi_1 U \psi_2 \in B$ if and only if $\psi_2 \in B$, or $\psi_1 \in B$ and $\psi_1 U \psi_2 \in B'$.
8. Acceptance. For each until formula $\theta = \psi_1 U \psi_2$ in $\mathrm{cl}(\varphi)$, let $F_\theta$ be the set of states $B$ with $\theta \notin B$ or $\psi_2 \in B$. A run is accepting when it meets every $F_\theta$ infinitely often.
9. Truth lemma. Let $B_0 B_1 \cdots$ be an accepting run on $w$. We show by induction on $\psi \in \mathrm{cl}(\varphi)$ that $\psi \in B_i$ if and only if $w^i \models \psi$, for all $i$.
10. Atoms: $p \in B_i$ if and only if $p \in w_i$, by the letter condition $w_i \cap \mathrm{cl}(\varphi) = B_i \cap AP$.
11. Negation and conjunction follow from steps 2 and 3 and the induction hypothesis.
12. Next: $X\psi \in B_i$ if and only if $\psi \in B_{i+1}$, by step 6. By the induction hypothesis this holds if and only if $w^{i+1} \models \psi$, that is, $w^i \models X\psi$.
13. Until, first direction. Let $\theta = \psi_1 U \psi_2 \in B_i$. Suppose that $\psi_2 \notin B_j$ for all $j \ge i$.
14. Then step 7 gives $\psi_1 \in B_j$ and $\theta \in B_{j+1}$ for all $j \ge i$, by induction on $j$. So no $B_j$ with $j \ge i$ is in $F_\theta$.
15. This contradicts acceptance. So there is a least $j \ge i$ with $\psi_2 \in B_j$.
16. For $i \le k < j$, step 7 and $\psi_2 \notin B_k$ give $\psi_1 \in B_k$. By the induction hypothesis, $w^j \models \psi_2$ and $w^k \models \psi_1$, so $w^i \models \theta$.
17. Until, second direction. Let $w^i \models \theta$ with witness $j \ge i$, and suppose $\theta \notin B_i$.
18. For $i \le k \le j$ we show $\theta \notin B_k$, by induction on $k$. If $\theta \notin B_k$, step 7 gives $\psi_2 \notin B_k$.
19. For $k < j$ we have $w^k \models \psi_1$, so $\psi_1 \in B_k$ by the induction hypothesis. Then step 7 gives $\theta \notin B_{k+1}$.
20. At $k = j$ we get $\psi_2 \notin B_j$, while $w^j \models \psi_2$. This contradicts the induction hypothesis, so $\theta \in B_i$.
21. Soundness. An accepting run has $\varphi \in B_0$ by step 4, so step 9 gives $w \models \varphi$.
22. Completeness. Let $w \models \varphi$, and put $B_i = \set{\psi \in \mathrm{cl}(\varphi) : w^i \models \psi}$. Steps 2 to 6 hold by the semantics.
23. Step 7 holds by the expansion law $\psi_1 U \psi_2 \equiv \psi_2 \vee (\psi_1 \wedge X(\psi_1 U \psi_2))$, which follows from the clause for until.
24. Suppose that some $F_\theta$ is met only finitely often. Then for some $N$, all $i \ge N$ have $w^i \models \theta$ and $w^i \not\models \psi_2$.
25. But $w^N \models \theta$ gives a $j \ge N$ with $w^j \models \psi_2$. This contradiction shows that the run $B_0 B_1 \cdots$ is accepting.
26. Degeneralization, cited. A generalized Büchi automaton with $n$ states and $k \ge 1$ acceptance sets has an equivalent Büchi automaton with $n \cdot k$ states. Its states are pairs (state, counter), and the counter waits for the sets in turn. If $k = 0$, all states are accepting.
27. Count. Here $k \le \lvert\varphi\rvert$ and $n \le 2^{2\lvert\varphi\rvert} = 4^{\lvert\varphi\rvert}$. So the Büchi automaton has at most $(\lvert\varphi\rvert + 1) \cdot 4^{\lvert\varphi\rvert}$ states.
28. Each state is a subset of $\mathrm{cl}(\varphi)$ and a counter, so it has $O(\lvert\varphi\rvert)$ bits. The conditions of steps 2 to 8 are checked in polynomial time, which gives part 3.

## Idea

A state guesses which subformulas are true at the current position.
The transition conditions make the guesses consistent with the next position.
Only the eventualities can be postponed forever, and the acceptance condition forbids that.

## Variants

1. Baier and Katoen give this construction, with the degeneralization of step 26, in chapters 4 and 5.
2. Alternating automata give a translation with $O(\lvert\varphi\rvert)$ states, and the exponential appears only when they are made nondeterministic.
