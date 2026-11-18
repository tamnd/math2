---
tag: PXBV25AQM8
kind: example
name: Buss's Frege proofs of the pigeonhole principle are not of bounded depth
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
not_instance_of:
  - target: 41QJ1WEMJ3
    note: the counting formulas in the proofs have depth that grows like log n, so no constant bounds the depth of the whole family
uses: [VRX23FZV21, PE43N5E9PR, 41QJ1WEMJ3, Q0ERK64J78]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Proof_complexity
    locator: Lower bounds
---

## Example

[[Buss's theorem|VRX23FZV21]] gives Frege proofs $\pi_n$ of $\neg \mathrm{PHP}^{n+1}_n$ of size polynomial in $n$.
The family $(\pi_n)$ is not a [[bounded-depth Frege|41QJ1WEMJ3]] family.

1. The [[proof|PE43N5E9PR]] uses counting formulas for the sum of $k$ bits, with $k$ up to $n(n+1)$.
2. These formulas are built by carry-save addition, with $O(\log k)$ layers of constant depth each, so their depth grows like $\log n$.
3. So the lines of $\pi_n$ have depth that tends to infinity with $n$, and no constant $d$ bounds the depth of every $\pi_n$.

No other polynomial-size family of bounded depth exists either.
By [[Ajtai's theorem|Q0ERK64J78]], for each fixed $d$, depth-$d$ Frege proofs of $\neg \mathrm{PHP}^{n+1}_n$ have superpolynomial size.

## Remarks

The example shows that depth is a separate resource.
The same formulas have polynomial-size proofs when depth is free, and superpolynomial ones when depth is bounded.
Counting $k$ bits needs depth that grows with $k$ in polynomial size, by the theorem that [[parity is not in AC0|W6T7X0QCFH]], so the counting method cannot be made shallow.

## Explanations

### L1 human

Buss's short proofs count pigeons with formulas that add many bits.
Adding many bits needs many layers of "and" and "or", and the number of layers grows with the number of bits.
So these proofs are short but deep, and bounded-depth Frege does not allow them.

### L2 human

We estimate the depth for $n = 1000$.

1. The double count sums $k = n(n+1) = 1001000$ bits.
2. Carry-save addition reduces three numbers to two per layer, so about $\log_{3/2} k \approx 34$ layers are needed.
3. Each layer has constant depth, so the counting formulas have depth a constant times $34$.

For $n = 10^6$ the number of layers is about $68$, so the depth keeps growing.
The typical use of the example is to separate Frege from bounded-depth Frege.
