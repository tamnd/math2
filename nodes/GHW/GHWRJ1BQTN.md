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

The conjecture $A$: "if $p$ is prime, then the [[Mersenne number|0YAG43TCXQ]] $2^p - 1$ is prime".
We test $A$ by one of its consequences and show that the reasoning is a deduction.

1. The consequence $B$: "$2^{11} - 1$ is prime". It follows from $A$, because $11$ is prime.
2. We compute $2^{11} - 1 = 2048 - 1 = 2047$.
3. We test small divisors. $2047 = 23 \cdot 89$, and $23 \cdot 89 = 2070 - 23 = 2047$. So $2047$ is not prime, and $B$ is false.
4. "$A$ implies $B$" and "$B$ is false" give "$A$ is false" by modus tollens, a rule of deduction.
5. The conclusion is certain. It does not depend on how many other primes $p$ were checked, so it is not a change of confidence.

So the argument is not [[plausible reasoning|8DHD3H1CJ9]]: it lacks the condition that the conclusion is only "more credible" or "less credible".

## Remarks

The earlier consequences $2^2 - 1 = 3$, $2^3 - 1 = 7$, $2^5 - 1 = 31$ and $2^7 - 1 = 127$ are all prime.
Each of them made $A$ more credible by the fundamental inductive pattern, and that was plausible reasoning.
The single false consequence of step 3 outweighs them, because it turns the question into a deduction.
The number $p = 11$ is a [[counterexample|0ED72CTBNP]] to $A$.

The converse statement, "if $2^n - 1$ is prime, then $n$ is prime", is true, and it has a proof by factoring $2^{ab} - 1$.
Pólya's pattern "$A$ implies $B$, $B$ false, so $A$ false" is in his list as the demonstrative pattern, next to the plausible patterns.

## Explanations

### L1 human

The guess was: "two to the power of a prime, minus one, is always prime".
It works for $2$, $3$, $5$ and $7$.
For $11$ we get $2047$, and $2047 = 23 \times 89$.
One failure is enough to kill the guess, and no further checks can save it.
This is not a matter of belief any more; it is certain.

### L2 human

We compare the two kinds of reasoning on the same conjecture.

1. Plausible: $2^7 - 1 = 127$ is prime, and this is a consequence of $A$. So $A$ is more credible, and nothing is proved.
2. Demonstrative: $2^{11} - 1 = 2047 = 23 \cdot 89$ is not prime, and this contradicts a consequence of $A$. So $A$ is false.

The typical use: before a long attempt to prove a conjecture, test consequences that are easy to compute, because one failure saves the work.
A trap: a refutation needs a consequence that really follows from $A$; checking $2^9 - 1 = 511 = 7 \cdot 73$ refutes nothing, because $9$ is not prime.
