---
tag: YMSC1Q4ST1
kind: example
name: Chaining two implications with the same consequent is not a hypothetical syllogism
msc: ["03B05", "11A05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 7MT8CPCEM4
    note: from p implies q and r implies q the argument derives p implies r, but the middle terms do not match, and the valuation p true, q true, r false is a countermodel
uses: [7MT8CPCEM4, 096PW7Q014, FWHBT4HABW]
sources:
  - url: https://en.wikipedia.org/wiki/Hypothetical_syllogism
    locator: lead section
---

## Example

"Dogs have four legs" and "cats have four legs" are both true, and they do not make dogs into cats.
Consider the argument form with premises $p \to q$ and $r \to q$, and conclusion $p \to r$.
We check that this form is not an instance of [[hypothetical syllogism|7MT8CPCEM4]], and that it is invalid.

1. Hypothetical syllogism needs premises $\varphi \to \psi$ and $\psi \to \chi$, where the consequent of the first is the antecedent of the second.
2. Here the consequent of the first premise is $q$, and the antecedent of the second premise is $r$.
   They differ, so the form is not hypothetical syllogism.
3. To show that the form is invalid, take the valuation with $p$ true, $q$ true and $r$ false.
4. In this valuation, $p \to q$ is true and $r \to q$ is true.
5. The conclusion $p \to r$ is false, because $p$ is true and $r$ is false.
6. So this valuation is a [[countermodel|FWHBT4HABW]].

Check with integers: "if $4 \mid n$, then $n$ is even" and "if $6 \mid n$, then $n$ is even" are both true, but "if $4 \mid n$, then $6 \mid n$" is false for $n = 4$.

## Remarks

### What the example shows

Two statements with a common consequence need not be related to each other.
The valid form with the same premises is different: from $p \to q$ and $r \to q$ we derive $(p \lor r) \to q$, by [[proof by cases|0WCP0PVET6]].
The argument becomes a hypothetical syllogism if the second premise is reversed to $q \to r$.
But "if $n$ is even, then $6 \mid n$" is false, so the conclusion is still not proved.

### Watch out

A broken chain can have a true conclusion by accident, so a true conclusion does not show that the chain is correct.
Underline the middle term in each link and confirm that it matches.

### Try it

Find the error: "every differentiable function is continuous, and every polynomial is continuous, so every differentiable function is a polynomial".
The form is $p \to q$, $r \to q$, therefore $p \to r$, and $\sin x$ refutes the conclusion, since it is differentiable and has infinitely many zeros without being the zero function.

## Explanations

### L1 human

"Dogs have four legs" and "cats have four legs" are both true.
They do not give "dogs are cats".
Two things that share a property are not the same thing.

### L2 human

A short wrong proof shows the pattern.
It claims that every differentiable function $f \colon \mathbb{R} \to \mathbb{R}$ is a polynomial, because every differentiable function is continuous and every polynomial is continuous.
Both premises are true theorems, and both end in "continuous", so the form is $p \to q$, $r \to q$, therefore $p \to r$.
The claim is false: $\sin x$ is differentiable on $\mathbb{R}$, and it is not a polynomial, because it has infinitely many zeros and is not the zero function.
