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
It is the kind of knowledge that a public announcement creates and that private messages do not, and it is what coordination needs.
In [[epistemic logic|EA34W4ERRE]] it is a new operator $C_G$ for each group $G$ of agents.
With $E_G \varphi = \bigwedge_{a \in G} K_a \varphi$ and $E_G^{k+1} \varphi = E_G E_G^k \varphi$, the [[definition|RRRHWH9F6Y]] reads as follows.
$$M, w \models C_G \varphi \iff M, w \models E_G^k \varphi \text{ for every } k \ge 1.$$
Equivalently, $C_G \varphi$ is true at $w$ when $\varphi$ is true at every world reachable from $w$ in one or more steps along the relations of the agents in $G$.

## Motivation

Coordination needs more than shared knowledge.
Two drivers who both know the rule "drive on the right" still need each to know that the other knows it, or one of them may swerve.
Each further level of "knows that the other knows" can matter, so the right notion is the limit of all levels.
A public announcement produces this limit at once, while a chain of private messages produces only finitely many levels.

Common knowledge of the rules and of rationality is a standing assumption in [[game theory|J8A9GBFSTY]].
[[Aumann's agreement theorem|DA0W4GM6B3]] shows its force: agents with a common prior cannot agree to disagree once their posteriors are common knowledge.
In computer science it is the knowledge that a distributed protocol needs before processes can act together, and it is exactly what unreliable channels fail to give.

## Notation

We write $C_G \varphi$, or $C \varphi$ when $G$ is the set of all agents; some authors write $CK_G$.
The formula $E_G \varphi$ is mutual knowledge, "everyone in $G$ knows $\varphi$", and $E_G^k$ is its $k$-fold iterate.
Distributed knowledge $D_G \varphi$ is the opposite construction, the box of the intersection of the relations.
In the game theory literature an event is a set of states, and $K_i(E)$ is the event that agent $i$ knows $E$.

## Remarks

### A first computation

Take three worlds in a row, $w_1$, $w_2$ and $w_3$, with $p$ true at $w_1$ and $w_2$ only.
Agent $a$ cannot tell $w_1$ from $w_2$, and agent $b$ cannot tell $w_2$ from $w_3$, and both relations are equivalence relations.
At $w_1$, agent $a$ considers $w_1$ and $w_2$, and agent $b$ considers only $w_1$, so both know $p$ and $E_G p$ is true at $w_1$.
At $w_2$, agent $b$ considers $w_3$ as well, where $p$ fails, so $E_G p$ is false at $w_2$.
Since $a$ considers $w_2$ at $w_1$, we get
$$M, w_1 \models E_G p \wedge \neg E_G^2 p.$$
So $p$ is mutual knowledge at $w_1$ but not common knowledge.
Check by reachability: $w_3$ is two steps from $w_1$ (via $a$ then $b$), and $p$ fails there.

### Fixed point and induction

The infinite conjunction has a finite description, by [[the theorem on the axioms of common knowledge|8K0CMPQXXB]].
The fixed point axiom says $C_G \varphi \leftrightarrow E_G (\varphi \wedge C_G \varphi)$: common knowledge is mutual knowledge of the fact and of its own common knowledge.
The induction rule says that from $\psi \to E_G (\varphi \wedge \psi)$ we may infer $\psi \to C_G \varphi$.
Together they make $C_G \varphi$ the greatest fixed point of $X \mapsto E_G (\varphi \wedge X)$.

The semantic side is reachability along the [[transitive closure|05J9NWX07X]] of $\bigcup_{a \in G} R_a$, so checking $C_G$ is a graph search.
[[The four-world example|365AVYV0MB]] does that search on a small model.
When every $R_a$ is an equivalence relation, the closure is too, so $C_G$ obeys $\mathsf{S5}$.

### Public versus private

After the father speaks in the [[muddy children puzzle|BG9TYCJ7HP]], "at least one child is muddy" is common knowledge, and before he speaks it is only mutual knowledge of finite depth.
That difference is what makes the puzzle work.
[[A public announcement|YDAHGYKQZN]] creates common knowledge in general, because it deletes the same worlds for everyone.

### What it is not

Mutual knowledge is not common knowledge, and the first computation shows a gap at depth 2.
Messages over an unreliable channel never create common knowledge, however many arrive, as [[the coordinated attack example|8XCDJBWS36]] shows.
Distributed knowledge is not common knowledge either: in [[the pooled information example|2C84ZDGE7K]] the group knows a fact in the distributed sense that no single member knows.

### Watch out

The reachability clause uses one or more steps, not zero or more.
So $C_G \varphi \to \varphi$ is valid on reflexive frames, but on a frame where $w$ sees only $v$, the fact $p$ can be common knowledge at $w$ and false there.

A second slip is to treat $C_G \varphi$ as a formula of plain epistemic logic.
Each $E_G^k \varphi$ is a formula, but their conjunction is not, and no formula without $C_G$ is equivalent to $C_G p$.
The reason is that a formula of modal depth $n$ cannot see worlds more than $n$ steps away.

### History

David Lewis analyzed conventions through common knowledge in Convention (1969).
Robert Aumann gave it a set-theoretic form with partitions in "Agreeing to disagree" (1976).
Halpern and Moses used it to analyze distributed protocols, and they showed that it cannot be reached over an unreliable channel.

### Try it

First, in the three-world model, is $p$ common knowledge at $w_1$ for the group $\{a\}$ alone?
Yes: for one agent with an equivalence relation, $C_{\{a\}} p$ is $K_a p$, and $a$ sees only $w_1$ and $w_2$.

Second, show that $C_G \varphi \to E_G^5 \varphi$ is valid.
A world five steps away along the union is reachable in one or more steps, so $\varphi$ holds there.

## Explanations

### L1 human

Common knowledge is what "everybody knows that everybody knows".
Suppose a teacher announces something to the whole class out loud.
Then every student knows it, every student knows that every other student heard it too, and so on.
That endless chain is common knowledge.
If instead the teacher tells each student the same thing in private, everyone knows it, but nobody knows that the others know.

### L2 human

Here is a typical check: is $p$ common knowledge at $w_1$ in a model with four worlds?
Draw the worlds, and draw an arrow for each pair related by some agent of the group.
Collect the worlds reachable from $w_1$ by one or more arrows, and check $p$ at each of them.
If $a$ links $w_1$ with $w_2$, $b$ links $w_2$ with $w_3$, and $w_4$ is linked to nothing, then the reachable set is $\{w_1, w_2, w_3\}$.
So $p$ is common knowledge at $w_1$ exactly when it holds at those three worlds, and $w_4$ does not matter.
The typical use is to find the first level at which a chain of "knows that knows" breaks, which is the length of the shortest path to a world where $p$ fails.

### L3 human

Common knowledge is the box of the transitive closure of $\bigcup_{a \in G} R_a$, so it is an iteration modality of the kind found in [[PDL|VJ78A0Q22R]] and in the mu-calculus.
The fixed point axiom and the induction rule make the logic $\mathsf{S5}_n^C$ weakly complete.
It is not compact: every finite part of $\{E_G^k p : k \ge 1\} \cup \{\neg C_G p\}$ is satisfiable, but the whole set is not.
Its satisfiability problem is EXPTIME-complete for two or more agents, compared with PSPACE without $C_G$.
[[Dynamic epistemic logic|9465T2PWZT]] studies how announcements and actions create it.
