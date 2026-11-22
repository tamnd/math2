---
tag: SBC0RA543V
kind: example
name: The average number of fixed points of a permutation is 1
msc: ["05A19", "05A05"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [0F8YBHF2W3]
uses: [0F8YBHF2W3, 05RWFKVTJ7, N8YF97HHQ5]
sources:
  - url: https://en.wikipedia.org/wiki/Double_counting_(proof_technique)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Fixed_point_(mathematics)
    locator: lead section
---

## Example

Let $n \geq 1$, and let $S_n$ be the set of all [[permutations|05RWFKVTJ7]] of $\{1, \dots, n\}$.
A fixed point of $\sigma \in S_n$ is an element $i$ with $\sigma(i) = i$, and $\operatorname{fix}(\sigma)$ is the number of fixed points of $\sigma$.
We show by [[double counting|0F8YBHF2W3]] that
$$\sum_{\sigma \in S_n} \operatorname{fix}(\sigma) = n!,$$
so the mean number of fixed points over the $n!$ permutations is $1$.

1. Let $R$ be the set of pairs $(\sigma, i)$ with $\sigma \in S_n$, $i \in \{1, \dots, n\}$ and $\sigma(i) = i$.
2. Count $R$ by permutations.
   For a fixed $\sigma$, the number of $i$ with $(\sigma, i) \in R$ is $\operatorname{fix}(\sigma)$, so $|R| = \sum_{\sigma \in S_n} \operatorname{fix}(\sigma)$.
3. Count $R$ by points.
   For a fixed $i$, the permutations with $\sigma(i) = i$ are the permutations of the other $n - 1$ points, and by the [[count of permutations that fix given points|N8YF97HHQ5]] there are $(n - 1)!$ of them.
4. So $|R| = n \cdot (n - 1)! = n!$.
5. Steps 2 and 4 give $\sum_{\sigma} \operatorname{fix}(\sigma) = n!$, and division by $|S_n| = n!$ gives the mean $1$.
6. Check with $n = 3$.
   The identity has $3$ fixed points, the three transpositions $(1\,2)$, $(1\,3)$, $(2\,3)$ have $1$ each, and the two $3$-cycles have none, so the total is $3 + 3 + 0 = 6 = 3!$.

## Remarks

Double counting can compute a sum whose terms are hard to find one by one.
The number of permutations with exactly $k$ fixed points needs the count of [[derangements|0TH61JR04G]], but the sum over all permutations needs only step 3.

The answer does not depend on $n$.
For $n = 4$, the identity gives $4$, the $6$ transpositions give $2$ each, the $8$ permutations that are $3$-cycles give $1$ each, and the other $9$ permutations give $0$:
$$4 + 6 \cdot 2 + 8 \cdot 1 + 9 \cdot 0 = 24 = 4!.$$
If you count pairs $(\sigma, \{i, j\})$ of two fixed points instead, the same method gives
$$\sum_{\sigma \in S_n} \binom{\operatorname{fix}(\sigma)}{2} = \binom{n}{2} (n - 2)! = \frac{n!}{2} \qquad (n \geq 2).$$
Check with $n = 4$: the identity gives $\binom{4}{2} = 6$ and each transposition gives $1$, so the sum is $12 = 24/2$.

## Explanations

### L1 human

Shuffle $3$ cards numbered $1$, $2$, $3$, and look at how many cards stay in their old place.
There are $6$ ways to order the cards.
If we add up the cards that stay in place over all $6$ orders, we get $3 + 1 + 1 + 1 + 0 + 0 = 6$.
We can also count card by card: each card stays in place in $2$ of the $6$ orders, so the total is $3 \times 2 = 6$.
So on average, exactly $1$ card stays in its place.

### L2 human

The same method finds the average number of $2$-cycles of a permutation in $S_4$.
Let $R$ be the set of pairs $(\sigma, \{i, j\})$ where $\sigma$ swaps $i \neq j$, which means $\sigma(i) = j$ and $\sigma(j) = i$.
Count by the pairs $\{i, j\}$ first.
There are $\binom{4}{2} = 6$ of them, and for each, $\sigma$ swaps $i$ and $j$ and permutes the other $2$ points in $2! = 2$ ways, so $|R| = 6 \cdot 2 = 12$.
Now count by permutations.
The $6$ transpositions have one $2$-cycle each, the $3$ permutations such as $(1\,2)(3\,4)$ have two each, and the other $15$ permutations have none, so $|R| = 6 + 6 = 12$.
The counts agree, and the mean number of $2$-cycles is $12 / 24 = \tfrac{1}{2}$.
The typical use is to find the mean of a statistic over all objects of one size.
Watch out in the first count: the swap of $i$ and $j$ is fixed, but the other points move freely, so the factor is $(n - 2)!$ and not $1$.

### L3 human

In the language of probability, $\operatorname{fix}(\sigma)$ is the sum of the indicator variables of the events $\sigma(i) = i$, and each event has probability $1/n$.
Linearity of [[expectation|0WQNRCNY3M]] gives the mean $n \cdot (1/n) = 1$, and this computation is the same double count.
[[Burnside's lemma|0Z47M1B2VS]] is the version of this count for a group acting on a set: the mean number of fixed points of the group elements is the number of orbits.
For the action of $S_n$ on $\{1, \dots, n\}$ there is one orbit, which gives the mean $1$ again.
