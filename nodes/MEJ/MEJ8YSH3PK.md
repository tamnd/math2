---
tag: MEJ8YSH3PK
kind: example
name: The Ackermann function exceeds its second argument
msc: ["00A35", "03D20"]
topics: [EEH2F76CYQ]
audience: ug2
instance_of: [AABX4YPKRR]
uses: [N470JF7ZJX, AABX4YPKRR, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Ackermann_function
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Induction on more than one counter
---

## Example

The [[Ackermann function|N470JF7ZJX]] $A \colon \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ is given by the three rules
$$A(0, n) = n + 1, \qquad A(m + 1, 0) = A(m, 1), \qquad A(m + 1, n + 1) = A(m, A(m + 1, n)).$$
We prove, by a [[double induction|AABX4YPKRR]] in nested form, that $A(m, n) > n$ for all natural numbers $m$ and $n$.
For each $m$, let $Q(m)$ be the claim "$A(m, n) > n$ for every natural number $n$".

1. Outer base case: $A(0, n) = n + 1 > n$ by the first rule, for every $n$. So $Q(0)$ holds.
2. Outer step: let $m$ be a natural number and assume $Q(m)$. We prove $Q(m + 1)$ by an inner [[induction|0ASJVEFA9J]] on $n$.
3. Inner base case: $A(m + 1, 0) = A(m, 1)$ by the second rule. By $Q(m)$ with $n = 1$, $A(m, 1) > 1 > 0$.
4. Inner step: let $n$ be a natural number and assume $A(m + 1, n) > n$. Since both sides are integers, $A(m + 1, n) \ge n + 1$.
5. Put $k = A(m + 1, n)$. The third rule gives $A(m + 1, n + 1) = A(m, k)$.
6. By $Q(m)$ with the second argument $k$, $A(m, k) > k$.
7. Steps 4 to 6 give $A(m + 1, n + 1) > k \ge n + 1$. This completes the inner step.
8. The inner induction proves $A(m + 1, n) > n$ for every $n$, that is, $Q(m + 1)$.
9. The outer induction proves $Q(m)$ for every $m$. So $A(m, n) > n$ for all $m$ and $n$.

The first values agree with the result.

| $A(m, n)$ | $n = 0$ | $n = 1$ | $n = 2$ | $n = 3$ | $n = 4$ |
|---|---|---|---|---|---|
| $m = 0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
| $m = 1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
| $m = 2$ | $3$ | $5$ | $7$ | $9$ | $11$ |
| $m = 3$ | $5$ | $13$ | $29$ | $61$ | $125$ |

## Remarks

1. Step 6 uses $Q(m)$ at the second argument $k = A(m + 1, n)$, which depends on $n$ and is large. This is why the outer claim $Q(m)$ must contain "for every $n$".
2. A corollary is that $A$ increases in the second argument. For $m = 0$, $A(0, n + 1) = n + 2 > A(0, n)$. For $m + 1$, the third rule and the result give $A(m + 1, n + 1) = A(m, A(m + 1, n)) > A(m + 1, n)$.
3. The bound is sharp for $m = 0$, where $A(0, n) = n + 1$. For $m \ge 1$ the values grow much faster, as the row $A(3, n) = 2^{n + 3} - 3$ of the table shows.
4. The same nested scheme proves that the rules define a value for every pair. The outer claim is "$A(m, n)$ is defined for every $n$", and the inner step again uses the outer claim at the argument $A(m + 1, n)$.

## Explanations

### L1 human

The Ackermann function takes two whole numbers and gives a whole number.
Its rules call the function again, at other inputs, until the first input becomes $0$.
We show that the output is always bigger than the second input.
For example, $A(2, 3) = 9$, and $9$ is bigger than $3$.
The proof first handles all inputs with first number $0$, then all with first number $1$, and so on.
Inside each first number, it goes through the second numbers one by one.

### L2 human

We follow the proof for $m + 1 = 2$ and $n + 1 = 2$, so $m = 1$ and $n = 1$.

1. The outer hypothesis $Q(1)$ says $A(1, n) > n$ for every $n$. In fact $A(1, n) = n + 2$.
2. The inner hypothesis says $A(2, 1) > 1$. In fact $A(2, 1) = 5$, so $k = 5$.
3. The third rule gives $A(2, 2) = A(1, 5)$.
4. The outer hypothesis $Q(1)$ at the argument $5$ gives $A(1, 5) > 5$. In fact $A(1, 5) = 7$.
5. So $A(2, 2) = 7 > 5 \ge 2$.

The typical use of this pattern is a property of a function defined by a recursion that calls itself inside its own argument.
A trap is to do the inner induction first, on $n$ with $m$ fixed: the step from $n$ to $n + 1$ then needs the case $m - 1$ at a large argument, which that induction has not proved.
