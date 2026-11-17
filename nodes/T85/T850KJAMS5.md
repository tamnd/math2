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

Consider the argument form with premises $p \to (q \to r)$ and $q$, and conclusion $r$.
We check that this form is not an instance of [[modus ponens|0Y0MQYST0M]], and that it is invalid.

1. Modus ponens needs a premise $\varphi \to \psi$ and a second premise equal to its antecedent $\varphi$.
2. The main connective of $p \to (q \to r)$ is the first arrow, so its antecedent is $p$ and its consequent is $q \to r$.
3. The second premise is $q$, which is not the antecedent $p$. So the form is not modus ponens.
4. The form is invalid. Take the valuation with $p$ false, $q$ true and $r$ false.
5. In this valuation, $p \to (q \to r)$ is true, because its antecedent $p$ is false.
6. The premise $q$ is true, and the conclusion $r$ is false.
7. So the valuation of steps 4 to 6 is a [[countermodel|FWHBT4HABW]]: both premises are true and the conclusion is false.

A mathematical instance: for an integer $n$, the premise "if $n$ is even, then (if $n$ is prime, then $n = 2$)" is true, and for $n = 3$ the premise "$n$ is prime" is true, but $3 \neq 2$.

## Remarks

The example shows that modus ponens works on the main connective of a formula, not on an arrow inside it.
To reach $r$, we also need the premise $p$: modus ponens on $p$ and $p \to (q \to r)$ gives $q \to r$, and modus ponens on $q$ and $q \to r$ gives $r$.
The form becomes valid if we swap the roles: from $p \to (q \to r)$ and $p$ we derive $q \to r$, which is modus ponens.

## Explanations

### L1 human

The rule "if a number is even, then: if it is prime, it equals $2$" is true.
The number $3$ is prime, but it is not even, so the rule says nothing about it.
Using only the inner part "if it is prime, it equals $2$" would give the false claim $3 = 2$.

### L2 human

We read a theorem with two hypotheses written as nested implications.

1. "If $f$ is continuous on $[a, b]$, then (if $f(a) < 0 < f(b)$, then $f$ has a zero in $(a, b)$)." This is the [[intermediate value theorem|00KAFBR32E]].
2. Let $g(x) = 1/x$ for $x \neq 0$ and $g(0) = 1$, on $[-1, 1]$. Then $g(-1) = -1 < 0 < 1 = g(1)$, so the inner antecedent holds.
3. We cannot detach "$g$ has a zero in $(-1, 1)$" from the inner implication, because the outer antecedent fails: $g$ is not continuous at $0$.
4. Indeed the conclusion fails: $1/x \neq 0$ for $x \neq 0$, and $g(0) = 1$, so $g$ has no zero.

The typical use of this check is the step "verify every hypothesis of the theorem" in a proof.
A trap is to see the inner implication, check its antecedent, and forget the outer one.
