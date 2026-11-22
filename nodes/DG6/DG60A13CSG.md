---
tag: DG60A13CSG
kind: example
name: The claim that n^2 + n + 41 is obviously prime for every n
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
not_instance_of:
  - target: Y0HXCJRB9B
    note: the claim is labeled obvious but it is false at n = 40, so the word does not mark a step that the reader can check
uses: [Y0HXCJRB9B, 01826KMG2H, 008BH74D7R, N2EY1EVPRB]
sources:
  - url: https://en.wikipedia.org/wiki/Formula_for_primes
    locator: Prime formulas and polynomial functions
---

## Example

Consider the [[polynomial|N2EY1EVPRB]] $p(n) = n^2 + n + 41$.
A student computes the first five values,
$$p(0) = 41, \quad p(1) = 43, \quad p(2) = 47, \quad p(3) = 53, \quad p(4) = 61,$$
and all five are [[prime numbers|01826KMG2H]].
The student then writes: "So $p(n)$ is `obviously` prime for every natural number $n$."
We show that this is not a correct use of the word "obvious" in the sense of [[trivial, obvious and clearly|Y0HXCJRB9B]].

1. "Obvious" claims that a short check from the definitions proves the statement.
   So the statement must at least be true.
2. Take $n = 40$ and factor out $40$ from the first two terms:
   $$p(40) = 40 \cdot 40 + 40 + 41 = 40 \cdot 41 + 41 = 41 \cdot 41 = 1681.$$
3. So $p(40) = 41^2$ is a [[composite number|008BH74D7R]], and it is not prime.
4. So the statement is false, and no check can prove it.

The values $p(0), p(1), \ldots, p(39)$ are all prime, so checking many cases does not find the error.
A correct sentence is: "$p(n)$ is prime for $n = 0, 1, \ldots, 39$, and $p(40) = 41^2$ is not prime."

## Remarks

"Obvious" is a claim about a proof, not about examples.
A pattern in many cases is evidence, and it is never a proof.
The next value fails too, by a direct factorization:
$$p(41) = 41^2 + 41 + 41 = 41 \cdot 43.$$
No polynomial in one variable with integer coefficients that is not constant takes only prime values at all natural numbers, so the search for such a formula was bound to fail.
Leonhard Euler noted in 1772 that $n^2 + n + 41$ is prime for the forty values $n = 0, 1, \ldots, 39$.

## Explanations

### L1 human

The rule "square the number, add the number, add $41$" gives prime numbers for $0$, $1$, $2$ and many more.
It gives primes for every number from $0$ to $39$.
At $40$ it gives $1681$, which is $41 \times 41$, so it is not prime.
Many good examples do not prove that a rule always works, and calling the rule obvious does not make it true.

### L2 human

Before you accept an "obvious" claim, look at the structure of the formula for a value that makes it factor.
Here $p(n) = n(n + 1) + 41$, so if $n$ or $n + 1$ is a multiple of $41$, then $41$ divides $p(n)$.
The first such values are $n = 40$ and $n = 41$:
$$p(40) = 40 \cdot 41 + 41 = 41 \cdot 41, \qquad p(41) = 41 \cdot 42 + 41 = 41 \cdot 43.$$
Both are larger than $41$ and divisible by $41$, so neither is prime.
This kind of search finds a counterexample in two lines, where a list of values would need forty-one tries.
Watch out: a long list of checked cases makes a claim feel obvious, but one counterexample is enough to refute it.
