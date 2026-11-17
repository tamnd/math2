---
tag: X49VTBJ08Z
kind: example
name: Upstairs and downstairs in the Gaussian integers
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug2
instance_of: [4M1FGQ0HNZ]
uses: [4M1FGQ0HNZ, 0K5W69AC0J, 0RVRNR7KA1, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_integer
    locator: Gaussian primes
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
---

## Example

Let $\mathbb{Z}[i] = \{a + bi : a, b \in \mathbb{Z}\}$ be the ring of [[Gaussian integers|0K5W69AC0J]], with $i^2 = -1$.
It contains the ring $\mathbb{Z}$ of integers.
In the [[jargon|4M1FGQ0HNZ]] of number theory, $\mathbb{Z}[i]$ is "upstairs" and $\mathbb{Z}$ is "downstairs".
The sentence "the prime $5$ splits upstairs, but $3$ stays prime upstairs" has an exact meaning, and we check it.

1. The norm of $a + bi$ is $N(a + bi) = a^2 + b^2$. It is multiplicative: $N(\alpha\beta) = N(\alpha) N(\beta)$, because $\lvert \alpha\beta \rvert^2 = \lvert \alpha \rvert^2 \lvert \beta \rvert^2$ for complex numbers.
2. The units of $\mathbb{Z}[i]$ are the elements of norm $1$: they are $1, -1, i, -i$. If $\alpha\beta = 1$, then $N(\alpha)N(\beta) = 1$ with both norms positive integers, so $N(\alpha) = 1$; and $a^2 + b^2 = 1$ has only the solutions $(\pm 1, 0)$ and $(0, \pm 1)$.
3. "$5$ splits upstairs" means that $5$ is a product of two non-units of $\mathbb{Z}[i]$. We compute $(2 + i)(2 - i) = 4 - i^2 = 4 + 1 = 5$. Both factors have norm $4 + 1 = 5 \neq 1$, so neither is a unit.
4. "$3$ stays prime upstairs" means that $3$ is a [[Gaussian prime|0RVRNR7KA1]]. Suppose $3 = \alpha\beta$ with $\alpha, \beta$ non-units. Then $N(\alpha) N(\beta) = N(3) = 9$ with $N(\alpha) \neq 1$ and $N(\beta) \neq 1$, so $N(\alpha) = 3$.
5. But $a^2 + b^2 = 3$ has no integer solutions: if $\lvert a \rvert \geq 2$ or $\lvert b \rvert \geq 2$, then $a^2 + b^2 \geq 4$, and otherwise $a^2 + b^2 \in \{0, 1, 2\}$.
6. So no factorization into non-units exists. Since $\mathbb{Z}[i]$ has unique factorization, an element with no factorization into non-units is prime, so $3$ is a Gaussian prime.

So $5$, a [[prime number|01826KMG2H]] downstairs, is a product of two primes upstairs, and $3$, also prime downstairs, stays prime upstairs.

## Remarks

The example shows that "upstairs" and "downstairs" are jargon for the larger and the smaller ring of an extension $\mathbb{Z} \subseteq \mathbb{Z}[i]$.
The words let a speaker say where an element lives without naming the rings each time.
The behaviour of a prime $p$ upstairs depends on $p$: an odd prime $p$ splits exactly when $p$ is a sum of two squares, which by [[Fermat's theorem on sums of two squares|043B3ENSTY]] happens exactly when $p \equiv 1 \pmod 4$.
The prime $2$ is a third case: $2 = -i(1 + i)^2$, so $2$ is a unit times the square of a Gaussian prime.
The same words are used for a covering space over its base, and for the numerator ("upstairs") and the denominator ("downstairs") of a fraction.

## Explanations

### L1 human

Think of the ordinary whole numbers as the ground floor, and of a larger number system that contains them as the floor above.
Mathematicians call the larger system "upstairs" and the smaller one "downstairs".
The number $5$ cannot be split into smaller whole-number factors downstairs.
Upstairs, with the new number $i$ whose square is $-1$, it splits: $(2 + i)(2 - i) = 5$.
The number $3$ cannot be split even upstairs.

### L2 human

We check that $13$ splits upstairs.

1. We look for $a^2 + b^2 = 13$ with integers $a, b$. We find $2^2 + 3^2 = 4 + 9 = 13$.
2. So $(3 + 2i)(3 - 2i) = 9 - 4i^2 = 9 + 4 = 13$.
3. Each factor has norm $13 \neq 1$, so neither is a unit, and $13$ splits upstairs.

The typical use of "upstairs" and "downstairs" is to compare a problem in a larger ring with the same problem in a smaller ring.
A trap: a prime downstairs need not be prime upstairs, and a unit upstairs, such as $i$, need not exist downstairs.
