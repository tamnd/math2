---
tag: XJ8F3NQMGN
kind: concept
name: Cryptographic hash function
msc: [94A60, 68P25]
sources:
  - url: https://en.wikipedia.org/wiki/Cryptographic_hash_function
same_as:
  wikidata: Q477202
  wikipedia: Cryptographic hash function
---

## Summary

A cryptographic hash function maps messages of any length to short strings of fixed length, called digests.
It must be infeasible to find two messages with the same digest.
Such collisions must exist, since there are more messages than digests, but nobody should be able to find one.
Hash functions are used to sign long messages, to check the integrity of files, to commit to values and to store passwords.
Examples in use are SHA-256 and SHA-3, whose security is believed but not proved.

## Explanations

### L1 human

A hash function is like a fingerprint for data.
The fingerprint is short, say $256$ bits, even for a file of many gigabytes.
Changing a single bit of the file changes the fingerprint completely and unpredictably.
It should be practically impossible to find two different files with the same fingerprint, or a file with a given fingerprint.
