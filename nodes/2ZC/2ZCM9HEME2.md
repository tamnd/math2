---
tag: 2ZCM9HEME2
kind: example
name: The multiples of 6 by double inclusion
msc: ["00A35", "11A05"]
topics: [MEKKHHQTKB]
audience: school
instance_of: [MKHVRNW68H]
uses: [MKHVRNW68H, 0PG2H7WKGG, 0ZNMMA9TF5]
sources:
  - url: https://en.wikipedia.org/wiki/Subset
    locator: lead section
  - book: isbn:9781108439534
    locator: Chapter 3
---

## Example

For an integer $m$, write $m\mathbb{Z} = \{ mk : k \in \mathbb{Z} \}$ for the set of integer multiples of $m$, so $n \in m\mathbb{Z}$ means that $m$ [[divides|0PG2H7WKGG]] $n$.
We prove
$$6\mathbb{Z} = 2\mathbb{Z} \cap 3\mathbb{Z}$$
by [[double inclusion|MKHVRNW68H]].

1. ($\subseteq$) Let $n \in 6\mathbb{Z}$, so $n = 6k$ for some integer $k$.
2. Then $n = 2(3k)$ with $3k$ an integer, so $n \in 2\mathbb{Z}$.
   Also $n = 3(2k)$ with $2k$ an integer, so $n \in 3\mathbb{Z}$.
3. So $n$ lies in the [[intersection|0ZNMMA9TF5]] $2\mathbb{Z} \cap 3\mathbb{Z}$, and $6\mathbb{Z} \subseteq 2\mathbb{Z} \cap 3\mathbb{Z}$.
4. ($\supseteq$) Let $n \in 2\mathbb{Z} \cap 3\mathbb{Z}$, so $n = 2a$ and $n = 3b$ for some integers $a$ and $b$.
5. We write $n$ as $3n - 2n$ and replace $n$ by a different form in each term:
   $$n = 3n - 2n = 3(2a) - 2(3b) = 6a - 6b = 6(a - b).$$
6. Since $a - b$ is an integer, $n \in 6\mathbb{Z}$.
   So $2\mathbb{Z} \cap 3\mathbb{Z} \subseteq 6\mathbb{Z}$, and with step 3 the two sets are equal.

Check: $n = 18$ has $a = 9$ and $b = 6$, and step 5 gives $6(9 - 6) = 18$.

## Remarks

The two halves have very different difficulty.
The half $\subseteq$ only regroups a product, while the half $\supseteq$ needs the idea $n = 3n - 2n$.
That idea works because $3 \cdot 1 + 2 \cdot (-1) = 1$, a [[Bézout identity|0DQVHMYAGA]] for the [[coprime integers|0VZ48N083F]] $2$ and $3$.

The same proof gives $m\mathbb{Z} \cap n\mathbb{Z} = mn\mathbb{Z}$ whenever $m$ and $n$ are coprime.
Write $1 = mu + nv$; then an $x$ that is a multiple of $m$ and of $n$ satisfies $x = mux + nvx$, and each of the two terms is a multiple of $mn$.

Without coprimality only one inclusion survives.
For $m = 4$ and $n = 6$ we still have $24\mathbb{Z} \subseteq 4\mathbb{Z} \cap 6\mathbb{Z}$, but $12 = 4 \cdot 3 = 6 \cdot 2$ lies in the intersection and not in $24\mathbb{Z}$.
The correct law is $m\mathbb{Z} \cap n\mathbb{Z} = \ell\mathbb{Z}$, where $\ell$ is the [[least common multiple|09S5SN35DJ]] of $m$ and $n$; for $4$ and $6$ it gives $12\mathbb{Z}$.

## Explanations

### L1 human

The claim is that a whole number is a multiple of $6$ exactly when it is even and also a multiple of $3$.
One direction is easy, because $6$ times a number is $2$ times something and $3$ times something.
The other direction needs a trick.
Take $18 = 2 \cdot 9 = 3 \cdot 6$ and write $18 = 3 \cdot 18 - 2 \cdot 18 = 54 - 36$.
Both $54 = 6 \cdot 9$ and $36 = 6 \cdot 6$ are multiples of $6$, so their difference $18$ is one too.

### L2 human

We try the same method on the false claim $4\mathbb{Z} \cap 6\mathbb{Z} = 24\mathbb{Z}$.

1. ($\supseteq$) If $n = 24k$, then $n = 4(6k) = 6(4k)$, so $24\mathbb{Z} \subseteq 4\mathbb{Z} \cap 6\mathbb{Z}$.
2. ($\subseteq$) To repeat the trick we need integers $u$ and $v$ with $4u + 6v = 1$.
3. No such integers exist, because $4u + 6v$ is always even.
4. Since the trick fails, we look for an element of the intersection outside $24\mathbb{Z}$, and $12$ is one.
5. So the claim is false, and only the inclusion of step 1 holds.

Double inclusion with numbers is the usual way to compute an intersection or a sum of ideals, such as $m\mathbb{Z} + n\mathbb{Z} = d\mathbb{Z}$ with $d = \gcd(m, n)$.
Watch out: stopping after the easy half would never have found the error.
