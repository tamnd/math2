---
tag: 3ZDPCTKC9M
kind: example
name: A correct strong induction proof that F_n < 2^n
msc: ["11B39", "97E50"]
topics: [EEH2F76CYQ]
audience: school
not_instance_of:
  - target: V52HDTMPV5
    note: the proof checks both base cases, proves the step for every n from 2 on, and applies the hypothesis only to values in its range, so it contains none of the usual errors
uses: [V52HDTMPV5, 0KMVFSHFGZ, 0GA9K57A39]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Complete (strong) induction
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Example

Let $F_n$ be the [[Fibonacci numbers|0GA9K57A39]]: $F_0 = 0$, $F_1 = 1$ and $F_n = F_{n-1} + F_{n-2}$ for $n \ge 2$.
Claim: $F_n < 2^n$ for every natural number $n$.
We prove it by [[strong induction|0KMVFSHFGZ]], and then check the proof against the list of [[errors in induction proofs|V52HDTMPV5]].

1. Let $P(n)$ be the statement "$F_n < 2^n$".
2. Base case $n = 0$: $F_0 = 0 < 1 = 2^0$.
3. Base case $n = 1$: $F_1 = 1 < 2 = 2^1$.
4. Step: let $n \ge 2$, and assume $P(k)$ for every natural number $k < n$.
5. Since $n \ge 2$, the numbers $n - 1$ and $n - 2$ are natural numbers less than $n$. So $F_{n-1} < 2^{n-1}$ and $F_{n-2} < 2^{n-2}$.
6. By the recursion and step 5, $F_n = F_{n-1} + F_{n-2} < 2^{n-1} + 2^{n-2} = 3 \cdot 2^{n-2}$.
7. Since $3 \cdot 2^{n-2} < 4 \cdot 2^{n-2} = 2^n$, we get $F_n < 2^n$, so $P(n)$ holds.
8. By strong induction, $P(n)$ holds for every $n \ge 0$.

We check the proof against each usual error.

1. Missing base case: both base cases are proved, in steps 2 and 3.
2. Assuming the result: the step starts from the hypothesis on smaller values and ends with $F_n < 2^n$. It never uses $P(n)$ itself.
3. A step that fails for small $n$: the step is used from $n = 2$ on, and at $n = 2$ it uses $P(1)$ and $P(0)$, which are both proved. It gives $F_2 = 1 < 3 < 4$.
4. Too few base cases: the step uses two earlier values, so it needs $n \ge 2$, and the two values below, $0$ and $1$, are both base cases.
5. Leaving the domain: step 5 checks that $n - 1$ and $n - 2$ are natural numbers less than $n$, so the hypothesis applies to them.
6. Wrong variable: the statement has one variable, so this error cannot occur.
7. Building up: the step starts from an arbitrary $n \ge 2$ and reduces it to smaller values, so no case is missed.

## Remarks

1. The second base case is needed. With only $n = 0$ checked, the step at $n = 1$ would need $F_{-1}$, which is not defined, and $P(1)$ would not be covered. This would be the error "too few base cases".
2. The bound is far from sharp. The Fibonacci numbers grow like $\varphi^n$ with $\varphi = \frac{1 + \sqrt{5}}{2} \approx 1.618$, and the same proof gives $F_n < \left(\frac{7}{4}\right)^n$ for $n \ge 1$, because $\frac{4}{7} + \frac{16}{49} = \frac{44}{49} < 1$.
3. The proof uses the hypothesis twice in one step, at $n - 1$ and at $n - 2$. This is why strong induction, or ordinary induction on the pair statement "$P(n)$ and $P(n + 1)$", is needed.
4. The proof would also be correct if it started with ordinary induction on $Q(n)$: "$F_n < 2^n$ and $F_{n+1} < 2^{n+1}$". Then $Q(0)$ contains both base cases.

## Explanations

### L1 human

The Fibonacci numbers start $0, 1, 1, 2, 3, 5, 8, 13$, and each is the sum of the two before it.
The powers of $2$ start $1, 2, 4, 8, 16, 32, 64, 128$, and each is twice the one before it.
Since the sum of the two previous Fibonacci numbers is at most twice the larger one, the Fibonacci numbers cannot catch up with the powers of $2$.
The proof checks the first two numbers by hand, because each later number needs the two numbers before it.

### L2 human

We follow the proof for $n = 2, 3, 4, 5$, using the step each time.

1. $n = 2$: $F_2 = F_1 + F_0 = 1 + 0 = 1$, and the step gives $F_2 < 2 + 1 = 3 < 4$.
2. $n = 3$: $F_3 = 1 + 1 = 2$, and the step gives $F_3 < 4 + 2 = 6 < 8$.
3. $n = 4$: $F_4 = 2 + 1 = 3$, and the step gives $F_4 < 8 + 4 = 12 < 16$.
4. $n = 5$: $F_5 = 3 + 2 = 5$, and the step gives $F_5 < 16 + 8 = 24 < 32$.

Each line uses only the two lines before it, and the first line uses the two base cases.
The typical use of the proof is as a model: for a step that uses $k$ earlier values, check $k$ base cases.
A trap is to check only $F_0 < 1$ and to start the step at $n = 1$.
