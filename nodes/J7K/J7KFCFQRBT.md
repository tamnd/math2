---
tag: J7KFCFQRBT
kind: concept
name: Affirming the consequent and denying the antecedent
aliases: [affirming-the-consequent-in-proofs, affirming-the-consequent, denying-the-antecedent, fallacy-of-the-converse, fallacy-of-the-inverse]
msc: ["00A35", "97E30"]
topics: [T6QQ749DM5]
audience: school
uses: [FA6YZGR2SS, 09A3N7ZN5G, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Affirming_the_consequent
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Denying_the_antecedent
    locator: lead section
  - book: isbn:9781108439534
---

## Summary

Affirming the consequent is the invalid inference "if $P$ then $Q$; $Q$; therefore $P$", and denying the antecedent is the invalid inference "if $P$ then $Q$; not $P$; therefore not $Q$".
Both start from a true [[conditional statement|FA6YZGR2SS]] $P \Rightarrow Q$ and draw a conclusion that would need a different statement: affirming the consequent needs the [[converse|09A3N7ZN5G]] $Q \Rightarrow P$, and denying the antecedent needs the inverse $\neg P \Rightarrow \neg Q$.
In proofs they appear as proving the converse instead of the claim, and as deriving a true statement from the claim and concluding that the claim is true.
The idea matters because these two errors are the most common logical errors in the proofs of students, and each looks like a valid rule.

## Motivation

The valid rule [[modus ponens|0Y0MQYST0M]] says: from $P \Rightarrow Q$ and $P$, conclude $Q$.
The valid rule modus tollens says: from $P \Rightarrow Q$ and $\neg Q$, conclude $\neg P$.
Each invalid form looks like one of these rules with the roles of $P$ and $Q$ exchanged.
In ordinary speech, "if" often means "if and only if", as in "if you finish your work, you can go out".
So the habit of daily language makes the two invalid forms feel correct, and a proof must break that habit.

## Notation

The errors have formal names in logic and informal names in teaching.

1. Affirming the consequent is also called the fallacy of the converse, or "proving the converse". In a proof it often reads "we want $P$; $P$ implies $Q$; $Q$ is true; done".
2. Denying the antecedent is also called the fallacy of the inverse. The inverse of $P \Rightarrow Q$ is $\neg P \Rightarrow \neg Q$, and it is equivalent to the converse.
3. In the conditional $P \Rightarrow Q$, $P$ is the antecedent (or hypothesis) and $Q$ is the consequent (or conclusion).

## Remarks

### Examples

1. "Every multiple of $4$ is even, and $6$ is even, so $6$ is a multiple of $4$" [[affirms the consequent|2XXTDXK1ZC]]. The conclusion is false.
2. "Every multiple of $4$ is even, and $6$ is not a multiple of $4$, so $6$ is not even" [[denies the antecedent|6FH1TVDXGS]]. The conclusion is false.
3. A student must prove "if $n^2$ is even, then $n$ is even", and proves "if $n$ is even, then $n^2$ is even". This proves the converse, and the claim remains unproved.
4. A student "proves" an identity by starting from it and deriving $0 = 0$. The steps prove "claim implies true", and concluding the claim affirms the consequent. The page on [[squaring both sides|FGS7ZJJYRK]] shows that the method can "prove" a false identity.
5. "A differentiable function is continuous, and $|x|$ is continuous, so $|x|$ is differentiable" affirms the consequent. The function $|x|$ is [[not differentiable at $0$|0CQ9ZM383N]].

### Non-examples

1. [[Modus tollens|QWTTHZ9C6T]]: "every multiple of $4$ is even, and $7$ is not even, so $7$ is not a multiple of $4$". This is valid.
2. The inference from $P \Rightarrow Q$ to its [[contrapositive|04T1CT7212]] $\neg Q \Rightarrow \neg P$ is valid, because the two statements are equivalent.
3. When the claim is a biconditional $P \Leftrightarrow Q$ and both directions are proved, the inference from $Q$ to $P$ is valid. It uses the proved direction $Q \Rightarrow P$.

### Basic properties

1. The truth table shows the failure: when $P$ is false and $Q$ is true, the premises $P \Rightarrow Q$ and $Q$ are true and the conclusion $P$ is false.
2. The same row refutes denying the antecedent: $P \Rightarrow Q$ and $\neg P$ are true there, and $\neg Q$ is false.
3. The two errors are one error in two forms. The inverse $\neg P \Rightarrow \neg Q$ is the contrapositive of the converse $Q \Rightarrow P$, so both errors use the converse without a proof.
4. A derivation "claim, therefore true statement" proves the claim when each step can be reversed. Then the steps read backwards are a direct proof. The page on [[non-reversible steps|641ZP4RA5S]] shows the steps that cannot be reversed.

### History

The names "affirming the consequent" and "denying the antecedent" describe the second premise of each form, and logic textbooks list both forms as standard formal fallacies.
Charles Sanders Peirce described abduction, the inference from an observed fact $Q$ and a rule $P \Rightarrow Q$ to the hypothesis $P$, as a way to form hypotheses, not to prove them.

### Common errors

1. A student proves the converse of the claim, often because the converse is the easier direction.
2. A student starts from the claim, reaches a true statement, and writes "so the claim holds".
3. A student reads "$P$ only if $Q$" as "if $Q$ then $P$". The correct reading is "if $P$ then $Q$".

## Explanations

### L1 human

"If it is a dog, then it has four legs" is true.
A cat also has four legs, but it is not a dog.
So "it has four legs, so it is a dog" is a bad argument: this is affirming the consequent.
And "it is not a dog, so it does not have four legs" is also bad: this is denying the antecedent.
Both mistakes read the "if" sentence backwards.

### L2 human

We check a student proof of the claim: for real $x$, if $x^2 - 5x + 6 = 0$, then $x = 2$ or $x = 3$.

1. The student writes: "If $x = 2$, then $x^2 - 5x + 6 = 4 - 10 + 6 = 0$. If $x = 3$, then $9 - 15 + 6 = 0$. So the claim holds."
2. These computations prove the converse: if $x = 2$ or $x = 3$, then $x^2 - 5x + 6 = 0$.
3. The claim says something else: no other $x$ is a root. The computations do not show this.
4. A proof of the claim: $x^2 - 5x + 6 = (x - 2)(x - 3)$. If the product is $0$, then one factor is $0$, so $x = 2$ or $x = 3$.
5. Together, the student's computation and step 4 prove the biconditional: $x^2 - 5x + 6 = 0$ exactly when $x = 2$ or $x = 3$.

The typical use of this check is to write the claim as $P \Rightarrow Q$ before the proof, and to verify that the proof starts from $P$ and ends at $Q$.
A trap is a claim of the form "the solutions are $2$ and $3$", which needs both directions: the two numbers are solutions, and there are no others.

### L3 human

In a semantics of truth values, a rule is valid when every valuation that makes the premises true makes the conclusion true; both forms fail at the valuation $P$ false, $Q$ true.
In a proof system, they correspond to no derivable rule, and they become valid only when the converse is added as a premise.
In probability, affirming the consequent becomes the question of how much $Q$ supports $P$, and Bayes' formula shows that the support depends on how likely $Q$ is without $P$; this is the subject of statistical reasoning, not of proof.
The same pattern appears in algebra as the confusion between a necessary condition and a sufficient condition, and in analysis as the use of a necessary condition such as $f'(c) = 0$ as if it were sufficient for an extremum.
