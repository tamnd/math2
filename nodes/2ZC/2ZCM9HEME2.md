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

For an integer $m$, write $m\mathbb{Z} = \{ mk : k \in \mathbb{Z} \}$ for the set of integer multiples of $m$.
So $n \in m\mathbb{Z}$ means that $m$ [[divides|0PG2H7WKGG]] $n$.
We prove
$$6\mathbb{Z} = 2\mathbb{Z} \cap 3\mathbb{Z}$$
by [[double inclusion|MKHVRNW68H]].

1. ($\subseteq$) Let $n$ be an arbitrary element of $6\mathbb{Z}$. Then $n = 6k$ for some integer $k$.
2. We have $n = 2 \cdot (3k)$, and $3k$ is an integer, so $n \in 2\mathbb{Z}$.
3. We have $n = 3 \cdot (2k)$, and $2k$ is an integer, so $n \in 3\mathbb{Z}$.
4. So $n \in 2\mathbb{Z} \cap 3\mathbb{Z}$, by the definition of [[intersection|0ZNMMA9TF5]]. This proves $6\mathbb{Z} \subseteq 2\mathbb{Z} \cap 3\mathbb{Z}$.
5. ($\supseteq$) Let $n$ be an arbitrary element of $2\mathbb{Z} \cap 3\mathbb{Z}$. Then $n = 2a$ and $n = 3b$ for some integers $a$ and $b$.
6. We write $n = 3n - 2n$. This holds for every number $n$.
7. In the term $3n$ we use $n = 2a$, so $3n = 6a$. In the term $2n$ we use $n = 3b$, so $2n = 6b$.
8. So $n = 6a - 6b = 6(a - b)$, and $a - b$ is an integer. Hence $n \in 6\mathbb{Z}$.
9. This proves $2\mathbb{Z} \cap 3\mathbb{Z} \subseteq 6\mathbb{Z}$. With step 4, the two sets are equal.

A check with numbers: $n = 18$ is in $2\mathbb{Z} \cap 3\mathbb{Z}$ with $a = 9$ and $b = 6$, and step 8 gives $18 = 6 \cdot (9 - 6) = 6 \cdot 3$.

## Remarks

1. The two halves have different difficulty. The half $\subseteq$ only regroups a product. The half $\supseteq$ needs an idea, the identity $n = 3n - 2n$.
2. The idea works because $3 - 2 = 1$. In general, $1 = 3 \cdot 1 + 2 \cdot (-1)$ is a [[Bézout identity|0DQVHMYAGA]] for the [[coprime integers|0VZ48N083F]] $2$ and $3$.
3. The same proof shows $mn\mathbb{Z} = m\mathbb{Z} \cap n\mathbb{Z}$ whenever $m$ and $n$ are coprime: write $1 = mu + nv$, and then $x = mux + nvx$, and each term is a multiple of $mn$.
4. Without coprimality only one inclusion survives. For $m = 4$ and $n = 6$ we have $24\mathbb{Z} \subseteq 4\mathbb{Z} \cap 6\mathbb{Z}$, but $12$ is in $4\mathbb{Z} \cap 6\mathbb{Z}$ and not in $24\mathbb{Z}$.
5. The correct general law is $m\mathbb{Z} \cap n\mathbb{Z} = \ell\mathbb{Z}$, where $\ell$ is the [[least common multiple|09S5SN35DJ]] of $m$ and $n$. For $4$ and $6$ this gives $12\mathbb{Z}$.

## Explanations

### L1 human

The claim is that a whole number is a multiple of $6$ exactly when it is both even and a multiple of $3$.
One direction is easy: $6$ times a number is $2$ times something and also $3$ times something.
The other direction needs a trick.
For $18$, which is $2 \cdot 9$ and $3 \cdot 6$, we can write $18 = 3 \cdot 18 - 2 \cdot 18 = 54 - 36$.
Both $54$ and $36$ are multiples of $6$, so their difference $18$ is a multiple of $6$ too.

### L2 human

We test the same method on the claim $4\mathbb{Z} \cap 6\mathbb{Z} = 24\mathbb{Z}$.

1. ($\supseteq$) If $n = 24k$, then $n = 4 \cdot 6k$ and $n = 6 \cdot 4k$. So $24\mathbb{Z} \subseteq 4\mathbb{Z} \cap 6\mathbb{Z}$.
2. ($\subseteq$) We try the trick of the example. We need integers $u$ and $v$ with $4u + 6v = 1$.
3. Such integers do not exist, because $4u + 6v$ is always even.
4. The trick fails, so we look for an element of $4\mathbb{Z} \cap 6\mathbb{Z}$ outside $24\mathbb{Z}$.
5. The number $12 = 4 \cdot 3 = 6 \cdot 2$ is such an element, since $12$ is not a multiple of $24$.
6. So the claim is false, and only the inclusion of step 1 holds.

The typical use of double inclusion with numbers is the computation of an intersection or a sum of ideals, such as $m\mathbb{Z} + n\mathbb{Z} = d\mathbb{Z}$ with $d = \gcd(m, n)$.
A trap is to stop after the easy half, because the easy half does not detect the error of step 6.
