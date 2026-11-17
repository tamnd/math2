---
tag: ~ddc1d33b
kind: example
name: Signs in front of 1 to 10 cannot give the sum 0
msc: ["00A35", "11A07"]
topics: [GB14W4SYPK]
audience: school
instance_of: [~d211a525]
uses: [~d211a525, 01QZNHQWYD]
sources:
  - url: https://en.wikipedia.org/wiki/Parity_(mathematics)
    locator: Properties
---

## Example

We show that no choice of the signs in
$$\pm 1 \pm 2 \pm 3 \pm \cdots \pm 10$$
gives the value $0$.

1. Let $S$ be the value of the expression for some choice of signs. We compare $S$ with the sum $T = 1 + 2 + \cdots + 10$, where every sign is plus.
2. By the formula for the [[sum of the first n natural numbers|01QZNHQWYD]], $T = 10 \cdot 11 / 2 = 55$, which is odd.
3. Let $A$ be the set of numbers $k$ that carry a minus sign in $S$. Each such $k$ contributes $-k$ to $S$ and $+k$ to $T$, so $T - S = \sum_{k \in A} 2k$.
4. The right side of step 3 is $2 \sum_{k \in A} k$, which is even. So $S$ and $T$ have the same parity.
5. By steps 2 and 4, $S$ is odd. The number $0$ is even, so $S \neq 0$.

## Remarks

The example shows a [[parity argument|~d211a525]] with an invariant: a change of one sign changes the sum by an even number $2k$, so the parity of the sum never changes.
We never need to try the $2^{10} = 1024$ choices of signs.

The answer depends on the last number $n$.
For the expression $\pm 1 \pm 2 \pm \cdots \pm n$, the same steps show that the value $0$ needs $n(n + 1)/2$ to be even.
This happens exactly when $n \equiv 0$ or $n \equiv 3 \pmod 4$.
For these $n$ a choice of signs with value $0$ exists: for $n = 3$ take $1 + 2 - 3$, for $n = 4$ take $1 - 2 - 3 + 4$, and for larger $n$ add blocks $k - (k + 1) - (k + 2) + (k + 3)$, each of value $0$.
A computer check of all choices of signs for $n = 1$ to $16$ confirms that the value $0$ occurs exactly for $n = 3, 4, 7, 8, 11, 12, 15, 16$.
So parity gives the exact answer in this family, but the existence part needs the construction.

## Explanations

### L1 human

Write the numbers $1$ to $10$ in a row and put a plus or a minus in front of each one.
We want the total to be $0$.
With all signs plus, the total is $55$, an odd number.
Turning one plus into a minus, say in front of $4$, lowers the total by $8$, an even number.
Each change of sign moves the total by an even number, so the total stays odd.
An odd number is never $0$, so the goal is impossible.

### L2 human

We apply the same steps to $\pm 1 \pm 2 \pm \cdots \pm 7$, where the answer is different.

1. The sum with all plus signs is $T = 7 \cdot 8 / 2 = 28$, which is even.
2. So the parity argument does not forbid the value $0$.
3. For value $0$, the numbers with a minus sign must add up to $T / 2 = 14$.
4. We choose $7 + 4 + 2 + 1 = 14$. The expression $-1 - 2 + 3 - 4 + 5 + 6 - 7$ has value $-14 + 14 = 0$.

The typical use of a parity argument is the first test of a target value.
The trap is step 2: an agreement of parities is only a necessary condition, and the existence of a solution needs a construction, as in step 4.
