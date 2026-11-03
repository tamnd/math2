---
tag: XVG8ZDKW90
kind: example
name: Diffusion-limited aggregation
msc: [82C24, 60K35, 60G50]
illustrates: [04VZE3FZXF]
uses: [04VZE3FZXF, CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Diffusion-limited_aggregation
same_as:
  wikidata: Q1224521
  wikipedia: Diffusion-limited aggregation
---

## Example

*Diffusion-limited aggregation* (DLA) on $\Z^2$ is a random growing sequence of finite connected sets $A_0 \subset A_1 \subset \cdots$.
Start with $A_0 = \set{0}$.
Given $A_n$, let $\partial A_n$ be the set of points of $\Z^2 \setminus A_n$ adjacent to $A_n$.
Release a simple [[random walk|04VZE3FZXF]] "from infinity", and let $A_{n+1} = A_n \cup \set{y}$, where $y$ is the first point of $\partial A_n$ that the walk visits.
Precisely, $y$ is chosen with the harmonic measure of $\partial A_n$ from infinity.
This is the limit, as $\abs{z} \to \infty$, of the law of the first point of $\partial A_n$ hit by a simple random walk started at $z$.

Check for the first step: $\partial A_0$ consists of the four neighbours of $0$.
By the symmetry of $\Z^2$ under rotation by a right angle, each of them is hit first with probability $1/4$.
So $A_1$ is $\set{0, e}$ for a uniformly random neighbour $e$ of $0$.
From then on the probabilities are no longer uniform.
Points at the tips of $A_n$ are much more likely to be hit than points in its fjords.

## Remarks

The model was introduced by Thomas Witten and Leonard Sander in 1981.
Its rule is the discrete analogue of growth driven by [[harmonic measure|CFD7BPM51W]], so it also models electrodeposition and viscous fingering.
Simulations show branching, fractal clusters, with a fractal dimension near $1.71$ in the plane, but this is not proved.
Harry Kesten proved that the radius of $A_n$ is at most of order $n^{2/3}$ almost surely in two dimensions.
It is not even known whether $A_n$ is, in a suitable sense, a fractal of dimension less than $2$.

## Explanations

### L1 human

Start with one particle stuck at the origin.
Let another particle wander at random from far away until it touches the cluster, and glue it there.
Repeat this thousands of times.
The arms of the cluster screen its inner parts, since a wandering particle almost always meets an arm first.
So the cluster grows into a branching tree with long thin arms, like frost on a window.
