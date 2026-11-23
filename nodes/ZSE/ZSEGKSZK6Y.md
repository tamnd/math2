---
tag: ZSEGKSZK6Y
kind: example
name: A chain of divisibility facts by Barbara
msc: ["03B10", "03-03"]
topics: [H8QZY0RZXZ]
audience: school
instance_of: [AC6XQ4KRNT, MZBNX2T6Q6]
uses: [AC6XQ4KRNT, MZBNX2T6Q6, KSJ9W29KXQ, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Syllogism
    locator: lead section
---

## Example

We use [[Barbara|AC6XQ4KRNT]] twice in a row to prove that every multiple of $12$ has a digit sum divisible by $3$.
Barbara says: from "all $M$ are $P$" and "all $S$ are $M$", infer "all $S$ are $P$".

1. All multiples of $6$ are multiples of $3$, because $6k = 3 \cdot 2k$.
2. All multiples of $12$ are multiples of $6$, because $12k = 6 \cdot 2k$.
3. Barbara with $S$ the multiples of $12$, $M$ the multiples of $6$ and $P$ the multiples of $3$ gives: all multiples of $12$ are multiples of $3$.
4. All multiples of $3$ have a digit sum that is a multiple of $3$, by the divisibility test for $3$.
5. Barbara with $S$ the multiples of $12$, $M$ the multiples of $3$ and $P$ the numbers whose digit sum is a multiple of $3$ gives: every multiple of $12$ has a digit sum that is a multiple of $3$.

In step 5 the conclusion of step 3 serves as the minor premise, and step 4 is the major premise.
Each step has three A propositions with the middle term first the subject and then the predicate, so each is an instance of Barbara.
Check with one number:
$$12 \cdot 17 = 204, \qquad 2 + 0 + 4 = 6 = 3 \cdot 2.$$

## Remarks

The example shows the typical use of Barbara in mathematics: a chain of inclusions, cut into links that are each easy to check.
In set notation the chain is
$$\text{multiples of } 12 \subseteq \text{multiples of } 6 \subseteq \text{multiples of } 3 \subseteq \{ n : 3 \text{ divides the digit sum of } n \}.$$
A chain of $n$ inclusions needs $n - 1$ uses of Barbara.
A chain of syllogisms in which each conclusion is a premise of the next is called a polysyllogism.

Reverse one link and the chain breaks.
"All multiples of $3$ are multiples of $6$" is false, as $9$ shows.
With this false premise, "all multiples of $3$ are multiples of $6$, all odd multiples of $3$ are multiples of $3$, so all odd multiples of $3$ are multiples of $6$" is still a valid instance of Barbara.
Its conclusion is false, since an odd number is never a multiple of $6$, so a valid form with a false premise proves nothing.

## Explanations

### L1 human

Every multiple of $12$ is a multiple of $6$, and every multiple of $6$ is a multiple of $3$.
So every multiple of $12$ is a multiple of $3$, and that is one use of Barbara.
Every multiple of $3$ has a digit sum divisible by $3$, so every multiple of $12$ has one too.
That is a second use of Barbara, with the result of the first as a premise.
For example, $204 = 12 \cdot 17$ has digit sum $6$.

### L2 human

We prove a longer chain: every multiple of $36$ has a digit sum divisible by $9$.

1. All multiples of $36$ are multiples of $9$, because $36k = 9 \cdot 4k$.
2. All multiples of $9$ have a digit sum divisible by $9$, by the divisibility test for $9$.
3. Barbara with $M$ the multiples of $9$ gives: all multiples of $36$ have a digit sum divisible by $9$.
4. Check: $36 \cdot 23 = 828$, and $8 + 2 + 8 = 18 = 9 \cdot 2$.

Each link of the chain is an inclusion you can verify alone, and Barbara joins them.
The trap is to read a link backwards: "all multiples of $9$ are multiples of $36$" is false, since $9$ itself is not a multiple of $36$.
