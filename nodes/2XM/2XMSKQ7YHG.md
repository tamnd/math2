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

Here is a proof made of a single example; is it a real proof or the error called [[proof by example|ZX6ERT3SW7]]?

> Claim: there are positive integers $a$, $b$, $c$ with $a^2 + b^2 = c^2$.
> Proof: take $a = 3$, $b = 4$, $c = 5$, and then $a^2 + b^2 = 9 + 16 = 25 = c^2$.

It is a real proof, and a complete one.
The reason is the shape of the claim.

1. The claim is an [[existential statement|ACSC75R7R5]]: "there are $a$, $b$, $c$ with a property".
2. An existential statement is true exactly when at least one object has the property.
3. The proof names one object and checks every condition: $3$, $4$, $5$ are positive integers, and the equation holds.
4. So nothing is generalized, and no case is left unchecked.

Change the claim and the same text stops being a proof.
"For all positive integers $a$ and $b$ there is a positive integer $c$ with $a^2 + b^2 = c^2$" is universal in $a$ and $b$.
The triple $3, 4, 5$ is then only one case, and $a = b = 1$ refutes the claim, because $2$ is not a perfect square.

## Remarks

The same words, one checked case, prove an existential statement and are only evidence for a universal one.
So before judging an example, write the claim with its quantifiers.
One [[counterexample|0ED72CTBNP]] is a complete proof for the same reason.
It proves the existential statement "there is an $x$ for which $P(x)$ fails", which is the negation of "$P(x)$ for every $x$".

## Explanations

### L1 human

"Some numbers are even and greater than $10$" is proved by the single number $12$.
We need no more numbers, because the claim only says that at least one such number exists.
"Every number greater than $10$ is even" is not proved by $12$, and $13$ shows that it is false.
One example is enough for "some" and never enough for "every".

### L2 human

We prove that some integer $n > 1$ divides $2^n - 2$ and is not prime.
Take $n = 341 = 11 \cdot 31$, which is not prime.
Since $2^{10} = 1024 = 93 \cdot 11 + 1$, we have $2^{10} \equiv 1 \pmod{11}$, so $2^{341} = (2^{10})^{34} \cdot 2 \equiv 2 \pmod{11}$.
Since $2^5 = 32 \equiv 1 \pmod{31}$, we have $2^{341} = (2^5)^{68} \cdot 2 \equiv 2 \pmod{31}$.
The coprime numbers $11$ and $31$ both divide $2^{341} - 2$, so $341$ divides it, and the claim is proved.

The typical use of a single example is to show that a converse fails; here it refutes "if $n$ divides $2^n - 2$, then $n$ is prime".
Watch out for an example whose conditions are not all checked, which is then neither a proof nor a counterexample.
