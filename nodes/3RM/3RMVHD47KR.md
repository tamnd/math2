---
tag: 3RMVHD47KR
kind: example
name: The binary predicate "x divides y" on the set {1, 2, 3, 4}
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
instance_of: [0QHEWQD30B]
uses: [0QHEWQD30B, 0T3DPBG981, 096PW7Q014, 05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Predicate_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Binary_relation
    locator: lead section
---

## Example

Let $D = \{1, 2, 3, 4\}$ and let $R(x, y)$ be the open sentence "$x$ [[divides|096PW7Q014]] $y$", that is, "there is an integer $k$ with $y = kx$".
We check that $R$ is a binary [[predicate|0T3DPBG981]] on $D$ and we find its truth set.

1. The free variables are $x$ and $y$; the variable $k$ is bound by "there is". Both $x$ and $y$ range over $D$.
2. For each pair $(a, b) \in D^2$, the sentence "$a$ divides $b$" is true or false, so $R(a, b)$ is a proposition.
3. Row $a = 1$: $1$ divides every integer, so $R(1, 1)$, $R(1, 2)$, $R(1, 3)$ and $R(1, 4)$ are true.
4. Row $a = 2$: $2 = 1 \cdot 2$ and $4 = 2 \cdot 2$, so $R(2, 2)$ and $R(2, 4)$ are true; $1$ and $3$ are odd, so $R(2, 1)$ and $R(2, 3)$ are false.
5. Row $a = 3$: among $1, 2, 3, 4$ only $3$ is a multiple of $3$, so only $R(3, 3)$ is true.
6. Row $a = 4$: among $1, 2, 3, 4$ only $4$ is a multiple of $4$, so only $R(4, 4)$ is true.
7. So the truth set is $T_R = \{(1, 1), (1, 2), (1, 3), (1, 4), (2, 2), (2, 4), (3, 3), (4, 4)\}$, with $8$ of the $16$ pairs.

## Remarks

The example shows that the truth set of a binary predicate is a [[binary relation|05AVARPXA2]] on $D$, a subset of $D \times D$.
The order of the variables matters: $R(1, 2)$ is true and $R(2, 1)$ is false.
Fixing a variable gives a unary predicate: $R(2, y)$ is "$y$ is even", with the truth set $\{2, 4\}$, and $R(x, 4)$ is "$x$ divides $4$", with the truth set $\{1, 2, 4\}$.
Quantifiers can bind one variable and leave the other free: $\forall y \in D \; R(x, y)$ is a unary predicate in $x$ with the truth set $\{1\}$.

## Explanations

### L1 human

The sentence "___ divides ___" has two blanks.
We fill them with two numbers from $1$ to $4$, the first one first.
"$2$ divides $4$" is true, and "$4$ divides $2$" is false, so the order matters.
Of the $16$ ways to fill the two blanks, exactly $8$ give a true sentence.

### L2 human

We find the truth set of $S(x, y)$: "$x < y$ and $x$ divides $y$" on the same $D$.

1. $S$ is true only for pairs in $T_R$, the truth set of "$x$ divides $y$".
2. Remove the pairs with $x \ge y$: these are $(1, 1)$, $(2, 2)$, $(3, 3)$ and $(4, 4)$.
3. So $T_S = \{(1, 2), (1, 3), (1, 4), (2, 4)\}$.

The typical use of this table method is to compute a relation on a small set before a general proof.
A trap is to list the pair $(4, 2)$ because "$2$ and $4$ are related": the predicate is not symmetric, and its truth set is a set of ordered pairs.
