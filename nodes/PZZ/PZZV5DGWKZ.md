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

Alice wants to send Bob the secret message $m = 1011$, and they share the key $k = 0110$.
We apply the [[exclusive or|PTMR3P9J6C]] bit by bit, with $1$ for T and $0$ for F.

1. Alice encrypts with $c = m \oplus k$.
   Bit by bit, $1 \oplus 0 = 1$, $0 \oplus 1 = 1$, $1 \oplus 1 = 0$ and $1 \oplus 0 = 1$, so $c = 1101$.
2. Each bit of $c$ is the sum of the bits of $m$ and $k$ modulo $2$, as in the [[integers modulo 2|03VFZ2WETT]].
3. Bob decrypts with $c \oplus k$.
   Bit by bit, $1 \oplus 0 = 1$, $1 \oplus 1 = 0$, $0 \oplus 1 = 1$ and $1 \oplus 0 = 1$, so $c \oplus k = 1011 = m$.
4. This works for every message and key.
   By associativity $(m \oplus k) \oplus k = m \oplus (k \oplus k)$.
   Since $x \oplus x = 0$ for each bit, $k \oplus k = 0000$, and since $0$ is the identity, $m \oplus 0000 = m$.

## Remarks

### Three laws at work

Decryption uses associativity, $x \oplus x = 0$ and $x \oplus 0 = x$.
These are the laws of addition modulo $2$, where every element is its own negative.
So the same operation, with the same key, both encrypts and decrypts.

### The one-time pad

This scheme is the [[one-time pad|MATWVFGKTD]] on bits.
When the key is random, as long as the message, and used once, the cipher text gives no information about the message.
If the same key encrypts two messages $m_1$ and $m_2$, then $c_1 \oplus c_2 = m_1 \oplus m_2$.
The key cancels, and the two messages leak information about each other.

### Why "or" does not work

Replace $\oplus$ by the inclusive [[disjunction|0F72FK8EKB]] and decryption fails.
Here $1011 \lor 0110 = 1111$, and many different messages give $1111$ with this key, for example $1001$ and $1111$ itself.
So Bob cannot recover $m$.

## Explanations

### L1 human

Think of the key as a list of instructions, "flip" ($1$) or "keep" ($0$), one for each position of the message.
Applying the key once scrambles the message.
Applying the same key again flips the same positions back.
So the second use of the key gives back the original message.

### L2 human

Check associativity on one instance: $a = 110$, $b = 011$, $c = 101$.

1. $a \oplus b = 101$, and $(a \oplus b) \oplus c = 101 \oplus 101 = 000$.
2. $b \oplus c = 110$, and $a \oplus (b \oplus c) = 110 \oplus 110 = 000$.
3. The two results agree.

Each column of the three strings holds an even number of $1$s, namely $1, 0, 1$, then $1, 1, 0$, then $0, 1, 1$.
So each bit of the result is $0$, as the parity rule says.
Watch out: $\oplus$ on bit strings is not the addition of binary numbers.
In binary, $011 + 001 = 100$ with a carry, while $011 \oplus 001 = 010$.
