---
tag: 0XCYGCCX8V
kind: statement
role: theorem
name: Number of elements of each order in a cyclic group
msc: ["20K01", "11A25"]
topics: [BAVE5RN4EE]
audience: ug1
about: [0KVGH0J5B3, 0WE2NHZJ7B, 0DAMHCT17R]
uses: [0KVGH0J5B3, 0WE2NHZJ7B, 0DAMHCT17R, 0PG2H7WKGG, 0423TXR9AN, 0VVPQNVM8S, 08V7JHS3QZ]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_group
    locator: Additional properties
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Divisor sum
  - book: isbn:9781305657960
    locator: Chapter 4
---

## Statement

Let $n$ be a positive integer.
Let $\varphi$ be [[Euler's totient function|0DAMHCT17R]]: for $d \geq 1$, $\varphi(d)$ is the number of integers $k$ with $1 \leq k \leq d$ and $\gcd(k, d) = 1$.

1. (Elements of each order.) Let $C = \langle c \rangle$ be a [[cyclic group|0KVGH0J5B3]] of order $n$, and let $d$ be a positive integer. If $d$ [[divides|0PG2H7WKGG]] $n$, then $C$ has exactly $\varphi(d)$ elements of [[order|0WE2NHZJ7B]] $d$. They are the elements $c^{kn/d}$ with $1 \leq k \leq d$ and $\gcd(k, d) = 1$. If $d$ does not divide $n$, then $C$ has no element of order $d$.
2. (Totient sum.) $\sum_{d \mid n} \varphi(d) = n$, where the sum runs over the positive divisors $d$ of $n$.
3. (Cyclicity criterion.) Let $G$ be a finite group of order $n$, with identity $e$. Suppose that for each positive divisor $d$ of $n$, the set $\set{x \in G : x^d = e}$ has at most $d$ elements. Then $G$ is cyclic.

## Remarks

### Why each hypothesis is needed

1. Part 1 needs a cyclic group. The [[Klein four-group|0PMRQJVTME]] has order $4$ and three elements of order $2$, but $\varphi(2) = 1$.
2. Part 1 needs a finite group for the count to make sense. In the infinite cyclic group $\Z$, only $0$ has finite order.
3. Part 3 needs the bound for each divisor $d$. In the Klein four-group, the bound holds for $d = 1$ and $d = 4$. It fails for $d = 2$, because all $4$ elements satisfy $x^2 = e$. The group is not cyclic.
4. Part 3 needs a finite group. In $(\Q, +)$, the equation $dx = 0$ with $d \geq 1$ has only the solution $x = 0$. So the bound holds for every $d \geq 1$, but $\Q$ is not cyclic.

### Consequences

1. A cyclic group of order $n$ has exactly $\varphi(n)$ generators. For example, $\Z/12$ has the $4$ generators $1, 5, 7, 11$.
2. In $\Z/12$, the numbers of elements of orders $1, 2, 3, 4, 6, 12$ are $1, 1, 2, 2, 2, 4$. These are $\varphi(1), \varphi(2), \varphi(3), \varphi(4), \varphi(6), \varphi(12)$, and their sum is $12$.
3. In any finite group, the number of elements of order $d$ is a multiple of $\varphi(d)$.
   1. Each element $x$ of order $d$ lies in exactly one cyclic subgroup of order $d$, namely $\langle x \rangle$. Indeed, a cyclic subgroup of order $d$ that contains $x$ contains $\langle x \rangle$, which also has order $d$.
   2. So each element of order $d$ is counted in exactly one cyclic subgroup of order $d$.
   3. Each such subgroup contains exactly $\varphi(d)$ elements of order $d$, by part 1. So the number of elements of order $d$ is $\varphi(d)$ times the number of cyclic subgroups of order $d$.
4. Part 3 is the main step in the proof that [[finite subgroups of the units of a field are cyclic|0CKGBEJX6B]]. There, a polynomial $x^d - 1$ has at most $d$ roots in the field.
5. In particular, the group of units of $\Z/p\Z$ is cyclic for a prime $p$. This gives [[primitive roots modulo a prime|0QTHB6PE52]].

### Converse

The converse of part 3 is true, so part 3 is a criterion.
Let $C$ be cyclic of order $n$, and let $d \mid n$.
Then $x^d = e$ holds exactly when the order of $x$ divides $d$.
By parts 1 and 2, the number of such $x$ is $\sum_{f \mid d} \varphi(f) = d$.
So a cyclic group of order $n$ has exactly $d$ solutions of $x^d = e$ for each $d \mid n$.

### Generalizations

1. A theorem of Frobenius is about any finite group of order $n$. For each $d \mid n$, the number of solutions of $x^d = e$ is a multiple of $d$.
2. A finite group of order $n$ is cyclic if and only if it has at most one subgroup of order $d$ for each $d \mid n$. The proof uses the same count as part 3.
3. Part 2 says that $\varphi * 1 = \mathrm{id}$ in the language of [[Dirichlet convolution|037F589D1D]]. By [[Möbius inversion|07Q4TBTFVB]], $\varphi(n) = \sum_{d \mid n} \mu(d) \, n/d$, where $\mu$ is the [[Möbius function|0FANE7P0DY]].

## Explanations

### L1 human

Take a clock with $6$ hours, where we add hours.
The order of an hour is the number of times we must add it to get back to $0$.
The hour $0$ has order $1$, and the hour $3$ has order $2$.
The hours $2$ and $4$ have order $3$, and the hours $1$ and $5$ have order $6$.
So the counts for the orders $1, 2, 3, 6$ are $1, 1, 2, 2$.
Each count is the number of integers from $1$ to $d$ that have no common factor with $d$ other than $1$.
For example, for $d = 6$ these numbers are $1$ and $5$, so the count is $2$.
The counts add up to $6$, the number of hours.

### L2 human

We count the elements of each order in $C = \Z/12$, with generator $c = 1$.

1. The divisors of $12$ are $1, 2, 3, 4, 6, 12$, and $\varphi$ takes the values $1, 1, 2, 2, 2, 4$ on them.
2. For $d = 4$, the elements of order $4$ are $k \cdot 12/4 = 3k$ with $1 \leq k \leq 4$ and $\gcd(k, 4) = 1$. So $k = 1, 3$, and the elements are $3$ and $9$.
3. For $d = 12$, the elements are $k$ with $1 \leq k \leq 12$ and $\gcd(k, 12) = 1$. These are $1, 5, 7, 11$.
4. For $d = 6$, the elements are $2k$ with $k = 1, 5$, so they are $2$ and $10$.
5. The total is $1 + 1 + 2 + 2 + 2 + 4 = 12$, as part 2 says.

The typical use is to count the generators of a cyclic group, or to prove that a group is cyclic with part 3.
A trap: $\varphi(d)$ counts the elements of order exactly $d$.
For each $d \mid n$, the number of elements $x$ with $x^d = e$ is $d$, because it also counts the elements whose order is a proper divisor of $d$.

### L3 human

Part 2 is an identity of number theory, and part 1 gives it a group proof: sort the elements of $\Z/n$ by their orders.
The [[sum of the totient over the divisors|09JXE6XMCC]] has other proofs, for example by sorting the fractions $k/n$ by their reduced denominators.

Part 3 is the standard tool to prove that a finite group is cyclic without a generator in hand.
It needs only an upper bound on the solutions of $x^d = e$, and in a field this bound comes from the degree of $x^d - 1$.
This is how one proves that the multiplicative group of a finite field is cyclic.
The field argument fails in division rings.
In the quaternions, $x^2 = -1$ has infinitely many solutions, and the [[quaternion group|0NRJGW864D]] of order $8$ is a finite subgroup that is not cyclic.
