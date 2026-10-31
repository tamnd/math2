---
records:
    - id: N4HRP6SQS6
      kind: monograph
      title: Understanding Analysis
      creators:
        - name: Stephen Abbott
          role: author
      date: "2001"
      expressions:
        - key: e1
          kind: edition
          date: "2001"
          ids:
            doi:
                - 10.1007/978-0-387-21506-8
                - 10.1007/978-1-4939-2712-8
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2001"
              ids:
                isbn:
                    - "9781441928665"
                    - "9780387215068"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2015"
              ids:
                isbn:
                    - "9781493927111"
                    - "9781493927128"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-0-387-21506-8
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4939-2712-8
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
