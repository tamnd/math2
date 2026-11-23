---
tag: DRH5CFRPR7
kind: example
name: A string of high circuit complexity from the dual weak pigeonhole principle
msc: ["03F30", "68Q06", "68Q15"]
topics: [RA380RWEC0]
audience: research
instance_of: [65K2S22DGZ]
uses: [65K2S22DGZ, HBTQ8ZVSG6, SQXNFGVADX, 2R30KR3Z5G, 4PGX7PHJCK]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_arithmetic
    locator: Theories
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
---

## Example

There are fewer short descriptions than long strings, so some long string has no short description.
If the descriptions are small circuits, that string is hard for circuits.
We carry out this argument with the [[dual weak pigeonhole principle|HBTQ8ZVSG6]] in place of counting, which is the easy direction of a theorem of Jeřábek.

A string $x$ of length $n$ is computed by a [[Boolean circuit|SQXNFGVADX]] $C$ on $\lvert n \rvert$ inputs if $C(u)$ is the $u$-th bit of $x$ for every $u < n$.
Let $n = \lvert a \rvert$ for some $a$, so that $2^n$ exists, and assume $n \ge 32$.
Put $k = \lvert n \rvert$, the number of inputs, and $m = \lfloor n / (4k) \rfloor$, the number of gates.

1. A circuit with exactly $m$ gates is a list of $m$ gates, each with a type of $2$ bits and two pointers to earlier gates or inputs.
   A pointer is a number below $m + k$, so it needs $w = \lvert m + k \rvert$ bits, and the whole code has $m(2 + 2w)$ bits.
2. The code fits into $n - 1$ bits.
   Since $m + k \le n$, we have $w \le k$, and since $k \ge 2$, we have $(1 + k)/(2k) \le 3/4$:
   $$m(2 + 2w) \le \frac{n}{4k}(2 + 2k) = n \cdot \frac{1 + k}{2k} \le \frac{3n}{4} \le n - 1.$$
3. Every circuit with at most $m$ gates computes the same function as one with exactly $m$ gates, whose last gate is the output.
   We add dummy gates, for example the conjunction of the output with itself.
4. Let $e$ map a string $c$ of length $n - 1$ to a string of length $n$.
   It reads the first $m(2 + 2w)$ bits of $c$ as a circuit, evaluates it at $u = 0, \dots, n - 1$, and outputs the $n$ results; an invalid code gives the all-zero string.
5. The map $e$ is polynomial-time, since it evaluates a circuit of size $m \le n$ at $n$ inputs.
6. Apply $\mathrm{dWPHP}(e)$ with $x = 2^{n-1}$ and $y = 1$, so that $\lvert y \rvert = 1$.
   It gives a number $v < 2^n$, a string of length $n$, that is not $e(c)$ for any $c < 2^{n-1}$.
7. If a circuit with at most $m$ gates computed $v$, then by steps 2 and 3 its padded code $c$ would satisfy $e(c) = v$.
   This contradicts step 6, so no circuit with at most $m = \lfloor n/(4\lvert n \rvert) \rfloor$ gates computes $v$.

## Remarks

The example shows how a counting statement turns into a statement about complexity: the pigeonhole principle for the coding map yields a hard truth table.
In the standard numbers the same conclusion follows from [[Shannon's counting argument|2R30KR3Z5G]].
The point is that a weak theory proves it from $\mathrm{dWPHP}(\mathsf{PV})$, without counting the $2^n$ strings.

Check the numbers for $n = 1024$.
Then $k = 11$ and $m = \lfloor 1024/44 \rfloor = 23$, so $w = \lvert 34 \rvert = 6$, and the code has $23 \cdot 14 = 322 \le 1023$ bits.
In general $2^{k-1} \le n < 2^k$, so $m = \lfloor n/(4k) \rfloor$ is exponential in the number $k$ of inputs.

The converse direction is harder.
Jeřábek proved in 2004 that over $S^1_2$, the principle $\mathrm{dWPHP}(\mathsf{PV})$ is equivalent to the existence of Boolean functions with exponential [[circuit complexity|4PGX7PHJCK]].
If we change the constant $4$ in $m$ to a larger one, the codes get shorter and the argument still works, but the bound on the circuit size gets weaker.

## Explanations

### L1 human

A short description can produce only a few different long strings.
There are fewer descriptions with $999$ bits than strings with $1000$ bits.
So some string with $1000$ bits has no description with $999$ bits.
If the descriptions are small circuits, such a string is "hard": no small circuit produces it.
The axiom of approximate counting is exactly what is needed to make this argument in a weak theory.

### L2 human

We count codes for $n = 256$.
Then $k = \lvert 256 \rvert = 9$, the circuits have $9$ inputs, and $m = \lfloor 256/36 \rfloor = 7$ gates.
A pointer is below $m + k = 16$, so $w = \lvert 16 \rvert = 5$, and a code has this many bits:

$$7 \cdot (2 + 2 \cdot 5) = 84.$$

There are $2^{84}$ codes and $2^{256}$ strings of length $256$, so almost all strings have no circuit with $7$ gates.
In the theory, step 6 of the example replaces this count, and $\mathrm{dWPHP}(e)$ gives a hard string directly.

The typical use is to obtain hard functions inside a theory, and then pseudorandom generators built from them.
Watch out: the theory cannot list all strings of length $n$, so the count of $2^{84}$ against $2^{256}$ is not available in it, and $\mathrm{dWPHP}$ takes its place.
