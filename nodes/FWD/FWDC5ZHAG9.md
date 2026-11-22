---
tag: FWDC5ZHAG9
kind: example
name: The equation 2^10 = 1024 is not deep
msc: ["00A35"]
topics: [Z2WNQ1DNTX]
audience: school
not_instance_of:
  - target: STHWD1K9AN
    note: the proof uses only multiplication of integers, the same concept as the statement
uses: [STHWD1K9AN]
sources:
  - url: https://en.wikipedia.org/wiki/Glossary_of_mathematical_jargon
    locator: Philosophy of mathematics
---

## Example

Consider the statement $2^{10} = 1024$.
We check that it is not [[deep|STHWD1K9AN]] in the sense of mathematical jargon.

1. We list the ideas in the statement.
   It uses the integers $2$, $10$ and $1024$ and the power $2^{10}$, which means $2$ multiplied by itself $10$ times.
2. We give a proof.
   It is a computation:
   $$2^5 = 32, \qquad 2^{10} = 2^5 \cdot 2^5 = 32 \cdot 32 = 1024.$$
3. We list the ideas in the proof.
   It uses only multiplication of integers, which the statement already needs.

A result is deep only when its proof needs ideas well beyond those of its statement, so this result is not deep.

Check: $32 \cdot 32 = 30 \cdot 32 + 2 \cdot 32 = 960 + 64 = 1024$.

## Remarks

The result is a computation, so most mathematicians would also call it [[trivial|Y0HXCJRB9B]].
Contrast it with [[Fermat's last theorem|0Y5X3SDBCZ]], whose statement also uses only integers and powers, but whose proof needs elliptic curves and modular forms.
So depth is a property of the gap between statement and proof, not of the size of the numbers or the look of the formula.

Large numbers do not change the verdict.
The exact value of $2^{1000}$ has $302$ digits, and it is still not deep, because repeated multiplication proves it.

## Explanations

### L1 human

We can check $2^{10} = 1024$ by doubling $2$ ten times: $2, 4, 8, 16, 32, 64, 128, 256, 512, 1024$.
We need only multiplication, the same idea that the statement uses.
So the result is not deep.
A deep result is one that needs much more mathematics in its proof than in its statement.

### L2 human

To test whether a result is deep, compare two lists.
The ideas of the statement here are integers and powers.
The ideas of the shortest known proof are integers and multiplication, and a power is repeated multiplication.
The second list adds nothing to the first, so the result is not deep.
The test uses the known proofs, so for an open or newly proved result the verdict can change when a simpler proof appears, as it did for the prime number theorem.
