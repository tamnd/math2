---
tag: WMZ1QP7KQY
kind: statement
role: theorem
name: Gärdenfors's triviality theorem
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: research
uses: [~30b6c328, ZGYG7WN7EC]
about: [~30b6c328, ZGYG7WN7EC]
proofs: [~2b5ef213]
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

Let $L$ be a language that contains the connectives of propositional logic and a binary conditional $>$, and let $\mathrm{Cn}$ be a consequence operation on $L$ that contains classical propositional logic.
A belief set is a set $K \subseteq L$ with $K = \mathrm{Cn}(K)$; $K_\bot = L$ is the inconsistent one, and $K + \varphi := \mathrm{Cn}(K \cup \set{\varphi})$.
A belief revision system is a pair $(\mathcal{K}, *)$, where $\mathcal{K}$ is a class of belief sets with $K + \varphi \in \mathcal{K}$ for all $K \in \mathcal{K}$ and $\varphi \in L$, and $* : \mathcal{K} \times L \to \mathcal{K}$.
Consider these conditions, for all $K \in \mathcal{K}$ and $\varphi, \psi \in L$:

1. (closure) $K * \varphi$ is a belief set;
2. (success) $\varphi \in K * \varphi$;
3. (preservation) if $\neg\varphi \notin K$, then $K \subseteq K * \varphi$;
4. (weak consistency) if $K$ is consistent and $\varphi$ is consistent, then $K * \varphi$ is consistent;
5. (Ramsey test) $\psi \in K * \varphi$ if and only if $(\varphi > \psi) \in K$.

The system is non-trivial when some $K \in \mathcal{K}$ and some formulas $A, B, C$ satisfy: $\neg A, \neg B, \neg C \notin K$, and $\vdash \neg(A \wedge B)$, $\vdash \neg(A \wedge C)$, $\vdash \neg(B \wedge C)$.

No non-trivial belief revision system satisfies conditions 1 to 5.

The proof is in [[the proof of the triviality theorem|~2b5ef213]].

## Remarks

### Why each hypothesis is needed

1. Non-triviality: the system with $\mathcal{K} = \set{K_\bot}$ and $K_\bot * \varphi = K_\bot$ satisfies conditions 1 to 5. Condition 4 is vacuous, and both sides of the Ramsey test always hold.
2. The Ramsey test: without it, any AGM revision on the class of all belief sets satisfies conditions 1 to 4, and the class is non-trivial as soon as the language has two atoms $p, q$, with $A = p \wedge q$, $B = p \wedge \neg q$, $C = \neg p$ and $K = \mathrm{Cn}(\emptyset)$.
3. Preservation: the proof uses it twice. Grahne showed that the Ramsey test is consistent with the Katsuno-Mendelzon postulates for update, which replace preservation by a monotone condition.
4. Weak consistency: let $\mathcal{K}$ be the belief sets that contain every formula $\varphi > \psi$, and let $K * \varphi = K_\bot$. Conditions 1, 2, 3 and 5 hold, and only condition 4 fails.
5. Closure of $\mathcal{K}$ under expansion: the proof needs the belief sets $K + A$, $K + (A \vee B)$ and $K + (A \vee C)$ in $\mathcal{K}$.

### Consequences

1. The AGM postulates imply conditions 1 to 4: vacuity gives preservation, and the AGM consistency postulate gives weak consistency. So [[AGM belief revision|~30b6c328]] cannot be combined with the Ramsey test when conditionals are in the belief sets.
2. The Ramsey test makes revision monotone in the belief set: $K \subseteq H$ gives $K * \varphi \subseteq H * \varphi$. The proof shows that this monotonicity, preservation, success and weak consistency cannot all hold in a non-trivial system.
3. Any epistemic semantics of [[conditional logic|ZGYG7WN7EC]] by the Ramsey test must give up one of the conditions.

### Converse

The theorem is an impossibility result, so its converse would be the claim that any four of the conditions are jointly satisfiable with non-triviality.
The examples above show this for dropping non-triviality, the Ramsey test and weak consistency.

### Generalizations

1. Gärdenfors also studied weakened versions of the test and proved further triviality theorems, including results for the negative Ramsey test, where $\psi \notin K * \varphi$ gives $\neg(\varphi > \psi) \in K$.
2. Lewis's triviality results for probabilities of conditionals are the probabilistic analogue: the probability of a conditional cannot be the conditional probability in every probability function of a non-trivial class.

## History

Gärdenfors proved the theorem in 1986, in "Belief revisions and the Ramsey test for conditionals", and discussed it in Knowledge in Flux (1988).
The probabilistic analogue is due to Lewis (1976).
Responses include Levi's view that conditionals are not objects of belief, restrictions of the Ramsey test to formulas without $>$, weakenings of preservation, and revision of epistemic states richer than belief sets.

## Explanations

### L1 human

Ramsey suggested a test for "if": to judge "if $A$, then $B$", add $A$ to your beliefs and see whether $B$ follows.
Belief revision theory says how to add $A$ when it contradicts you.
Gärdenfors showed that the two ideas clash if "if" sentences are themselves beliefs.
For example, with three outcomes of a race that exclude each other, the rules force someone to believe two of them at once.
So one of the rules must be weakened.

### L2 human

We trace the key step of the proof with three runners $A$, $B$, $C$, exactly one of whom wins.

1. Start from a belief set where each runner can still win.
2. Learn "$A$ or $B$ wins" and then revise by "$B$ or $C$ wins". Preservation keeps "$A$ or $B$", so we conclude "$B$ wins".
3. Learn "$A$ or $C$ wins" and revise by "$B$ or $C$ wins". In the same way we conclude "$C$ wins".
4. Someone who learns "$A$ wins" knows both earlier pieces of news. The Ramsey test makes this person conclude both "$B$ wins" and "$C$ wins".

The typical use of the theorem is as a constraint on any theory that links conditionals with belief change.
A trap: the theorem does not refute AGM theory or the Ramsey test alone; it refutes their combination with conditionals in the belief sets.

### L3 human

The theorem is a monotonicity clash: the Ramsey test makes $K \mapsto K * \varphi$ monotone, while preservation and consistency force non-monotone behaviour.
The same tension appears between update and revision: update is monotone in this sense, and the Ramsey test fits it.
Ranking functions and plausibility models separate the epistemic state from the belief set, so the Ramsey test can hold at the level of states without triviality.
