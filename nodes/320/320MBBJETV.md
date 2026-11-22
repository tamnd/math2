---
tag: 320MBBJETV
kind: example
name: Average number of divisors of the integers up to n
msc: ["11A25", "00A35"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [HXP9VMXV8S]
uses: [HXP9VMXV8S, 0VV3ZMRF88, 0F8YBHF2W3, 08GR54CKEA, 0NANDX7V02]
sources:
  - url: https://en.wikipedia.org/wiki/Divisor_function
    locator: Approximate growth rate
  - url: https://en.wikipedia.org/wiki/Harmonic_number
    locator: lead section
---

## Example

For a positive integer $k$, let $d(k)$ be the [[number of divisors|0VV3ZMRF88]] of $k$.
Let $n$ be a positive integer, and let $H_n = 1 + \frac{1}{2} + \cdots + \frac{1}{n}$ be the $n$-th [[harmonic number|0NANDX7V02]].
We prove by an [[averaging argument|HXP9VMXV8S]] that some $k$ with $1 \le k \le n$ has $d(k) > H_n - 1$.

1. The family is the set $\{1, \ldots, n\}$, and the score of $k$ is $d(k)$.
2. The sum $\sum_{k=1}^{n} d(k)$ counts the pairs $(j, k)$ with $1 \le j, k \le n$ and $j \mid k$, because $d(k)$ counts the $j$ that go with a fixed $k$.
3. We count the same pairs by $j$, which is [[double counting|0F8YBHF2W3]].
   For a fixed $j$, the multiples of $j$ up to $n$ are $j, 2j, \ldots, \lfloor n/j \rfloor j$, and there are $\lfloor n/j \rfloor$ of them.
4. So, with the [[floor function|08GR54CKEA]],
   $$\sum_{k=1}^{n} d(k) = \sum_{j=1}^{n} \left\lfloor \frac{n}{j} \right\rfloor.$$
5. For each $j$, the definition of the floor function gives $\lfloor n/j \rfloor > n/j - 1$.
6. Add these $n$ inequalities:
   $$\sum_{j=1}^{n} \left\lfloor \frac{n}{j} \right\rfloor > \sum_{j=1}^{n} \left(\frac{n}{j} - 1\right) = n H_n - n.$$
7. Divide by $n$: the average of $d(k)$ over $1 \le k \le n$ is greater than $H_n - 1$.
8. By the averaging argument, some $k \le n$ has $d(k)$ at least the average, so $d(k) > H_n - 1$.

We check the case $n = 12$.

1. The values $d(1), \ldots, d(12)$ are $1, 2, 2, 3, 2, 4, 2, 4, 3, 4, 2, 6$, with sum $35$.
2. The values $\lfloor 12/j \rfloor$ for $j = 1, \ldots, 12$ are $12, 6, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1$, with sum $35$ as well, as step 4 says.
3. The average is $35/12 \approx 2.92$, and $H_{12} - 1 \approx 2.10$, so step 7 holds.
4. Some $k \le 12$ has $d(k) \ge 35/12$, so $d(k) \ge 3$ since $d(k)$ is an integer.
   Indeed $d(4) = 3$, and $d(12) = 6$ is larger.

## Remarks

The single values $d(k)$ are irregular: $d(k) = 2$ for every prime $k$, and $d(12) = 6$.
Their sum is regular, because the count by $j$ replaces the irregular values by the smooth values $\lfloor n/j \rfloor$.
So an average can be computed exactly when no single value is easy to predict.

The bound grows with $n$.
Since $H_n > \ln n$, the average number of divisors up to $n$ is greater than $\ln n - 1$, so some integers have many divisors.
For $n = 100$, the sum is $482$, the average is $4.82$, and $H_{100} - 1 \approx 4.19$.
The largest value up to $100$ is $12$, at $k = 60$ for example, so the maximum is far above the average.

## Explanations

### L1 human

The number $12$ has six divisors: $1, 2, 3, 4, 6, 12$.
The number $7$ has only two: $1$ and $7$.
If you list the divisors of every number from $1$ to $12$, you write $35$ divisors in total.
So the numbers have about three divisors each on average, and at least one of them has three divisors or more.
You can find the total $35$ without listing the divisors: $12$ numbers are multiples of $1$, $6$ are multiples of $2$, $4$ are multiples of $3$, and so on.

### L2 human

We compute the average number of divisors up to $n = 10$ by the count of step 4.
The values $\lfloor 10/j \rfloor$ for $j = 1, \ldots, 10$ are $10, 5, 3, 2, 2, 1, 1, 1, 1, 1$, so
$$\sum_{k=1}^{10} d(k) = 10 + 5 + 3 + 2 + 2 + 1 + 1 + 1 + 1 + 1 = 27.$$
The average is $2.7$, so some $k \le 10$ has $d(k) \ge 3$.
Check: $d(1), \ldots, d(10)$ are $1, 2, 2, 3, 2, 4, 2, 4, 3, 4$, and their sum is $27$.

The same count is the first step toward the average order of $d(k)$ in number theory, which is close to $\ln n$.
Watch out: the average is not a typical value.
For large $n$, most integers up to $n$ have far fewer than $\ln n$ divisors, and a few integers with many divisors raise the average.
The [[Hardy-Ramanujan theorem|ZJNW10PZKK]] makes the idea of a typical integer precise for the number of prime factors.
