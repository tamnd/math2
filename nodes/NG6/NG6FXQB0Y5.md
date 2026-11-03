---
tag: NG6FXQB0Y5
kind: statement
role: theorem
name: Jackson network
msc: [60K25, 90B15, 90B22]
uses: [P64V0HTE78, TWQFE0FZZS, 0KRH5157WP, 0MTNR28K60, 0E99F51GVB]
about: [P64V0HTE78]
sources:
  - url: https://en.wikipedia.org/wiki/Jackson_network
same_as:
  wikidata: Q2524990
  wikipedia: Jackson network
---

## Statement

Consider an open network of $J$ queues, numbered $1, \ldots, J$, each with one server and first-come first-served discipline.
Customers arrive from outside at queue $i$ as a [[Poisson process|0MTNR28K60]] of rate $\alpha_i \ge 0$, independently for different $i$.
Service times at queue $i$ are [[exponential|0E99F51GVB]] of rate $\mu_i > 0$, and all service times and arrival processes are independent.
After service at queue $i$, a customer moves to queue $j$ with probability $p_{ij}$ and leaves the network with probability $1 - \sum_j p_{ij}$, independently of everything else.
Assume that every customer leaves the network with probability $1$, so that $I - P$ is invertible, where $P = (p_{ij})$.
Let $(\lambda_1, \ldots, \lambda_J)$ be the unique solution of the traffic equations
$$\lambda_i = \alpha_i + \sum_{j=1}^{J} \lambda_j p_{ji}, \qquad i = 1, \ldots, J,$$
and let $\rho_i = \lambda_i / \mu_i$.
If $\rho_i < 1$ for every $i$, then the vector $(n_1, \ldots, n_J)$ of queue lengths is a [[continuous-time Markov chain|TWQFE0FZZS]] with [[stationary distribution|0KRH5157WP]]
$$\pi(n_1, \ldots, n_J) = \prod_{i=1}^{J} (1 - \rho_i) \rho_i^{n_i}, \qquad n_1, \ldots, n_J \ge 0.$$

## Remarks

The proof checks the global balance equations directly, or uses the partial balance at each queue together with the reversed process.
The number $\lambda_i$ is the total rate of arrivals into queue $i$, from outside and from other queues.
In steady state, the queue lengths at a fixed time are independent, and queue $i$ looks like an [[M/M/1 queue|GTFRPF5J2K]] of load $\rho_i$.
The internal flows need not be Poisson processes when customers can return to a queue, so the product form is not a consequence of [[Burke's theorem|YVQYFMF9HZ]] alone.
For a tandem of two queues with $\alpha_1 = \lambda$, $\alpha_2 = 0$, $p_{12} = 1$ and $p_{2j} = 0$, the traffic equations give $\lambda_1 = \lambda_2 = \lambda$.
The stationary law is then $(1 - \rho_1)\rho_1^{n_1} (1 - \rho_2) \rho_2^{n_2}$ with $\rho_i = \lambda / \mu_i$.
If some $\rho_i \ge 1$, queue $i$ is unstable and no stationary distribution exists.
The theorem extends to queues with several servers, or with service rates depending on the queue length, with each factor replaced by the stationary law of the corresponding single queue.

## Explanations

### L1 human

A Jackson network is a set of service stations through which customers wander at random, like patients moving between departments of a hospital.
Jackson's theorem says that, in the long run, each station behaves as if it were a single queue on its own, fed with the right total arrival rate.
The numbers of customers at the different stations are independent.
This makes a large and complicated network easy to compute.

### L2 human

To use the theorem, first solve the linear traffic equations for the total arrival rates $\lambda_i$.
Then check stability station by station with $\rho_i < 1$.
Mean queue lengths are $\rho_i / (1 - \rho_i)$, and [[Little's law|JN2YME6F4A]] gives mean sojourn times.
The closed version of the model, with a fixed number of customers, is the [[Gordon–Newell theorem|S2WX7J4805]], and the multi-class generalisation is the [[BCMP network|WVNP7RQQ9D]] theorem.
