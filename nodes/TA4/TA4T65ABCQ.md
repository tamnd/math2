---
tag: TA4T65ABCQ
kind: statement
role: theorem
name: Friedberg–Muchnik theorem below C
sources:
  - wikipedia: en:61969687@r1369417176
    locator: Friedberg–Muchnik theorem, section Friedberg–Muchnik theorem below C
    note: adopted
    mention: wikipedia://en/61969687#I9IV
    sections: [Statement]
inventory: [KB1E8H1QF6]
---

## Statement

This shows that the order-structure of Turing degrees is quite complicated, even among enumerable sets.

WLOG, we assume that $C$ is enumerated as $C_0 \subsetneq C_1 \subsetneq C_2 \subsetneq \cdots$, each $C_n$ being a [[finite set|070R982G4B]].

To prove the theorem, we define the concept of **permission**. Technically, this is the Yates permitting. There are other kids of permissions.

Given two sequences of finite sets $A_n \uparrow A, C_n \uparrow C$, we say that $\{C_n\}_{n \in \mathbb{N}}$ *permits* $\{A_n\}_{n \in \mathbb{N}}$ iff

$$\forall n, i \quad C_n \cap [0:i] = C \cap [0:i] \implies i \not\in A_{n+1} \setminus A_n$$

A bit more generally, if $f : \mathbb{N} \to \mathbb{N}$, then we say that $\{C_n\}_{n \in \mathbb{N}}$ *f*-*permits* $\{A_n\}_{n \in \mathbb{N}}$ iff

$$\forall n, i \quad C_n \cap [0:f(i)] = C \cap [0:f(i)] \implies i \not\in A_{n+1} \setminus A_n$$
