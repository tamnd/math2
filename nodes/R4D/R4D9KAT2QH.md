---
tag: R4D9KAT2QH
kind: example
name: In "2 and 3 are coprime", the word "and" is not a connective
msc: ["97E40"]
topics: [WMY13MXY3W]
audience: school
not_instance_of:
  - target: 12QQ51VK01
    note: the word "and" joins two numbers in one relation, not two statements
uses: [12QQ51VK01, 0VZ48N083F]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_conjunction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Coprime_integers
    locator: lead section
---

## Example

Two integers $a$ and $b$ are [[coprime|0VZ48N083F]] when their only common positive divisor is $1$.
Consider the statement $S$: "$2$ and $3$ are coprime".
We show that the word "and" in $S$ is not a [[connective|12QQ51VK01]], which joins two statements.

1. A connective "and" would split $S$ into two statements: "$2$ is coprime" and "$3$ is coprime".
2. "Coprime" is a relation between two integers. The phrase "$2$ is coprime" names only one integer, so it is not a statement.
3. So $S$ does not split in this way. The word "and" joins the two numbers $2$ and $3$ into the pair to which the relation applies.
4. The statement $S$ is true: the positive divisors of $2$ are $1, 2$, and those of $3$ are $1, 3$, so the only common positive divisor is $1$.

## Remarks

The example shows that the same English word can be a connective in one sentence and not in another.
In "$2$ and $3$ are prime", the word "and" is a connective: the sentence means "$2$ is prime and $3$ is prime".
The test is to split the sentence into two sentences and to check that each part is a statement with the same meaning.

The same problem appears with three numbers.
"$6$, $10$ and $15$ are coprime" usually means that the three numbers have no common divisor greater than $1$, which is true.
It can also mean that each two of them are coprime, which is false, because $\gcd(6, 10) = 2$.
Careful authors write "pairwise coprime" for the second meaning.

## Explanations

### L1 human

"Anna and Ben are tall" means "Anna is tall and Ben is tall".
"Anna and Ben are cousins" does not mean "Anna is a cousin and Ben is a cousin".
It says something about the two people together.
In the same way, "$2$ and $3$ are coprime" says something about the pair, not about each number.

### L2 human

We sort four sentences with the word "and".

1. "$4$ and $9$ are perfect squares." This splits into "$4$ is a perfect square" and "$9$ is a perfect square", so "and" is a connective. Both parts are true.
2. "$4$ and $9$ are coprime." This does not split, because "coprime" needs two numbers. The statement is true, because $\gcd(4, 9) = 1$.
3. "The lines $y = x$ and $y = -x$ are perpendicular." This does not split, because "perpendicular" needs two lines.
4. "The lines $y = x$ and $y = -x$ pass through the origin." This splits, so "and" is a connective.

The typical use is in negation.
The negation of sentence 1 is "$4$ is not a perfect square or $9$ is not a perfect square", but the negation of sentence 2 is simply "$4$ and $9$ are not coprime".

A trap: a student who splits sentence 2 gets the meaningless "$4$ is not coprime or $9$ is not coprime".
