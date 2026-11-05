---
tag: GQK0F07JG2
kind: concept
name: Damgård–Jurik cryptosystem
aliases: [damgaard-jurik-cryptosystem]
sources:
  - wikipedia: en:6856307@r1302902249
    locator: Damgård–Jurik cryptosystem
    note: adopted
    mention: wikipedia://en/6856307
    sections: [Summary]
same_as:
  wikidata: Q1158421
  wikipedia: Damgård–Jurik cryptosystem
inventory: [MF2D4QAXWE]
---

## Summary

The **Damgård–Jurik cryptosystem** is a generalization of the Paillier cryptosystem. It uses computations modulo $n^{s+1}$ where $n$ is an RSA modulus and $s$ a (positive) [[natural number|0MWKJ44V5A]]. Paillier's scheme is the special case with $s=1$. The order $\varphi(n^{s+1})$ ([[Euler's totient function|0DAMHCT17R]]) of $Z^*_{n^{s+1}}$ can be divided by $n^s$. Moreover, $Z^*_{n^{s+1}}$ can be written as the direct product of $G \times H$. $G$ is cyclic and of order $n^s$, while $H$ is isomorphic to $Z^*_n$. For encryption, the message is transformed into the corresponding [[coset|564VVAQTNR]] of the factor group $G\times H/H$ and the security of the scheme relies on the difficulty of distinguishing random elements in different cosets of $H$. It is semantically secure if it is hard to decide if two given elements are in the same coset. Like Paillier, the security of Damgård–Jurik can be proven under the decisional composite residuosity assumption.
