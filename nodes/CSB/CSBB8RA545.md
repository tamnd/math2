---
tag: CSBB8RA545
kind: example
name: A set of formulas with a free variable is not a theory
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
not_instance_of:
  - target: 92SWXST1ZM
    note: the formula x · e = x has the free variable x, so it is not a sentence, and a theory consists of sentences only
uses: [92SWXST1ZM, FZRMYTQFRR, DKFGQTRYZE, 9CNGDRAMGC]
sources:
  - url: https://en.wikipedia.org/wiki/Theory_(mathematical_logic)
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 2
---

## Example

Let $\sigma = \{ \cdot, e, {}^{-1} \}$ be the signature of groups, and let $S = \{ x \cdot e = x \}$.
We check that $S$ is not a [[first-order theory|92SWXST1ZM]].

1. The formula $x \cdot e = x$ is atomic, and the variable $x$ occurs in it.
2. No quantifier occurs, so the occurrence of $x$ is [[free|9CNGDRAMGC]], and $\operatorname{FV}(x \cdot e = x) = \{ x \}$.
3. A [[sentence|DKFGQTRYZE]] is a formula with no free variables, so $x \cdot e = x$ is not a sentence.
4. A theory is a set of sentences, by the [[definition|FZRMYTQFRR]], so $S$ is not a theory.
5. The truth of $x \cdot e = x$ in a structure depends on the value of $x$.
   Take $\mathbb{Z}$ with $\cdot$ read as multiplication, $e$ read as $2$, and ${}^{-1}$ read as the identity map.
   Then $x \cdot e = x$ holds for $x = 0$, since $0 \cdot 2 = 0$, and fails for $x = 1$, since $1 \cdot 2 = 2$.

So $S$ has no truth value in a structure, and "model of $S$" has no meaning without a further convention.

## Remarks

The universal closure $\forall x \, (x \cdot e = x)$ is a sentence, and $\{ \forall x \, (x \cdot e = x) \}$ is a theory.

Mendelson allows formulas with free variables as proper axioms, and a model must satisfy them under every assignment.
Under this convention $S$ and its universal closure have the same models.

The existential closure $\exists x \, (x \cdot e = x)$ is a different sentence.
Every model of the universal closure is a model of it, but not conversely, so the choice of closure matters.

## Explanations

### L1 human

The rule $x \cdot e = x$ has the letter $x$ in it with no "for all" in front.
So it does not say whether it means one $x$ or every $x$.
A theory must consist of complete sentences, which are true or false without choosing a value for $x$.
Writing "for all $x$, $x \cdot e = x$" fixes this.

### L2 human

We compare the two closures in $\mathbb{Z}$ with $\cdot$ read as multiplication and ${}^{-1}$ read in any way.

1. With $e$ read as $1$, the universal closure $\forall x \, (x \cdot 1 = x)$ is true, since $1$ is the identity of multiplication.
2. With $e$ read as $0$, the universal closure $\forall x \, (x \cdot 0 = x)$ is false, since $1 \cdot 0 \neq 1$.
3. With $e$ read as $0$, the existential closure $\exists x \, (x \cdot 0 = x)$ is true, with $x = 0$.

The typical use of the closure is to turn a law written with free variables into an axiom.
Watch out: textbooks often write group laws with free variables, and the universal reading is then a convention, not part of the formula.
