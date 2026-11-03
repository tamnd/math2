---
tag: AB22FWBQ0M
kind: problem
name: Tarski's finite basis problem
msc: [08B05, 03B25, 03C05]
uses: [YGYZAQ12MZ, 9Q008GMZSW, PKD440G2XW, KZSB5E471K, 5RFPT46DXX, 35G4HQG2FN]
about: [YGYZAQ12MZ]
sources:
  - url: https://doi.org/10.1142/S0218196796000040
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
history:
  posed_by: "Alfred Tarski"
---

## Problem

A finite algebra $A$ of finite signature is given by the finite tables of its operations.
It is [[finitely based|YGYZAQ12MZ]] if it has a finite [[equational basis|9Q008GMZSW]].
That is, some finite set of [[identities|PKD440G2XW]] true in $A$ implies every identity true in $A$.
Tarski's finite basis problem asks for an algorithm, that is, a [[computable function|KZSB5E471K]], with the following task.
Given a finite algebra of finite signature, it decides whether the algebra is finitely based.

## Remarks

The problem was solved negatively by Ralph McKenzie in 1996: no such algorithm exists.
Earlier work showed that the answer to "is every finite algebra finitely based?" is no.
Lyndon showed that every two-element algebra of finite signature is finitely based, and he also gave a [[seven-element algebra|W76V9BZGST]] that is not.
Many classes of finite algebras are known to consist of finitely based algebras, among them finite groups, by the [[Oates–Powell theorem|5RFPT46DXX]], and finite lattices.
[[Baker's finite basis theorem|35G4HQG2FN]] covers all finite algebras of finite signature that generate a congruence-distributive variety.
The decision problem restricted to finite semigroups is still open.

## Explanations

### L1 human

The identities true in a finite algebra form an infinite list.
Sometimes finitely many of them imply all the others, and sometimes they do not.
Tarski asked whether a computer could always tell which case happens, just by looking at the tables of the operations.
McKenzie proved that no computer program can do this for all finite algebras.
