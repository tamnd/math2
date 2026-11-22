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
We prove that $F_n < 2^n$ for every natural number $n$ by [[strong induction|0KMVFSHFGZ]], and then we check the proof against the list of [[errors in induction proofs|V52HDTMPV5]].

1. Let $P(n)$ be the statement "$F_n < 2^n$".
2. Base cases.
   We have $F_0 = 0 < 1 = 2^0$ and $F_1 = 1 < 2 = 2^1$.
3. Step.
   Let $n \ge 2$, and assume $P(k)$ for every natural number $k < n$.
4. Since $n \ge 2$, the numbers $n - 1$ and $n - 2$ are natural numbers less than $n$.
   So the assumption gives $F_{n-1} < 2^{n-1}$ and $F_{n-2} < 2^{n-2}$.
5. Use the recursion and step 4:
   $$F_n = F_{n-1} + F_{n-2} < 2^{n-1} + 2^{n-2} = 3 \cdot 2^{n-2} < 4 \cdot 2^{n-2} = 2^n.$$
   So $P(n)$ holds.
6. By strong induction, $P(n)$ holds for every $n \ge 0$.

Now we check the proof against the usual errors.

1. Base cases: the step uses two earlier values, so it needs $n \ge 2$, and the two values below, $0$ and $1$, are both proved in step 2.
2. Assuming the result: the step starts from the hypothesis on smaller values, ends with $F_n < 2^n$, and never uses $P(n)$ itself.
3. The smallest case of the step: at $n = 2$ the step uses $P(1)$ and $P(0)$, which are proved, and gives $F_2 = 1 < 3 < 4$.
4. The domain: step 4 checks that $n - 1$ and $n - 2$ are natural numbers less than $n$, so the hypothesis applies to them.
5. The variable and the direction: the claim has one variable, and the step starts from an arbitrary $n \ge 2$ and reduces it to smaller values, so no case is missed.

## Remarks

The second base case is needed.
With only $n = 0$ checked, the step at $n = 1$ would need $F_{-1}$, which is not defined, and $P(1)$ would not be covered; that is the error of [[too few base cases|32AP5ZDMJJ]].

The step uses the hypothesis twice, at $n - 1$ and at $n - 2$, and that is why strong induction is the natural tool.
Ordinary induction also works if we carry two cases at once, with $Q(n)$: "$F_n < 2^n$ and $F_{n+1} < 2^{n+1}$".
Then $Q(0)$ contains both base cases, and $Q(n)$ gives $Q(n + 1)$ by the same calculation.

The bound is far from sharp.
The Fibonacci numbers grow like $\varphi^n$ with $\varphi = \tfrac{1 + \sqrt{5}}{2} \approx 1.618$, and the same proof gives $F_n < \left(\tfrac74\right)^n$ for every $n$, because
$$\frac47 + \frac{16}{49} = \frac{44}{49} < 1.$$

## Explanations

### L1 human

The Fibonacci numbers start $0, 1, 1, 2, 3, 5, 8, 13$, and each is the sum of the two before it.
The powers of $2$ start $1, 2, 4, 8, 16, 32, 64, 128$, and each is twice the one before it.
A sum of the two previous Fibonacci numbers is at most twice the larger one, so the Fibonacci numbers cannot catch up with the powers of $2$.
The proof checks the first two numbers by hand, because each later number needs the two numbers before it.

### L2 human

We follow the step for $n = 2, 3, 4, 5$, and each time compare $F_n$ with the bound $2^{n-1} + 2^{n-2}$ from step 5 and with $2^n$:
$$F_2 = 1 < 3 < 4, \quad F_3 = 2 < 6 < 8, \quad F_4 = 3 < 12 < 16, \quad F_5 = 5 < 24 < 32.$$
Each case uses only the two cases before it, and the first case uses the two base cases.

Use the proof as a model: for a step that uses $k$ earlier values, check $k$ base cases.
Watch out for the version that checks only $F_0 < 1$ and starts the step at $n = 1$, because that step needs the undefined $F_{-1}$.
