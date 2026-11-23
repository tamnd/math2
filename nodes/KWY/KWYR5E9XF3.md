---
tag: KWYR5E9XF3
kind: example
name: Deep inference proof of identity for a conjunction
msc: ["03F05", "03F52"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [4ZW0SHW2RG]
uses: [4ZW0SHW2RG, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_structures
    locator: SKSg
  - url: https://en.wikipedia.org/wiki/Deep_inference
    locator: lead section
---

## Example

We prove the formula
$$(a \wedge b) \vee \bar{a} \vee \bar{b}$$
in the system SKS of [[deep inference|4ZW0SHW2RG]].
By the De Morgan laws, $\bar{a} \vee \bar{b}$ is the negation of $a \wedge b$, so the formula is the [[law of excluded middle|0RYYK8PG4S]] for $a \wedge b$.
The proof uses only atomic identity $\mathsf{ai}{\downarrow}$, switch $\mathsf{s}$ and the equations.
Each step names the rule, the context $S\{\ \}$ and the rewritten subformula.

1. Start from $\mathsf{t}$, and use the equation $A \wedge \mathsf{t} = A$ with $A = \mathsf{t}$ to get $\mathsf{t} \wedge \mathsf{t}$.
2. Apply $\mathsf{ai}{\downarrow}$ in the context $\{\ \} \wedge \mathsf{t}$, which gives $(a \vee \bar{a}) \wedge \mathsf{t}$.
3. Apply $\mathsf{ai}{\downarrow}$ in the context $(a \vee \bar{a}) \wedge \{\ \}$, which gives $(a \vee \bar{a}) \wedge (b \vee \bar{b})$.
4. Apply $\mathsf{s}$ in the empty context, with $A = a \vee \bar{a}$, $B = b$ and $C = \bar{b}$, which gives $((a \vee \bar{a}) \wedge b) \vee \bar{b}$.
5. Commutativity of $\wedge$ rewrites the left disjunct as $b \wedge (a \vee \bar{a})$.
6. Apply $\mathsf{s}$ in the context $\{\ \} \vee \bar{b}$, with $A = b$, $B = a$ and $C = \bar{a}$, which gives $((b \wedge a) \vee \bar{a}) \vee \bar{b}$.
7. Associativity of $\vee$ and commutativity of $\wedge$ give $(a \wedge b) \vee \bar{a} \vee \bar{b}$.

Step 6 is a deep step: the rule acts on the left disjunct and leaves $\bar{b}$ alone.
Both contexts used for switch are positive, because negation occurs only on atoms.

Finally we check that the switch steps are sound.

8. Switch is valid: if $A$ holds and $B \vee C$ holds, then $A \wedge B$ holds when $B$ does, and $C$ holds otherwise.
9. The context $\{\ \} \vee \bar{b}$ of step 6 is monotone: if $X \to Y$ is valid, so is $X \vee \bar{b} \to Y \vee \bar{b}$.
10. So each step goes from a true formula to a true formula, and the conclusion is a tautology.

Check: under $a$ true and $b$ false the goal reads "false or false or true", which is true.

## Remarks

The same pattern proves $A \vee \bar{A}$ for every formula $A$, by induction on $A$.
For $A = B \wedge C$, start from $\mathsf{t} \wedge \mathsf{t}$, prove the identities for $B$ and $C$ inside the two halves, and use two switches as above.
For $A = B \vee C$, start from $(\bar{B} \vee B) \wedge (\bar{C} \vee C)$, and the same two switches give $((\bar{C} \wedge \bar{B}) \vee B) \vee C$.
So the general identity rule is derivable, and the system needs identity only for atoms.

Compare a sequent calculus.
There the identity $a \wedge b \Rightarrow a \wedge b$ comes from ${\wedge}$L and ${\wedge}$R, rules that act on the main connective.
In deep inference the same work happens inside one formula, by switch.

If the switches are done in the other order, first on $b \vee \bar{b}$ and then on $a \vee \bar{a}$, the proof ends in $(b \wedge a) \vee \bar{b} \vee \bar{a}$, the same formula modulo the equations.

## Explanations

### L1 human

The goal is the statement "($a$ and $b$) is true, or $a$ is false, or $b$ is false".
This is always true, and we want to build it from very small steps.
We start from "true", and replace it by "$a$ or not $a$" and "$b$ or not $b$".
Then the switch rule moves pieces around inside the formula, one small step at a time.
At the end we have exactly the goal, and every step touched only a small part of the formula.

### L2 human

The proof has two phases.
First, atomic identities: two steps of $\mathsf{ai}{\downarrow}$ turn $\mathsf{t} \wedge \mathsf{t}$ into $(a \vee \bar{a}) \wedge (b \vee \bar{b})$.
Then rearrangement: two switches, the second one deep inside a disjunction, bring $a$ and $b$ together under one conjunction.
This two-phase pattern is how every identity reduces to atomic identities.
Watch out for the direction of switch.
From $(A \wedge B) \vee C$ to $A \wedge (B \vee C)$ is not valid, since it fails when $A$ is false and $C$ is true.
