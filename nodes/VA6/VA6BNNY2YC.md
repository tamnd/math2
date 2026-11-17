---
tag: VA6BNNY2YC
kind: statement
role: theorem
name: Church's theorem on undecidability of first-order logic
aliases: [church-turing-theorem-on-the-entscheidungsproblem, undecidability-of-first-order-validity]
msc: ["03B25", "03D35", "03B10"]
topics: [E4AVTNWE9E]
audience: ug2
uses: [086QKPF0A6, DKFGQTRYZE, 5SDS9T8E7J, PPGD5KW8JC, TN9G24VABN, 758EYCN27B, Z7TN2B35B0, WQ1ZE255SF]
about: [086QKPF0A6, 5SDS9T8E7J]
resolves:
  - target: ~58802204
    outcome: settled
    note: The answer is negative, since no algorithm decides validity.
history:
  first_stated: "1936"
  notes: Proved independently by Alonzo Church in "A note on the Entscheidungsproblem" (1936) and by Alan Turing in "On computable numbers, with an application to the Entscheidungsproblem" (1936).
sources:
  - url: https://en.wikipedia.org/wiki/Entscheidungsproblem
    locator: Negative answer
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
  - book: isbn:9780521701464
---

## Statement

There is a finite first-order signature $L$ such that the set of [[valid|5SDS9T8E7J]] $L$-[[sentences|DKFGQTRYZE]] is not a [[computable set|PPGD5KW8JC]].
So no algorithm decides, for every $L$-sentence $\sigma$, whether $\sigma$ is true in every $L$-structure.

Two signatures with this property are proved on the proof pages.

1. The signature $L_M$ of a Turing machine $M$: a constant $0$, a unary function symbol $'$, a binary relation symbol $<$, and one binary relation symbol for each state and each tape symbol of $M$.
2. The signature $\set{0, S, +, \cdot}$ of arithmetic.

The set of valid $L$-sentences is [[computably enumerable|TN9G24VABN]] for every finite signature $L$, so validity is semi-decidable but not decidable.

## Remarks

### Why each hypothesis is needed

- The logic must be first-order with quantifiers. In propositional logic, the set of tautologies is decidable by [[truth tables|05RSK4Q657]].
- The signature must contain a symbol of arity at least $2$. If every symbol is a unary relation symbol, validity is decidable, by the [[finite model property of monadic logic|~2f4e10fc]]; see the [[monadic predicate calculus|SERN6CRVWW]].
- Validity means truth in all structures, finite and infinite. Truth in all finite structures is also undecidable, but for a different reason; see [[Trakhtenbrot's theorem|~3e65890a]].

### Consequences

1. The [[Entscheidungsproblem|~58802204]] has a negative answer.
2. The set of satisfiable $L$-sentences is not computably enumerable. Its complement in the set of sentences is $\set{\sigma : \neg \sigma \text{ is valid}}$, which is computably enumerable; if both were computably enumerable, validity would be computable.
3. Undecidability passes to larger signatures. If $L \subseteq L'$, an $L$-sentence is valid among $L$-structures if and only if it is valid among $L'$-structures, because every $L$-structure expands to an $L'$-structure.
4. A theory with finitely many axioms $\alpha_1, \ldots, \alpha_n$ that is undecidable gives a second proof: $\alpha_1 \wedge \cdots \wedge \alpha_n \to \sigma$ is valid if and only if $\sigma$ follows from the axioms.
5. An automated theorem prover for first-order logic can confirm every valid sentence, by [[Gödel's completeness theorem|WQ1ZE255SF]], but on some invalid sentences it must run forever.

### Converse

The theorem does not say that every signature gives an undecidable validity problem; consequence 3 goes in one direction only.
For a signature whose symbols are all unary relation symbols, validity is decidable.
For every signature that contains a binary relation symbol, validity is undecidable: one binary relation can code the finitely many relations of $L_M$.
That coding is longer, and we do not prove it here.

### Generalizations

- The proofs show more than undecidability. The halting set reduces to validity by a computable map, so validity is complete among the computably enumerable sets for many-one reductions.
- Many small fragments of first-order logic are already undecidable, for example the prenex sentences with prefix $\forall \exists \forall$ and only binary relation symbols. The decidable fragments are listed in [[decidable prefix classes|~48b4c091]].
- Every consistent theory that is [[essentially undecidable|~c0b3bb9c]] and finitely axiomatized gives a signature with undecidable validity, by consequence 4.

## History

Hilbert and Ackermann posed the Entscheidungsproblem in 1928.
Church published "A note on the Entscheidungsproblem" in 1936.
He used his result, from the same year, that no algorithm decides whether a term of the lambda calculus has a normal form.
Turing proved the result independently in "On computable numbers, with an application to the Entscheidungsproblem", with the machines that he introduced in the same paper.
Turing's proof is the model for the first proof page.

## Explanations

### L1 human

The theorem says that no computer program can judge every statement of logic as "always true" or "not always true".
The reason is that statements of logic can describe the run of any computer program step by step.
For a program, one can write a statement that is always true exactly when the program stops.
A judge for logic would therefore predict whether every program stops, and Turing proved that this prediction is impossible.

### L2 human

We write the sentence of the first proof for a machine $M$ that halts after one step.
$M$ has states $q_0$ and $q_1$, tape symbols $\square$ (blank) and $1$, and one instruction: in state $q_0$ reading $\square$, write $1$, move right, go to $q_1$.
The input is empty, so the tape is blank.

1. The premises contain the initial axiom $Q_{q_0}(0, 0) \wedge \forall y \, C_{\square}(y, 0)$: at time $0$ the head is at cell $0$ in state $q_0$, and every cell is blank.
2. The instruction gives the axiom $\forall x \, \forall t \, (Q_{q_0}(x, t) \wedge C_{\square}(x, t) \to Q_{q_1}(x', t') \wedge C_1(x, t') \wedge F)$, where $F$ says that the other cells keep their symbols.
3. With $x = 0$ and $t = 0$, step 1 and step 2 give $Q_{q_1}(0', 0')$.
4. The order axioms give $0 \neq 0'$, so the frame condition $F$ and $C_{\square}(0', 0)$ give $C_{\square}(0', 0')$.
5. The pairs without an instruction are $(q_0, 1)$, $(q_1, \square)$ and $(q_1, 1)$. The halting formula $H$ says that for some $x$ and $t$, one of these pairs occurs at $(x, t)$.
6. Steps 3 and 4 give the pair $(q_1, \square)$ at $x = 0'$ and $t = 0'$, so $H$ holds. So the sentence "premises imply $H$" is true in every structure, that is, valid.

For a machine that moves right forever, the standard structure on $\N$ satisfies the premises and makes $H$ false, so the sentence is not valid.
The typical use of the theorem is as a source of reductions: a decision problem that can express validity is undecidable.
A trap is to conclude that validity of one fixed sentence is undecidable; each single sentence is valid or not, and the theorem is about the whole set.

### L3 human

In terms of degrees, the set of valid sentences of $L_M$ for a universal machine $M$ is a complete computably enumerable set, of the same degree as the [[halting problem|Z7TN2B35B0]].
The proof is a reduction: configurations of a machine become elements of a structure, and transitions become universal axioms.
The same method, with tiles in place of machines, shows that the prefix class $\forall \exists \forall$ is undecidable, as in the work of Kahr, Moore and Wang on [[Wang tiles|AJH5HPD2B7]].
The finite version of the problem, [[Trakhtenbrot's theorem|~3e65890a]], uses the same encoding with finite structures, and the arithmetic version leads to the [[essential undecidability|~c0b3bb9c]] of $\mathsf{Q}$ and to [[Gödel's incompleteness theorems|X9WYNYE29C]].
