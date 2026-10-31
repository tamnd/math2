---
records:
    - id: 2KS8DM4NTE
      kind: monograph
      title: Mathematical Methods of Classical Mechanics
      creators:
        - name: V. I. Arnold
          role: author
      date: "1978"
      expressions:
        - key: e1
          kind: edition
          date: "1978"
          ids:
            doi:
                - 10.1007/978-1-4757-1693-1
                - 10.1007/978-1-4757-2063-1
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1978"
              ids:
                isbn:
                    - "9781475716955"
                    - "9781475716931"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1989"
              ids:
                isbn:
                    - "9781441930873"
                    - "9781475720631"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-1693-1
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-2063-1
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
