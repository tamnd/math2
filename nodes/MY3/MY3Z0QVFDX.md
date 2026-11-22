---
tag: MY3Z0QVFDX
kind: example
name: Recursive definition of the factorial
msc: ["00A35", "05A10"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [B60DBNF77S]
uses: [B60DBNF77S, 0XWG0JGDFW, BQ1D7T0EGD, 0ASJVEFA9J, 0MWKJ44V5A]
sources:
  - url: https://en.wikipedia.org/wiki/Factorial
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Recursive_definition
    locator: Examples of recursive definitions
---

## Example

The [[factorial|0XWG0JGDFW]] is the function $n \mapsto n!$ on the [[natural numbers|0MWKJ44V5A]] given by two rules:
$$0! = 1, \qquad (n + 1)! = (n + 1) \cdot n! \quad \text{for each } n \ge 0.$$
This is a recursive definition, one of the [[kinds of definitions|B60DBNF77S]], and its obligation is to show that the two rules fix exactly one function.

1. The base case gives the value at $0$, namely $0! = 1$.
2. The recursive case gives the value at $n + 1$ from the value at $n$ alone.
   It never refers to a larger argument.
3. Existence.
   The [[principle of recursive definition|BQ1D7T0EGD]] gives a function $h \colon \mathbb{N} \to \mathbb{N}$ with $h(0) = 1$ and $h(n + 1) = (n + 1) h(n)$.
4. Uniqueness.
   Let $g$ be a function with $g(0) = 1$ and $g(n + 1) = (n + 1) g(n)$.
   We show $g(n) = h(n)$ for every $n$ by [[mathematical induction|0ASJVEFA9J]].
5. The base step is $g(0) = 1 = h(0)$.
6. For the induction step, suppose $g(n) = h(n)$.
   Then
   $$g(n + 1) = (n + 1) g(n) = (n + 1) h(n) = h(n + 1).$$
7. So $g = h$, and the symbol $n!$ has exactly one meaning.

The first values follow from the rules one step at a time:
$$1! = 1 \cdot 1 = 1, \quad 2! = 2 \cdot 1 = 2, \quad 3! = 3 \cdot 2 = 6, \quad 4! = 4 \cdot 6 = 24, \quad 5! = 5 \cdot 24 = 120.$$
Check: $5! = 1 \cdot 2 \cdot 3 \cdot 4 \cdot 5 = 120$.

## Remarks

The recursive definition agrees with the product $n! = 1 \cdot 2 \cdots n$ for $n \ge 1$.
Induction proves it, because the product also satisfies the recursive rule and gives $1$ at $n = 1$.

The base case is part of the definition and cannot be left out.
With $0! = c$ in place of $0! = 1$, the same rules give the function $n \mapsto c \cdot n!$, so each $c$ gives a different function.
The choice $c = 1$ is the one that makes $1! = 1 \cdot 0!$ equal $1$, and it matches the count of orderings of the empty set, which is one.

The same pattern defines powers, with $a^0 = 1$ and $a^{n + 1} = a \cdot a^n$, and sums, with an empty sum equal to $0$.

## Explanations

### L1 human

The factorial of a number is the product of all whole numbers from $1$ up to it.
We can compute it step by step.
The factorial of $0$ is $1$ by agreement.
Each next factorial is the next number times the previous factorial.
So the factorials are $1, 1, 2, 6, 24, 120$, and each one comes from the one before.

### L2 human

We prove from the recursive definition that $n! \ge 2^{n - 1}$ for every $n \ge 1$.

1. For $n = 1$ we have $1! = 1 = 2^0$.
2. Suppose that $n! \ge 2^{n - 1}$ for some $n \ge 1$.
3. By the recursive case, $(n + 1)! = (n + 1) \cdot n!$.
4. Since $n \ge 1$, we have $n + 1 \ge 2$.
5. By steps 2 and 4,
   $$(n + 1)! \ge 2 \cdot 2^{n - 1} = 2^n.$$
6. By induction, the inequality holds for every $n \ge 1$.

Check: $4! = 24 \ge 8 = 2^3$.
The induction step of the proof uses the recursive case, and that is the usual way to prove facts about a recursively defined function.
Watch out: the product $1 \cdot 2 \cdots n$ has no factors at $n = 0$, so the value $0! = 1$ comes from the base case or from the convention for an empty product, not from the product formula.
