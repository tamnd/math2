---
tag: CER1EHMKW6
kind: example
name: The inclusive or in "n is even or n is a multiple of 3"
msc: ["97E40"]
topics: [WMY13MXY3W]
audience: school
instance_of: [12QQ51VK01]
uses: [12QQ51VK01, 0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_disjunction
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
---

## Example

For an integer $n$, let $D(n)$ be the statement "$n$ is even or $n$ is a multiple of $3$".
In mathematics "or" is inclusive, as [[connectives in mathematical language|12QQ51VK01]] explains, so $D(n)$ is true when at least one of its parts is true.
We find the truth value of $D(n)$ for four values of $n$, one for each pattern of the two parts.

1. $n = 4$: $4 = 2 \cdot 2$ is even, and $4$ is not a multiple of $3$.
   One part is true, so $D(4)$ is true.
2. $n = 9$: $9$ is odd, and $9 = 3 \cdot 3$ is a multiple of $3$.
   One part is true, so $D(9)$ is true.
3. $n = 6$: $6 = 2 \cdot 3$ is even and a multiple of $3$.
   Both parts are true, so $D(6)$ is true.
4. $n = 7$: $7$ is odd, and $7 = 2 \cdot 3 + 1$ is not a multiple of $3$.
   Both parts are false, so $D(7)$ is false.

## Remarks

Case 3 is the only case where the inclusive and the exclusive or differ.
On the exclusive reading $D(6)$ would be false, because both parts are true.
Every mathematical text uses the inclusive [[disjunction|0F72FK8EKB]] unless it adds "but not both".

The difference shows up in a count.
The numbers $n$ from $1$ to $12$ with $D(n)$ true form the union of the even numbers and the multiples of $3$:
$$\{2, 4, 6, 8, 10, 12\} \cup \{3, 6, 9, 12\} = \{2, 3, 4, 6, 8, 9, 10, 12\}.$$
That is $6 + 4 - 2 = 8$ numbers.
The exclusive reading removes $6$ and $12$ and leaves $6$ numbers.
If we replace "or" by "and", the statement is true exactly for the multiples of $6$, which are $6$ and $12$ in this range.

## Explanations

### L1 human

Take the claim "the number is even or it can be split into $3$ equal whole parts".
For $4$ it is true, because $4$ is even.
For $9$ it is true, because $9 = 3 + 3 + 3$.
For $6$ both parts hold, and in mathematics the claim is still true.
For $7$ neither part holds, so the claim is false.

### L2 human

Count the integers from $1$ to $30$ for which $D(n)$ is true.
There are $15$ even numbers and $10$ multiples of $3$ in this range.
A number is both even and a multiple of $3$ exactly when it is a multiple of $6$, and there are $5$ of those.
With the inclusive or we count the union, so we subtract the overlap once:
$$15 + 10 - 5 = 20.$$
With the exclusive or we remove the overlap completely: $20 - 5 = 15$.

"At least one of two events" in probability is an inclusive or, and its count needs exactly this subtraction.
Watch out: the answer $15 + 10 = 25$ counts the multiples of $6$ twice, and it is wrong for both readings of "or".
