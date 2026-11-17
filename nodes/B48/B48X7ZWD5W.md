---
tag: B48X7ZWD5W
kind: example
name: A written proof that the product of two odd integers is odd
msc: ["00A35", "11A05"]
topics: [STSM6PR7TX]
audience: ug1
instance_of: [8JQHJK94RZ]
uses: [8JQHJK94RZ, BV6E0ZG3YN, 0C4JS9RF5M, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: Nature and purpose
  - url: https://en.wikipedia.org/wiki/Parity_(mathematics)
    locator: lead section
---

## Example

We give a complete written proof of a short result, and then we check it against the rules of [[writing proofs|8JQHJK94RZ]].
The text of the proof is the following.

> **Proposition.** Let $m$ and $n$ be integers.
> If $m$ and $n$ are odd, then $mn$ is odd.
>
> **Proof.** Suppose that $m$ and $n$ are odd.
> By the [[definition of an odd integer|BV6E0ZG3YN]], there are integers $a$ and $b$ with $m = 2a + 1$ and $n = 2b + 1$.
> We multiply these two equations and expand the product:
> $$mn = (2a + 1)(2b + 1) = 4ab + 2a + 2b + 1 = 2(2ab + a + b) + 1.$$
> Let $k = 2ab + a + b$.
> Then $k$ is an integer, because sums and products of [[integers|0C4JS9RF5M]] are integers.
> So $mn = 2k + 1$ for an integer $k$, and hence $mn$ is odd.
> $\square$

We check the text, one rule at a time.

1. The statement comes first, and it is complete. It names the objects ($m$ and $n$, integers), the hypothesis (both are odd) and the conclusion ($mn$ is odd).
2. The first sentence of the proof says what we assume. The word "Suppose" marks the hypothesis of the [[direct proof|0NTF6DMVAP]].
3. The second sentence gives the reason for the forms $2a + 1$ and $2b + 1$: the definition of an odd integer. The letters $a$ and $b$ are introduced with their type, "integers".
4. The display is a sentence with a verb ("$=$") and a final full stop. Each equality is a step of algebra: the first expands the product, the second takes out the factor $2$ from $4ab + 2a + 2b$.
5. The new letter $k$ gets a name and a reason for its type. This is the condition that the definition of "odd" requires.
6. The last sentence states the conclusion in the words of the statement, and the mark $\square$ ends the proof.

We check the algebra with a numerical case.
For $m = 3$ and $n = 5$ we have $a = 1$ and $b = 2$, so $k = 2 \cdot 1 \cdot 2 + 1 + 2 = 7$ and $2k + 1 = 15 = 3 \cdot 5$.

## Remarks

1. The proof has six sentences, and each sentence does one job. A reader can check each sentence without the others, except for the letters that earlier sentences define.
2. The same text with the words removed, "$m = 2a+1$, $n = 2b+1$, $mn = 2(2ab+a+b)+1$", is a correct calculation but a weaker proof. The reader must guess what is assumed, why $a$ and $b$ exist, and what the last line shows.
3. If we change the hypothesis to "$m$ is odd and $n$ is even", the same plan works with $n = 2b$. The step becomes $mn = (2a + 1) \cdot 2b = 2(2ab + b)$, so $mn$ is even.
4. The proof uses the definition in both directions. It uses "odd means $2a + 1$" to unpack the hypothesis, and "$2k + 1$ means odd" to reach the conclusion.

## Explanations

### L1 human

An odd number is one more than an even number, such as $7 = 6 + 1$.
The page shows how to write down why "odd times odd is odd" in a way that anyone can check.
First we say exactly what we claim.
Then we write each odd number as "two times something, plus one".
We multiply, and we see that the answer is again "two times something, plus one".
For $3 \times 5 = 15$, the "something" is $7$, because $15 = 2 \times 7 + 1$.

### L2 human

We use the same plan to prove that the sum of an odd integer and an even integer is odd.

1. Statement: let $m$ be odd and let $n$ be even; then $m + n$ is odd.
2. By definition, there are integers $a$ and $b$ with $m = 2a + 1$ and $n = 2b$.
3. Then $m + n = 2a + 1 + 2b = 2(a + b) + 1$.
4. The number $a + b$ is an integer, as a sum of integers.
5. So $m + n$ is odd, by the definition of an odd integer.

The typical use of this pattern is every proof about parity and divisibility in a first course.
A trap is to write $m = 2a + 1$ and $n = 2a$ with the same letter $a$: that assumes $n = m - 1$, which the hypothesis does not say.
