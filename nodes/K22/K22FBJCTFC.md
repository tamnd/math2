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

We build an automaton whose states guess the true subformulas, prove that accepting runs guess correctly, and then count the states.
We prove [[the translation theorem|BYMYN6GN8E]] for formulas in the grammar of [[the definition|8S64VZ6A1S]].
First we build a generalized Büchi automaton, which accepts a run when the run meets each of several sets infinitely often.
At the end we cite the standard reduction to an ordinary [[Büchi automaton|92DM43HQZT]].

### The automaton

1. Let $\mathrm{cl}(\varphi)$ be the set of subformulas of $\varphi$ and their negations, where we identify $\neg\neg\psi$ with $\psi$.
   Then $\lvert \mathrm{cl}(\varphi) \rvert \le 2\lvert\varphi\rvert$.
2. A state is a set $B \subseteq \mathrm{cl}(\varphi)$ that contains exactly one of $\psi$ and $\neg\psi$ for each $\psi \in \mathrm{cl}(\varphi)$, and that contains $\psi_1 \wedge \psi_2$ exactly when it contains $\psi_1$ and $\psi_2$.
   A state is fixed by its choice on the subformulas, so there are at most $2^{\lvert\varphi\rvert}$ states.
3. The initial states are the states $B$ with $\varphi \in B$.
4. There is a transition from $B$ to $B'$ on the letter $a \subseteq AP$ when $a \cap \mathrm{cl}(\varphi) = B \cap AP$ and two conditions hold.
   For each $X\psi \in \mathrm{cl}(\varphi)$, we need $X\psi \in B$ if and only if $\psi \in B'$.
   For each $\psi_1 U \psi_2 \in \mathrm{cl}(\varphi)$, we need $\psi_1 U \psi_2 \in B$ if and only if $\psi_2 \in B$, or $\psi_1 \in B$ and $\psi_1 U \psi_2 \in B'$.
5. For each until formula $\theta = \psi_1 U \psi_2$ in $\mathrm{cl}(\varphi)$, let $F_\theta$ be the set of states $B$ with $\theta \notin B$ or $\psi_2 \in B$.
   A run is accepting when it meets every $F_\theta$ infinitely often.

### The truth lemma

6. Let $B_0 B_1 \cdots$ be an accepting run on $w$.
   We show by induction on $\psi \in \mathrm{cl}(\varphi)$ that $\psi \in B_i$ if and only if $w^i \models \psi$, for all $i$.
7. For an atom $p$, the letter condition $w_i \cap \mathrm{cl}(\varphi) = B_i \cap AP$ gives $p \in B_i$ if and only if $p \in w_i$.
   Negation and conjunction follow from step 2 and the induction hypothesis.
8. For next, step 4 gives $X\psi \in B_i$ if and only if $\psi \in B_{i+1}$.
   By the induction hypothesis this holds if and only if $w^{i+1} \models \psi$, that is, $w^i \models X\psi$.
9. Let $\theta = \psi_1 U \psi_2 \in B_i$, and suppose that $\psi_2 \notin B_j$ for all $j \ge i$.
   Then the until condition of step 4 gives $\psi_1 \in B_j$ and $\theta \in B_{j+1}$ for all $j \ge i$, by induction on $j$.
   So no $B_j$ with $j \ge i$ is in $F_\theta$, which contradicts acceptance.
10. So there is a least $j \ge i$ with $\psi_2 \in B_j$.
    For $i \le k < j$, the until condition and $\psi_2 \notin B_k$ give $\psi_1 \in B_k$.
    By the induction hypothesis, $w^j \models \psi_2$ and $w^k \models \psi_1$, so $w^i \models \theta$.

### The truth lemma, continued

11. Now let $w^i \models \theta$ with witness $j \ge i$, and suppose that $\theta \notin B_i$.
    We show $\theta \notin B_k$ for $i \le k \le j$, by induction on $k$.
12. If $\theta \notin B_k$, the until condition gives $\psi_2 \notin B_k$.
    For $k < j$ we have $w^k \models \psi_1$, so $\psi_1 \in B_k$ by the induction hypothesis, and then the until condition gives $\theta \notin B_{k+1}$.
13. At $k = j$ we get $\psi_2 \notin B_j$, while $w^j \models \psi_2$.
    This contradicts the induction hypothesis, so $\theta \in B_i$.
14. An accepting run has $\varphi \in B_0$ by step 3, so the truth lemma gives $w \models \varphi$.

### Every model has an accepting run

15. Let $w \models \varphi$, and put $B_i = \{\psi \in \mathrm{cl}(\varphi) : w^i \models \psi\}$.
    Steps 2 and 3 and the next condition hold by the semantics.
16. The until condition holds by the expansion law $\psi_1 U \psi_2 \equiv \psi_2 \vee (\psi_1 \wedge X(\psi_1 U \psi_2))$, which follows from the clause for until.
17. Suppose that some $F_\theta$ is met only finitely often.
    Then for some $N$, all $i \ge N$ have $w^i \models \theta$ and $w^i \not\models \psi_2$.
    But $w^N \models \theta$ gives a $j \ge N$ with $w^j \models \psi_2$, a contradiction, so the run is accepting.

### The count

18. We cite degeneralization: a generalized Büchi automaton with $n$ states and $k \ge 1$ acceptance sets has an equivalent Büchi automaton with $n \cdot k$ states.
    Its states are pairs of a state and a counter, and the counter waits for the acceptance sets in turn.
    If $k = 0$, every state is accepting.
19. Here $k \le \lvert\varphi\rvert$ and $n \le 2^{\lvert\varphi\rvert} \le 4^{\lvert\varphi\rvert}$, so the Büchi automaton has at most $(\lvert\varphi\rvert + 1) \cdot 4^{\lvert\varphi\rvert}$ states.
20. Each state is a subset of $\mathrm{cl}(\varphi)$ and a counter, so it has $O(\lvert\varphi\rvert)$ bits.
    The conditions of steps 2 to 5 can be checked in polynomial time, which gives the time bound of part 3.

## Idea

A state guesses which subformulas are true at the current position.
The transition conditions force the guesses to agree with the next position, through the one-step unfoldings of next and until.
These local checks cannot stop a run from postponing an until forever, and the acceptance sets forbid exactly that.

## Variants

Baier and Katoen give this construction, with the degeneralization of step 18, in chapters 4 and 5 of Principles of Model Checking.
Alternating automata give a translation with $O(\lvert\varphi\rvert)$ states, and the exponential appears only when they are made nondeterministic.
