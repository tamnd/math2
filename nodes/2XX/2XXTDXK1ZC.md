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

Consider this argument with two premises and a conclusion.
Premise 1: if an integer $n$ is divisible by $4$, then $n$ is even.
Premise 2: the integer $6$ is even.
Conclusion: so $6$ is divisible by $4$.
We check whether the argument is a valid [[deduction|5V35SGEN1T]].

1. Premise 1 is true.
   If $n = 4k$, then $n = 2(2k)$, so $n$ is even.
2. Premise 2 is true, because $6 = 2 \cdot 3$.
3. The conclusion is false, because $6 = 4 \cdot 1 + 2$ leaves the remainder $2$.
4. A valid deduction never leads from true premises to a false conclusion.
   This argument does, by steps 1 to 3, so it is not valid.
5. The form of the argument is "if $P$ then $Q$; $Q$; so $P$".
   This form is called [[affirming the consequent|J7KFCFQRBT]].
6. The form silently uses the [[converse|09A3N7ZN5G]] "if $n$ is even, then $n$ is divisible by $4$".
   That converse is false, and $n = 6$ is a [[counterexample|0ED72CTBNP]] to it.

## Remarks

Validity depends on the form of an argument, not on whether its parts happen to be true.
Run the same form with $n = 8$: "$8$ is even, so $8$ is divisible by $4$".
The conclusion is true, but only by luck, and the form is just as invalid as before.
The valid form with the same premise is modus ponens, "if $P$ then $Q$; $P$; so $Q$", as in "$12$ is divisible by $4$, so $12$ is even".

The invalid form still has a use in discovery.
When an observed fact $Q$ would follow from a hypothesis $P$, then $P$ becomes a candidate explanation of $Q$.
That is abductive reasoning, and it gives a hypothesis to test, not a conclusion.

## Explanations

### L1 human

"If it rains, the street gets wet" is true.
"The street is wet" can also be true.
But it does not follow that it rained, because a water truck could have passed.
The same mistake with numbers: every multiple of $4$ is even, and $6$ is even, but $6$ is not a multiple of $4$.

### L2 human

Test four arguments that start from the premise "if $n$ is divisible by $4$, then $n$ is even".
Argument A: "$20$ is divisible by $4$, so $20$ is even."
This is modus ponens, and it is valid.
Argument B: "$10$ is even, so $10$ is divisible by $4$."
This affirms the consequent, and $10 = 4 \cdot 2 + 2$ refutes it.
Argument C: "$7$ is not even, so $7$ is not divisible by $4$."
This is modus tollens, "if $P$ then $Q$; not $Q$; so not $P$", and it is valid.
Argument D: "$10$ is not divisible by $4$, so $10$ is not even."
This denies the antecedent, and $10$ refutes it.
So two of the four forms are valid, and the two invalid ones both rely on the converse "if $Q$ then $P$" without a proof.
When you read a proof, ask of each step which of these forms it uses.
