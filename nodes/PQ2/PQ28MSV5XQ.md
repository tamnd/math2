---
tag: PQ28MSV5XQ
kind: example
name: The sentence "n is even, i.e. n = 4" misuses i.e.
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
not_instance_of:
  - target: 4ZNYMYRRY3
    note: the abbreviation i.e. must introduce an equivalent restatement, but n = 4 is only one instance of an even number
uses: [4ZNYMYRRY3, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/List_of_mathematical_abbreviations
    locator: lead section
---

## Example

Consider the sentence "Let $n$ be an even [[integer|0C4JS9RF5M]], `i.e.` $n = 4$."
We show that it is not a correct use of the [[abbreviation|4ZNYMYRRY3]] `i.e.`.

1. `i.e.` stands for the Latin "id est", "that is".
   It joins two statements that say the same thing in other words.
2. So the sentence claims that an integer $n$ is even exactly when $n = 4$.
3. The integer $6$ is even, because $6 = 2 \cdot 3$.
4. The integer $6$ is not equal to $4$.
5. So "$n$ is even" and "$n = 4$" are different statements, and the use of `i.e.` is wrong.

Two correct sentences are close to the wrong one.
"Let $n$ be an even integer, `e.g.` $n = 4$" uses `e.g.`, "for example", to give one case.
"Let $n$ be an even integer, `i.e.` $n = 2k$ for some integer $k$" uses `i.e.` with the definition of "even", which says the same thing.

## Remarks

The two short forms differ in what the reader may do next.
After `i.e.`, the reader may replace the first part by the second in every later step.
After `e.g.`, the reader may not, because the second part is one case only.
So a proof that writes "`i.e.` $n = 4$" and then uses $n = 4$ proves the result for one number.

Change one word and the sentence becomes correct.
"Let $n$ be an even prime, `i.e.` $n = 2$" is a true restatement, because $2$ is the only even prime.

## Explanations

### L1 human

The short form `i.e.` means "that is", and it repeats the same idea in other words.
The short form `e.g.` means "for example", and it gives one case.
"Even numbers, `e.g.` $4$" is right, because $4$ is one even number.
"Even numbers, `i.e.` $4$" is wrong, because $6$ and $8$ are even too.

### L2 human

To test a use of `i.e.`, read its two parts as statements $P$ and $Q$, and check both $P \Rightarrow Q$ and $Q \Rightarrow P$.
Take "$n$ is an even prime, `i.e.` $n = 2$".
If $n$ is an even prime, then $2 \mid n$ and the only positive divisors of $n$ are $1$ and $n$, so $n = 2$.
Conversely, $2$ is even and prime.
Both directions hold, so the use is correct.
For "$n$ is even, `i.e.` $n = 4$" the direction $P \Rightarrow Q$ fails at $n = 6$.
Watch out for an `i.e.` that introduces a consequence instead of a restatement, as in "$n$ is divisible by $4$, `i.e.` $n$ is even".
The forward direction holds, but the converse fails at $n = 2$, so the writer should say "so" instead.
