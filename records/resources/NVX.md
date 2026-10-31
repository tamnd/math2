---
records:
    - id: NVXACZ172H
      kind: monograph
      title: Topics in Invariant Theory
      creators:
        - name: Marie-Paule Malliavin
          role: author
      date: "1991"
      expressions:
        - key: e1
          kind: edition
          date: "1991"
          ids:
            doi: 10.1007/bfb0083499
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1991"
              ids:
                isbn:
                    - "9783540543770"
                    - "9783540475927"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0083499
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: NVXJ3QBD9V
      kind: course
      title: An invitation to mathematics
      creators:
        - name: Sankaran Vishwanath
          role: instructor
      expressions:
        - key: e1
          kind: edition
          language: en
          manifestations:
            - key: m1
              kind: page
              publisher: IMSc
              ids:
                nptel: "111106083"
      scope:
        value: in
        rule: S6
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: nptel
          snapshot: blake3:89dc2ec164a0108adbecf0ec8c793929c947e196b164e762035d3fdd89a3f469
          native_id: "111106083"
          level: manifestation
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to deferred
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.4 scope/1
          note: from deferred to in
---
