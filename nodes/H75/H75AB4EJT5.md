---
tag: H75AB4EJT5
kind: example
name: Forty prime values of n^2 + n + 41 do not prove a statement
msc: ["00A35", "11A41"]
topics: [N4P3E53HM0, T6QQ749DM5]
audience: school
instance_of: [5V35SGEN1T, ZX6ERT3SW7]
not_instance_of:
  - target: 0B94TKFQJX
    note: forty checked cases support the guess that n^2 + n + 41 is always prime, but they are not a proof, and the guess fails at n = 40
uses: [0SN0MAEKYX, 0ED72CTBNP, ZX6ERT3SW7]
sources:
  - url: https://en.wikipedia.org/wiki/Formula_for_primes
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Inductive_reasoning
    locator: lead section
---

## Example

Let $f(n) = n^2 + n + 41$ for each natural number $n$.
We test the guess "$f(n)$ is a [[prime number|0SN0MAEKYX]] for each natural number $n$".

1. We compute the first values: $f(0) = 41$, $f(1) = 43$, $f(2) = 47$, $f(3) = 53$, $f(4) = 61$ and $f(5) = 71$. Each of these numbers is prime.
2. We continue to $n = 39$. Each value $f(0), f(1), \ldots, f(39)$ is prime, and the last one is $f(39) = 1601$. A computer check of the forty values confirms this.
3. On this evidence, the guess "$f(n)$ is always prime" is a reasonable conjecture. This is inductive reasoning: we pass from many cases to a general claim.
4. We compute $f(40) = 1600 + 40 + 41 = 1681$.
5. We factor: $1681 = 41 \cdot 41$. So $f(40)$ is not prime, and $n = 40$ is a [[counterexample|0ED72CTBNP]] to the guess.
6. We can find this counterexample without a search: $f(40) = 40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41 \cdot 41$.
7. In the same way, $f(41) = 41^2 + 41 + 41 = 41 \cdot 43 = 1763$, so $f(41)$ is not prime either.

## Remarks

The example shows the gap between evidence and [[proof|0B94TKFQJX]].
Forty confirming cases gave strong support to the guess, and the guess is false.
To conclude the guess from the forty cases is the error of [[proof by example|ZX6ERT3SW7]].
Step 6 also shows how a proof-like idea finds the error: the value at $n = 41 - 1$ has the factor $41$ by algebra.

The same idea shows that no polynomial $g(n) = n^2 + n + c$ with an integer $c \geq 2$ gives only primes.
The value $g(c - 1) = (c - 1)^2 + (c - 1) + c = c^2$ is not prime.
Leonhard Euler studied the polynomial $n^2 + n + 41$, and the values that it takes are often used to warn against conclusions from cases.

## Explanations

### L1 human

Put $n = 0, 1, 2, 3$ into $n^2 + n + 41$ and we get $41$, $43$, $47$ and $53$, all prime numbers.
This goes on for forty values of $n$ in a row.
It is tempting to say that the formula always gives a prime number.
But for $n = 40$ the formula gives $1681$, and $1681 = 41 \times 41$.
So the pattern breaks, and forty good cases were not enough to be sure.

### L2 human

We find all $n$ from $0$ to $100$ for which $f(n) = n^2 + n + 41$ is divisible by $41$.

1. We reduce modulo $41$: $f(n) \equiv n^2 + n = n(n + 1) \pmod{41}$.
2. The number $41$ is prime, so $41$ divides $n(n + 1)$ exactly when $41$ divides $n$ or $41$ divides $n + 1$.
3. So $41$ divides $f(n)$ exactly when $n \equiv 0$ or $n \equiv 40 \pmod{41}$.
4. In the range $0$ to $100$ these values are $n = 0, 40, 41, 81, 82$.
5. For $n = 0$ we have $f(0) = 41$, which is prime. For the other four values, $f(n) > 41$ and $41$ divides $f(n)$, so $f(n)$ is not prime.

The typical use of such a check is to test a conjecture before we try to prove it.
A trap is to stop the search at a convenient bound, for example at $n = 30$, and to report the pattern as a fact.
Only a proof covers all $n$, and here no proof can exist, because the claim is false.
