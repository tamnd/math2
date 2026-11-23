---
tag: 2D3GCG17FA
kind: example
name: Erdős's lower bound for Ramsey numbers is a proof
msc: ["05C55", "05D40"]
topics: [DME0TPC348]
audience: ug2
not_instance_of:
  - target: VCQQNJ3SEZ
    note: the argument uses random colorings, but each step is rigorous and the conclusion is certain, so it is a probabilistic proof, not a heuristic
uses: [VCQQNJ3SEZ, 0K9QVPJYJF, SAZNT80CG5, 3B55HNS754]
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey%27s_theorem
    locator: Ramsey numbers
  - url: https://en.wikipedia.org/wiki/Probabilistic_method
    locator: lead section
---

## Example

Color each edge of the complete graph on $32$ vertices red or blue by a coin toss.
The expected number of sets of $10$ vertices whose $45$ edges all have one color is about $0.0000037$, far below $1$.
So some coloring of $K_{32}$ has no such set at all, and this conclusion is certain, not merely likely.

The [[Ramsey number|0K9QVPJYJF]] $R(k, k)$ is the least $n$ such that every red and blue coloring of the edges of $K_n$ contains a $K_k$ with all edges of one color.
Paul Erdős proved in 1947 that $R(k, k) > \lfloor 2^{k/2} \rfloor$ for $k \ge 3$.
His argument uses random colorings, and we check that it is a proof and not a [[heuristic argument|VCQQNJ3SEZ]].

1. Let $n = \lfloor 2^{k/2} \rfloor$, and color each edge of $K_n$ red or blue by an independent fair coin toss.
2. A fixed set of $k$ vertices spans $\binom{k}{2}$ edges, and it is monochromatic when all of them are red or all are blue:
$$P(\text{monochromatic}) = 2 \cdot 2^{-\binom{k}{2}} = 2^{1 - \binom{k}{2}}.$$
3. By linearity of expectation, the expected number of monochromatic $k$-sets is $\binom{n}{k} 2^{1 - \binom{k}{2}}$.
4. We bound this number.
   Since $\binom{n}{k} < n^k / k!$ and $n^k \le 2^{k^2/2}$, we get
$$\binom{n}{k} 2^{1 - \binom{k}{2}} < \frac{2^{k^2/2}}{k!} \cdot 2^{1 - k(k-1)/2} = \frac{2^{1 + k/2}}{k!}.$$
   For $k = 3$ the right side is $2^{2.5}/6 \approx 0.943$, and it decreases as $k$ grows, so it is less than $1$ for every $k \ge 3$.
5. A random variable with values in $\{0, 1, 2, \dots\}$ and expectation below $1$ takes the value $0$ with positive probability.
   So some coloring of $K_n$ has no monochromatic $K_k$, and $R(k, k) > n$.

Every step is a statement about a finite probability space, that is, about a finite sum over the $2^{\binom{n}{2}}$ colorings.
No step assumes that a fixed object behaves like a random one.
So the argument is a proof by the [[probabilistic method|3B55HNS754]], and its conclusion is certain.

## Remarks

### Where the randomness lives

A heuristic and a probabilistic proof often use the same words, and the difference is in what is random.
In the Cramér model of the primes, the primes are fixed, and the model assumes that they behave like random numbers.
That assumption is not proved, so the conclusions of the model are only predictions.
In Erdős's argument the coloring is chosen at random from a finite set that the argument controls completely.
The conclusion is the existence of one good coloring, and it follows by counting.

### What the proof does not give

The proof gives no explicit coloring.
Explicit colorings with no large monochromatic set are much harder to construct, and none known matches the bound $2^{k/2}$.
The [[probabilistic lower bound for diagonal Ramsey numbers|SAZNT80CG5]] states the bound in a sharper form.

### Watch out

The words "with positive probability" in step 5 do not weaken the result.
A finite probability space gives positive probability only to events that contain at least one outcome, so the good coloring exists.
The weak point would be a step that assumes randomness of a fixed object, and the argument has none.

### Try it

For $k = 4$, what does the bound give?
Here $n = \lfloor 2^2 \rfloor = 4$, so $R(4, 4) > 4$; the true value is $R(4, 4) = 18$, so the bound is far from sharp for small $k$.

## Explanations

### L1 human

Draw $n$ dots and join every pair by a line.
Color each line red or blue by tossing a coin.
Now count how many groups of $k$ dots we expect to have all their lines in one color.
If this expected number is less than $1$, then some coloring must have no such group at all, because a count that is always at least $1$ would have average at least $1$.
The argument uses chance, but its conclusion is certain.
That is the difference between a proof that uses probability and a guess based on probability.

### L2 human

We check step 4 for $k = 10$.
Then $n = \lfloor 2^5 \rfloor = 32$, and we need two binomial coefficients:
$$\binom{32}{10} = 64512240, \qquad \binom{10}{2} = 45.$$
The expected number of monochromatic $10$-sets is
$$64512240 \cdot 2^{1 - 45} = 64512240 \cdot 2^{-44} \approx 3.7 \cdot 10^{-6}.$$
This is far below $1$, so some coloring of $K_{32}$ has no monochromatic $K_{10}$, and $R(10, 10) > 32$.
The typical use: an expected number of bad configurations below $1$ proves that an object with none of them exists.
Watch out: the proof shows that the coloring exists, and it does not tell you how to find it.
