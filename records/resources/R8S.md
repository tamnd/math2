---
records:
    - id: R8S882AWPX
      kind: monograph
      title: Infinite-Dimensional Dynamical Systems in Mechanics and Physics
      creators:
        - name: Roger Temam
          role: author
      date: "1988"
      expressions:
        - key: e1
          kind: edition
          date: "1988"
          ids:
            doi:
                - 10.1007/978-1-4612-0645-3
                - 10.1007/978-1-4684-0313-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1997"
              ids:
                isbn:
                    - "9781461268536"
                    - "9781461206453"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1988"
              ids:
                isbn:
                    - "9781468403152"
                    - "9781468403138"
      relations:
        - kind: part_of
          to: 2M0N86YNGA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-0645-3
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0313-8
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
