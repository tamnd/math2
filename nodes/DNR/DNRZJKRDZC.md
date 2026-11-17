---
tag: DNRZJKRDZC
kind: example
name: A formal derivation of the transitivity of implication
msc: ["00A35", "03F03"]
topics: [1BTHSHST4M]
audience: ug2
instance_of: [8VZ77R4R8S]
uses: [8VZ77R4R8S, 6KT3BJZ7D1, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Formal_proof
    locator: lead section
---

## Example

We derive the formula $(P \to Q) \to ((Q \to R) \to (P \to R))$ in [[natural deduction|6KT3BJZ7D1]] for propositional logic, with no premises.
Two rules suffice.
The rule $\to$E, or [[modus ponens|0Y0MQYST0M]], gives $B$ from $A \to B$ and $A$.
The rule $\to$I gives $A \to B$ from a derivation of $B$ under the assumption $A$, and it discharges $A$.

1. $P \to Q$. Assumption, to be discharged at line 8.
2. $Q \to R$. Assumption, to be discharged at line 7.
3. $P$. Assumption, to be discharged at line 6.
4. $Q$. By $\to$E from lines 1 and 3.
5. $R$. By $\to$E from lines 2 and 4.
6. $P \to R$. By $\to$I from lines 3 to 5; the assumption of line 3 is discharged.
7. $(Q \to R) \to (P \to R)$. By $\to$I from lines 2 to 6; the assumption of line 2 is discharged.
8. $(P \to Q) \to ((Q \to R) \to (P \to R))$. By $\to$I from lines 1 to 7; the assumption of line 1 is discharged.

After line 8 no assumption remains open, so the formula of line 8 is a theorem of the system.
Each line names its rule and the earlier lines that it uses, which is what makes the derivation a [[formal proof|8VZ77R4R8S]].

## Remarks

The informal proof of the same fact is one sentence: "if $P$ gives $Q$ and $Q$ gives $R$, then $P$ gives $R$".
The formal derivation makes three things explicit.
It shows the order in which the assumptions are made and dropped.
It shows that the proof uses only the rules for $\to$, and no rule for negation or for "or".
It lets a program check the derivation line by line, by comparing each line with the pattern of its rule.

The derivation is valid in intuitionistic logic as well as in classical logic, since it uses no rule for negation.
Under the Curry-Howard correspondence it matches the program that composes two functions.

## Explanations

### L1 human

The sentence "if it rains, the ground is wet; if the ground is wet, the grass is slippery; so if it rains, the grass is slippery" is an informal proof.
A formal proof writes each small step on its own line and names the rule that allows it.
First we assume the two "if" sentences, then we assume that it rains.
Then we use the first "if" sentence to get "the ground is wet", and the second to get "the grass is slippery".
Last, we drop the assumption that it rains, and we keep the "if" sentence.

### L2 human

We check line 5 and line 6 against the rules.

1. Line 5 claims $R$ by $\to$E from lines 2 and 4. Line 2 has the form $A \to B$ with $A = Q$ and $B = R$, and line 4 is $A = Q$. So the rule gives $B = R$, as claimed.
2. Line 6 claims $P \to R$ by $\to$I from lines 3 to 5. Line 3 assumes $P$, and line 5 derives $R$ while line 3 is open. So the rule gives $P \to R$ and closes line 3.

The typical use of such a check is to find an error in a derivation, for example a rule applied to the wrong lines.
A trap is to use a line after its assumption has been discharged: after line 6, line 4 depends on a closed assumption, and it may not be used again.
