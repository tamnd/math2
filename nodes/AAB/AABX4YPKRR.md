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

Double induction is a way to prove a statement $P(m, n)$ for every pair $(m, n)$ of [[natural numbers|0MWKJ44V5A]] with [[mathematical induction|0ASJVEFA9J]].
It has three common forms.
In a nested induction, an outer induction on $m$ proves the statement $Q(m)$: "$P(m, n)$ holds for every natural number $n$".
The base case and the step of the outer induction are then each proved by an inner induction on $n$.
In an induction on the sum, an ordinary or [[strong induction|0KMVFSHFGZ]] on $s = m + n$ proves "$P(m, n)$ holds for all pairs with $m + n = s$".
In a lexicographic induction, each case $P(m, n)$ is proved from the cases $P(m', n')$ with $(m', n')$ smaller in the [[lexicographic order|0G77XFBV00]].
The method matters because many functions of two variables, such as the binomial coefficients and the Ackermann function, are defined by rules that change both variables.

## Motivation

A recursion in two variables often refers to more than one earlier pair.
Pascal's rule computes $\binom{s}{k}$ from $\binom{s - 1}{k - 1}$ and $\binom{s - 1}{k}$, so a proof about all binomial coefficients must reach every pair $(s, k)$.
The Ackermann function computes $A(m + 1, n + 1)$ from $A(m + 1, n)$ and from $A(m, k)$ for a large $k$.
Ordinary induction on one variable, with the other variable fixed, does not reach the pair $(m, k)$.
Double induction gives an order on the pairs in which every case rests on cases that are already proved.

## Notation

1. A nested induction is often announced as "induction on $m$, and for fixed $m$ induction on $n$".
2. The statement of the outer induction must contain "for every $n$". In Lean 4, the tactic `induction m generalizing n` makes this explicit.
3. The lexicographic order is written $(m', n') <_{\mathrm{lex}} (m, n)$. It means $m' < m$, or $m' = m$ and $n' < n$.
4. Some books say "induction on $m + n$" for the second form. The name "double induction" is used for all three forms.

## Remarks

### Examples

1. The [[Ackermann function|N470JF7ZJX]] satisfies $A(m, n) > n$ for all $m$ and $n$, by a [[nested induction on m and n|MEJ8YSH3PK]]. The step for $m + 1$ uses the case $m$ at a large second argument, so the outer statement must hold for every $n$.
2. The [[number of lattice paths to (m, n)|HPB4XV5ACB]] is $\binom{m + n}{m}$, by induction on $m + n$. The step uses the two pairs $(m - 1, n)$ and $(m, n - 1)$, which both have the sum $m + n - 1$.
3. The [[commutativity of addition|0DFZNHJ0S2]] of natural numbers has a [[proof by nested induction|4EQPCHKEBH]]. Lemmas proved by induction on one variable are used inside the main induction on the other variable.
4. The [[factorial formula for binomial coefficients|N10HP9QWX7]] is proved by induction on the top index $n$, with a statement for all $k$ at each $n$.
5. The [[proof of Ramsey's theorem by induction on r + s|1VP19TWGTB]] bounds a function of two variables by induction on the sum.

### Non-examples

1. An [[induction along the diagonal|NF8SZ82JAC]] proves $P(n, n)$ for each $n$, and nothing about the pairs $(m, n)$ with $m \neq n$. Its steps move from $(n, n)$ to $(n + 1, n + 1)$, so they never leave the diagonal.
2. An induction on $m$ with a fixed value $n_0$ proves $P(m, n_0)$ for every $m$. It proves nothing about $P(m, n)$ for the other values of $n$.

### Basic properties

1. A nested induction is valid, because it is two ordinary inductions. The inner inductions prove $Q(0)$ and the implication $Q(m) \Rightarrow Q(m + 1)$, and the outer induction then gives $Q(m)$ for every $m$.
2. An induction on the sum is valid. Each pair $(m, n)$ has a sum $s = m + n$, and the induction on $s$ proves every case with that sum.
3. The lexicographic order on $\mathbb{N} \times \mathbb{N}$ is a well-order. Let $X$ be a nonempty set of pairs. By the [[well-ordering principle|01BX15HSRR]], the first coordinates of the pairs in $X$ have a least value $m_0$. The second coordinates of the pairs in $X$ with first coordinate $m_0$ have a least value $n_0$, and $(m_0, n_0)$ is the least element of $X$.
4. So lexicographic induction is valid. Suppose that each $P(m, n)$ follows from all $P(m', n')$ with $(m', n') <_{\mathrm{lex}} (m, n)$, and that the set $X$ of pairs where $P$ fails is nonempty. All pairs below the least element $(m_0, n_0)$ of $X$ satisfy $P$, so $P(m_0, n_0)$ holds, which is a contradiction.
5. The lexicographic order is not a copy of the order of $\mathbb{N}$. The pair $(1, 0)$ has infinitely many smaller pairs $(0, n)$, so no induction that counts $0, 1, 2, \ldots$ visits the pairs in this order.
6. Prefix induction is a related method for one variable. It proves $P(0)$, and for each $k$ it proves that $P(k)$ implies $P(2k)$ and $P(2k + 1)$. It is valid by strong induction, because each $n \ge 1$ equals $2k$ or $2k + 1$ with $k = \lfloor n/2 \rfloor < n$.
7. Prefix induction reaches $n$ after as many steps as $n$ has binary digits. For example, $100$ has $7$ binary digits, and the chain of prefixes is $1, 3, 6, 12, 25, 50, 100$.

### History

Wilhelm Ackermann published his function in 1928, and nested induction is the standard way to prove that its recursion gives a value for every pair.
The two-variable form that most books use today is due to Rózsa Péter and Raphael Robinson.
The proof of the commutativity of addition from the [[Peano axioms|0QFT7Z76N5]] is the classical example of a nested induction.

### Common errors

1. A student moves both variables at once, from $(n, n)$ to $(n + 1, n + 1)$. This proves the statement only on the diagonal.
2. A student fixes $n$ in the outer induction hypothesis. Then the step cannot use the hypothesis at another value of $n$, and the proof for the Ackermann function fails.
3. In an induction on $m + n$ whose step uses $(m - 1, n)$ and $(m, n - 1)$, a student forgets the boundary cases $m = 0$ and $n = 0$, where one of these pairs does not exist.

## Explanations

### L1 human

Think of a table with infinitely many rows and columns, and one claim in each cell.
To prove all the claims, we need an order in which every cell comes after the cells that it depends on.
One way is to go row by row, and inside each row, cell by cell.
Another way is to go along the diagonals where the row number plus the column number is $0$, then $1$, then $2$, and so on.
For example, the cell in row $2$ and column $3$ lies on diagonal $5$, and we reach it after all the cells of diagonal $4$.

### L2 human

Let $h(m, n)$ be defined by $h(m, 0) = 1$, $h(0, n) = 1$, and $h(m, n) = h(m - 1, n) + h(m, n - 1)$ for $m, n \ge 1$.
We prove $h(m, n) \le 2^{m + n}$ for all natural numbers $m$ and $n$, by induction on $s = m + n$.

1. Let $R(s)$ be the claim "$h(m, n) \le 2^{m + n}$ for all $m, n$ with $m + n = s$".
2. Base case $s = 0$: the only pair is $(0, 0)$, and $h(0, 0) = 1 = 2^0$.
3. Step: let $s \ge 1$, assume $R(s - 1)$, and let $m + n = s$.
4. If $m = 0$ or $n = 0$, then $h(m, n) = 1 \le 2^s$ by the definition.
5. If $m, n \ge 1$, then $(m - 1, n)$ and $(m, n - 1)$ have the sum $s - 1$. By $R(s - 1)$, both values are at most $2^{s - 1}$.
6. So $h(m, n) \le 2^{s - 1} + 2^{s - 1} = 2^s$. This proves $R(s)$.
7. By induction on $s$, $R(s)$ holds for every $s$. Each pair $(m, n)$ is covered by $R(m + n)$.

For example, $h(2, 2) = 6 \le 16$, and in fact $h(m, n) = \binom{m + n}{m}$ by the [[lattice path example|HPB4XV5ACB]].
The typical use of double induction is a recursion in two variables, from combinatorics or from the theory of computable functions.
A trap is step 4: the formula of the step does not apply on the boundary, so the boundary pairs need their own argument.

### L3 human

Double induction is the case $\mathbb{N} \times \mathbb{N}$ of induction over a [[well-founded relation|0DQPNJNPYK]].
The lexicographic order on $\mathbb{N}^k$ is a well-order of order type $\omega^k$, so lexicographic induction on $k$ counters is a case of [[transfinite induction|0ZHQMQ2C1N]].
The product order, in which $(m', n') \le (m, n)$ means $m' \le m$ and $n' \le n$, is also well-founded, and induction on $m + n$ is one way to use it.
In computer science, a recursive program stops on every input when each recursive call decreases a measure in a well-founded order, and the Ackermann function is the standard example of a lexicographic measure.
The same function shows the reach of the method: it is not [[primitive recursive|97QF3KHSBY]], so a recursion on one counter at a time does not produce it.
The later pages on [[structural induction|12MQ2NJ29A]] and [[induction on size|B2D8PTFNN1]] treat induction over other well-founded orders.
