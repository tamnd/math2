---
tag: YVQYFMF9HZ
kind: statement
role: theorem
name: Burke's theorem
msc: [60K25, 90B22]
uses: [GTFRPF5J2K, 0MTNR28K60, 0KRH5157WP, TWQFE0FZZS]
about: [GTFRPF5J2K, P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/Burke%27s_theorem
same_as:
  wikidata: Q4998912
  wikipedia: Burke's theorem
---

## Statement

Let $\lambda > 0$ and $\mu > 0$ with $\lambda < \mu$.
Consider an [[M/M/1 queue|GTFRPF5J2K]] with arrival rate $\lambda$ and service rate $\mu$, started in its [[stationary distribution|0KRH5157WP]].
Then:

1. The departure process is a [[Poisson process|0MTNR28K60]] of rate $\lambda$.
2. For each time $t$, the number of customers in the system at time $t$ is independent of the departure times before $t$.

## Remarks

The same holds for the M/M/$c$ queue with $\lambda < c \mu$ and for the M/M/$\infty$ queue.
The proof uses reversibility.
The queue length is a birth–death process, and a stationary birth–death process is reversible.
Reversed in time, the departures of the queue become the arrivals of the reversed process, which form a Poisson process of rate $\lambda$.
The arrivals after $t$ are independent of the state at $t$, and in reversed time this gives part 2.
For example, take two M/M/1 queues in series.
The second queue sees Poisson arrivals of rate $\lambda$, so in steady state it is again an M/M/1 queue.
The two queue lengths at a fixed time are independent.
The stationarity hypothesis is needed: a queue started empty has departures that are not a Poisson process.

## Explanations

### L1 human

Customers arrive at random at a single counter and are served one at a time.
Burke's theorem says that, once the system has settled, the stream of customers leaving looks exactly like the stream arriving: random, with the same rate.
The server does not make the output more regular, even though it cannot serve two people at once.
Also, knowing how many people left recently tells you nothing about how many are waiting now.

### L2 human

The theorem is the key step from single queues to networks of queues.
Since the output of a stationary M/M/1 queue is Poisson, queues in series can be analysed one at a time.
Their joint stationary law is a product of geometric laws.
This is the simplest case of the product form of [[Jackson networks|NG6FXQB0Y5]].
The proof is a model of the use of time reversal for stationary Markov chains.
