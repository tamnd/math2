---
tag: 3DJDNG0ZC9
kind: example
name: Modus ponens applied to a divisibility theorem
msc: ["03B05", "11A05"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0Y0MQYST0M]
uses: [0Y0MQYST0M, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
---

## Example

Consider the argument with two premises and a conclusion.

- Premise 1: for every integer $n$, if $6$ [[divides|096PW7Q014]] $n$, then $3$ divides $n$.
- Premise 2: $6$ divides $312$.
- Conclusion: $3$ divides $312$.

We check that the argument is an instance of [[modus ponens|0Y0MQYST0M]], and that its premises are true.

1. Premise 1 is true. If $n = 6k$ for an integer $k$, then $n = 3(2k)$.
2. Premise 1 with $n = 312$ gives the implication $\varphi \to \psi$, where $\varphi$ is "$6 \mid 312$" and $\psi$ is "$3 \mid 312$". Reason: a universal statement holds for each element of its domain.
3. Premise 2 is the antecedent $\varphi$. It is true, because $312 = 6 \cdot 52$.
4. The premises $\varphi$ and $\varphi \to \psi$ give $\psi$ by modus ponens. So $3 \mid 312$.
5. A direct check of the conclusion: $312 = 3 \cdot 104$.

## Remarks

The example shows the usual shape of modus ponens in mathematics: a universal theorem, an instance of it, and a check of the antecedent.
If we replace premise 2 by "$6$ does not divide $314$", modus ponens does not apply, and the conclusion "$3$ does not divide $314$" would be [[denying the antecedent|J7KFCFQRBT]].
If we replace premise 2 by "$3$ divides $315$", modus ponens does not apply either, and indeed $6 \nmid 315$ because $315$ is odd.

## Explanations

### L1 human

We know a rule: every number that splits into $6$ equal whole parts also splits into $3$ equal whole parts.
We know a fact: $312$ splits into $6$ parts of $52$.
So $312$ splits into $3$ equal whole parts, and indeed it splits into $3$ parts of $104$.

### L2 human

We use the same pattern with a different theorem to show that $2^{10} - 1$ is divisible by $3$.

1. Premise: for every natural number $k$, if $k$ is even, then $3$ divides $2^k - 1$. Reason: $2^k - 1 = 4^{k/2} - 1$, and $4 \equiv 1 \pmod 3$ gives $4^{k/2} \equiv 1 \pmod 3$.
2. Instance: if $10$ is even, then $3$ divides $2^{10} - 1$.
3. Antecedent: $10 = 2 \cdot 5$ is even.
4. Modus ponens: $3$ divides $2^{10} - 1 = 1023$, and indeed $1023 = 3 \cdot 341$.

The typical use is in step 3: the work of the proof is to check the antecedent.
A trap is to apply the premise to an odd exponent: $2^5 - 1 = 31$ is not divisible by $3$, and the premise says nothing about it.
