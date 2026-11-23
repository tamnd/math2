---
tag: GHWRJ1BQTN
kind: example
name: Refuting a conjecture by a false consequence
msc: ["00A35", "11A41"]
topics: [DME0TPC348]
audience: ug1
not_instance_of:
  - target: 8DHD3H1CJ9
    note: a false consequence refutes the conjecture with certainty, so the reasoning is demonstrative, not plausible
uses: [8DHD3H1CJ9, 0ED72CTBNP, 0YAG43TCXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mersenne_prime
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Plausible_reasoning
    locator: "Volume II: Patterns of Plausible Inference"
---

## Example

Take the conjecture $A$: "if $p$ is prime, then the [[Mersenne number|0YAG43TCXQ]] $2^p - 1$ is prime".
The first four primes support it:
$$2^2 - 1 = 3, \quad 2^3 - 1 = 7, \quad 2^5 - 1 = 31, \quad 2^7 - 1 = 127,$$
and all four values are prime.
We now test $A$ by one more consequence and show that this test is a deduction, not a change of confidence.

1. The consequence $B$ is "$2^{11} - 1$ is prime".
   It follows from $A$, because $11$ is prime.
2. We compute $2^{11} - 1 = 2048 - 1 = 2047$.
3. Trial division by small primes finds a factor:
   $$2047 = 23 \cdot 89, \qquad 23 \cdot 89 = 23 \cdot 90 - 23 = 2070 - 23 = 2047.$$
   So $2047$ is not prime, and $B$ is false.
4. "$A$ implies $B$" and "$B$ is false" give "$A$ is false" by modus tollens, a rule of deduction.
5. The conclusion is certain, whatever the number of primes $p$ that were checked before.

So the argument is not [[plausible reasoning|8DHD3H1CJ9]]: it fails the condition that the conclusion is only "more credible" or "less credible".
The number $p = 11$ is a [[counterexample|0ED72CTBNP]] to $A$.

## Remarks

### Two kinds of reasoning on one conjecture

The four prime values $3, 7, 31, 127$ each made $A$ more credible by Pólya's fundamental inductive pattern, and that was plausible reasoning.
The one false consequence at $p = 11$ outweighs them, because it turns the question into a deduction.
Pólya listed the pattern "$A$ implies $B$, $B$ false, so $A$ false" as the demonstrative pattern, next to the plausible ones.
A pattern that holds in many cases is not a proof, and here four cases ended in a refutation at the fifth.

### The converse

The converse statement, "if $2^n - 1$ is prime, then $n$ is prime", is true.
If $n = ab$ with $1 < a < n$, then
$$2^{ab} - 1 = (2^a - 1)\bigl(2^{a(b-1)} + 2^{a(b-2)} + \cdots + 1\bigr),$$
and the first factor lies strictly between $1$ and $2^n - 1$.

### Watch out

A refutation needs a consequence that really follows from $A$.
Checking $2^9 - 1 = 511 = 7 \cdot 73$ refutes nothing, because $9$ is not prime and $A$ says nothing about it.

### Try it

Show that $2^{23} - 1$ is not prime, given that $47$ divides it.
Since $23$ is prime, this is a second false consequence of $A$; indeed $2^{23} - 1 = 8388607 = 47 \cdot 178481$.

## Explanations

### L1 human

The guess was: "two to the power of a prime, minus one, is always prime".
It works for $2$, $3$, $5$ and $7$.
For $11$ we get $2047$, and $2047 = 23 \times 89$.
One failure is enough to end the guess, and no further checks can save it.
This is no longer a matter of belief; it is certain.

### L2 human

We compare the two kinds of reasoning on the same conjecture.
The plausible step is "$2^7 - 1 = 127$ is prime, and this is a consequence of $A$, so $A$ is more credible", and nothing is proved.
The demonstrative step is "$2^{11} - 1 = 2047 = 23 \cdot 89$ is not prime, and this contradicts a consequence of $A$, so $A$ is false".
The typical use: before a long attempt to prove a conjecture, test consequences that are easy to compute, because one failure saves the work.
