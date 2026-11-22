---
tag: 1YJTRBDGC3
kind: example
name: The if in a definition does not introduce a hypothesis
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: ug1
not_instance_of:
  - target: W48XN2MEM9
    note: a definition such as "n is even if n = 2k for some integer k" gives a name to a condition; its "if" means "if and only if", and the sentence has no hypothesis and no conclusion to prove
uses: [W48XN2MEM9, 5M5Q062R1X]
sources:
  - url: https://en.wikipedia.org/wiki/If_and_only_if
    locator: Usage
  - url: https://en.wikipedia.org/wiki/Definition
    locator: lead section
---

## Example

Consider the sentence "an integer $n$ is even if $n = 2k$ for some integer $k$".
It looks like a theorem "if $H$, then $C$", with $H$ the condition "$n = 2k$ for some integer $k$" and $C$ the claim "$n$ is even".
We check that it is a definition, and that it has no [[hypothesis and conclusion|W48XN2MEM9]] in the sense of a theorem.

1. Before the sentence, the word "even" has no meaning in the text.
   So the sentence cannot assert a fact about even numbers: it gives the meaning.
2. Nothing in the sentence needs a proof, because it fixes the use of a new word and there is nothing to check it against.
3. The sentence is used in the direction "if".
   From $6 = 2 \cdot 3$ we conclude that $6$ is even.
4. It is also used in the direction "only if".
   In [[the proof that the sum of two even integers is even|5M5Q062R1X]] we pass from "$m$ is even" to "$m = 2a$ for some integer $a$", and a one-way conditional would not allow that step.
5. The direction "only if" is also what shows that $7$ is not even.
   The equation $7 = 2k$ gives $k = 3.5$, which is not an integer.
6. So the "if" of the definition means "if and only if".
   The sentence is a definition, not a conditional statement with a hypothesis and a conclusion.

## Remarks

This is a convention of mathematical English: in a definition, "if" stands for "if and only if".
Some authors write "iff", "exactly when" or $:\Leftrightarrow$ in definitions, and many set the defined word in italic type, to make the convention visible.
In a theorem, "if" keeps its one-way meaning, and the converse needs its own proof.
For example, "if $n$ is divisible by $4$, then $n$ is even" is a theorem, and its converse fails at $n = 6$.

## Explanations

### L1 human

The sentence "a number is even if it is two times a whole number" is a definition.
It tells us what the word "even" means.
It is not a fact that needs a proof, and it works both ways: the even numbers are exactly the numbers of the form two times a whole number.
That is why we can say that $7$ is not even: $7$ is not two times a whole number.

### L2 human

Sort three sentences into definitions and theorems.
"A prime is an integer $p > 1$ whose only positive divisors are $1$ and $p$" is a definition, and it works in both directions.
"If $p$ is a prime greater than $2$, then $p$ is odd" is a theorem, with the hypothesis "$p$ is a prime greater than $2$" and the conclusion "$p$ is odd".
Its converse is false, because $9$ is odd and not prime.
"An integer $n$ is odd if $n = 2k + 1$ for some integer $k$" is a definition, so its "if" means "if and only if".
The test is simple: a sentence that introduces a new word is a definition, and a sentence about words already defined is a claim that needs a proof.
