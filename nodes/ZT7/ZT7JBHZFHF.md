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
In the [[jargon|4M1FGQ0HNZ]] of mathematicians, "$f$ vanishes at $2$ and at $-2$, and nowhere else" means "$f(x) = 0$ exactly when $x = 2$ or $x = -2$".
We check this exact form.

1. "Vanishes at $a$" means $f(a) = 0$, so $a$ is a zero of $f$, or a [[root|019MA1VTR2]] of the polynomial $x^2 - 4$.
2. At $x = 2$ and at $x = -2$, the square is $4$:
   $$f(2) = 4 - 4 = 0, \qquad f(-2) = 4 - 4 = 0.$$
3. Factor the polynomial as a difference of squares:
   $$x^2 - 4 = (x - 2)(x + 2).$$
4. A product of two real numbers is $0$ exactly when one factor is $0$.
   So $f(x) = 0$ exactly when $x - 2 = 0$ or $x + 2 = 0$, that is, when $x = 2$ or $x = -2$.
5. So $f$ vanishes at $2$ and at $-2$, and at no other point.
6. "Vanishes identically" would mean $f(x) = 0$ for every $x$.
   This fails, because $f(0) = -4 \neq 0$.

## Remarks

"Vanish" is jargon with an exact meaning: once the function is fixed, the claim can be checked line by line.
The related phrases are exact too.
"$f$ vanishes to first order at $2$" means $f(2) = 0$ and $f'(2) \neq 0$, and here $f'(x) = 2x$ gives $f'(2) = 4$.

Change the function and the answer changes.
The function $g(x) = (x - 2)^2$ vanishes only at $2$, and it vanishes to second order there, because $g(2) = g'(2) = 0$ and $g''(2) = 2 \neq 0$.
The function $h(x) = x^2 + 4$ vanishes nowhere on $\mathbb{R}$, because $x^2 + 4 \geq 4$ for every real $x$.

## Explanations

### L1 human

"Vanish" is how mathematicians say "becomes zero".
For the rule "square the number and subtract $4$", the input $2$ gives $4 - 4 = 0$, and the input $-2$ gives $4 - 4 = 0$ too.
Every other input gives a number that is not zero; for example, $3$ gives $9 - 4 = 5$.
So the function vanishes at exactly two points.

### L2 human

Find where $p(x) = x^3 - 4x$ vanishes.
Take out the common factor $x$, and then factor the difference of squares:
$$x^3 - 4x = x(x^2 - 4) = x(x - 2)(x + 2).$$
A product is zero exactly when one factor is zero, so $p$ vanishes at $0$, $2$ and $-2$.
Check: $p(2) = 8 - 8 = 0$ and $p(-2) = -8 + 8 = 0$.
The word is used most in statements such as "a polynomial of degree $n$ that does not vanish identically vanishes at most $n$ times".
Watch out: "$f$ does not vanish identically" is weaker than "$f$ vanishes nowhere".
The function $x^2 - 4$ satisfies the first and not the second.
