---
tag: 2XMSKQ7YHG
kind: example
name: One example proves an existential statement
msc: ["00A35", "97E50"]
topics: [T6QQ749DM5]
audience: school
not_instance_of:
  - target: ZX6ERT3SW7
    note: the claim is existential, and one example with a full check is a complete proof of it
uses: [ZX6ERT3SW7, ACSC75R7R5, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_example
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Constructive_proof
    locator: lead section
---

## Example

The claim is: there are positive integers $a$, $b$, $c$ with $a^2 + b^2 = c^2$.
We prove it by one example.

1. Take $a = 3$, $b = 4$ and $c = 5$. All three are positive integers.
2. Compute: $a^2 + b^2 = 9 + 16 = 25$.
3. Compute: $c^2 = 25$.
4. So $a^2 + b^2 = c^2$, and the claim holds.

We check that this is not an instance of [[proof by example|ZX6ERT3SW7]] in the sense of an error.

1. The claim is an [[existential statement|ACSC75R7R5]]: "there are $a$, $b$, $c$ with a property".
2. An existential statement is true exactly when at least one object has the property.
3. Steps 1 to 4 show that one object has the property, with each condition checked.
4. So the example is a complete proof, not a generalization from cases.

## Remarks

The example shows that the same text, one checked case, is a proof of an existential statement and only evidence for a universal statement.
If the claim is changed to "for all positive integers $a$ and $b$ there is a positive integer $c$ with $a^2 + b^2 = c^2$", the case $3, 4, 5$ proves nothing, and $a = b = 1$ refutes the claim, because $2$ is not a square.
In the same way, one [[counterexample|0ED72CTBNP]] is a complete proof that a universal statement is false, since it proves the existential statement "there is an $x$ for which $P(x)$ fails".

## Explanations

### L1 human

"Some numbers are both even and greater than $10$" is proved by the single number $12$.
We do not need more numbers, because the claim says only that at least one such number exists.
But "every number greater than $10$ is even" is not proved by $12$, and $13$ shows that it is false.
So one example is enough for "some" and never enough for "every".

### L2 human

We prove that there is an integer $n > 1$ such that $n$ divides $2^n - 2$ and $n$ is not prime.

1. Take $n = 341 = 11 \cdot 31$. It is not prime.
2. We show $2^{341} \equiv 2 \pmod{11}$. Since $2^{10} = 1024 = 93 \cdot 11 + 1$, we have $2^{10} \equiv 1 \pmod{11}$, and $2^{341} = (2^{10})^{34} \cdot 2 \equiv 2 \pmod{11}$.
3. We show $2^{341} \equiv 2 \pmod{31}$. Since $2^5 = 32 \equiv 1 \pmod{31}$, we have $2^{341} = (2^5)^{68} \cdot 2 \equiv 2 \pmod{31}$.
4. The numbers $11$ and $31$ are coprime and both divide $2^{341} - 2$, so $341$ divides $2^{341} - 2$.
5. So $n = 341$ proves the claim.

The typical use of a single example is to prove that a converse fails: here, "if $n$ divides $2^n - 2$, then $n$ is prime" is false.
A trap is to give an example without checking each condition, which is then neither a proof nor a counterexample.
