---
tag: T850KJAMS5
kind: example
name: Detaching an inner conditional without its outer antecedent is not modus ponens
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0Y0MQYST0M
    note: from p implies (q implies r) and q the argument derives r, but q is not the antecedent of the premise, and the valuation p false, q true, r false is a countermodel
uses: [0Y0MQYST0M, 05RSK4Q657, FWHBT4HABW]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
---

## Example

"If $n$ is even, then: if $n$ is prime, then $n = 2$" is true, and $3$ is prime, but $3 \neq 2$.
Consider the argument form with premises $p \to (q \to r)$ and $q$, and conclusion $r$.
We check that this form is not an instance of [[modus ponens|0Y0MQYST0M]], and that it is invalid.

1. Modus ponens needs a premise $\varphi \to \psi$ and a second premise equal to its antecedent $\varphi$.
2. The main connective of $p \to (q \to r)$ is the first arrow, so its antecedent is $p$ and its consequent is $q \to r$.
3. The second premise is $q$, which is not the antecedent $p$, so the form is not modus ponens.
4. To show that the form is invalid, take the valuation with $p$ false, $q$ true and $r$ false.
5. In this valuation $p \to (q \to r)$ is true, because its antecedent $p$ is false.
6. The premise $q$ is true, and the conclusion $r$ is false.
7. So this valuation is a [[countermodel|FWHBT4HABW]], with both premises true and the conclusion false.

The opening sentence is an instance with $n = 3$: $p$ is "$3$ is even", which is false, $q$ is "$3$ is prime", which is true, and $r$ is "$3 = 2$", which is false.

## Remarks

### What the example shows

Modus ponens works on the main connective of a formula, not on an arrow inside it.
To reach $r$ we also need the premise $p$.
Modus ponens on $p$ and $p \to (q \to r)$ gives $q \to r$, and modus ponens on $q$ and $q \to r$ then gives $r$.
From $p \to (q \to r)$ and $p$ alone, modus ponens gives $q \to r$.

### Watch out

The [[intermediate value theorem|00KAFBR32E]] reads "if $f$ is continuous on $[a, b]$, then (if $f(a) < 0 < f(b)$, then $f$ has a zero in $(a, b)$)".
Let $g(x) = 1/x$ for $x \neq 0$ and $g(0) = 1$, on $[-1, 1]$.
Then $g(-1) = -1 < 0 < 1 = g(1)$, so the inner antecedent holds, but $g$ is not continuous at $0$.
The conclusion fails too, since $g$ has no zero.

### Try it

From $p \to (q \to r)$, $p$ and $q$, derive $r$, and count the uses of modus ponens.
Two uses: first $q \to r$ from $p$, then $r$ from $q$.

## Explanations

### L1 human

The rule "if a number is even, then: if it is prime, it equals $2$" is true.
The number $3$ is prime, but it is not even, so the rule says nothing about it.
Using only the inner part "if it is prime, it equals $2$" would give the false claim $3 = 2$.

### L2 human

A theorem with two hypotheses is often written as nested implications, as the intermediate value theorem is above.
To apply it, check the outer antecedent first and then the inner one.
The function $g$ passes the inner check and fails the outer one, so nothing follows about its zeros.
This check is the step "verify every hypothesis of the theorem" in a proof.
