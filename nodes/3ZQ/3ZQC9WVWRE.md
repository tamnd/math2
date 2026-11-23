---
tag: 3ZQC9WVWRE
kind: example
name: The perfect squares form a Δ0-definable set
msc: ["03F30", "03D15"]
topics: [RA380RWEC0]
audience: research
instance_of: [FYGWNXETVJ]
uses: [FYGWNXETVJ, GE43CSZTS9, HCGCPW8ZFE]
sources:
  - url: https://en.wikipedia.org/wiki/Rudimentary_function
    locator: lead section
---

## Example

Is $45$ a perfect square?
Try the numbers $0, 1, \dots, 45$: the square of $6$ is $36$ and the square of $7$ is $49$, so no square equals $45$.
The search never passes $45$, and that bound is what makes the property $\Delta_0$.

In exact terms, let $\mathrm{Sq} = \{ 0, 1, 4, 9, 16, \dots \}$ be the set of [[perfect squares|HCGCPW8ZFE]].
Let $\theta(x)$ be the formula $\exists y < x + 1 \, (y \cdot y = x)$ of the language of arithmetic, where $x + 1$ abbreviates $x + S0$.
We check that $\theta$ is $\Delta_0$, that it defines $\mathrm{Sq}$, and that $\mathrm{Sq}$ lies in the [[linear-time hierarchy|FYGWNXETVJ]].

1. The only quantifier is $\exists y < x + 1$, and $y$ does not occur in the bound.
   The matrix $y \cdot y = x$ is atomic, so $\theta$ is a [[$\Delta_0$ formula|GE43CSZTS9]].
2. Let $n \in \mathrm{Sq}$, so $n = m^2$ for some $m$.
   If $m \ge 1$, then $m \le m^2 = n < n + 1$, and if $m = 0$, then $m < n + 1$.
   So the witness $m$ is inside the bound, and $\mathbb{N} \models \theta(n)$.
3. If $\mathbb{N} \models \theta(n)$, then some $m < n + 1$ satisfies $m \cdot m = n$, so $n \in \mathrm{Sq}$.
4. For $n = 45$, no value $m = 0, \dots, 45$ has $m^2 = 45$, since $6^2 = 36$ and $7^2 = 49$, and larger $m$ give larger squares.
   So $\mathbb{N} \models \neg \theta(45)$.
5. For $n = 49$, the value $m = 7 < 50$ gives $7 \cdot 7 = 49$, so $\mathbb{N} \models \theta(49)$.
6. By steps 1 to 3 and the equality of the $\Delta_0$ sets with $\mathrm{LinH}$, the set $\mathrm{Sq}$ is in $\mathrm{LinH}$, with $n$ written in binary.

## Remarks

The example shows the typical shape of a $\Delta_0$ definition: a bounded guess of a witness, then an atomic check.
A witness $y$ has at most about half the binary length of $x$, so the alternating machine guesses fewer bits than the input has.

What changes when the exponent changes?
For a fixed exponent $k$, the formula $\exists y < x + 1 \, (y^k = x)$, with $y^k$ written as a product of $k$ factors, still works.
For a variable exponent, as in the set $\{ (x, k) : x = y^k \text{ for some } y \}$, the set is still $\Delta_0$-definable, but the formula needs Bennett's $\Delta_0$ definition of the graph of exponentiation, because $y^k$ is no longer a term.

## Explanations

### L1 human

A perfect square is a number like $49 = 7 \cdot 7$.
To test whether a number is a square, it is enough to try all numbers up to it.
For $45$ we try $0, 1, 2, \dots$ and find that $6 \cdot 6 = 36$ is too small and $7 \cdot 7 = 49$ is too big.
So $45$ is not a square.
Because the search never goes past the number itself, the property is bounded.

### L2 human

We find the witness for $n = 144$ and count its bits.
In binary $144 = 10010000_2$, with $8$ digits, and the witness $12 = 1100_2$ has $4$ digits, half the length.
The check is one product:
$$12 \cdot 12 = 144.$$
So $\theta(144)$ is true, and a nondeterministic machine accepts by guessing the $4$ bits of $12$ and then verifying the product.

The typical use is as a first test of the correspondence: a natural set has a short $\Delta_0$ definition, so it is in $\mathrm{LinH}$.
Watch out: the machine does not try all $145$ values of $y$, which would take time exponential in the length; it guesses one value with few bits.
