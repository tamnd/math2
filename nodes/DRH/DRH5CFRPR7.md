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

Jeřábek proved that over $S^1_2$ the principle $\mathrm{dWPHP}(\mathsf{PV})$ is equivalent to the existence of Boolean functions with exponential [[circuit complexity|4PGX7PHJCK]].
We give the easy direction: [[the dual weak pigeonhole principle|HBTQ8ZVSG6]] for one polynomial-time map yields a hard string.
Here a string $x$ of length $n$ is computed by a [[Boolean circuit|SQXNFGVADX]] $C$ on $\abs n$ inputs if $C(u)$ is the $u$-th bit of $x$ for every $u < n$.

1. Let $n = \abs a$ for some $a$, so that $2^n$ exists. Let $m = \floor{n / (2 \abs n)}$.
2. Fix a coding of circuits on $\abs n$ inputs by binary strings. A circuit of size at most $m$ has a code of at most $2m(\abs m + 1)$ bits.
3. For $\abs n \ge 2$ we have $m \le n/4$, so $\abs m \le \abs n - 2$. Hence $2m(\abs m + 1) \le (n / \abs n)(\abs n - 1) \le n - 1$.
4. Pad codes to length $n - 1$ in a fixed decodable way. Let $e$ map a string $c$ of length $n - 1$ to the truth table of the circuit coded by $c$, of length $n$. Invalid codes go to the all-zero string.
5. The map $e$ is polynomial-time: it evaluates a circuit of size at most $n$ on $n$ inputs.
6. $\mathrm{dWPHP}(e)$ gives a string $x$ of length $n$ that is not a value of $e$. The domain has $2^{n-1}$ elements and the target $2^n$; over $S^1_2$ the forms of the principle with different ratios are equivalent.
7. If a circuit of size at most $m$ computed $x$, its code would have at most $n - 1$ bits by step 3, and $e$ would map it to $x$.
8. So $x$ is not computed by any circuit of size at most $m = \floor{n / (2 \abs n)}$.

## Remarks

The example shows how a counting statement becomes a statement about complexity: the pigeonhole principle for the coding map gives a hard truth table.
In $\N$ the same conclusion follows from [[Shannon's counting argument|2R30KR3Z5G]]; the point here is that the theory proves it from $\mathrm{dWPHP}(\mathsf{PV})$.
For $n = 1024$, the circuits have $11$ inputs and $m = 46$, and the codes have at most $92 \cdot 7 = 644 \le 1023$ bits.
The converse direction, from hard functions to $\mathrm{dWPHP}(\mathsf{PV})$, is harder; it is cited here from Jeřábek's paper of 2004.
With hard functions available, Jeřábek formalized the Nisan-Wigderson generator, and with it derandomization arguments, in an extension of $S^1_2 + \mathrm{dWPHP}(\mathsf{PV})$.

## Explanations

### L1 human

A short description can produce only a few different long strings.
There are fewer descriptions with $999$ bits than strings with $1000$ bits.
So some string with $1000$ bits has no description with $999$ bits.
If the descriptions are small circuits, such a string is "hard": no small circuit produces it.
The axiom of approximate counting is exactly what is needed to make this argument in a weak theory.

### L2 human

We count codes for $n = 64$.

1. $\abs{64} = 7$, so the circuits have $7$ inputs, and $m = \floor{64/14} = 4$.
2. A circuit with at most $4$ gates has a code of at most $2 \cdot 4 \cdot (\abs 4 + 1) = 8 \cdot 4 = 32$ bits.
3. There are at most $2^{33}$ codes of at most $32$ bits, and there are $2^{64}$ strings of length $64$.
4. So most strings of length $64$ are computed by no circuit with at most $4$ gates.
5. In the theory, step 6 of the example replaces this count: $\mathrm{dWPHP}(e)$ gives such a string directly.

The typical use is to obtain hard functions inside a theory, and then pseudorandom generators built from them.
A trap is to forget that the theory cannot list all strings of length $n$: the count in step 3 is not available, and $\mathrm{dWPHP}$ takes its place.
