---
tag: 8K0CMPQXXB
kind: statement
role: theorem
name: Fixed point axiom, induction rule and reachability for common knowledge
msc: ["03B42", "03B45"]
topics: [CQM9SRN8PM]
audience: grad
uses: [7BCMKF2P7X, RRRHWH9F6Y, ERG3KAQWYF, 05J9NWX07X, 0FDKRX9M9Y, DBD64TH52D, RHXP3HA64M]
about: [7BCMKF2P7X]
proofs: [8Y7VESEXNG]
sources:
  - url: https://en.wikipedia.org/wiki/Common_knowledge_(logic)
    locator: section Modal logic (syntactic characterization)
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapters 2 and 3
---

## Statement

Common knowledge, defined as an infinite conjunction, is the same as truth along all paths of the agents' relations, and it is the greatest solution of a short equation.

Let $M = (W, (R_a)_{a \in \mathcal{A}}, V)$ be a multi-agent Kripke model, with no condition on the relations.
Let $G \subseteq \mathcal{A}$ be nonempty, and interpret $C_G$ as in [[the definition of common knowledge|RRRHWH9F6Y]].
Let $R_G = \bigcup_{a \in G} R_a$, and let $R_G^+$ be its [[transitive closure|05J9NWX07X]], so $w R_G^+ v$ when $v$ is reachable from $w$ in one or more $R_G$-steps.
Write $[\![\chi]\!]$ for the set of worlds where $\chi$ is true.

1. Reachability: $M, w \models C_G \varphi$ if and only if $M, v \models \varphi$ for every $v$ with $w R_G^+ v$.
2. Fixed point axiom: $C_G \varphi \leftrightarrow E_G (\varphi \wedge C_G \varphi)$ is true at every world of $M$.
3. Induction rule: if $\psi \to E_G (\varphi \wedge \psi)$ is true at every world of $M$, then so is $\psi \to C_G \varphi$.
4. Greatest fixed point: for $Y \subseteq W$ let $f(Y) = \{w : v \in [\![\varphi]\!] \cap Y \text{ for all } v \text{ with } w R_G v\}$.
   Then $[\![C_G \varphi]\!]$ is the largest $Y$ with $Y \subseteq f(Y)$, and it satisfies $f(Y) = Y$.

## Remarks

### Why each hypothesis is needed

The group must be nonempty so that $E_G$ is a real conjunction.
For the empty group, $E_G \varphi$ is the empty conjunction $\top$, and $C_G \varphi$ becomes $\top$ as well, which carries no information.

The reachability clause uses one or more steps, and that choice matters.
With zero steps allowed, $C_G \varphi$ would imply $\varphi$ on every frame.
But if $w$ sees only $v$ and $v$ sees only $v$, with $p$ true at $v$ only, then every $E_G^k p$ holds at $w$ while $p$ fails there.

No condition on the relations is needed, and that is a strength.
The theorem covers common belief, with relations of $\mathsf{KD45}$ type, as well as common knowledge with equivalence relations.

### What it gives you

Adding the fixed point axiom and the induction rule to $\mathsf{K}_n$, $\mathsf{T}_n$, $\mathsf{S4}_n$, $\mathsf{S5}_n$ or $\mathsf{KD45}_n$ gives a sound and complete axiomatization with common knowledge.
Fagin, Halpern, Moses and Vardi prove the completeness, by a finite canonical model, in chapter 3.

Part 2 gives $C_G \varphi \to E_G^k \varphi$ for every $k$, by induction on $k$.
If every $R_a$ with $a \in G$ is an equivalence relation, so is $R_G^+$, and part 1 then shows that $C_G$ obeys $\mathsf{S5}$.
Part 1 also reduces model checking of $C_G$ to graph [[reachability|0FDKRX9M9Y]], which takes time linear in the size of the model.

### Fixed point and induction together

The fixed point axiom says that $[\![C_G \varphi]\!]$ is a fixed point of the monotone map $f$.
The induction rule says that every post-fixed point lies below it, so it is the greatest one, as in the [[Knaster-Tarski theorem|RHXP3HA64M]].
This is the dual of the [[least fixed point|DBD64TH52D]] description of reachability.
In the modal mu-calculus the theorem reads $C_G \varphi = \nu X.\, E_G (\varphi \wedge X)$.
In [[propositional dynamic logic|VJ78A0Q22R]], $C_G \varphi$ is $[(a_1 \cup \cdots \cup a_n)^+] \varphi$ for $G = \{a_1, \dots, a_n\}$.

## History

Halpern and Moses used the fixed point axiom and the induction rule in their work on knowledge in distributed systems.
Their 1992 paper "A guide to completeness and complexity for modal logics of knowledge and belief" proved completeness and complexity results for these logics.
Barwise compared the iterate, fixed point and shared situation views of common knowledge in 1988.

## Explanations

### L1 human

Common knowledge has a short description that refers to itself.
"Everyone knows the fact, and everyone knows that it is common knowledge" says the same thing as the infinite tower of "knows that knows".
To prove that something is common knowledge, find a situation that tells everyone the fact, and that everyone knows has happened.

### L2 human

Here is a typical use of the induction rule: a public announcement.
Let $\psi$ say "$\varphi$ was announced publicly, and $\varphi$ is true".
Suppose that in our model, wherever $\psi$ holds, every agent knows $\varphi$ and knows that $\psi$ holds.
That is exactly the premise, valid in the whole model:
$$\psi \to E_G (\varphi \wedge \psi).$$
The induction rule then gives $\psi \to C_G \varphi$, so the announcement makes $\varphi$ common knowledge.
Watch out: the premise must be true at every world of the model, not only at the actual world, or the rule does not apply.

### L3 human

Parts 1 and 4 are the two classical views of common knowledge, iteration and fixed point, and part 3 is the finitary rule that links them.
The rule replaces an infinite conjunction, at the price of compactness: the set $\{E_G^k p : k \ge 1\} \cup \{\neg C_G p\}$ is finitely satisfiable but not satisfiable.
[[Public announcement logic|9465T2PWZT]] with common knowledge needs a further rule of the same shape, because its reduction axioms do not cover $C_G$.
