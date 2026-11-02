---
tag: ECT6RNF865
kind: concept
name: Shooting method
msc: [65L10, 34B15]
sources:
  - url: https://en.wikipedia.org/wiki/Shooting_method
same_as:
  wikidata: Q1749769
  wikipedia: Shooting method
---

## Summary

The shooting method solves a [[boundary value problem|TM8VQJWGHZ]] by solving a family of [[initial value problems|0FXDW992DS]] instead.
One guesses the missing initial data, solves forward, and adjusts the guess until the condition at the far end holds.
This turns the boundary value problem into a root-finding problem for a function of the missing initial data.
It is used both as a numerical method and as a tool in existence proofs.

## Explanations

### L1 human

Think of firing a cannon at a target on a hill.
You know where the cannon stands but not the right angle.
You fire, see whether the ball lands too short or too far, and correct the angle.
For $y'' = -y$, $y(0) = 0$, $y(\pi/2) = 1$, one shoots with $y'(0) = s$ and gets $y = s \sin x$.
The ball hits the target $y(\pi/2) = 1$ exactly when $s = 1$.
