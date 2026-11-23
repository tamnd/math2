---
tag: WMZ1QP7KQY
kind: statement
role: theorem
name: Gärdenfors's triviality theorem
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: research
uses: [Y05YQN7HGQ, ZGYG7WN7EC]
about: [Y05YQN7HGQ, ZGYG7WN7EC]
proofs: [DQ2XRGXWP9]
history:
  first_stated: "Gärdenfors, 1986"
  notes: "Gärdenfors proved the theorem in Belief revisions and the Ramsey test for conditionals (Philosophical Review, 1986) and discussed it in Knowledge in Flux (1988)."
sources:
  - wikipedia: en:44316374@r1373780575
    locator: Ramsey test, section Triviality theorem in belief revision
    note: adopted
    mention: wikipedia://en/44316374#GZJ9
    sections: [Statement]
  - url: https://en.wikipedia.org/wiki/Ramsey_test
    locator: Triviality theorem in belief revision
  - book: isbn:9780262071093
    locator: Gärdenfors, Knowledge in Flux
inventory: [7SJ5S1EFCR]
---

## Statement

The Ramsey test for conditionals and the preservation of old beliefs cannot hold together in any belief revision system rich enough to talk about three exclusive possibilities.

Let $L$ be a language with the propositional connectives and a binary conditional $>$, and let $\mathrm{Cn}$ be a consequence operation on $L$ that includes classical propositional logic.
A belief set is a set $K \subseteq L$ with $K = \mathrm{Cn}(K)$, the set $K_\bot = L$ is the inconsistent one, and $K + \varphi := \mathrm{Cn}(K \cup \{\varphi\})$.
A belief revision system is a pair $(\mathcal{K}, *)$, where $\mathcal{K}$ is a class of belief sets closed under expansion and $* : \mathcal{K} \times L \to \mathcal{K}$.
Consider these conditions, for all $K \in \mathcal{K}$ and $\varphi, \psi \in L$.

1. Closure: $K * \varphi$ is a belief set.
2. Success: $\varphi \in K * \varphi$.
3. Preservation: if $\neg\varphi \notin K$, then $K \subseteq K * \varphi$.
4. Weak consistency: if $K$ and $\varphi$ are consistent, then $K * \varphi$ is consistent.
5. Ramsey test: $\psi \in K * \varphi$ if and only if $(\varphi > \psi) \in K$.

The system is nontrivial when some $K \in \mathcal{K}$ and some formulas $A, B, C$ have $\neg A, \neg B, \neg C \notin K$, while $\vdash \neg(A \wedge B)$, $\vdash \neg(A \wedge C)$ and $\vdash \neg(B \wedge C)$.
Then no nontrivial belief revision system satisfies conditions 1 to 5.

## Remarks

### Three runners

Think of $A$, $B$ and $C$ as "Ann wins", "Bob wins" and "Cat wins" in a race with one winner, and let $K$ leave all three open.
Learn "Ann or Bob wins", and then revise by "Bob or Cat wins".
Preservation keeps "Ann or Bob", so you conclude "Bob wins".
In the same way, from "Ann or Cat wins" the same revision gives "Cat wins".
Someone who believes "Ann wins" believes both earlier pieces of news, and the Ramsey test makes revision monotone in the belief set.
So that person, revising by "Bob or Cat wins", must conclude that Bob wins and that Cat wins, which is inconsistent.
[[The proof|DQ2XRGXWP9]] turns this story into twelve steps.

### Why each hypothesis is needed

Nontriviality is needed: the system with $\mathcal{K} = \{K_\bot\}$ and $K_\bot * \varphi = K_\bot$ satisfies conditions 1 to 5, since condition 4 never applies and both sides of the Ramsey test always hold.

The Ramsey test is needed.
Without it, any AGM revision on the class of all belief sets satisfies conditions 1 to 4.
The class is nontrivial once the language has two atoms, with $A = p \wedge q$, $B = p \wedge \neg q$, $C = \neg p$ and $K = \mathrm{Cn}(\emptyset)$.

Weak consistency is needed.
Let $\mathcal{K}$ be the belief sets that contain every formula $\varphi > \psi$, and let $K * \varphi = K_\bot$ always.
Then conditions 1, 2, 3 and 5 hold, and only condition 4 fails.

Preservation is used in the key step of the proof, and closure of $\mathcal{K}$ under expansion is used to form the belief sets $K + A$, $K + (A \vee B)$ and $K + (A \vee C)$.

### What it gives you

The AGM postulates imply conditions 1 to 4, since vacuity gives preservation and the AGM consistency postulate gives weak consistency.
So [[AGM belief revision|Y05YQN7HGQ]] cannot be joined with the Ramsey test when conditionals are themselves beliefs.
The key fact is that the Ramsey test makes revision monotone: $K \subseteq H$ gives $K * \varphi \subseteq H * \varphi$.
Monotonicity, preservation, success and weak consistency cannot all hold in a nontrivial system.
So any reading of [[conditional logic|ZGYG7WN7EC]] by the Ramsey test must give up one of the conditions.

### Generalizations

Gärdenfors also proved triviality results for weakened forms of the test.
One of them uses the negative Ramsey test, where $\psi \notin K * \varphi$ gives $\neg(\varphi > \psi) \in K$.
Lewis's triviality results for probabilities of conditionals are the probabilistic analogue.
They show that the probability of a conditional cannot equal the conditional probability in every probability function of a nontrivial class.

## History

Gärdenfors proved the theorem in 1986, in "Belief revisions and the Ramsey test for conditionals", and discussed it in Knowledge in Flux (1988).
The probabilistic analogue is due to Lewis (1976).
The responses include Levi's view that conditionals are not objects of belief, restrictions of the Ramsey test to formulas without $>$, weakenings of preservation, and revision of epistemic states that are richer than belief sets.

## Explanations

### L1 human

Ramsey suggested a test for "if": to judge "if A, then B", add A to your beliefs and see whether B follows.
Belief revision theory says how to add A when it contradicts what you believe.
Gärdenfors showed that the two ideas clash when "if" sentences are themselves beliefs.
With three runners and one winner, the rules force someone to believe that two different runners win.
So one of the rules must be weakened.

### L2 human

We check the step that uses the Ramsey test.
Let $K_1 = K + (A \vee B)$ and $H = K + A$, so $K_1 \subseteq H$, because $A$ implies $A \vee B$.
Suppose that $B \in K_1 * (B \vee C)$.
The Ramsey test turns this into the belief $(B \vee C) > B$ in $K_1$, and so in $H$.
The Ramsey test, read the other way, gives $B \in H * (B \vee C)$.
This is the typical use of the theorem: any theory that links conditionals with belief change must say which of these steps it blocks.
Watch out: the theorem refutes neither AGM theory nor the Ramsey test alone, only their combination with conditionals inside belief sets.

### L3 human

The theorem is a clash of monotonicity: the Ramsey test makes $K \mapsto K * \varphi$ monotone, while preservation and consistency force nonmonotone behavior.
Update, unlike revision, is monotone in this sense, and Grahne showed that the Ramsey test is consistent with the Katsuno-Mendelzon postulates for update.
Ranking functions and plausibility models separate the epistemic state from the belief set, so the Ramsey test can hold at the level of states without triviality.
