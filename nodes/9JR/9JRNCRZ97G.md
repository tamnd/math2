---
tag: 9JRNCRZ97G
kind: example
name: Smoluchowski coagulation equation
msc: [45K05, 82C22]
instance_of: [YRKW2KX2CW]
sources:
  - url: https://en.wikipedia.org/wiki/Smoluchowski_coagulation_equation
same_as:
  wikidata: Q971184
  wikipedia: Smoluchowski coagulation equation
---

## Example

Let $n(x, t) \ge 0$ be the number density of clusters of mass $x > 0$ at time $t \ge 0$.
Let the coagulation kernel $K(x, y) = K(y, x) \ge 0$ be the rate at which clusters of masses $x$ and $y$ merge.
The continuous Smoluchowski coagulation equation is
$$\frac{\partial n(x, t)}{\partial t} = \frac12 \int_0^x K(x - y, y) \, n(x - y, t) \, n(y, t) \, dy - n(x, t) \int_0^\infty K(x, y) \, n(y, t) \, dy.$$
The first term counts the clusters of mass $x$ formed from two smaller ones, with the factor $\frac12$ because each pair is counted twice.
The second term counts the clusters of mass $x$ lost by merging with any other cluster.
It is a nonlinear [[integro-differential equation|YRKW2KX2CW]]: a time derivative of $n$ and integrals of $n$ over mass.

Check for the constant kernel $K = k > 0$: let $N(t) = \int_0^\infty n(x, t) \, dx$ be the total number of clusters.
Integrating over $x$ and exchanging the order of integration in the first term gives $N'(t) = \frac{k}{2} N^2 - k N^2 = -\frac{k}{2} N^2$.
Hence $N(t) = \frac{N(0)}{1 + k N(0) t / 2}$, so the number of clusters decreases like $\frac{2}{kt}$.

## Remarks

For bounded kernels the total mass $\int_0^\infty x \, n(x, t) \, dx$ is conserved.
For the product kernel $K(x, y) = xy$ the mass is conserved only up to a finite time, after which mass escapes into an infinitely large cluster; this is called gelation.
The discrete version replaces the integrals by sums over integer cluster sizes.

## Explanations

### L1 human

Small particles in a smoke or a polymer solution collide and stick together, forming bigger clusters.
The equation describes how the distribution of cluster sizes changes in time.
A cluster of a given size is created when two smaller ones meet, which gives an integral over the ways to split it.
It is destroyed when it meets any other cluster.
