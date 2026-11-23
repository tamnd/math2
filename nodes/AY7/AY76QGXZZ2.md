---
tag: AY76QGXZZ2
kind: example
name: The proof that 0.999... equals 1 is not a fallacy
msc: ["00A35", "40A05"]
topics: [T6QQ749DM5]
audience: school
not_instance_of:
  - target: S2BW0FDHV8
    note: each step is valid, because the series that defines 0.999... converges, and the conclusion is true
uses: [S2BW0FDHV8, 0NN5JEMTVE, 01X5CVV1Q5]
sources:
  - url: https://en.wikipedia.org/wiki/0.999...
    locator: Infinite series and sequences
---

## Example

Many readers meet the following argument and suspect a trick.

1. Let $x = 0.999\ldots$, with the digit $9$ at every place after the point.
2. Multiply by $10$: $10x = 9.999\ldots$.
3. Subtract the first line from the second: $9x = 9$.
4. So $x = 1$.

This argument is not a [[mathematical fallacy|S2BW0FDHV8]].
Every step is valid, and the conclusion [[$0.999\ldots = 1$|0NN5JEMTVE]] is true.
We check the steps one at a time.

1. Step 1 names a real number. By definition, $0.999\ldots$ is the sum of a [[geometric series|01X5CVV1Q5]] with ratio $\frac{1}{10}$, and such a series converges:
   $$x = \sum_{k=1}^{\infty} \frac{9}{10^k}.$$
2. Step 2 is valid, because a convergent series may be multiplied by a constant term by term:
   $$10x = \sum_{k=1}^{\infty} \frac{9}{10^{k-1}} = 9 + \sum_{k=1}^{\infty} \frac{9}{10^k} = 9 + x.$$
3. Step 3 subtracts $x$ from both sides of $10x = 9 + x$, which gives $9x = 9$.
4. Step 4 divides by $9$, which is not zero.

## Remarks

What makes this argument a proof, when arguments of the same shape are fallacies?
The answer is step 1: the series converges, so $x$ is a number and the algebra is allowed.
Run the same steps on $y = 1 + 10 + 100 + \cdots$.
They give $10y = 10 + 100 + \cdots = y - 1$, so $y = -\frac{1}{9}$, an absurd value for a sum of positive numbers.
There step 1 fails, because the series diverges and $y$ names nothing.
The [[fallacies with infinite series|KDXKVT5K1E]] make the same error with $S = 1 - 1 + 1 - \cdots$.
So a full proof must say why the series converges, and the short argument above leaves that reason silent.

## Explanations

### L1 human

The number $0.999\ldots$, with nines that never stop, is exactly $1$.
Ten times it is $9.999\ldots$.
If you take away the first number, all the nines after the point cancel and $9$ is left.
So nine times the number is $9$, and the number is $1$.
This is not a trick, because the endless string of nines has a value; the same game with $1 + 10 + 100 + \cdots$ is a trick, because that sum has no value.

### L2 human

We prove the equality with finite pieces, to see where convergence enters.
Let $s_n = \frac{9}{10} + \frac{9}{100} + \cdots + \frac{9}{10^n}$.
Multiply by $10$ and subtract; every term except two cancels:
$$10 s_n - s_n = 9 - \frac{9}{10^n}, \quad \text{so} \quad s_n = 1 - \frac{1}{10^n}.$$
As $n \to \infty$, $\frac{1}{10^n} \to 0$, so $s_n \to 1$.
By definition $0.999\ldots$ is the limit of $s_n$, so it equals $1$.

Check: $s_3 = 0.999 = 1 - 0.001$.
This is the safe way to test any "infinite" manipulation: do it on the finite partial sums first, then take the limit.
Watch out: for a divergent series the last step has no limit to take, and the manipulation proves nothing.
