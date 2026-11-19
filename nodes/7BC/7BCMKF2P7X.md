---
tag: 7BCMKF2P7X
kind: concept
name: Common knowledge
msc: [03B42, 91A27]
topics: [CQM9SRN8PM]
audience: grad
uses: [05J9NWX07X, 0FDKRX9M9Y, DBD64TH52D, J8A9GBFSTY, RRRHWH9F6Y]
sources:
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Modal logic (syntactic characterization), section Set theoretic (semantic characterization)
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapters 2 and 6
same_as:
  wikidata: Q372650
  wikipedia: Common knowledge (logic)
---

## Summary

A fact is common knowledge in a group when everyone knows it, everyone knows that everyone knows it, and so on without end.
The philosopher David Lewis described the notion in 1969, and Robert Aumann gave it a precise set-theoretic form in 1976.
In [[epistemic logic|EA34W4ERRE]] it is a new operator $C_G$, and $C_G\varphi$ is true at a world when $\varphi$ is true at every world reachable by a chain of steps along the relations of the agents in $G$.
It is much stronger than the statement that everyone knows the fact.
Common knowledge of the rules and of rationality is a standing assumption in [[game theory|J8A9GBFSTY]], and results such as [[Aumann's agreement theorem|DA0W4GM6B3]] depend on it.

## Motivation

Coordination needs more than shared knowledge.
Two drivers who both know that the rule is "drive on the right" still need each to know that the other knows it, or one of them may swerve.
Each further level of "knows that the other knows" can matter, so the right notion is the limit of all levels.
A public announcement produces this limit at once, while private messages produce only finitely many levels.
The logic of common knowledge explains this difference, and it shows that common knowledge is a fixed point, not only an infinite conjunction.

## Notation

1. $E_G\varphi = \bigwedge_{a \in G} K_a\varphi$: everyone in $G$ knows $\varphi$. Set $E_G^1 = E_G$ and $E_G^{k+1}\varphi = E_G E_G^k\varphi$.
2. $C_G\varphi$: $\varphi$ is common knowledge in $G$. Semantically $C_G\varphi$ is the infinite conjunction of all $E_G^k\varphi$ with $k \ge 1$.
3. $D_G\varphi$: $\varphi$ is distributed knowledge in $G$, true when $\varphi$ holds at every world that all agents of $G$ together consider possible.
4. In the set-theoretic form of [[the definition|RRRHWH9F6Y]], events are sets of states and $K_i(E)$ is the event that agent $i$ knows $E$.

## Remarks

### Examples

1. On a four-world model, reachability decides which facts are common knowledge, see [[the reachability example|365AVYV0MB]].
2. A partition model where an event is common knowledge because it is a union of blocks of the meet is in [[the definition|RRRHWH9F6Y]].
3. Two agents can have distributed knowledge of a fact that neither of them knows, see [[the distributed knowledge example|2C84ZDGE7K]].
4. After the father's announcement in the [[muddy children puzzle|BG9TYCJ7HP]], "at least one child is muddy" is common knowledge.

### Non-examples

1. Messages over an unreliable channel never create common knowledge, however many arrive, see [[the coordinated attack example|8XCDJBWS36]].
2. Mutual knowledge $E_G\varphi$ is not common knowledge. The partition example in [[the definition|RRRHWH9F6Y]] has $E_G$ without $E_G^2$.

### Basic properties

By [[the theorem on the axioms of common knowledge|8K0CMPQXXB]]:

1. Fixed point axiom: $C_G\varphi \leftrightarrow E_G(\varphi \wedge C_G\varphi)$.
2. Induction rule: from $\psi \to E_G(\varphi \wedge \psi)$ infer $\psi \to C_G\varphi$.
3. Semantics: $C_G\varphi$ is true at $w$ iff $\varphi$ holds at every world reachable from $w$ in one or more steps along $\bigcup_{a \in G} R_a$, the [[transitive closure|05J9NWX07X]] of the union.
4. So $C_G\varphi$ is the greatest fixed point of $X \mapsto E_G(\varphi \wedge X)$, and it is expressible in the modal mu-calculus.
5. If each $R_a$ is an equivalence relation, $C_G$ obeys the $\mathsf{S5}$ axioms.
6. $C_G$ is not definable in the language without it. A formula of modal depth $n$ cannot separate worlds that differ only beyond $n$ steps.

### History

David Lewis analysed conventions through common knowledge in Convention (1969).
Aumann defined it with partitions in "Agreeing to disagree" (1976), and proved that with a common prior, common knowledge of posteriors forces them to agree.
Halpern and Moses used it to analyse distributed protocols, and showed that it cannot be reached over an unreliable channel.

### Common errors

1. Identifying common knowledge with "everyone knows". The gap between the two is the point of the coordinated attack problem.
2. Treating $C_G\varphi$ as a finite formula. Each $E_G^k\varphi$ is a formula, but their conjunction is not, so $C_G$ is a primitive operator.
3. Reading the reachability clause with zero steps. The clause uses one or more steps, so $C_G\varphi \to \varphi$ is valid on reflexive frames but not on all frames.

## Explanations

### L1 human

Common knowledge is what "everybody knows that everybody knows".
Suppose a teacher announces something to the whole class out loud.
Then not only does every student know it, but every student knows that every other student heard it too, and knows that the others know this, and so on.
That endless chain is common knowledge.
If instead the teacher tells each student the same thing privately, everyone knows it, but nobody knows that the others know.
Public announcements create common knowledge; private messages usually do not.

### L2 human

We test common knowledge in a model with a graph search.

1. Draw the worlds, and draw an arrow for each pair related by some agent of the group.
2. Collect the worlds reachable from the actual world by one or more arrows.
3. The fact is common knowledge when it is true at all of them.

For example, take three worlds $w_1 - w_2 - w_3$, where agent $a$ links $w_1$ and $w_2$ and agent $b$ links $w_2$ and $w_3$.
A fact true at $w_1$ and $w_2$ but false at $w_3$ is not common knowledge at $w_1$, since $w_3$ is reachable.
A trap: if $b$ sees only $w_1$ from $w_1$, both agents know the fact at $w_1$.
So everyone knows it there, while common knowledge fails.

### L3 human

Common knowledge is the box of the transitive closure of $\bigcup_{a \in G} R_a$, so it is a [[PDL|VJ78A0Q22R]]-style iteration modality.
The fixed point axiom and induction rule make the logic $\mathsf{S5}_n^C$ weakly complete.
It is not compact: every finite part of $\set{E_G^k p : k \ge 1} \cup \set{\neg C_G p}$ is satisfiable, but the whole set is not.
Its satisfiability problem is EXPTIME-complete for two or more agents, compared with PSPACE without $C_G$.
Distributed knowledge is the dual construction: the box of the intersection $\bigcap_{a \in G} R_a$.
