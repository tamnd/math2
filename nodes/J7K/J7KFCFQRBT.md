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

Here is a short proof from a homework sheet; decide whether it proves the claim.

> Claim: for every integer $n$, if $n^2$ is even, then $n$ is even.
> Proof: let $n$ be even, say $n = 2k$, and then $n^2 = 4k^2 = 2(2k^2)$ is even.

The computation is right, but it proves a different statement, "if $n$ is even, then $n^2$ is even".
That is the [[converse|09A3N7ZN5G]] of the claim, and the claim is still open.
A correct proof shows the contrapositive: if $n$ is odd, say $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$ is odd.

The error is called affirming the consequent.
In general it is the invalid inference "if $P$ then $Q$; $Q$; therefore $P$".
Its twin, denying the antecedent, is the invalid inference "if $P$ then $Q$; not $P$; therefore not $Q$".
Both start from a true [[conditional statement|FA6YZGR2SS]] $P \Rightarrow Q$ and quietly use the converse $Q \Rightarrow P$ instead.

## Motivation

Two inference rules are valid, and each invalid form is one of them with $P$ and $Q$ swapped.
[[Modus ponens|0Y0MQYST0M]] concludes $Q$ from $P \Rightarrow Q$ and $P$; affirming the consequent concludes $P$ from $P \Rightarrow Q$ and $Q$.
Modus tollens concludes $\neg P$ from $P \Rightarrow Q$ and $\neg Q$; denying the antecedent concludes $\neg Q$ from $P \Rightarrow Q$ and $\neg P$.
In daily speech "if" often means "if and only if", as in "if you finish your homework, you can go out".
So everyday habit makes the invalid forms feel right, and a proof has to unlearn that habit.

## Notation

The errors have formal names in logic and informal names in teaching.
In $P \Rightarrow Q$, the statement $P$ is the antecedent, or hypothesis, and $Q$ is the consequent, or conclusion.
Affirming the consequent is also called the fallacy of the converse, and teachers call it "proving the converse".
Denying the antecedent is also called the fallacy of the inverse, after the inverse $\neg P \Rightarrow \neg Q$.
The inverse is the contrapositive of the converse, so it is equivalent to the converse.

## Remarks

### Examples to sort

Decide for each argument whether it is valid before you read the verdict.

1. "Every multiple of $4$ is even, and $6$ is even, so $6$ is a multiple of $4$." This [[affirms the consequent|2XXTDXK1ZC]], and the conclusion is false.
2. "Every multiple of $4$ is even, and $6$ is not a multiple of $4$, so $6$ is not even." This [[denies the antecedent|6FH1TVDXGS]], and the conclusion is false.
3. "Every multiple of $4$ is even, and $7$ is not even, so $7$ is not a multiple of $4$." This is [[modus tollens|QWTTHZ9C6T]], and it is valid.
4. "A differentiable function is continuous, and $|x|$ is continuous, so $|x|$ is differentiable." This affirms the consequent, and $|x|$ is [[not differentiable at $0$|0CQ9ZM383N]].

The inference from $P \Rightarrow Q$ to its [[contrapositive|04T1CT7212]] $\neg Q \Rightarrow \neg P$ is valid, since the two statements are equivalent.
When both directions of $P \Leftrightarrow Q$ are proved, concluding $P$ from $Q$ is valid too, because it uses the proved direction $Q \Rightarrow P$.

### Why the forms fail

One row of the truth table refutes both forms: $P$ false and $Q$ true.
In that row the premises $P \Rightarrow Q$ and $Q$ are true while $P$ is false, and the premises $P \Rightarrow Q$ and $\neg P$ are true while $\neg Q$ is false.
In words, a conditional says nothing about the cases where its hypothesis fails.
The two errors are one error in two disguises, since both use the converse without proof.

### Working backward

A disguised form is common in algebra.
A student starts from the identity to be proved, transforms it, reaches $0 = 0$, and writes "so the identity holds".
The steps prove "claim implies true", and concluding the claim from a true statement affirms the consequent.
The argument becomes a proof when every step can be reversed, because then the steps read backward form a direct proof.
[[Squaring both sides|FGS7ZJJYRK]] is a step that cannot be reversed, and [[non-reversible steps|641ZP4RA5S]] collects others.

### Watch out

A claim like "the solutions of $x^2 - 5x + 6 = 0$ are $2$ and $3$" has two directions.
Plugging in $2$ and $3$ proves only that they are solutions.
The other direction, that there are no others, needs the factoring $(x - 2)(x - 3) = 0$ and the fact that a product is $0$ only when a factor is $0$.
Also, "$P$ only if $Q$" means "if $P$ then $Q$", not "if $Q$ then $P$".

### History

Logic textbooks list both forms among the standard formal fallacies, and each name describes the second premise of the form.
Charles Sanders Peirce called the inference from a fact $Q$ and a rule $P \Rightarrow Q$ to the hypothesis $P$ abduction, and he treated it as a way to form hypotheses, not to prove them.

### Try it

A rectangle is a parallelogram, and a given quadrilateral is not a rectangle.
Can you conclude that it is not a parallelogram?
No: that denies the antecedent, and a rhombus that is not a square is a counterexample.

A student proves "if $3 \mid n$, then $3 \mid n^2$" to show that "$3 \mid n^2$ implies $3 \mid n$".
What is missing?
The given direction is the converse, and the claim needs its own proof, for example that $3 \nmid n$ gives $n^2 \equiv 1 \pmod 3$.

## Explanations

### L1 human

"If it is a dog, then it has four legs" is true.
A cat also has four legs, but it is not a dog.
So "it has four legs, so it is a dog" is a bad argument, and that is affirming the consequent.
"It is not a dog, so it does not have four legs" is bad too, and that is denying the antecedent.
Both mistakes read the "if" sentence backward.

### L2 human

We check a student proof that, for real $x$, if $x^2 - 5x + 6 = 0$, then $x = 2$ or $x = 3$.
The student writes: "If $x = 2$, then $4 - 10 + 6 = 0$, and if $x = 3$, then $9 - 15 + 6 = 0$, so the claim holds."
These computations prove the converse, that $2$ and $3$ are roots.
The claim says that no other $x$ is a root, and the computations say nothing about that.
A proof of the claim: $x^2 - 5x + 6 = (x - 2)(x - 3)$, and a product of real numbers is $0$ only when a factor is $0$.
Together the two arguments prove the biconditional.

The typical use of this check is to write the claim as $P \Rightarrow Q$ before reading a proof, and to verify that the proof starts at $P$ and ends at $Q$.
Watch out: a proof that ends at $P$ has gone the wrong way, however clean its steps are.

### L3 human

A rule is valid when every valuation that makes its premises true makes its conclusion true, and both forms fail at the valuation with $P$ false and $Q$ true.
No proof system for classical logic derives either rule, and each becomes derivable only when the converse is added as a premise.
In probability, affirming the consequent turns into the question of how much $Q$ supports $P$.
Bayes' formula answers it: the support depends on how likely $Q$ is when $P$ fails, which is a question for statistics, not for proof.
In analysis the same pattern appears when a necessary condition, such as $f'(c) = 0$ for an interior extremum, is used as if it were sufficient.
