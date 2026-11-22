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
We show that the word "and" in $S$ is not a [[connective|12QQ51VK01]], because it does not join two statements.

1. A connective "and" would split $S$ into two statements, "$2$ is coprime" and "$3$ is coprime".
2. "Coprime" is a relation between two integers.
   The phrase "$2$ is coprime" names only one integer, so it is not a statement at all.
3. So $S$ does not split.
   The word "and" joins the numbers $2$ and $3$ into the pair to which the relation applies.
4. The statement $S$ itself is true.
   The positive divisors of $2$ are $1$ and $2$, those of $3$ are $1$ and $3$, and the only common one is $1$.

## Remarks

The test is to split the sentence into two sentences and to check that each part is a statement with the intended meaning.
In "$2$ and $3$ are prime" the test succeeds: the sentence means "$2$ is prime and $3$ is prime".
In "$2$ and $3$ are coprime" it fails, so there "and" builds a pair, not a compound statement.

With three numbers a second problem appears.
"$6$, $10$ and $15$ are coprime" usually means that the three numbers have no common divisor greater than $1$, and that is true.
It can also mean that each two of them are coprime, and that is false, because $\gcd(6, 10) = 2$.
Careful authors write "pairwise coprime" for the second meaning.

## Explanations

### L1 human

"Anna and Ben are tall" means "Anna is tall and Ben is tall".
"Anna and Ben are cousins" does not mean "Anna is a cousin and Ben is a cousin".
It says something about the two people together.
In the same way, "$2$ and $3$ are coprime" says something about the pair, not about each number.

### L2 human

Sort four sentences that contain "and".
"$4$ and $9$ are perfect squares" splits into "$4$ is a perfect square" and "$9$ is a perfect square", so "and" is a connective, and both parts are true.
"$4$ and $9$ are coprime" does not split, because "coprime" needs two numbers; it is true, since $\gcd(4, 9) = 1$.
"The lines $y = x$ and $y = -x$ are perpendicular" does not split, because "perpendicular" needs two lines.
"The lines $y = x$ and $y = -x$ pass through the origin" splits, so "and" is a connective.

The difference matters when you negate.
The negation of the first sentence is "$4$ is not a perfect square or $9$ is not a perfect square".
The negation of the second is simply "$4$ and $9$ are not coprime".
Watch out: splitting the second sentence gives the meaningless "$4$ is not coprime or $9$ is not coprime".
