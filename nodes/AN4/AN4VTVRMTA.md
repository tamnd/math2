---
tag: AN4VTVRMTA
kind: example
name: A variable in the scope of a quantifier on another variable is free
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: Y3FZTH5158
    fails: [5]
    note: the occurrence of x lies in the scope of a quantifier on y, and a bound occurrence needs a quantifier on x itself
uses: [9CNGDRAMGC, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Free_variables_and_bound_variables
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $<$ be a binary relation symbol, and let $\varphi = \forall y \, (x < y)$.
We show that the occurrence of $x$ in $\varphi$ is not bound, although it lies inside a quantifier.

1. The only quantifier in $\varphi$ is $\forall y$, and its scope is $x < y$.
2. The occurrence of $x$ lies in this scope.
3. By item 5 of the [[definition|Y3FZTH5158]], a bound occurrence of $x$ must lie in the scope of a quantifier $\forall x$ or $\exists x$.
   The quantifier $\forall y$ is not on $x$, and $\varphi$ has no other quantifier.
4. So the occurrence of $x$ is free.
5. The recursion agrees: $\operatorname{FV}(x < y) = \{ x, y \}$, and $\forall y$ removes $y$ only, so $\operatorname{FV}(\varphi) = \{ x \}$.

## Remarks

The occurrence of $y$ is bound by $\forall y$, so $\operatorname{BV}(\varphi) = \{ y \}$.
Since $x$ is free, $\varphi$ is not a [[sentence|DKFGQTRYZE]], and its truth depends on the value of $x$.
In $(\mathbb{Z}, <)$ it is false for every value of $x$, because $y = x$ fails $x < y$.
In the structure $(\{ 0, 1 \}, \le)$, where the symbol $<$ is read as $\le$, it is true exactly for $x = 0$.
If we put a quantifier in front, $\exists x \, \forall y \, (x < y)$ is a sentence, and now $x$ is bound.

The formula is also the start of the standard capture example.
Putting $y$ for the free $x$ gives $\forall y \, (y < y)$, and the new $y$ is bound by the old quantifier; the page on [[variable capture|WW01WZR9MF]] works this out.

## Explanations

### L1 human

The claim "every number $y$ is larger than $x$" is about one unknown number $x$.
The words "every number" cover only the letter $y$.
So the claim cannot be judged until we know $x$.
In the integers it is false for every $x$, because $y = x$ itself is not larger than $x$.

### L2 human

We test $\varphi$ in the structure $(\{ 0, 1 \}, \le)$, reading $<$ as $\le$.
For $x = 0$ we have $0 \le 0$ and $0 \le 1$, so $\forall y \, (x \le y)$ is true.
For $x = 1$ we have $1 \le 0$ false, so $\forall y \, (x \le y)$ is false.
The truth value changes with $x$, which confirms that $x$ is free.
This test is a quick way to show that a formula is not a sentence.
The converse fails, though: a free variable can have no effect on the truth value, as $x$ in $x = x$.
