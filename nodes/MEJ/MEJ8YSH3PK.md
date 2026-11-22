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

The [[Ackermann function|N470JF7ZJX]] $A \colon \mathbb{N} \times \mathbb{N} \to \mathbb{N}$ is given by three rules:
$$A(0, n) = n + 1, \qquad A(m + 1, 0) = A(m, 1), \qquad A(m + 1, n + 1) = A(m, A(m + 1, n)).$$
We prove that $A(m, n) > n$ for all natural numbers $m$ and $n$, by a [[double induction|AABX4YPKRR]] in nested form.
For each $m$, let $Q(m)$ be the claim "$A(m, n) > n$ for every natural number $n$".

1. Outer base case.
   The first rule gives $A(0, n) = n + 1 > n$ for every $n$, so $Q(0)$ holds.
2. Outer step.
   Let $m$ be a natural number and assume $Q(m)$.
   We prove $Q(m + 1)$ by an inner [[induction|0ASJVEFA9J]] on $n$.
3. Inner base case.
   The second rule gives $A(m + 1, 0) = A(m, 1)$, and $Q(m)$ at the argument $1$ gives $A(m, 1) > 1 > 0$.
4. Inner step.
   Let $n$ be a natural number and assume $A(m + 1, n) > n$.
   Both sides are integers, so $k = A(m + 1, n)$ satisfies $k \ge n + 1$.
5. The third rule gives $A(m + 1, n + 1) = A(m, k)$.
6. The outer hypothesis $Q(m)$ at the argument $k$ gives $A(m, k) > k$.
7. Steps 4 to 6 give $A(m + 1, n + 1) > k \ge n + 1$, which completes the inner step.
8. The inner induction proves $A(m + 1, n) > n$ for every $n$, that is, $Q(m + 1)$.
9. The outer induction proves $Q(m)$ for every $m$, so $A(m, n) > n$ for all $m$ and $n$.

The first values agree with the result.

| $A(m, n)$ | $n = 0$ | $n = 1$ | $n = 2$ | $n = 3$ | $n = 4$ |
|---|---|---|---|---|---|
| $m = 0$ | $1$ | $2$ | $3$ | $4$ | $5$ |
| $m = 1$ | $2$ | $3$ | $4$ | $5$ | $6$ |
| $m = 2$ | $3$ | $5$ | $7$ | $9$ | $11$ |
| $m = 3$ | $5$ | $13$ | $29$ | $61$ | $125$ |

Check: $A(2, 1) = A(1, A(2, 0)) = A(1, 3) = 5$, and $A(3, 1) = A(2, A(3, 0)) = A(2, 5) = 13$, since $A(2, n) = 2n + 3$.

## Remarks

Step 6 is the heart of the proof.
It uses the outer hypothesis $Q(m)$ at the second argument $k = A(m + 1, n)$, which depends on $n$ and is large.
So the outer claim must say "for every $n$"; a claim about one fixed $n$ would not reach the argument $k$.

The result gives a corollary at once: $A$ increases in its second argument.
For $m = 0$ we have $A(0, n + 1) = n + 2 > A(0, n)$.
For $m + 1$, the third rule and the result at the argument $A(m + 1, n)$ give
$$A(m + 1, n + 1) = A(m, A(m + 1, n)) > A(m + 1, n).$$

The bound is sharp for $m = 0$, where $A(0, n) = n + 1$.
For larger $m$ the values grow much faster, and the row $m = 3$ of the table is $A(3, n) = 2^{n + 3} - 3$.
The same nested scheme proves that the three rules define a value for every pair: the outer claim is "$A(m, n)$ is defined for every $n$", and the inner step again uses the outer claim at the argument $A(m + 1, n)$.

## Explanations

### L1 human

The Ackermann function takes two whole numbers and gives a whole number.
Its rules call the function again, at other inputs, until the first input becomes $0$.
We show that the output is always bigger than the second input.
For example, $A(2, 3) = 9$, and $9$ is bigger than $3$.
The proof first handles all inputs with first number $0$, then all with first number $1$, and so on.
Inside each first number, it goes through the second numbers one by one.

### L2 human

Follow the proof for $m + 1 = 2$ and $n + 1 = 2$, so that $m = 1$ and $n = 1$.
The outer hypothesis $Q(1)$ says that $A(1, n) > n$ for every $n$, and in fact $A(1, n) = n + 2$.
The inner hypothesis says that $A(2, 1) > 1$, and in fact $A(2, 1) = 5$, so $k = 5$.
The third rule gives $A(2, 2) = A(1, 5)$, and $Q(1)$ at the argument $5$ gives $A(1, 5) > 5$.
So
$$A(2, 2) = A(1, 5) = 7 > 5 \ge 2.$$
This pattern fits any function whose recursion calls itself inside its own argument.
Watch out: the outer induction must be on $m$, because no call of the recursion increases $m$, while the second argument can jump from $n + 1$ to $k$.
An induction on $n$ with $m$ fixed fails, because its step needs the row $m - 1$ at the large argument $k$, which that induction never proves.
