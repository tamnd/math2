---
tag: WVNP7RQQ9D
kind: statement
role: theorem
name: BCMP network
msc: [60K25, 90B15, 90B22]
uses: [P64V0HTE78, TWQFE0FZZS, 0KRH5157WP, 0MTNR28K60]
about: [P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/BCMP_network
same_as:
  wikidata: Q4835204
  wikipedia: BCMP network
---

## Statement

Consider a network of queues with several classes of customers, which may be open, closed or mixed.
In an open part, customers arrive from outside as a [[Poisson process|0MTNR28K60]].
After service, a customer moves to a new queue and possibly a new class according to fixed routing probabilities.
Assume each queue is of one of the following four types:

1. First-come first-served, with exponential service times whose rate is the same for all classes and may depend on the number of customers at the queue.
2. Processor sharing, with a single server.
3. Infinite server: each customer begins service at once on arrival.
4. Last-come first-served with preemptive resume.

For types 2, 3 and 4, the service time distribution may depend on the class and is required to have a rational Laplace transform.
Then the [[stationary distribution|0KRH5157WP]] of the network state, when it exists, has product form.
It is a normalising constant times a product over the queues of factors, each depending only on the state of its queue.
For queues of types 2, 3 and 4, the stationary distribution depends on each service time distribution only through its mean.

## Remarks

The theorem is due to Baskett, Chandy, Muntz and Palacios (1975), whose initials give the name.
Its proof writes each non-exponential service time as a mix of exponential phases, which makes the network a [[continuous-time Markov chain|TWQFE0FZZS]], and checks local balance at each queue.
The rational Laplace transform condition allows such a phase representation.
A single-class open network of type 1 queues with one server each is a [[Jackson network|NG6FXQB0Y5]], and the closed version is the [[Gordon–Newell theorem|S2WX7J4805]].
A first-come first-served queue whose service times are not exponential, or whose rates differ between classes, falls outside the four types, and the product form fails in general.

## Explanations

### L1 human

Real systems, such as computers and communication networks, serve many kinds of jobs that follow different routes.
The BCMP theorem names four ways a station may serve its jobs for which the whole network still has a simple long-run behaviour.
In each of these cases, the probability of a state of the whole network splits into one factor per station.
This makes performance of large networks computable.

### L2 human

The BCMP theorem is the main generalisation of Jackson's and Gordon–Newell's product form theorems.
The processor sharing type models time-sharing computers, and the infinite server type models terminals with think times.
For performance evaluation, its product form allows normalising-constant algorithms and mean value analysis for multi-class closed networks.
The insensitivity of types 2, 3 and 4 explains why only mean service times matter in many models.
