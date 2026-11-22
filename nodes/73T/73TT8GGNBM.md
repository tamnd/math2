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

Here is the definition.
Let $a$ and $b$ be [[integers|0C4JS9RF5M]].
We say that $a$ *divides* $b$, and we write $a \mid b$, if there is an integer $k$ with $b = ak$.
This defines the relation of [[divisibility|0PG2H7WKGG]].
We check the parts of the [[mathematical definition|8ZCZ3HW91Z]] and then decide five cases.

1. The definiendum is the relation "$a$ divides $b$", with the new symbol $a \mid b$.
2. The definiens is "there is an integer $k$ with $b = ak$".
   It uses only integers, multiplication and "there is", so it is not circular.
3. The relation $3 \mid 12$ holds, because $12 = 3 \cdot 4$.
4. The relation $3 \mid 7$ fails.
   For $k \le 2$ we get $3k \le 6$, and for $k \ge 3$ we get $3k \ge 9$, so $3k \neq 7$.
5. For every integer $a$, the relation $a \mid 0$ holds, because $0 = a \cdot 0$.
6. In particular $0 \mid 0$ holds, with $k = 0$ or with any other integer $k$.
7. If $b \neq 0$, then $0 \mid b$ fails, because $0 \cdot k = 0 \neq b$ for every integer $k$.

## Remarks

Step 6 surprises many readers, because "$0/0$" has no value.
The two expressions are of different types.
The expression $a \mid b$ is a statement, true or false, while $b / a$ is a number.
The definition asks only that some $k$ exists, not that it is unique, so $0 \mid 0$ is true even though no single quotient $0/0$ exists.
Some books add the condition $a \neq 0$, and in those books "$0 \mid b$" is not defined, so check the convention before you quote a statement about $0$.

The domain of $k$ carries the meaning, as it does for [[even integers|BV6E0ZG3YN]].
If $k$ could be rational, every nonzero $a$ would divide every $b$, because $b = a \cdot \tfrac{b}{a}$.

The first properties come straight from unfolding.
If $a \mid b$ and $b \mid c$, then $b = ak$ and $c = bl$ for integers $k$ and $l$, so
$$c = (ak) l = a (kl),$$
and $a \mid c$.
Check: $2 \mid 6$ and $6 \mid 18$ give $18 = 2 \cdot 9$ with $kl = 3 \cdot 3 = 9$.

## Explanations

### L1 human

The number $3$ divides $12$ because $12$ is $3$ groups of $4$.
The number $3$ does not divide $7$, because $3$ groups of $2$ give $6$ and $3$ groups of $3$ give $9$.
The definition only asks whether the second number is a whole number of copies of the first.
For the second number $0$ the answer is always yes, since $0$ copies of anything give $0$.

### L2 human

We prove from the definition that if $a \mid b$ and $a \mid c$, then $a \mid b + c$.

1. By the definition there is an integer $k$ with $b = ak$.
2. By the definition again there is an integer $l$ with $c = al$.
   We use a new letter, because $c$ may need another multiplier.
3. By the distributive law,
   $$b + c = ak + al = a(k + l).$$
4. The number $k + l$ is an integer, so $a \mid b + c$ by the definition.

Check: $4 \mid 12$ and $4 \mid 20$, and $32 = 4 \cdot 8$ with $k + l = 3 + 5$.
Each hypothesis "$a \mid b$" gives one integer and one equation, and the conclusion needs one integer and one equation, which is the usual shape of a divisibility proof.
Watch out: do not write $b/a$ in such a proof, because for $a = 0$ the fraction has no meaning while the definition still works.
