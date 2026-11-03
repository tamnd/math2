---
tag: 68HRRNMWKZ
kind: definition
name: Unicity distance
msc: [94A60, 94A17]
defines: 36BZ88VBY8
uses: [7YNRCX56CM, Y86E072V0V]
sources:
  - url: https://en.wikipedia.org/wiki/Unicity_distance
---

## Definition

Let a [[cryptosystem|7YNRCX56CM]] encrypt strings over a finite alphabet $\Sigma$ with a key drawn from a finite key space $\mathcal{K}$.
Let $H(K)$ be the [[Shannon entropy|Y86E072V0V]] of the key in bits, equal to $\log_2 \abs{\mathcal{K}}$ when the key is uniform.
Let $H_L$ be the entropy rate of the plaintext language in bits per character, and let $D = \log_2 \abs{\Sigma} - H_L$ be its redundancy per character.
If $D > 0$, the *unicity distance* of the system is
$$U = \frac{H(K)}{D}.$$

## Remarks

Example: a simple substitution cipher on English has $\abs{\mathcal{K}} = 26!$, so $H(K) = \log_2 26! \approx 88.4$ bits.
With the common estimate $H_L \approx 1.5$, the redundancy is $D \approx 4.7 - 1.5 = 3.2$, and $U \approx 88.4 / 3.2 \approx 28$ characters.

Non-example: if the plaintexts are uniformly random strings, then $H_L = \log_2 \abs{\Sigma}$ and $D = 0$.
The formula does not apply, and indeed no length of ciphertext ever singles out the key.

Shannon derived $U$ from a random-cipher model.
A spurious key is a wrong key that decrypts the ciphertext to plausible text.
The value $U$ estimates the ciphertext length at which the expected number of spurious keys drops to about zero.
Compressing the plaintext before encryption lowers $D$ and so raises $U$.
