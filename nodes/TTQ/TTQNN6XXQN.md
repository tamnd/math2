---
tag: TTQNN6XXQN
kind: example
name: Combinatorial proof that k C(n, k) = n C(n - 1, k - 1)
msc: ["00A35", "05A19"]
topics: [GB14W4SYPK]
audience: ug1
instance_of: [SS07J9ZAQ7]
uses: [SS07J9ZAQ7, 0GBZM0MT0F, 0VPK4X73Q0]
sources:
  - url: https://en.wikipedia.org/wiki/Combinatorial_proof
    locator: lead section
---

## Example

Let $n$ and $k$ be integers with $1 \le k \le n$.
We prove
$$k\binom{n}{k} = n\binom{n-1}{k-1}$$
by a [[combinatorial proof|SS07J9ZAQ7]]: both sides count the same set.

1. Let $S$ be the set of pairs $(A, c)$, where $A$ is a subset of $[n] = \{1, \dots, n\}$ with $k$ elements and $c$ is an element of $A$.
   Think of $A$ as a committee and of $c$ as its chair.
2. First count: choose $A$, then $c$.
   There are $\binom{n}{k}$ choices of $A$, and for each of them $k$ choices of $c$ in $A$.
3. Each pair in $S$ arises from exactly one such pair of choices, so the [[rule of product|0VPK4X73Q0]] gives $|S| = k\binom{n}{k}$.
4. Second count: choose $c$, then the other members.
   There are $n$ choices of $c$ in $[n]$.
5. For each $c$, the set $A \setminus \{c\}$ is a subset of $[n] \setminus \{c\}$ with $k - 1$ elements, and each such subset gives exactly one $A$, so there are $\binom{n-1}{k-1}$ choices.
6. Each pair in $S$ arises from exactly one such pair of choices, so $|S| = n\binom{n-1}{k-1}$.
7. Steps 3 and 6 count the same set $S$, so $k\binom{n}{k} = n\binom{n-1}{k-1}$.
8. Check with $n = 4$ and $k = 2$: there are $6$ committees of size $2$, each with $2$ choices of chair, so $|S| = 12$, and $4\binom{3}{1} = 12$.

## Remarks

The example shows double counting in its plainest form: one set, and two orders for the same two choices.
The proof uses only the meaning of $\binom{n}{k}$ as a number of subsets, and never the factorial formula.
For $n = 5$ and $k = 2$, both sides equal $20$.

If you allow committees of every size, the same set proves $\sum_{k} k\binom{n}{k} = n 2^{n-1}$.
The identity also gives $\binom{n}{k} = \frac{n}{k}\binom{n-1}{k-1}$, and repeated use of it gives the factorial formula:
$$\binom{n}{k} = \frac{n}{k} \cdot \frac{n-1}{k-1} \cdots \frac{n-k+1}{1} = \frac{n!}{k!\,(n-k)!}.$$
The [[algebraic proof of the same identity|RSYQ7GQMX6]] goes the other way, from the factorial formula.

## Explanations

### L1 human

A club has $n$ members and wants a committee of $k$ members, one of whom is the chair.
One way to choose is to pick the committee, then pick the chair from it.
Another way is to pick the chair first, then the $k - 1$ other members from the rest of the club.
Both ways produce the same list of possible committees with chairs.
So the two counts are equal, and this is the identity.

### L2 human

Here is the set $S$ for $n = 4$ and $k = 2$, with both counts visible.
The committees are
$$\{1,2\},\ \{1,3\},\ \{1,4\},\ \{2,3\},\ \{2,4\},\ \{3,4\},$$
so there are $\binom{4}{2} = 6$, and each has $2$ choices of chair, which gives $6 \cdot 2 = 12$ pairs.
Now group the $12$ pairs by the chair.
With chair $1$, the other member is $2$, $3$ or $4$, which is $3 = \binom{3}{1}$ pairs, and the same holds for each of the $4$ chairs, which gives $4 \cdot 3 = 12$ pairs.
The typical use is a product of a binomial coefficient and a factor, where the factor is a choice of one special element.
Watch out: if the chair is chosen from all $n$ people in step 2, the chair need not be on the committee, and the count becomes $n\binom{n}{k}$.
