---
tag: GMVXG3TBP6
kind: example
name: The successor function in PV
msc: ["03F30"]
topics: [RA380RWEC0]
audience: research
instance_of: [H1B2VD0KVP]
uses: [FMM44KFZQT, H1B2VD0KVP]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Cook's equational theory
---

## Example

Adding $1$ to a number means changing its last digit and perhaps carrying, so it takes one step per digit.
We write numbers in dyadic notation, with $s_1(m) = 2m + 1$ and $s_2(m) = 2m + 2$, as in [[Cook's theory PV|FMM44KFZQT]].
The successor $\mathrm{succ}(y) = y + 1$ is introduced by limited recursion on notation with the equations below.
$$\mathrm{succ}(0) = s_1(0), \qquad \mathrm{succ}(s_1(y)) = s_2(y), \qquad \mathrm{succ}(s_2(y)) = s_1(\mathrm{succ}(y)).$$
We check that this is a legal definition in $\mathsf{PV}$, so that $\mathrm{succ}$ and its equations can be used in a [[feasibly constructive proof|H1B2VD0KVP]].

1. The equations have the form $f(0) = g$ and $f(s_i(y)) = h_i(y, f(y))$, with $g = s_1(0)$, $h_1(y, z) = s_2(y)$ and $h_2(y, z) = s_1(z)$.
   Each of $g$, $h_1$ and $h_2$ is a composition of initial functions.
2. For the bound on $h_1$, take $l_1(y) = s_2(y)$.
   The value $s_2(y)$ is a final segment of the dyadic string $z \frown s_2(y)$, so it is bounded by this concatenation.
3. For the bound on $h_2$, take $l_2(y) = s_1(0)$, the one-digit string $1$.
   Then $h_2(y, z) = s_1(z)$ is exactly the concatenation $z \frown 1$.
4. At $0$ the definition is correct, since $0 + 1 = 1 = s_1(0)$.
5. For $s_1$ it is correct, since $s_1(y) + 1 = 2y + 2 = s_2(y)$ in $\mathbb{N}$.
6. For $s_2$ it is correct, since $s_2(y) + 1 = 2y + 3 = 2(y + 1) + 1 = s_1(y + 1)$ in $\mathbb{N}$.
7. Each equation removes one dyadic digit of $y$, so computing $\mathrm{succ}(y)$ uses at most $\lvert y \rvert + 1$ applications of the equations, where $\lvert y \rvert$ is the number of dyadic digits.

So $\mathrm{succ}$ is a $\mathsf{PV}$ symbol, and steps 4 to 6 show that it computes $y \mapsto y + 1$.

## Remarks

The example shows how recursion on notation handles a carry.
A last digit $1$ becomes $2$ and the work stops, while a last digit $2$ becomes $1$ and the carry moves to the rest of the string.
In binary notation the same definition reads $\mathrm{succ}(2y) = 2y + 1$ and $\mathrm{succ}(2y + 1) = 2 \, \mathrm{succ}(y)$.
Addition and multiplication are defined in the same way, by recursion on the digits of one argument, with bounds of the same kind.

What changes if the recursion runs on the value of $y$ instead of its digits?
The definition $\mathrm{succ}(y) = y + 1$ itself is fine, but a function such as $x \cdot y$ defined by $y$ additions takes $y$ rounds.
That is exponential in $\lvert y \rvert$, and it is not a $\mathsf{PV}$ definition.

## Explanations

### L1 human

Adding $1$ to a number written in digits is done from the right.
If the last digit can grow, it grows, and the work is done.
If not, it resets and $1$ is carried to the next place.
The number of steps is at most the number of digits, so it is fast even for very long numbers.

### L2 human

Let us compute $\mathrm{succ}(10)$ in dyadic notation.
Since $2 \cdot 4 + 2 = 10$, we have $10 = s_2(4)$, and since $2 \cdot 1 + 2 = 4$, we have $4 = s_2(1)$.
Both last digits are $2$, so the third equation carries twice:
$$\mathrm{succ}(10) = s_1(\mathrm{succ}(4)) = s_1(s_1(\mathrm{succ}(1))).$$
Since $1 = s_1(0)$, the second equation stops the carry with $\mathrm{succ}(1) = s_2(0) = 2$.
So $\mathrm{succ}(10) = s_1(s_1(2)) = s_1(5) = 11$.
Check: $10 + 1 = 11$.
Almost every later $\mathsf{PV}$ definition uses the successor as a building block.
Watch out: do not look for a digit $0$, since dyadic notation has only the digits $1$ and $2$, and every even number $n \ge 2$ ends in $2$.
