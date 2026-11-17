---
tag: PZZV5DGWKZ
kind: example
name: Exclusive or on bit strings and the one-time pad
msc: ["03B05", "94A60"]
topics: [PM1AYWABA7]
audience: school
instance_of: [PTMR3P9J6C]
uses: [PTMR3P9J6C, 03VFZ2WETT, MATWVFGKTD]
sources:
  - url: https://en.wikipedia.org/wiki/Exclusive_or
    locator: lead section
  - url: https://en.wikipedia.org/wiki/One-time_pad
    locator: lead section
---

## Example

We apply the [[exclusive or|PTMR3P9J6C]] bit by bit to strings of $4$ bits, with $1$ for T and $0$ for F.
Let the message be $m = 1011$ and the key be $k = 0110$.

1. Encrypt: $c = m \oplus k$. Bit by bit, $1 \oplus 0 = 1$, $0 \oplus 1 = 1$, $1 \oplus 1 = 0$, $1 \oplus 0 = 1$. So $c = 1101$.
2. Each bit of $c$ is the sum of the bits of $m$ and $k$ modulo $2$, as in the [[integers modulo 2|03VFZ2WETT]].
3. Decrypt: $c \oplus k$. Bit by bit, $1 \oplus 0 = 1$, $1 \oplus 1 = 0$, $0 \oplus 1 = 1$, $1 \oplus 0 = 1$. So $c \oplus k = 1011 = m$.
4. The reason: $(m \oplus k) \oplus k = m \oplus (k \oplus k)$ by associativity, $k \oplus k = 0000$ because $x \oplus x = 0$ for each bit, and $m \oplus 0000 = m$ because $0$ is the identity.

## Remarks

The example shows three laws of $\oplus$ at work: associativity, $x \oplus x = 0$ and $x \oplus 0 = x$.
These are the laws of addition modulo $2$, where every element is its own negative.

This scheme is the [[one-time pad|MATWVFGKTD]] on bits.
When the key is random, as long as the message, and used once, the cipher text gives no information about the message.
If the same key encrypts two messages $m_1$ and $m_2$, then $c_1 \oplus c_2 = m_1 \oplus m_2$, so the key cancels and the two messages leak information.

If we replace $\oplus$ by the inclusive [[disjunction|0F72FK8EKB]], decryption fails: $1011 \lor 0110 = 1111$, and the string $1111$ is the result for many different messages, so $m$ cannot be recovered.

## Explanations

### L1 human

Think of the key as a list of instructions "flip" ($1$) or "keep" ($0$) for each position of the message.
Applying the key once scrambles the message.
Applying the same key again flips the same positions back.
So the second use of the key gives back the original message.

### L2 human

We check that $\oplus$ on strings is associative on one instance: $a = 110$, $b = 011$, $c = 101$.

1. $a \oplus b = 101$, and $(a \oplus b) \oplus c = 101 \oplus 101 = 000$.
2. $b \oplus c = 110$, and $a \oplus (b \oplus c) = 110 \oplus 110 = 000$.
3. The two results agree.

Each column of the three strings contains an even number of $1$s ($1, 0, 1$; $1, 1, 0$; $0, 1, 1$), so each bit of the result is $0$, as the parity rule says.

The typical use of $\oplus$ on strings is in codes and ciphers, where it adds data and keys without carries.

A trap: $\oplus$ on bit strings is not the addition of binary numbers.
In binary, $011 + 001 = 100$ with a carry, while $011 \oplus 001 = 010$.
