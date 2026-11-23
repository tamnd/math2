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

The informal argument is one sentence: if $P$ gives $Q$ and $Q$ gives $R$, then $P$ gives $R$.
We turn it into a derivation of
$$(P \to Q) \to \big((Q \to R) \to (P \to R)\big)$$
in [[natural deduction|6KT3BJZ7D1]] for propositional logic, with no premises.

Two rules are enough.
The rule $\to$E, which is [[modus ponens|0Y0MQYST0M]], gives $B$ from $A \to B$ and $A$.
The rule $\to$I gives $A \to B$ from a derivation of $B$ under the assumption $A$, and it discharges $A$, so $A$ is no longer an open assumption.

1. $P \to Q$. Assumption, discharged at line 8.
2. $Q \to R$. Assumption, discharged at line 7.
3. $P$. Assumption, discharged at line 6.
4. $Q$. By $\to$E from lines 1 and 3.
5. $R$. By $\to$E from lines 2 and 4.
6. $P \to R$. By $\to$I from lines 3 to 5, which discharges line 3.
7. $(Q \to R) \to (P \to R)$. By $\to$I from lines 2 to 6, which discharges line 2.
8. $(P \to Q) \to ((Q \to R) \to (P \to R))$. By $\to$I from lines 1 to 7, which discharges line 1.

After line 8 no assumption is open, so the formula of line 8 is a theorem of the system.
Each line names its rule and the earlier lines that it uses, and that is what makes the derivation a [[formal proof|8VZ77R4R8S]].

## Remarks

The derivation makes three things visible that the one-sentence argument hides.
It shows the order in which the assumptions are made and dropped: the last one made is the first one dropped.
It shows that the proof uses only the rules for $\to$, and no rule for negation or for "or".
And it lets a program check each line by comparing it with the pattern of its rule.

Because no rule for negation appears, the derivation is valid in intuitionistic logic as well as in classical logic.
Under the Curry-Howard correspondence it matches the program that takes functions $f$ from $P$ to $Q$ and $g$ from $Q$ to $R$ and returns their composite $x \mapsto g(f(x))$.

What changes if we drop line 2 and make $Q \to R$ a premise instead?
Then line 7 disappears, and the derivation proves $(P \to Q) \to (P \to R)$ from the premise $Q \to R$, which is the statement $\{Q \to R\} \vdash (P \to Q) \to (P \to R)$.

## Explanations

### L1 human

The sentence "if it rains, the ground is wet; if the ground is wet, the grass is slippery; so if it rains, the grass is slippery" is an informal proof.
A formal proof writes each small step on its own line and names the rule that allows it.
First we assume the two "if" sentences, and then we assume that it rains.
The first "if" sentence gives "the ground is wet", and the second gives "the grass is slippery".
Last, we drop the assumption that it rains and keep the "if" sentence that we have earned.

### L2 human

We check lines 5 and 6 against their rules.
Line 5 claims $R$ by $\to$E from lines 2 and 4.
Line 2 has the form $A \to B$ with $A = Q$ and $B = R$, and line 4 is $Q$, so the rule gives $R$, as claimed.
Line 6 claims $P \to R$ by $\to$I from lines 3 to 5.
Line 3 assumes $P$, and line 5 derives $R$ while line 3 is still open, so the rule gives $P \to R$ and closes line 3.

The typical use of such a check is to find an error in a derivation, for example a rule applied to the wrong lines.
Watch out for a line used after its assumption has been discharged.
After line 6, line 4 depends on the closed assumption $P$, so no later line may use it.
