---
tag: DZSC3MRGFF
kind: example
name: Divisibility by 4 and divisibility by 6 are incomparable
msc: ["00A35", "11A05"]
topics: [Z2WNQ1DNTX]
audience: ug1
not_instance_of:
  - target: KCK4AQ469Q
    note: Neither property implies the other, so neither is stronger than the other.
uses: [KCK4AQ469Q, 0PG2H7WKGG, 007NPQX34K]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Descriptive informalities
---

## Example

For an integer $n$, let $A(n)$ be "$4$ [[divides|0PG2H7WKGG]] $n$" and let $B(n)$ be "$6$ divides $n$".
We show that neither property is [[stronger|KCK4AQ469Q]] than the other.

1. If $A$ were stronger than $B$, then each $n$ with $A(n)$ would also have $B(n)$.
2. The number $n = 4$ has $A(4)$, because $4 = 1 \cdot 4$. It does not have $B(4)$, because $0 < 4 < 6$. So $A$ is not stronger than $B$.
3. The number $n = 6$ has $B(6)$. It does not have $A(6)$, because $6 = 1 \cdot 4 + 2$. So $B$ is not stronger than $A$.
4. So $A$ and $B$ are incomparable.
5. The two properties can still hold together. The property "$A(n)$ and $B(n)$" is equivalent to "$12$ divides $n$", because $12$ is the [[least common multiple|007NPQX34K]] of $4$ and $6$; for example $n = 12$ and $n = 24$.

## Remarks

The property "$12$ divides $n$" is stronger than each of $A$ and $B$, and the property "$2$ divides $n$" is weaker than each of them.
In general, "$a$ divides $n$" is stronger than "$b$ divides $n$" exactly when $b$ divides $a$.
For $a = 4$ and $b = 6$, neither number divides the other, which is the reason for the incomparability.

## Explanations

### L1 human

Some numbers are in the four times table, like $4$, $8$ and $12$.
Some numbers are in the six times table, like $6$, $12$ and $18$.
Neither list contains the other: $4$ is only in the first list, and $6$ is only in the second.
So neither property is "stronger", even though both lists contain $12$.

### L2 human

We decide which of the properties "$3$ divides $n$" and "$9$ divides $n$" is stronger.

1. If $9$ divides $n$, then $n = 9k = 3 \cdot (3k)$, so $3$ divides $n$.
2. The number $3$ is divisible by $3$ but not by $9$.
3. So "$9$ divides $n$" is strictly stronger than "$3$ divides $n$".

The typical use of this test is to compare two conditions by a proof in one direction and a counterexample in the other.
A trap: one common example, such as $12$ here, does not make two properties comparable.
