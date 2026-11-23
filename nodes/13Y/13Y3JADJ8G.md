---
tag: 13Y3JADJ8G
kind: proof
name: Cutting-planes refutation of the pigeonhole formulas by counting
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
proves: 40KJ0VKNG7
uses: [6RA1FTFWYR, KKCX2HQP2K, RJ571F7FF0]
methods: [01XM7JEKHY, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Proof systems
---

## Proof

We build the refutation in the [[cutting-planes system|KKCX2HQP2K]] in three stages, and then we count its lines and the bits of its numbers.
We write $\sum a_i x_i \leq \gamma$ for the line $\sum (-a_i) x_i \geq -\gamma$, as in the definition.

1. The pigeon clause of pigeon $i$ becomes the line $P_i \colon \sum_{j=1}^n x_{ij} \geq 1$.
2. The hole clause $\neg x_{ij} \vee \neg x_{kj}$ becomes $(1 - x_{ij}) + (1 - x_{kj}) \geq 1$, which is the line $x_{ij} + x_{kj} \leq 1$.

Stage one fixes a hole $j$ and derives, for $k = 1, \dots, n + 1$, the line
$$H_k \colon \sum_{i=1}^{k} x_{ij} \leq 1.$$

3. $H_1$ is $x_{1j} \leq 1$, which is a Boolean axiom.
4. Let $1 \leq k \leq n$ and suppose that $H_k$ is derived.
   Linear combination with weight $k - 1$ gives the following line:
   $$(k - 1) \sum_{i=1}^{k} x_{ij} \leq k - 1.$$
5. The $k$ hole axioms $x_{ij} + x_{k+1, j} \leq 1$ for $i = 1, \dots, k$ have this sum:
   $$\sum_{i=1}^{k} x_{ij} + k \, x_{k+1, j} \leq k.$$
6. The sum of the lines of steps 4 and 5 has the coefficient $k$ on every variable:
   $$k \sum_{i=1}^{k+1} x_{ij} \leq 2k - 1.$$
7. Since $k$ divides every coefficient, the division rule applies with $c = k$.
   It gives $\sum_{i=1}^{k+1} x_{ij} \leq \lfloor (2k - 1)/k \rfloor$, and $\lfloor 2 - 1/k \rfloor = 1$ because $1 \leq 2 - 1/k < 2$.
   This line is $H_{k+1}$.
8. By [[induction|0ASJVEFA9J]] on $k$, we reach $H_{n+1}$.
   Call it $Q_j \colon \sum_{i=1}^{n+1} x_{ij} \leq 1$.
   For $k = 2$, steps 4 to 7 are [[the cut for three pairwise exclusions|6RA1FTFWYR]].

Stage two adds the hole lines, and stage three adds the pigeon lines.

9. The sum of $Q_1, \dots, Q_n$ is $\sum_{i,j} x_{ij} \leq n$, because each variable $x_{ij}$ occurs in exactly one line, namely $Q_j$.
10. The sum of $P_1, \dots, P_{n+1}$ is $\sum_{i,j} x_{ij} \geq n + 1$, because each variable $x_{ij}$ occurs in exactly one line, namely $P_i$.
11. The sum of the lines of steps 9 and 10 cancels every variable and leaves $0 \geq (n + 1) - n$, which is $0 \geq 1$.

Now we count the lines.

12. The passage from $H_k$ to $H_{k+1}$ writes one line in step 4, $k$ axioms and $k - 1$ partial sums in step 5, and one line each in steps 6 and 7.
   That is $2k + 2$ lines.
13. One hole needs at most this many lines:
   $$1 + \sum_{k=1}^{n} (2k + 2) = 1 + n(n + 1) + 2n = n^2 + 3n + 1.$$
14. All $n$ holes need at most $n(n^2 + 3n + 1)$ lines, and steps 9 to 11 add $(n - 1) + (n + 1) + n + 1 = 3n + 1$ lines.
   So the length is $O(n^3)$.

Last, we bound the size.

15. In stage one every coefficient is at most $k \leq n$ in absolute value, and every constant is at most $2k - 1 \leq 2n - 1$.
16. In stages two and three every coefficient is $-1$, $0$ or $1$, and every constant is at most $n + 1 \leq 2n$ in absolute value.
17. So each number has $O(\log n)$ bits, and a line on the $n(n+1)$ variables has $O(n^2 \log n)$ bits.
   With $O(n^3)$ lines the size is $O(n^5 \log n)$.

The formula $\mathrm{PHP}^{n+1}_n$ has $\Theta(n^3)$ literals, so the refutation has length $O(n^3)$ and polynomial size, which proves the theorem.

## Idea

The refutation counts pigeons twice.
The clauses only say that no two pigeons share a hole, so we first turn them into the statement that each hole holds at most one pigeon.
That takes an induction on the number of pigeons, with one division per step, and each division throws away a fraction below $1$.
Then the holes say that at most $n$ pigeons are placed, the pigeons say that at least $n + 1$ are placed, and one addition finishes.

## Variants

For $\mathrm{PHP}^m_n$ with $m > n + 1$, the same refutation works with the hole lines for the first $n + 1$ pigeons and the pigeon lines of those $n + 1$ pigeons only.

A single division cannot replace the induction.
The sum of all hole axioms of hole $j$ is $n \sum_{i} x_{ij} \leq \binom{n+1}{2}$, and division by $n$ gives only $\sum_i x_{ij} \leq \lfloor (n+1)/2 \rfloor$.
That bound is at least $2$ once $n \geq 3$, so it is too weak for the final count.

Cook, Coullard and Turán gave a refutation of this kind in 1987, when they introduced cutting planes as a proof system.
