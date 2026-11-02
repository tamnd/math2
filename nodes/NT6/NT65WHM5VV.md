---
tag: NT65WHM5VV
kind: example
name: Tetration
msc: [26A18, 39B12]
illustrates: [AYVTR2ES5B]
uses: [091AV9YHZY, AYVTR2ES5B, 68SHB7Z721, 5M3THA1S6E]
sources:
  - url: https://en.wikipedia.org/wiki/Tetration
same_as:
  wikidata: Q194324
  wikipedia: Tetration
---

## Example

Let $a > 0$ and let $\exp_a(x) = a^x$ be [[real exponentiation|091AV9YHZY]] to base $a$.
For integers $n \ge 1$, the *tetration* ${}^{n}a$ is defined by
$${}^{1}a = a, \qquad {}^{n+1}a = a^{\left({}^{n}a\right)}.$$
So ${}^{n}a$ is a tower of $n$ copies of $a$, evaluated from the top down.
With ${}^{0}a = 1$, one has ${}^{n}a = \exp_a^{\,n}(1)$, the $n$-th [[iterate|AYVTR2ES5B]] of $\exp_a$ applied to $1$.

Check for $a = 2$: ${}^{1}2 = 2$, ${}^{2}2 = 2^2 = 4$, ${}^{3}2 = 2^4 = 16$ and ${}^{4}2 = 2^{16} = 65536$.
And $\exp_2(1) = 2$, $\exp_2(2) = 4$, $\exp_2(4) = 16$, $\exp_2(16) = 65536$, as claimed.

## Remarks

Tetration is the next operation after addition, multiplication and exponentiation: repeated exponentiation, as exponentiation is repeated multiplication.
It grows very fast: ${}^{5}2 = 2^{65536}$ has $19729$ decimal digits.
Defining ${}^{x}a$ for real heights $x$ is a problem of [[fractional iteration|5M3THA1S6E]] of $\exp_a$.
One asks for a function $F$ with $F(0) = 1$ and $F(x + 1) = a^{F(x)}$; its inverse is a solution of the [[Abel equation|68SHB7Z721]] for $\exp_a$.
These conditions alone do not determine $F$, so one adds regularity conditions such as real analyticity.
The infinite tower $a^{a^{a^{\cdots}}}$ is the limit of ${}^{n}a$ as $n \to \infty$; see [[iterated exponentiation|RDC61V812J]].

## Explanations

### L1 human

Multiplication repeats addition, and powers repeat multiplication.
Tetration repeats powers: ${}^{3}2$ means $2^{2^2} = 16$.
The values explode: ${}^{4}2 = 65536$, and ${}^{5}2$ is a number with almost twenty thousand digits.
Each step applies the map $x \mapsto 2^x$ once more, so tetration is a picture of iterating a function.
