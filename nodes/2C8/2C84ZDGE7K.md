---
tag: 2C84ZDGE7K
kind: example
name: Distributed knowledge that no agent has
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: grad
instance_of: [EA34W4ERRE]
uses: [7BCMKF2P7X, 0G8VEZ3WTK, ERG3KAQWYF]
sources:
  - book: isbn:9780262562003
    locator: Fagin, Halpern, Moses and Vardi, Reasoning about Knowledge, chapter 2
  - url: https://en.wikipedia.org/wiki/Epistemic_modal_logic
    locator: section Multi-agent systems
---

## Example

Ann knows that $p$ is true, and Bob knows that $p \to q$ is true.
Neither of them knows $q$, but if they pooled what they know, modus ponens would give it.
In [[epistemic logic|EA34W4ERRE]] this pooled knowledge is distributed knowledge.
For a group $G$, the formula $D_G \varphi$ is true at $w$ when $\varphi$ holds at every $v$ with $w R_a v$ for all $a \in G$.

Take two atoms $p$ and $q$, and one world for each valuation.
$$w_1 = (p, q), \quad w_2 = (p, \neg q), \quad w_3 = (\neg p, q), \quad w_4 = (\neg p, \neg q).$$
Agent $a$ has seen whether $p$ holds, and agent $b$ has seen whether $p \to q$ holds.
So both relations are [[equivalence relations|0G8VEZ3WTK]], and their classes are as follows.
Agent $a$ has the classes $\{w_1, w_2\}$, where $p$ is true, and $\{w_3, w_4\}$, where $p$ is false.
Agent $b$ has the classes $\{w_1, w_3, w_4\}$, where $p \to q$ is true, and $\{w_2\}$, where it is false.
We evaluate at $w_1$ with $G = \{a, b\}$.

1. $K_a p$ is true, since $p$ is true at both worlds of $\{w_1, w_2\}$.
2. $K_b (p \to q)$ is true, since $p \to q$ is true at $w_1$, $w_3$ and $w_4$.
3. $K_a q$ is false, since $q$ is false at $w_2$, which $a$ cannot rule out.
4. $K_b q$ is false, since $q$ is false at $w_4$, which $b$ cannot rule out.
5. The worlds that neither agent can rule out are the common ones:
   $$\{w_1, w_2\} \cap \{w_1, w_3, w_4\} = \{w_1\}.$$
6. The atom $q$ is true at $w_1$, so $D_G q$ is true at $w_1$.

Neither agent knows $q$, but the group knows it in the distributed sense.

## Remarks

Distributed knowledge is the box of the intersection $\bigcap_{a \in G} R_a$.
[[Common knowledge|7BCMKF2P7X]] is the box of the transitive closure of the union, so the two group operators sit at opposite ends.
The chain $C_G \varphi \to E_G \varphi \to D_G \varphi$ is valid, and here $D_G q$ holds while $E_G q$ fails at the first step.
For a group with one member, $D_{\{a\}}$ is just $K_a$.

If $a$ tells $b$ that $p$ is true, then $b$ removes $w_3$ and $w_4$ from his class and now knows $q$.
So distributed knowledge is what a full exchange of messages could turn into knowledge.
If we change $b$'s information to "whether $q$ holds", the intersection at $w_1$ is $\{w_1, w_2\} \cap \{w_1, w_3\} = \{w_1\}$ again, but now $b$ knows $q$ alone.

## Explanations

### L1 human

Ann knows it rained, and Bob knows that if it rained the match was cancelled.
Neither knows the match was cancelled.
Together they have all the information, so the fact is distributed knowledge.
It becomes real knowledge once they talk.

### L2 human

To check $D_G \varphi$ at a world, list for each agent the worlds she cannot rule out there, intersect the lists, and check $\varphi$ on the intersection.
Here the intersection at $w_1$ is $\{w_1\}$, so every fact true at $w_1$ is distributed knowledge at $w_1$.
The typical use is to describe what a system of processes knows as a whole.
Watch out: $D_G \varphi$ is not $K_a \varphi \vee K_b \varphi$, and in this example both disjuncts fail while $D_G q$ holds.

### L3 human

$D_G$ is not definable from the boxes $K_a$, because intersection of relations is not modally definable.
The usual axioms add $D_{\{a\}} \varphi \leftrightarrow K_a \varphi$, monotonicity $D_G \varphi \to D_{G'} \varphi$ for $G \subseteq G'$, and the $\mathsf{S5}$ axioms for each $D_G$.
The intersection of equivalence relations is an equivalence relation, so $D_G$ also obeys $\mathsf{S5}$.
