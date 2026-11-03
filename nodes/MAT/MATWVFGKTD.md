---
tag: MATWVFGKTD
kind: concept
name: One-time pad
msc: [94A60, 68P25]
specializes: [7YNRCX56CM]
sources:
  - url: https://en.wikipedia.org/wiki/One-time_pad
same_as:
  wikidata: Q150474
  wikipedia: One-time pad
---

## Summary

The one-time pad is the cipher that adds to the message a random key of the same length, symbol by symbol.
When the key is uniformly random and never used again, the ciphertext gives no information at all about the message.
Shannon proved this perfect secrecy and also proved that no cipher can have it with fewer keys than messages.
The price is a key as long as all the data, which makes the pad hard to use in practice.

## Explanations

### L1 human

Write the message as bits and flip a fair coin for each bit to make the key.
The ciphertext is the bitwise sum: $0110 \oplus 1100 = 1010$.
The receiver adds the same key again and gets $1010 \oplus 1100 = 0110$ back.
Any message of four bits could have produced $1010$ with some key, and all keys are equally likely, so the eavesdropper learns nothing.
If the key is used twice, the sum of the two ciphertexts is the sum of the two messages, and the secrecy is gone.
