---
tag: ~1fb74cff
kind: example
name: Deep inference proof of identity for a conjunction
msc: ["03F05", "03F52"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [~110b1691]
uses: [~110b1691, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Calculus_of_structures
    locator: SKSg
  - url: https://en.wikipedia.org/wiki/Deep_inference
    locator: lead section
---

## Example

We prove the formula
$$(a \wedge b) \vee \bar{a} \vee \bar{b}$$
in the system SKS of [[deep inference|~110b1691]].
By the De Morgan laws, $\bar{a} \vee \bar{b}$ is the negation of $a \wedge b$, so the formula is the [[law of excluded middle|0RYYK8PG4S]] for $a \wedge b$.
The proof uses only atomic identity $\mathsf{ai}{\downarrow}$, switch $\mathsf{s}$ and the equations.
Each step names the rule, the context $S\{\ \}$ and the rewritten subformula.

1. Start from $\mathsf{t}$. The equation $A \wedge \mathsf{t} = A$ with $A = \mathsf{t}$ gives $\mathsf{t} \wedge \mathsf{t}$.
2. Apply $\mathsf{ai}{\downarrow}$ in the context $\{\ \} \wedge \mathsf{t}$. This gives $(a \vee \bar{a}) \wedge \mathsf{t}$.
3. Apply $\mathsf{ai}{\downarrow}$ in the context $(a \vee \bar{a}) \wedge \{\ \}$. This gives $(a \vee \bar{a}) \wedge (b \vee \bar{b})$.
4. Apply $\mathsf{s}$ in the empty context, with $A = a \vee \bar{a}$, $B = b$ and $C = \bar{b}$. This gives $((a \vee \bar{a}) \wedge b) \vee \bar{b}$.
5. Commutativity of $\wedge$ rewrites the left disjunct as $b \wedge (a \vee \bar{a})$.
6. Apply $\mathsf{s}$ in the context $\{\ \} \vee \bar{b}$, with $A = b$, $B = a$ and $C = \bar{a}$. This gives $((b \wedge a) \vee \bar{a}) \vee \bar{b}$.
7. Associativity of $\vee$ and commutativity of $\wedge$ give $(a \wedge b) \vee \bar{a} \vee \bar{b}$.

Step 6 is a deep step: the rule acts on the left disjunct and leaves $\bar{b}$ unchanged.
Both contexts used for switch are positive, because negation occurs only on atoms.

We check that the two switch instances are sound.

8. Switch is valid: if $A$ holds and $B \vee C$ holds, then $A \wedge B$ holds or $C$ holds.
9. In step 4 the premise $(a \vee \bar{a}) \wedge (b \vee \bar{b})$ is true for all values, and so is the conclusion.
10. In step 6 the context $\{\ \} \vee \bar{b}$ is monotone, so the valid implication of step 8 stays valid inside it.

## Remarks

The same pattern proves $A \vee \bar{A}$ for every formula $A$, by induction on $A$.
For $A = B \wedge C$, we use $\mathsf{t} \wedge \mathsf{t}$, the identities for $B$ and $C$ inside the two halves, and two switches as above.
For $A = B \vee C$, we start from $(\bar{B} \vee B) \wedge (\bar{C} \vee C)$ and the same two switches give $((\bar{C} \wedge \bar{B}) \vee B) \vee C$.
So the general identity rule is derivable, and the system needs identity only for atoms.

In a sequent calculus, the identity axiom for $a \wedge b$ would be derived with the rules ${\wedge}$L and ${\wedge}$R, which act on the main connective.
In deep inference the work is done inside the formula by switch.

## Explanations

### L1 human

The goal is the statement "($a$ and $b$) is true, or $a$ is false, or $b$ is false".
This is always true, and we want to build it from very small steps.
We start from "true", and replace it by "$a$ or not $a$" and by "$b$ or not $b$".
Then the switch rule moves pieces around inside the formula, one small step at a time.
At the end we have exactly the goal, and every step touched only a small part of the formula.

### L2 human

The proof has two phases.

1. Create atomic identities: two steps of $\mathsf{ai}{\downarrow}$ turn $\mathsf{t} \wedge \mathsf{t}$ into $(a \vee \bar{a}) \wedge (b \vee \bar{b})$.
2. Rearrange: two switches, the second one deep inside a disjunction, bring $a$ and $b$ together under one conjunction.

The typical use of this pattern is to reduce general identity to atomic identity.
A trap is to apply switch the wrong way round: from $(A \wedge B) \vee C$ to $A \wedge (B \vee C)$ is not valid when $A$ is false and $C$ is true.
