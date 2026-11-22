---
tag: 55FJH3WXE9
kind: example
name: Reduction from Z/6Z to Z/3Z is well defined
msc: ["00A35", "11A07"]
topics: [BP0WAF23HB]
audience: ug1
instance_of: [HNGZEBKVY2]
uses: [HNGZEBKVY2, 03VFZ2WETT, 0PG2H7WKGG]
sources:
  - url: https://en.wikipedia.org/wiki/Well-defined_expression
    locator: Functions with one argument
---

## Example

Write $[a]_6$ for the class of $a$ in $\mathbb{Z}/6\mathbb{Z}$ and $[a]_3$ for its class in $\mathbb{Z}/3\mathbb{Z}$, the [[integers modulo $n$|03VFZ2WETT]] for $n = 6$ and $n = 3$.
The proposed map is
$$r \colon \mathbb{Z}/6\mathbb{Z} \to \mathbb{Z}/3\mathbb{Z}, \qquad r([a]_6) := [a]_3.$$
We show that $r$ is [[well defined|HNGZEBKVY2]].

1. The rule uses a representative $a$ of the class $[a]_6$, so we must show that every representative gives the same value.
2. Let $[a]_6 = [a']_6$.
   Then $6 \mid a' - a$, so $a' - a = 6k$ for an integer $k$, by the definition of [[divisibility|0PG2H7WKGG]].
3. Then $a' - a = 3 \cdot (2k)$, and $2k$ is an integer, so $3 \mid a' - a$.
4. So $[a']_3 = [a]_3$, and the value of $r$ does not depend on the representative.

The six values of $r$ are
$$[0]_6, [3]_6 \mapsto [0]_3, \qquad [1]_6, [4]_6 \mapsto [1]_3, \qquad [2]_6, [5]_6 \mapsto [2]_3.$$
Check: $[4]_6 = [10]_6$, and both representatives give $[4]_3 = [10]_3 = [1]_3$.

## Remarks

The proof used only that $3$ divides $6$, so the same proof shows that $[a]_n \mapsto [a]_m$ is well defined whenever $m \mid n$.
The condition is also necessary.
Since $[0]_n = [n]_n$, a well-defined rule must give $[0]_m = [n]_m$, and that says $m \mid n$.
So the reverse rule $[a]_3 \mapsto [a]_6$ is not well defined, because $[0]_3 = [3]_3$ but $[0]_6 \neq [3]_6$.

The map $r$ respects both operations, since $r([a]_6 + [b]_6) = [a + b]_3 = [a]_3 + [b]_3$ and in the same way for products.
So $r$ is a ring homomorphism.
It is surjective, and exactly two classes modulo $6$ go to each class modulo $3$.

## Explanations

### L1 human

The numbers that leave remainder $4$ when divided by $6$ are $4$, $10$, $16$, and so on.
All these numbers leave remainder $1$ when divided by $3$.
The reason is that $6$ is a multiple of $3$, so a step of $6$ never changes the remainder by $3$.
So "the remainder by $3$" depends only on "the remainder by $6$", and the rule gives one answer.

### L2 human

We test the reverse rule $s([a]_3) := [a]_6$ and find where it fails.
The class $[1]_3$ is $\{ \ldots, -2, 1, 4, 7, \ldots \}$.
The representative $1$ gives $s([1]_3) = [1]_6$, and the representative $4$ gives $s([1]_3) = [4]_6$.
Since $6 \nmid 4 - 1$, these classes differ, so $s$ gives two values for one input and is not a function.
The forward map $r$ is what makes reduction of congruences work: a solution of a congruence modulo $6$ gives a solution modulo $3$.
Watch out: the converse fails, since a solution modulo $3$ does not single out one solution modulo $6$, because each class modulo $3$ splits into two classes modulo $6$.
