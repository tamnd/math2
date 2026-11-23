---
tag: QWTTHZ9C6T
kind: example
name: Modus tollens is a valid deduction
msc: ["00A35", "97E30"]
topics: [T6QQ749DM5, PM1AYWABA7]
audience: school
instance_of: [32AQPJQQAM]
not_instance_of:
  - target: J7KFCFQRBT
    note: the argument denies the consequent, not the antecedent, and this form is valid
uses: [J7KFCFQRBT, 04T1CT7212, 0Y0MQYST0M, 32AQPJQQAM]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_tollens
    locator: lead section
---

## Example

This argument looks a lot like a famous fallacy; decide whether it is valid before you read on.

> Every integer divisible by $4$ is even.
> The integer $7$ is not even.
> So $7$ is not divisible by $4$.

It is valid, and it is not an instance of [[affirming the consequent or denying the antecedent|J7KFCFQRBT]].
We check this in four steps.

1. The form is "if $P$ then $Q$; not $Q$; so not $P$", with $P$ the statement "$n$ is divisible by $4$" and $Q$ the statement "$n$ is even". Logic calls this form [[modus tollens|32AQPJQQAM]], short for the Latin *modus tollendo tollens*, "the mode that denies by denying", and teachers call it "denying the consequent".
2. The form is valid. Suppose that both premises hold and that $P$ holds too. Then $Q$ holds by the first premise, which contradicts the second, so $P$ fails.
3. A second reason: $P \Rightarrow Q$ is equivalent to its [[contrapositive|04T1CT7212]] $\neg Q \Rightarrow \neg P$, and the argument applies [[modus ponens|0Y0MQYST0M]] to the contrapositive.
4. The second premise denies $Q$, the consequent. The fallacy of denying the antecedent would deny $P$ instead, as in "$6$ is not divisible by $4$, so $6$ is not even".

Check the conclusion directly: $7 = 4 \cdot 1 + 3$, so $7$ is not divisible by $4$.

## Remarks

The position of the "not" decides validity.
Denying the consequent gives a valid argument, and denying the antecedent gives an invalid one.
Modus tollens is close to proof by contrapositive, but the two differ.
Proof by contrapositive proves the conditional $P \Rightarrow Q$ by proving $\neg Q \Rightarrow \neg P$.
Modus tollens uses a conditional that is already known, together with $\neg Q$, to derive $\neg P$.
Every [[counterexample|ZX6ERT3SW7]] refutation is modus tollens in disguise: "if the claim were true, this case would satisfy it; it does not; so the claim is false".

## Explanations

### L1 human

"If it is a dog, then it has four legs" is true.
A bird has two legs, so the bird cannot be a dog.
That argument is correct: if the bird were a dog, it would have four legs.
Saying no to the second half of an "if" sentence is allowed; saying no to the first half is the trap.

### L2 human

We use modus tollens to prove that $2$ is not the cube of a positive integer.
Let $P(x)$ be "$x$ is the cube of a positive integer", and let $Q(x)$ be "$x = 1$ or $x \ge 8$".
First premise: $P(x)$ implies $Q(x)$ for every $x$, because $m^3 = 1$ when $m = 1$, and $m^3 \ge 2^3 = 8$ when $m \ge 2$.
Second premise: $Q(2)$ is false, since $2 \neq 1$ and $2 < 8$.
By modus tollens, $P(2)$ is false.

The typical use of modus tollens is to rule out a candidate: find a property that every solution has and that the candidate lacks.
Watch out for swapping the roles of the premises, which turns modus tollens into denying the antecedent.
