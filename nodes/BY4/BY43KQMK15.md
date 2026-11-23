---
tag: BY43KQMK15
kind: example
name: The primes form a Δ0-definable set
msc: ["03F30", "03D15"]
topics: [RA380RWEC0]
audience: research
instance_of: [FYGWNXETVJ]
uses: [FYGWNXETVJ, GE43CSZTS9, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Rudimentary_function
    locator: lead section
---

## Example

The number $15$ is not prime, because $15 = 3 \cdot 5$ with both factors below $15$.
The number $7$ is prime, because no product of two numbers below $7$ equals $7$.
That test only looks at numbers below the input, so primality is a bounded property.

In exact terms, let $\mathrm{Pr}$ be the set of [[prime numbers|01826KMG2H]], and let $\pi(x)$ be the following formula:
$$S0 < x \land \forall u < x \, \forall v < x \, \neg (u \cdot v = x).$$
We check that $\pi$ is $\Delta_0$ and defines $\mathrm{Pr}$ in $\mathbb{N}$, so that $\mathrm{Pr}$ lies in the [[linear-time hierarchy|FYGWNXETVJ]].

1. The quantifiers $\forall u < x$ and $\forall v < x$ are bounded by $x$, which contains neither $u$ nor $v$.
   The rest is a Boolean combination of atomic formulas, so $\pi$ is a [[$\Delta_0$ formula|GE43CSZTS9]].
2. Let $p$ be prime, so $1 < p$.
   Suppose $u \cdot v = p$ with $u, v < p$.
   Since $p$ is prime, $u = 1$ or $v = 1$, so the other factor is $p$, which contradicts $u, v < p$.
   So $\mathbb{N} \models \pi(p)$.
3. If $n \le 1$, the first conjunct fails, so $\mathbb{N} \models \neg \pi(n)$.
4. If $n > 1$ is not prime, then $n = a \cdot b$ with $1 < a < n$ and $1 < b < n$.
   The pair $u = a$, $v = b$ refutes the second conjunct, so $\mathbb{N} \models \neg \pi(n)$.
5. Check with numbers.
   For $n = 15$, the pair $u = 3$, $v = 5$ is below $15$ and $3 \cdot 5 = 15$, so $\pi(15)$ is false.
   For $n = 7$, the only factorizations are $1 \cdot 7$ and $7 \cdot 1$, and each uses the factor $7$, which is not below $7$, so $\pi(7)$ is true.
6. By steps 1 to 4 and the equality of the $\Delta_0$ sets with $\mathrm{LinH}$, the set $\mathrm{Pr}$ is in $\mathrm{LinH}$.

## Remarks

The formula has two bounded universal quantifiers, so the alternating machine guesses $u$ and $v$ in universal states and rejects if some product hits $x$.
The complement, the composite numbers together with $0$ and $1$, has the dual definition, and its machine makes existential guesses instead.
Watch out: the final check $u \cdot v = x$ is not known to run in deterministic linear time, so the count of quantifiers in the formula does not give the exact level of $\mathrm{LinH}$.

The bound matters.
Watch out: if you write $u \le x$ and $v \le x$ instead of $u < x$ and $v < x$, the pair $u = 1$, $v = x$ gives $u \cdot v = x$, and no number satisfies the formula.

That primality is in polynomial time is a much deeper result, the [[AKS primality test|XMHQCDWZW1]].
The $\Delta_0$ definition only gives membership in $\mathrm{LinH}$, and it says nothing about what a weak theory can prove about primes.
Paris, Wilkie and Woods showed that $\mathsf{I}\Delta_0 + \Omega_1$ proves that there are infinitely many primes.

## Explanations

### L1 human

A prime number, like $7$, cannot be written as a product of two smaller numbers.
The number $15$ is not prime, since $15 = 3 \cdot 5$.
To test a number, it is enough to look at products of numbers smaller than it.
The search never goes past the number itself, so being prime is a bounded property.

### L2 human

We evaluate $\pi(9)$ step by step.
The first conjunct holds, since $1 < 9$.
For the second conjunct, the pairs $(u, v)$ with $u, v < 9$ include $(3, 3)$, and that pair gives the product below:
$$3 \cdot 3 = 9.$$
So the second conjunct fails, $\pi(9)$ is false, and $9$ is not prime.

The typical use of such a formula is to state facts of number theory inside $\mathsf{I}\Delta_0$, for example "there is a prime between $x$ and $2x$".
Stating a fact is not proving it: the formula makes the statement expressible, and the strength of the theory decides whether it is provable.
