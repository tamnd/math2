---
tag: X4E6ZF7HP5
kind: concept
name: Counting points on elliptic curves
aliases: [point-counting-of-elliptic-curves]
sources:
  - wikipedia: en:21275881@r1192691994
    locator: Counting points on elliptic curves
    note: adopted
    mention: wikipedia://en/21275881
    sections: [Summary]
same_as:
  wikidata: Q5177153
  wikipedia: Counting points on elliptic curves
inventory: [NCTXCHJMCX]
---

## Summary

An important aspect in the study of elliptic curves is devising effective ways of **counting points on the curve**. There have been several approaches to do so, and the algorithms devised have proved to be useful tools in the study of various fields such as number theory, and more recently in cryptography and Digital Signature Authentication (See elliptic curve cryptography and elliptic curve DSA). While in number theory they have important consequences in the solving of Diophantine equations, with respect to cryptography, they enable us to make effective use of the difficulty of the discrete logarithm problem (DLP) for the group $E(\mathbb{F}_q)$, of elliptic curves over a [[finite field|0ZXZ82FTX2]] $\mathbb{F}_q$, where *q* = *p*<sup>*k*</sup> and *p* is a prime. The DLP, as it has come to be known, is a widely used approach to public key cryptography, and the difficulty in solving this problem determines the level of security of the cryptosystem. This article covers algorithms to count points on elliptic curves over fields of large characteristic, in particular *p* > 3. For curves over fields of small characteristic more efficient algorithms based on *p*-adic methods exist.
