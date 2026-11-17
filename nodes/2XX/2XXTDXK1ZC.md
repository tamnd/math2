---
tag: 2XXTDXK1ZC
kind: example
name: Affirming the consequent is not a valid deduction
msc: ["00A35"]
topics: [N4P3E53HM0, T6QQ749DM5]
audience: school
instance_of: [J7KFCFQRBT]
not_instance_of:
  - target: 5V35SGEN1T
    note: the argument claims a certain conclusion, but its form is not valid, so it is not a deduction; it gives at most a hypothesis to test
uses: [5V35SGEN1T, 09A3N7ZN5G, 0ED72CTBNP, J7KFCFQRBT]
sources:
  - url: https://en.wikipedia.org/wiki/Affirming_the_consequent
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Deductive_reasoning
    locator: lead section
---

## Example

Consider the argument with two premises and a conclusion:

- Premise 1: if an integer $n$ is divisible by $4$, then $n$ is even.
- Premise 2: the integer $6$ is even.
- Conclusion: so $6$ is divisible by $4$.

We check whether this argument is a valid [[deduction|5V35SGEN1T]].

1. Premise 1 is true. If $n = 4k$, then $n = 2(2k)$, so $n$ is even.
2. Premise 2 is true, because $6 = 2 \cdot 3$.
3. The conclusion is false, because $6 = 4 \cdot 1 + 2$ leaves the remainder $2$.
4. A valid deduction never leads from true premises to a false conclusion. By steps 1 to 3, this argument does, so it is not valid.
5. The form of the argument is "if $P$ then $Q$; $Q$; so $P$", which [[affirms the consequent|J7KFCFQRBT]]. The same form with $n = 8$ gives a true conclusion, but only by chance.
6. The form uses the [[converse|09A3N7ZN5G]] "if $Q$ then $P$" without a proof. This converse is false here, and $n = 6$ is a [[counterexample|0ED72CTBNP]] to it.

## Remarks

The example shows that a valid deduction depends on the form of the argument, not only on the truth of its parts.
The valid form with the same premise 1 is modus ponens: "if $P$ then $Q$; $P$; so $Q$".
For example, "$12$ is divisible by $4$, so $12$ is even" is valid.

The invalid form has a use in discovery.
When an observed fact $Q$ would follow from a hypothesis $P$, then $P$ becomes a candidate explanation of $Q$.
This is abductive reasoning, and it gives a hypothesis to test, not a conclusion.

## Explanations

### L1 human

"If it rains, the street gets wet" is true.
"The street is wet" can also be true.
But it does not follow that it rained, because a water truck could have passed.
The same mistake in numbers: every multiple of $4$ is even, and $6$ is even, but $6$ is not a multiple of $4$.

### L2 human

We test two arguments with the premise "if $n$ is divisible by $4$, then $n$ is even".

1. Argument A: "$20$ is divisible by $4$, so $20$ is even". This is modus ponens, and it is valid.
2. Argument B: "$10$ is even, so $10$ is divisible by $4$". This affirms the consequent, and $10 = 4 \cdot 2 + 2$ refutes it.
3. Argument C: "$10$ is not even, so $10$ is not divisible by $4$". The premise "$10$ is not even" is false, so the argument says nothing about $10$, although its form (modus tollens) is valid.

The typical use of this check is to read each step of a proof and to ask which rule of inference it uses.
A trap is to accept an argument because its conclusion is true, as in the case $n = 8$.
