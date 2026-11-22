---
tag: AABX4YPKRR
kind: concept
name: Double induction
aliases: [induction-on-two-variables, nested-induction]
msc: ["00A35", "97E50", "03F30"]
topics: [EEH2F76CYQ, G9JFJGY4TQ]
audience: ug1
specializes: [0ASJVEFA9J]
uses: [0ASJVEFA9J, 0KMVFSHFGZ, 01BX15HSRR, 0G77XFBV00]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Induction on more than one counter
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Prefix induction
  - url: https://en.wikipedia.org/wiki/Ackermann_function
    locator: General remarks
---

## Summary

Double induction proves a claim $P(m, n)$ about every pair of [[natural numbers|0MWKJ44V5A]].
The idea is to put the pairs in an order in which each pair comes after the pairs that its proof needs, and then to run [[mathematical induction|0ASJVEFA9J]] along that order.

Here is a short theorem proved this way.
A path on the grid from $(0, 0)$ to $(m, n)$ that uses only the unit steps right and up has exactly $m + n$ steps, and the number of such paths is $\binom{m + n}{m}$.
The last step of a path to $(m, n)$ comes from $(m - 1, n)$ or from $(m, n - 1)$, so for $m, n \ge 1$ the number $L(m, n)$ of paths satisfies
$$L(m, n) = L(m - 1, n) + L(m, n - 1).$$
Both pairs on the right have the sum $m + n - 1$, so an induction on the sum $s = m + n$ proves the formula for every pair, as [[the lattice path count|HPB4XV5ACB]] shows in full.

Three forms are in common use.
In a *nested induction*, an outer induction on $m$ proves $Q(m)$: "$P(m, n)$ holds for every natural number $n$", and the base case and the step of the outer induction are each proved by an inner induction on $n$.
In an *induction on the sum*, an ordinary or [[strong induction|0KMVFSHFGZ]] on $s$ proves "$P(m, n)$ holds for every pair with $m + n = s$".
In a *lexicographic induction*, each $P(m, n)$ is proved from all $P(m', n')$ with $(m', n')$ smaller in the [[lexicographic order|0G77XFBV00]].

## Motivation

Many objects of two variables are defined by a recursion that refers to more than one earlier pair.
Pascal's rule computes $\binom{s}{k}$ from $\binom{s - 1}{k - 1}$ and $\binom{s - 1}{k}$, so a proof about all binomial coefficients must reach every pair $(s, k)$.
The [[Ackermann function|N470JF7ZJX]] is worse: it computes $A(m + 1, n + 1)$ from $A(m + 1, n)$ and from $A(m, k)$, where $k = A(m + 1, n)$ can be very large.
An induction on one variable, with the other variable fixed, never reaches the pair $(m, k)$.
Double induction solves this by choosing an order on the pairs that the recursion respects.

The same need appears in computing.
A recursive program with two arguments stops on every input when each recursive call goes to a smaller pair in a well-founded order, and the proof that it stops is a double induction.
[[Structural induction|12MQ2NJ29A]] and [[induction on size|B2D8PTFNN1]] apply the same idea to other orders.

## Notation

A nested induction is often announced as "induction on $m$, and for fixed $m$ induction on $n$".
The outer statement must contain the words "for every $n$", and in Lean 4 the tactic `induction m generalizing n` makes this explicit.
The lexicographic order is written $(m', n') <_{\mathrm{lex}} (m, n)$, and it means that $m' < m$, or that $m' = m$ and $n' < n$.
Some books say "induction on $m + n$" for the second form, and the name "double induction" covers all three forms.

## Remarks

### Why the three forms are valid

A nested induction is two ordinary inductions, one inside the other.
The inner inductions prove $Q(0)$ and the implication $Q(m) \Rightarrow Q(m + 1)$, and then the outer induction gives $Q(m)$ for every $m$.

An induction on the sum is one ordinary induction on $s$.
Every pair $(m, n)$ has a sum $s = m + n$, so the claim for that $s$ includes the pair.

A lexicographic induction rests on the fact that the lexicographic order on $\mathbb{N} \times \mathbb{N}$ is a well-order.
Let $X$ be a nonempty set of pairs.
By the [[well-ordering principle|01BX15HSRR]], the first coordinates of the pairs in $X$ have a least value $m_0$.
The second coordinates of the pairs in $X$ with first coordinate $m_0$ have a least value $n_0$, and then $(m_0, n_0)$ is the least element of $X$.
Now suppose that each $P(m, n)$ follows from all $P(m', n')$ with $(m', n') <_{\mathrm{lex}} (m, n)$, and let $X$ be the set of pairs where $P$ fails.
If $X$ were nonempty, all pairs below its least element would satisfy $P$, so $P$ would hold at that least element, which is a contradiction.

### The lexicographic order is not a counting order

Why do we need a well-order and not just a count $0, 1, 2, \dots$?
The pair $(1, 0)$ comes after every pair $(0, n)$, and there are infinitely many of these.
So if we list the pairs in this order, the pair $(1, 0)$ never appears at a finite position, and an induction that counts the positions cannot reach it.
This is exactly the order that the Ackermann recursion needs, and it is why the proof for the [[Ackermann function exceeds its second argument|MEJ8YSH3PK]] is a nested induction and not an induction on one counter.

### Choosing the form

Look at the pairs that the recursion uses.
If they all have a smaller sum, as $(m - 1, n)$ and $(m, n - 1)$ do, induct on $m + n$.
If one variable goes down while the other can go up, as in the Ackermann function, use a nested or lexicographic induction on the variable that always goes down first.
For example, the [[proof of Ramsey's theorem by induction on r + s|1VP19TWGTB]] uses the sum, and the [[proof of the commutativity of addition by induction|4EQPCHKEBH]] proves lemmas by induction on one variable and uses them inside the induction on the other.
The [[factorial formula for binomial coefficients|N10HP9QWX7]] is proved by induction on the top index $n$, with a claim for every $k$ at each $n$.

### A one-variable cousin: prefix induction

Prefix induction proves $P(0)$, and for each $k$ it proves that $P(k)$ implies both $P(2k)$ and $P(2k + 1)$.
It is valid by strong induction, because each $n \ge 1$ equals $2k$ or $2k + 1$ with $k = \lfloor n/2 \rfloor < n$.
It reaches $n$ in as many steps as $n$ has binary digits.
For example, $100$ is $1100100$ in binary, and the chain of prefixes is
$$1, \; 3, \; 6, \; 12, \; 25, \; 50, \; 100.$$
Check: each number is twice the one before, or twice plus one.

### What double induction is not

An [[induction along the diagonal|NF8SZ82JAC]] proves $P(0, 0)$ and the step from $P(n, n)$ to $P(n + 1, n + 1)$.
Its steps never leave the diagonal, so it proves $P(n, n)$ for each $n$ and nothing about the pairs with $m \neq n$.
In the same way, an induction on $m$ with a fixed value $n_0$ proves $P(m, n_0)$ for every $m$, and nothing about the other values of $n$.

### Watch out

The first error is to fix $n$ in the outer hypothesis.
In the Ackermann proof, the step for $m + 1$ needs the case $m$ at the second argument $k = A(m + 1, n)$, so a hypothesis about one fixed $n$ is useless there.
The correct outer claim is "for every $n$".

The second error is to forget the boundary.
In an induction on $m + n$ whose step uses $(m - 1, n)$ and $(m, n - 1)$, the pairs with $m = 0$ or $n = 0$ have only one of these neighbors.
For example, $L(3, 0) = 1$, and it is not $L(2, 0) + L(3, -1)$, which has no meaning.
So the boundary pairs need their own argument.

### History

Wilhelm Ackermann published his function in 1928, and nested induction is the standard way to prove that its recursion gives a value for every pair.
The two-variable form of the function that most books use today is due to Rózsa Péter and Raphael Robinson.

### Try it

First, compute $A(1, 2)$ from the rules $A(0, n) = n + 1$, $A(m + 1, 0) = A(m, 1)$ and $A(m + 1, n + 1) = A(m, A(m + 1, n))$.
You get $A(1, 0) = A(0, 1) = 2$, then $A(1, 1) = A(0, 2) = 3$, then $A(1, 2) = A(0, 3) = 4$.

Second, write the chain of prefixes that prefix induction uses to reach $37$.
In binary $37$ is $100101$, so the chain is $1, 2, 4, 9, 18, 37$.

## Explanations

### L1 human

Think of a table with infinitely many rows and columns, and one claim in each cell.
To prove all the claims, we need an order in which every cell comes after the cells that it depends on.
One way is to go row by row, and inside each row, cell by cell.
Another way is to go along the diagonals where the row number plus the column number is $0$, then $1$, then $2$, and so on.
For example, the cell in row $2$ and column $3$ lies on diagonal $5$, and we reach it after all the cells of diagonal $4$.

### L2 human

Define $h(m, 0) = 1$, $h(0, n) = 1$, and $h(m, n) = h(m - 1, n) + h(m, n - 1)$ for $m, n \ge 1$.
We prove that $h(m, n) \le 2^{m + n}$ for all natural numbers $m$ and $n$, by induction on $s = m + n$.
Let $R(s)$ be the claim "$h(m, n) \le 2^{m + n}$ for all pairs with $m + n = s$".

For $s = 0$ the only pair is $(0, 0)$, and $h(0, 0) = 1 = 2^0$.
Now let $s \ge 1$, assume $R(s - 1)$, and take a pair with $m + n = s$.
If $m = 0$ or $n = 0$, the definition gives $h(m, n) = 1 \le 2^s$.
If $m, n \ge 1$, both pairs $(m - 1, n)$ and $(m, n - 1)$ have the sum $s - 1$, so $R(s - 1)$ bounds both values:
$$h(m, n) = h(m - 1, n) + h(m, n - 1) \le 2^{s - 1} + 2^{s - 1} = 2^s.$$
This proves $R(s)$, and every pair $(m, n)$ is covered by $R(m + n)$.

Check: $h(2, 2) = h(1, 2) + h(2, 1) = 3 + 3 = 6 \le 16$.
In fact $h(m, n) = \binom{m + n}{m}$ by the [[lattice path count|HPB4XV5ACB]], so the bound is far from sharp.
The proof shows the typical use: a recursion in two variables whose recursive pairs all have a smaller sum.

### L3 human

Double induction is the case $\mathbb{N} \times \mathbb{N}$ of induction over a [[well-founded relation|0DQPNJNPYK]].
The lexicographic order on $\mathbb{N}^k$ is a well-order of order type $\omega^k$, so lexicographic induction on $k$ counters is a case of [[transfinite induction|0ZHQMQ2C1N]].
The product order, in which $(m', n') \le (m, n)$ means $m' \le m$ and $n' \le n$, is also well-founded, and induction on $m + n$ is one way to use it.
In the theory of programs, termination proofs choose a measure that decreases in a well-founded order at each recursive call, and the Ackermann function is the standard example of a lexicographic measure.
The same function shows the reach of the method: it is [[not primitive recursive|97QF3KHSBY]], so a recursion on one counter at a time does not produce it.
