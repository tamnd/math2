---
tag: ~bee5aa17
kind: statement
role: theorem
name: The algebraic numbers form a field
msc: [11R04]
uses: [~1de0949f, ~1fa33f36, ~c467433f, ~00a26465]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_number
    locator: Field
  - url: https://en.wikipedia.org/wiki/Algebraic_element
    locator: Properties
---

## Statement

Let $\overline{\mathbb{Q}}$ be the set of the complex numbers that are [[algebraic|~1de0949f]] over $\mathbb{Q}$.
Then $\overline{\mathbb{Q}}$ is a [[subfield|~00a26465]] of $\mathbb{C}$.

## Remarks

The proof: if $a, b$ are algebraic over $\mathbb{Q}$, then $\mathbb{Q}(a, b)$ is a finite extension of $\mathbb{Q}$, by the [[tower law|~1fa33f36]]. So $a + b$, $a - b$, $a b$ and $a/b$ for $b \neq 0$ are algebraic, because [[finite extensions are algebraic|~c467433f]].
More generally, for every extension $L/K$, the elements of $L$ that are algebraic over $K$ form a subfield of $L$.
The field $\overline{\mathbb{Q}}$ is countable and algebraically closed. It is an [[algebraic closure|~e0c69761]] of $\mathbb{Q}$.

## Explanations

### L1 human

The sum and the product of two algebraic numbers are algebraic.
For example, $\sqrt{2} + \sqrt{3}$ is a root of $x^4 - 10x^2 + 1$.
The proof does not need to find such a polynomial: it uses only dimensions of vector spaces.
