---
tag: ZT7JBHZFHF
kind: example
name: The function x^2 - 4 vanishes at 2 and at -2
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [4M1FGQ0HNZ]
uses: [4M1FGQ0HNZ, 019MA1VTR2, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Zero_of_a_function
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
---

## Example

Let $f \colon \mathbb{R} \to \mathbb{R}$ be the function $f(x) = x^2 - 4$ on the [[real numbers|08J2M1JYAG]].
The [[jargon|4M1FGQ0HNZ]] sentence "$f$ vanishes at $2$ and at $-2$, and nowhere else" means "$f(x) = 0$ exactly when $x = 2$ or $x = -2$".
We check it.

1. "Vanishes at $a$" means $f(a) = 0$, that is, $a$ is a zero of $f$, or a [[root|019MA1VTR2]] of the polynomial $x^2 - 4$.
2. At $x = 2$: $f(2) = 4 - 4 = 0$.
3. At $x = -2$: $f(-2) = 4 - 4 = 0$.
4. We factor: $x^2 - 4 = (x - 2)(x + 2)$.
5. A product of two real numbers is $0$ exactly when one of the factors is $0$. So $f(x) = 0$ exactly when $x - 2 = 0$ or $x + 2 = 0$, that is, when $x = 2$ or $x = -2$.
6. So $f$ vanishes at $2$ and at $-2$, and at no other point.
7. "Vanishes identically" would mean $f(x) = 0$ for every $x$. This fails, because $f(0) = -4 \neq 0$.

## Remarks

The example shows that "vanish" is jargon with an exact meaning: once the function is fixed, the claim can be checked.
Related phrases have exact meanings too.
"$f$ vanishes to first order at $2$" means $f(2) = 0$ and $f'(2) \neq 0$; here $f'(2) = 4$.
If we change the function to $g(x) = (x - 2)^2$, then $g$ vanishes only at $2$, and it vanishes to second order there, because $g(2) = g'(2) = 0$ and $g''(2) = 2 \neq 0$.
If we change it to $h(x) = x^2 + 4$, then $h$ vanishes nowhere on $\mathbb{R}$, because $x^2 + 4 \geq 4$.

## Explanations

### L1 human

"Vanish" is how mathematicians say "becomes zero".
For the rule "square the number and subtract $4$", the input $2$ gives $4 - 4 = 0$, and the input $-2$ gives $4 - 4 = 0$ too.
Every other input gives a number that is not zero, for example $3$ gives $5$.
So the function vanishes at exactly two points.

### L2 human

We find where $p(x) = x^3 - 4x$ vanishes.

1. Factor out $x$: $p(x) = x(x^2 - 4)$.
2. Factor again: $p(x) = x(x - 2)(x + 2)$.
3. A product is $0$ exactly when one factor is $0$, so $p$ vanishes at $0$, $2$ and $-2$.

The typical use of "vanish" is in statements such as "a polynomial of degree $n$ that does not vanish identically vanishes at most $n$ times".
A trap: "$f$ does not vanish identically" is weaker than "$f$ vanishes nowhere"; the function $x^2 - 4$ satisfies the first but not the second.
