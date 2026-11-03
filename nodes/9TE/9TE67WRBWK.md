---
tag: 9TE67WRBWK
kind: concept
name: Digital signature
msc: [94A62, 94A60]
sources:
  - url: https://en.wikipedia.org/wiki/Digital_signature
same_as:
  wikidata: Q220849
  wikipedia: Digital signature
---

## Summary

A digital signature scheme lets the holder of a private key attach a short string to a message.
Anyone can check this string with the matching public key.
A valid signature shows that the message comes from the key holder and was not changed.
Security means that nobody without the private key can sign a new message.
This must hold even for someone who has seen signatures on messages of their choice.
Signatures are one of the two main tasks of [[public-key cryptography|01E9MNJYEX]], beside encryption.

## Explanations

### L1 human

A handwritten signature is the same on every document, so it can be cut and pasted.
A digital signature depends on the document: change one letter and the old signature no longer fits.
Only the signer can make signatures, because making one needs the private key.
Anyone can check them, because checking needs only the public key.
In RSA signatures, for instance, signing is raising to the secret exponent and checking is raising to the public exponent.
