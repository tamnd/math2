---
tag: 73TT8GGNBM
kind: example
name: Definition of divisibility of integers
msc: ["00A35", "11A05"]
topics: [BP0WAF23HB]
audience: school
instance_of: [8ZCZ3HW91Z]
uses: [8ZCZ3HW91Z, 0PG2H7WKGG, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor
    locator: lead section
---

## Example

The definition reads as follows.
Let $a$ and $b$ be [[integers|0C4JS9RF5M]].
We say that $a$ *divides* $b$, and we write $a \mid b$, if there is an integer $k$ with $b = ak$.
This defines the relation of [[divisibility|0PG2H7WKGG]].
We check the parts of the [[mathematical definition|8ZCZ3HW91Z]] and then decide five cases.

1. The definiendum is the relation "$a$ divides $b$", with the new symbol $a \mid b$.
2. The definiens is "there is an integer $k$ with $b = ak$". It uses only integers, multiplication and "there is", so it is not circular.
3. The relation $3 \mid 12$ holds, because $12 = 3 \cdot 4$.
4. The relation $3 \mid 7$ fails. For $k \leq 2$ we get $3k \leq 6$, and for $k \geq 3$ we get $3k \geq 9$, so $3k \neq 7$.
5. For each integer $a$, the relation $a \mid 0$ holds, because $0 = a \cdot 0$.
6. In particular $0 \mid 0$ holds, with $k = 0$ (or with any other integer $k$).
7. If $b \neq 0$, then $0 \mid b$ fails, because $0 \cdot k = 0 \neq b$ for each integer $k$.

## Remarks

1. The expression $a \mid b$ is a statement, which is true or false. The expression $b / a$ is a number. So "$0 \mid 0$" is true, while "$0 / 0$" has no value.
2. Step 6 surprises many readers. The definition asks only for the existence of $k$, and it does not ask for $k$ to be unique. That is why $0 \mid 0$ holds although "$0/0$" is not defined.
3. Some books add the condition $a \neq 0$ to the definition. In those books, "$0 \mid b$" is not defined, and statements must be read with this convention in mind.
4. If $k$ may range over the rational numbers, then each nonzero $a$ divides each $b$, because $b = a \cdot (b/a)$. So the domain of $k$ carries the meaning, as for [[even integers|BV6E0ZG3YN]].
5. The definition gives the first properties by unfolding. For example, if $a \mid b$ and $b \mid c$, then $b = ak$ and $c = bl$, so $c = a(kl)$ and $a \mid c$.

## Explanations

### L1 human

The number $3$ divides $12$ because $12$ is $3$ groups of $4$.
The number $3$ does not divide $7$, because $3$ groups of $2$ give $6$ and $3$ groups of $3$ give $9$.
The definition only asks: is the second number a whole number of copies of the first?
For the second number $0$, the answer is always yes: $0$ copies of anything give $0$.

### L2 human

We prove from the definition: if $a \mid b$ and $a \mid c$, then $a \mid b + c$.

1. By the definition, there is an integer $k$ with $b = ak$.
2. By the definition again, there is an integer $l$ with $c = al$. We use a new letter, because $c$ may need another multiplier.
3. Then $b + c = ak + al = a(k + l)$ by the distributive law.
4. The number $k + l$ is an integer.
5. So $a \mid b + c$ by the definition.

The typical use: each hypothesis "$a \mid b$" gives an integer and an equation, and the conclusion needs one integer and one equation.
A trap is to write $b/a$ in the proof: when $a = 0$, the fraction has no meaning, but the definition still works.
