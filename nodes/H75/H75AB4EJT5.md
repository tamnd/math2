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
We test the guess "$f(n)$ is a [[prime number|0SN0MAEKYX]] for every natural number $n$".

1. Compute the first values:
   $$f(0) = 41, \quad f(1) = 43, \quad f(2) = 47, \quad f(3) = 53, \quad f(4) = 61, \quad f(5) = 71.$$
   Each of these numbers is prime.
2. Continue to $n = 39$.
   Each of the forty values $f(0), f(1), \dots, f(39)$ is prime, and the last is $f(39) = 1521 + 39 + 41 = 1601$.
   A short computer run confirms the forty values.
3. On this evidence the guess is a reasonable conjecture.
   This is inductive reasoning in the everyday sense: we pass from many cases to a general claim.
4. Compute the next value:
   $$f(40) = 40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41 \cdot 41 = 1681.$$
   So $f(40)$ is not prime, and $n = 40$ is a [[counterexample|0ED72CTBNP]] to the guess.
5. The next value fails too:
   $$f(41) = 41^2 + 41 + 41 = 41 \cdot 43 = 1763.$$

Check: $41 \cdot 41 = 1600 + 80 + 1 = 1681$, and $41 \cdot 43 = 1763$.

## Remarks

Forty confirming cases gave strong support to the guess, and the guess is false.
To conclude the general claim from the cases is the error called [[proof by example|ZX6ERT3SW7]].
Step 4 also shows how algebra finds the failure without a search: at $n = 40$ every term has the factor $41$.

The same idea works for every polynomial $g(n) = n^2 + n + c$ with an integer $c \ge 2$.
At $n = c - 1$ we get
$$g(c - 1) = (c - 1)^2 + (c - 1) + c = c^2 - 2c + 1 + 2c - 1 = c^2,$$
which is not prime.
So no polynomial of this shape gives only primes.
The value $c = 41$ is the largest $c$ for which every value before $n = c - 1$ is prime.

Leonhard Euler studied the values of $n^2 + n + 41$, and they remain the standard warning against conclusions from cases.

## Explanations

### L1 human

Put $n = 0, 1, 2, 3$ into $n^2 + n + 41$ and you get $41$, $43$, $47$ and $53$, all prime numbers.
This goes on for forty values of $n$ in a row.
It is tempting to say that the formula always gives a prime.
But for $n = 40$ the formula gives $1681$, which is $41 \times 41$.
So the pattern breaks, and forty good cases were not enough to be sure.

### L2 human

Which $n$ from $0$ to $100$ make $f(n)$ divisible by $41$?
Reduce modulo $41$, where the constant term disappears:
$$f(n) \equiv n^2 + n = n(n + 1) \pmod{41}.$$
The number $41$ is prime, so it divides $n(n + 1)$ exactly when it divides $n$ or $n + 1$.
So $41$ divides $f(n)$ exactly when $n \equiv 0$ or $n \equiv 40 \pmod{41}$, which in the range gives $n = 0, 40, 41, 81, 82$.
For $n = 0$ the value is $41$ itself, which is prime.
For the other four values $f(n)$ is larger than $41$ and divisible by $41$, so it is not prime.
A short argument of this kind finds the failures that a search would only stumble on, and it is the usual first test of a conjecture before anyone tries to prove it.
