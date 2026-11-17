---
tag: P4NCHC44NJ
kind: example
name: The definition of a function uses the uniqueness quantifier
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0QAJHFGZZJ]
uses: [0QAJHFGZZJ, 0N3ADS4CHH, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Function_(mathematics)
    locator: lead section
---

## Example

Let $X$ and $Y$ be sets, and let $f \subseteq X \times Y$ be a relation.
The relation $f$ is a [[function|0EPAT51DXQ]] from $X$ to $Y$ when
$$\forall x \in X \; \exists! y \in Y \; (x, y) \in f.$$
We check this condition for $X = Y = \{1, 2, 3\}$ and $f = \{(1, 2), (2, 2), (3, 1)\}$, with the definition of the [[uniqueness quantifier|0N3ADS4CHH]].

1. For $x = 1$, the only pair of $f$ with first entry $1$ is $(1, 2)$. So $y = 2$ exists, and every $y'$ with $(1, y') \in f$ equals $2$.
2. For $x = 2$, the only pair with first entry $2$ is $(2, 2)$. So the unique $y$ is $2$.
3. For $x = 3$, the only pair with first entry $3$ is $(3, 1)$. So the unique $y$ is $1$.
4. Steps 1 to 3 cover every $x \in X$, so the condition holds and $f$ is a function. Its values are $f(1) = 2$, $f(2) = 2$ and $f(3) = 1$.

## Remarks

The definition of a function contains two conditions in one formula.
The existence part says that each $x$ has a value, and the uniqueness part says that the value is well defined.
The relation $g = \{(1, 2), (1, 3), (2, 2), (3, 1)\}$ is not a function, because $x = 1$ has the two partners $2$ and $3$, so uniqueness fails.
The relation $h = \{(1, 2), (2, 2)\}$ is not a function on $X$, because $x = 3$ has no partner, so existence fails.
The notation $f(x)$ for "the $y$ with $(x, y) \in f$" is allowed exactly because of the $\exists!$ in the definition.
The formula does not require uniqueness of $x$ for a given $y$: in $f$, both $1$ and $2$ go to $2$.
Uniqueness in that direction is the definition of an [[injective function|09NWETVTNY]].

## Explanations

### L1 human

A function is like a machine that gives exactly one output for each input.
Each input must give some output, and it must not give two different outputs.
Think of a list of people and their birthdays.
Each person has a birthday, and no person has two birthdays, so "the birthday of a person" makes sense.
Two people can share a birthday, and that is allowed.

### L2 human

To check that a rule is a function, we check the two parts of $\exists!$ for each input.

1. Take $f(x) = \sqrt{x}$ on $X = \{x \in \mathbb{R} : x \geq 0\}$, with the relation "$y \geq 0$ and $y^2 = x$".
2. Existence: for $x \geq 0$, the number $y = \sqrt{x}$ satisfies $y \geq 0$ and $y^2 = x$.
3. Uniqueness: if $y, y' \geq 0$ and $y^2 = y'^2 = x$, then $(y - y')(y + y') = 0$. If $y + y' = 0$, then $y = y' = 0$, because both are non-negative. Otherwise $y - y' = 0$. In both cases $y = y'$.
4. So the relation is a function.

A trap is the relation "$y^2 = x$" without the condition $y \geq 0$: for $x = 4$ both $y = 2$ and $y = -2$ satisfy it, so it is not a function.
